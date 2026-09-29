---
title: "Tool runner (SDK) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:28Z"
tags: ["api", "sdk"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Ftool-runner)

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

[Messages](../../01-Getting-Started/intro.md)Tools

# Tool runner (SDK)

Copy page



Use the SDK's tool runner to handle the agentic loop, error wrapping, and type safety automatically.

Copy page



The tool runner handles the agentic loop, error wrapping, and type safety so you don't have to. When you need human-in-the-loop approval, custom logging, or conditional execution, use the [manual loop](agents-and-tools-tool-use-handle-tool-calls.md) instead.

Instead of manually handling tool calls, tool results, and conversation management, the tool runner automatically:

- Runs tools when Claude calls them
- Handles the request/response cycle
- Manages conversation state
- Provides type safety and validation



The tool runner is in beta and available in the [Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md), [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers), [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp/blob/main/examples/ToolRunnerExample/Program.cs), [Go SDK](https://github.com/anthropics/anthropic-sdk-go/blob/main/tools.md), [Java SDK](https://github.com/anthropics/anthropic-sdk-java/blob/main/anthropic-java-example/src/main/java/com/anthropic/example/BetaToolRunnerRunnableToolExample.java), [PHP SDK](https://github.com/anthropics/anthropic-sdk-php/blob/main/examples/beta/beta_tool_runner.php), and [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby/blob/main/helpers.md#3-auto-looping-tool-runner-beta).

## Basic usage

Define tools using the SDK helpers, then use the tool runner to run them.

Depending on the SDK's tool signature, a tool returns its result as a string or as content blocks (text, image, or document blocks), so a tool can return multimodal results. A returned string becomes a single text content block. To return structured data, such as a JSON object or a number, encode it as a string first.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Use the `@beta_tool` decorator to define tools with type hints and docstrings.



If you're using the async client, replace `@beta_tool` with `@beta_async_tool` and define the function with `async def`.

```python
import json
from anthropic import Anthropic, beta_tool

client = Anthropic()


@beta_tool
def get_weather(location: str, unit: str = "fahrenheit") -> str:
    """Get the current weather in a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: Temperature unit, either 'celsius' or 'fahrenheit'
    """
    return json.dumps({"temperature": "20°C", "condition": "Sunny"})


@beta_tool
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return str(a + b)


runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
        {
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
        }
    ],
)
for message in runner:
    print(message)
```



The `@beta_tool` decorator inspects the function arguments and docstring to derive the JSON schema for you.

## Iterating over the tool runner

The tool runner is an iterable that yields messages from Claude. On each iteration, the runner checks whether Claude requested a tool use. If so, it runs the tool and sends the result back to Claude automatically, then yields the next message from Claude to continue your loop.

You can end the loop at any iteration with a `break` statement. The runner loops until Claude returns a message without a tool use, or until it reaches `max_iterations` if you set it.

If you don't need intermediate messages, you can get the final message directly:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Use `runner.until_done()` to get the final message.

```python
client = anthropic.Anthropic()
# ...
runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
        {
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
        }
    ],
)
final_message = runner.until_done()
for block in final_message.content:
    if block.type == "text":
        print(block.text)
```



## Advanced usage

Within the loop, you can read each response message and modify the runner's state before the next API call. Each iteration follows this lifecycle:

1.  The runner sends a request to the Messages API with its current state.
2.  The runner yields the response message to your loop body.
3.  Your loop body runs. You can read the message and optionally modify the runner's state.
4.  When your loop body returns, the runner checks whether you modified its message history.
    - **If you did not modify message history:** If the message contains tool calls, the runner appends the assistant message and the tool results, then continues. If there are no tool calls, the loop exits.
    - **If you modified message history:** The runner skips its automatic append and uses your state unchanged. See [Taking over message history](#taking-over-message-history).

### Taking over message history

By default, the runner manages conversation state for you: after each tool-call turn, it appends the assistant message and any tool results to its own message history. You take over message history when you want to retry a turn (discard the response and resend), inject a follow-up message, or build the tool result yourself.

You take over by modifying the runner's messages from inside the loop body. The exact method depends on the SDK. See the per-language tabs that follow.

When you take over for an iteration, the runner does not append the assistant message or tool results from that turn. You become responsible for keeping the conversation valid: append the assistant message and a tool result yourself (if you want the turn to count), modify state conditionally so the loop can still exit when there are no tool calls, and pass `max_iterations` to bound the loop. All seven SDKs support `max_iterations`.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Use `generate_tool_call_response()` to inspect or compute the tool result. Calling `append_messages()` inside the loop tells the runner you're managing history yourself, so include the assistant message and tool result in what you append.

```python
runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    max_iterations=10,
    tools=[get_weather],
    messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()
    if tool_response is not None:
        # append_messages() flags state as modified, so the runner skips its
        # automatic append for this iteration. Append the assistant message and
        # tool result yourself, plus any follow-up.
        runner.append_messages(
            message,
            tool_response,
            {"role": "user", "content": "Please be concise."},
        )
    # When there's no tool call, leave state untouched so the loop exits.
```



To change request parameters such as `max_tokens` without taking over message history, use `set_messages_params()`. The runner still appends the assistant message and tool result automatically.

```python
for message in runner:
    runner.set_messages_params(lambda params: {**params, "max_tokens": 2048})
```



### Automatic context management

For long-running agentic tasks, the TypeScript and Ruby tool runners support automatic [compaction](../Guides/build-with-claude-context-editing.md#client-side-compaction-sdk), which generates summaries when token usage exceeds a threshold so the conversation can continue beyond context window limits. Both SDKs have deprecated this client-side option in favor of [server-side compaction](../Guides/build-with-claude-compaction-threshold.md), which works with every SDK's tool runner through the `context_management` request parameter. The Python SDK (v1.0 and later) and the Go, Java, C#, and PHP tool runners don't include client-side compaction. The Python, TypeScript, C#, Go, Java, PHP, and Ruby tool runners have a `compact_before_next_turn()` helper for on-demand compaction. See [Compact in a loop](../Guides/build-with-claude-compaction-on-demand.md#compact-in-a-loop). Use it or a `context_management` compaction edit on a runner, not both.

### Debugging tool execution

When a tool throws an exception, the tool runner catches it and returns the error to Claude as a tool result with `is_error: true`. The tool result carries the exception's message (in Python, its type and message), not the full stack trace.

What the SDK logs is language-specific. The Python SDK logs the full exception, including its stack trace, through the standard `logging` module whenever a tool raises an unhandled exception. The Python, TypeScript, and Java SDKs read the `ANTHROPIC_LOG` environment variable to turn on the SDK's logging, which includes request and response detail:

```python
# Log at info level
export ANTHROPIC_LOG=info

# Log at debug level for more verbose output
export ANTHROPIC_LOG=debug
```



The Go, Ruby, C#, and PHP SDKs don't read `ANTHROPIC_LOG`. Outside Python, no SDK logs a failed tool: to see why a tool failed, catch and log the exception inside the tool function before returning or rethrowing it.

### Intercepting tool errors

By default, tool errors are passed back to Claude, which can then respond appropriately. However, you might want to detect errors and handle them differently, for example, to stop execution early or implement custom error handling.

In the Python and TypeScript SDKs, use the tool response method (`generate_tool_call_response()` in Python, `generateToolResponse()` in TypeScript) to intercept tool results and check for errors before they're sent to Claude. The other SDKs don't expose that hook. Their tabs describe the closest alternative:

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
client = anthropic.Anthropic()
# ...
runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[my_tool],
    messages=[{"role": "user", "content": "Run my_tool with the query 'hello'."}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Check if any tool result has an error
        for block in tool_response["content"]:
            if block.get("is_error"):
                # Option 1: Raise an exception to stop the loop
                raise RuntimeError(f"Tool failed: {json.dumps(block['content'])}")

                # Option 2: Log and continue (let Claude handle it)
                # logger.error(f"Tool error: {json.dumps(block['content'])}")

    # Process the message normally
    print(message.content)
```



### Modifying tool results

You can modify tool results before they're sent back to Claude. This is useful for adding metadata such as `cache_control` to enable [prompt caching](../Guides/build-with-claude-prompt-caching.md) on tool results, or for transforming the tool output.

In the Python and TypeScript SDKs, use the tool response method to get the tool result, then modify it before the runner proceeds. Whether you explicitly append the modified result or mutate it in place depends on the SDK. See the code comments in each tab.

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
client = anthropic.Anthropic()
# ...
runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[search_documents],
    messages=[
        {
            "role": "user",
            "content": "Search for information about the climate of San Francisco",
        }
    ],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Modify the tool result to add cache control
        for block in tool_response["content"]:
            if block["type"] == "tool_result":
                # Add cache_control to cache this tool result
                block["cache_control"] = {"type": "ephemeral"}

        # Append the modified response (this prevents auto-append of the original)
        runner.append_messages(message, tool_response)

    print(message.content)
```





Adding `cache_control` to tool results is particularly useful when tools return large amounts of data (such as document search results) that you want to cache for subsequent API calls. See [Prompt caching](../Guides/build-with-claude-prompt-caching.md) for more details on caching strategies.

## Streaming

Enable streaming to process each turn's response incrementally. Each iteration yields a stream object that you can iterate for events.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Set `stream=True` and use `get_final_message()` to get the accumulated message.

```python
client = anthropic.Anthropic()
# ...
runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=1024,
    tools=[calculate_sum],
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    stream=True,
)

# When streaming, the runner returns BetaMessageStream
for message_stream in runner:
    for event in message_stream:
        print("event:", event)
    print("message:", message_stream.get_final_message())

print(runner.until_done())
```



## Next steps



[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)

Enforce JSON Schema compliance on Claude's tool inputs with grammar-constrained sampling.

[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)

Parse `tool_use` blocks, format `tool_result` responses, and handle errors with `is_error`.



[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)

Enable, format, and disable parallel tool calls, with message-history guidance and troubleshooting.



[Define tools](agents-and-tools-tool-use-implement-tool-use.md)

Specify tool schemas, write effective descriptions, and control when Claude calls your tools.
