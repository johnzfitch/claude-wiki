---
title: "Fine-grained tool streaming - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:25Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ffine-grained-tool-streaming)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Tool infrastructure

# Fine-grained tool streaming

Copy page



Stream tool inputs without server-side JSON buffering for latency-sensitive applications.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

Fine-grained tool streaming delivers a tool's input to your client as Claude generates it, without server-side buffering or JSON validation. Skipping the buffering step reduces the time to the first fragment of a large parameter, such as a document or a block of code, and the fragments arrive through the same [Streaming messages](../Guides/build-with-claude-streaming.md) events as standard tool use.



Because the API does not buffer or validate a tool's input before streaming it, you might receive partial or invalid JSON. A response that ends with the [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) `max_tokens` can also cut a parameter off midway. Accumulate the fragments, guard the parse, and see [Handling invalid JSON in tool responses](#handling-invalid-json-in-tool-responses) for how to return unparseable input to Claude.

## How to use fine-grained tool streaming

All models support fine-grained tool streaming on the Claude API, [Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). To use it, set `eager_input_streaming` to `true` on any user-defined tool where you want fine-grained streaming enabled, and enable streaming on your request.

The `eager_input_streaming` field is optional. Setting it to `true` turns on fine-grained streaming for that tool, and omitting it gives you standard buffered streaming, in which the API buffers and validates each parameter value before streaming it back. The exception is a request that still sends the legacy `fine-grained-tool-streaming-2025-05-14` beta header, which turns fine-grained streaming on for tools that leave the field unset. The per-tool field replaces that header, and an explicit `false` keeps buffered streaming for a tool even when a request still sends it. The legacy header cannot be combined with a [computer use](agents-and-tools-tool-use-computer-use-tool.md) or [browser use](agents-and-tools-tool-use-browser-use-tool.md) toolset entry: the API rejects a request that sends both, so remove the header and set `eager_input_streaming` on the user-defined tools that need it. See [Tool reference](agents-and-tools-tool-use-tool-reference.md) for the field definition.

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

Every tab turns on fine-grained streaming for the `make_file` tool. The SDK tabs print each input fragment the moment it arrives, then print the complete accumulated input once the stream ends. The cURL tab shows the raw event stream, and the CLI tab uses `jq` to print just the fragments. Because the printed fragments join into the full tool input, the poem fills your terminal as Claude writes it:

```python
{"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", "", "I.", "", "Beneath the vast and star-strewn sky,", "Where silver moonbeams softly lie,", ...
Complete tool input: {"filename": "poem.txt", "lines_of_text": ["The Wanderer's Journey", ...]}
```



Without `eager_input_streaming`, the API buffers and validates each parameter value before streaming it back, so nothing prints for a large parameter until Claude has finished generating it. With it, fragments start arriving as soon as Claude begins the parameter, and they are typically longer, with fewer mid-word breaks.

## Accumulating tool input deltas

The accumulation contract is the same as for standard tool-use streaming, so this section applies with and without `eager_input_streaming`. See [Input JSON delta](../Guides/build-with-claude-streaming.md#input-json-delta) in Streaming messages for the event format. Fine-grained tool streaming changes what you can assume about the result: the server streams fragments without validating them, so the accumulated string might not be valid JSON.

When a `tool_use` content block streams, the initial `content_block_start` event contains `input: {}` (an empty object). This is a placeholder. The actual input arrives as a series of `input_json_delta` events, each carrying a `partial_json` string fragment. To assemble the full input, concatenate these fragments and parse the result when the block closes.

Where your SDK provides an accumulator helper (as the Python, TypeScript, Go, Java, and Ruby tabs in the previous example do), it handles this for you. The manual pattern is for SDKs without a helper, or when you want full control over how the input is assembled.

The accumulation contract:

1.  On `content_block_start` with `type: "tool_use"`, initialize an empty string: `input_json = ""`
2.  For each `content_block_delta` with `type: "input_json_delta"`, append: `input_json += event.delta.partial_json`
3.  On `content_block_stop`, parse the accumulated string

Guard the parse, as the following SDK examples do. A response can also stop at `max_tokens` midway through a parameter. Check the [stop reason](../Guides/build-with-claude-handling-stop-reasons.md) and decide whether to retry the request with a higher `max_tokens` or repair the partial input.

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

Parse tool_use blocks, format tool_result responses, and handle errors with is_error.



[Tool reference](agents-and-tools-tool-use-tool-reference.md)

Directory of Anthropic-provided tools and reference for optional tool definition properties.
