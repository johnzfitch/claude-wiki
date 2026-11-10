---
title: "Fine-grained tool streaming - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-05T06:35:11Z"
tags: ["api"]
---

# Fine-grained tool streaming

Copy page



Stream tool inputs without server-side JSON buffering for latency-sensitive applications.

Copy page



Fine-grained tool streaming

Feature of  
[Message streaming](../Guides/build-with-claude-streaming.md)

[APIs](#feature-availability)  
Messages APIAvailable

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableAmazon BedrockInvokeModelAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

[Data handling](#feature-data-handling)  
ZDR eligibleHIPAA eligible

Fine-grained tool streaming delivers a tool’s input to your client as Claude generates it, without server-side buffering or JSON validation. Skipping the buffering step reduces the time to the first fragment of a large parameter, such as a document or a block of code, and the fragments arrive through the same [Streaming messages](../Guides/build-with-claude-streaming.md) events as standard tool use.



Because the API does not buffer or validate a tool’s input before streaming it, you might receive partial or invalid JSON. A response that ends with the [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) `max_tokens` can also cut a parameter off midway. Accumulate the fragments, guard the parse, and see [Handling invalid JSON in tool responses](#handling-invalid-json-in-tool-responses) for how to return unparseable input to Claude.

## How to use fine-grained tool streaming

All models support fine-grained tool streaming on the Claude API, [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud (Google managed)](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.

The `eager_input_streaming` field is optional. Setting it to `true` turns on fine-grained streaming for that tool, and omitting it gives you standard buffered streaming, in which the API buffers and validates each parameter value before streaming it back. The exception is a request that sends the `fine-grained-tool-streaming-2025-05-14` beta header, which turns fine-grained streaming on for tools that leave the field unset. The per-tool field replaces that header, and an explicit `false` keeps buffered streaming for a tool even when a request sends it. The header cannot be combined with a [computer use](agents-and-tools-tool-use-computer-use-tool.md) or [browser use](agents-and-tools-tool-use-browser-use-tool.md) toolset entry: the API rejects a request that sends both, so remove the header and set `eager_input_streaming` on the user-defined tools that need it. See [Tool reference](agents-and-tools-tool-use-tool-reference.md) for the field definition.

The following example turns on fine-grained streaming for a `make_file` tool and asks Claude for a long poem, so the tool input is large enough to watch it stream in:

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

with client.messages.stream(
    max_tokens=65536,
    model="claude-opus-5-5",
    tools=[
        {
            "name": "make_file",
            "description": "Write text to a file",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "The filename to write text to",
                    },
                    "lines_of_text": {
                        "type": "array",
                        "description": "An array of lines of text to write to the file",
                    },
                },
                "required": ["filename", "lines_of_text"],
            },
        }
    ],
    messages=[
        {
            "role": "user",
            "content": "Can you write a long poem and make a file called poem.txt?",
        }
    ],
) as stream:
    for event in stream:
        if event.type == "input_json":
            print(event.partial_json, end="", flush=True)
    final_message = stream.get_final_message()

print()
for block in final_message.content:
    if block.type == "tool_use":
        print(f"Complete tool input: {block.input}")
```

Each input fragment arrives the moment Claude writes it, and the fragments join into the full tool input, so the poem arrives piece by piece:

```python
{"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", "", "I.", "", "Beneath the vast and star-strewn sky,", "Where silver moonbeams softly lie,", ...
Complete tool input: {"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", ...]}
```



Without `eager_input_streaming`, the API buffers and validates each parameter value before streaming it back, so nothing prints for a large parameter until Claude has finished generating it. With it, fragments arrive from the moment Claude starts the parameter, and they are typically longer, with fewer mid-word breaks.

## Accumulating tool input deltas

The accumulation contract is the same as for standard tool-use streaming, so this section applies with and without `eager_input_streaming`. See [Input JSON delta](../Guides/build-with-claude-streaming.md#input-json-delta) in Streaming messages for the event format. Fine-grained tool streaming changes what you can assume about the result: the server streams fragments without validating them, so the accumulated string might not be valid JSON.

When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.

Where your SDK provides an accumulator helper (as the Python, TypeScript, Go, Java, and Ruby tabs in the previous example do), it handles this for you. Use the manual pattern when your SDK has no helper or when you want full control over how the input is assembled.

The accumulation contract:

1.  On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`.
2.  For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`.
3.  On `content_block_stop`, parse the accumulated string.

Guard the parse, as the following SDK example does. A response can also stop at `max_tokens` midway through a parameter. Check the [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) and decide whether to retry the request with a higher `max_tokens` or repair the partial input.

The type mismatch between the initial `input: {}` (object) and `partial_json` (string) is by design. The empty object marks the slot in the content array. The delta strings build the real value.

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

tool_inputs: dict[int, str] = {}  # index -> accumulated JSON string

with client.messages.stream(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[
        {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "eager_input_streaming": True,
            "input_schema": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        }
    ],
    messages=[{"role": "user", "content": "Weather in Paris?"}],
) as stream:
    for event in stream:
        match event.type:
            case "content_block_start" if event.content_block.type == "tool_use":
                tool_inputs[event.index] = ""
            case "content_block_delta" if event.delta.type == "input_json_delta":
                tool_inputs[event.index] += event.delta.partial_json
            case "content_block_stop" if event.index in tool_inputs:
                raw_input = tool_inputs[event.index]
                try:
                    parsed = json.loads(raw_input)
                except json.JSONDecodeError:
                    # The accumulated string is not guaranteed to be valid JSON.
                    # See "Handling invalid JSON in tool responses" on this page.
                    print(f"Invalid tool input: {raw_input}")
                else:
                    print(f"Tool input: {parsed}")
```



Reacting to fragments and assembling them are separate concerns. The first example reacts to each fragment as it arrives and still hands assembly to the SDK in the tabs that use an accumulator helper. Use the manual pattern when you are not using an accumulator helper or when you want full control over assembly.

## Handling invalid JSON in tool responses

With fine-grained tool streaming, the accumulated input for a tool call might be invalid or incomplete JSON. When it is, you cannot run the tool, so report the failure back to Claude instead. The `content` of a tool result does not have to be JSON, but wrapping the raw string in a JSON object under a single key makes it unambiguous to Claude that you received invalid JSON, and preserves the original input for debugging:

```python
{
  "INVALID_JSON": "<the unparseable input you received>"
}
```



Return the wrapper, serialized to a string, as the `content` of a [tool result](agents-and-tools-tool-use-handle-tool-calls.md#handling-errors-with-is-error) content block with `is_error` set to `true`:

```python
{
  "type": "tool_result",
  "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
  "is_error": true,
  "content": "{\"INVALID_JSON\": \"<the unparseable input you received>\"}"
}
```





Build the wrapper with your JSON library rather than by concatenating strings, so quotes and other special characters in the invalid input are escaped correctly.

## Next steps



[Context windows](../Guides/build-with-claude-context-windows.md)

Understand how the context window works, how extended thinking and tool use count toward it, and how to manage context as conversations grow.



[Streaming messages](../Guides/build-with-claude-streaming.md)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.

[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)

Parse `tool_use` blocks, format `tool_result` responses, and handle errors with `is_error`.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.

## Availability

Fine-grained tool streaming is available on every model and eligible for zero data retention and HIPAA readiness.

### API support

[Messages API](../Guides/build-with-claude-working-with-messages.md)

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)InvokeModel
- [Claude Models on Google Cloud](../Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

HIPAAEligible
