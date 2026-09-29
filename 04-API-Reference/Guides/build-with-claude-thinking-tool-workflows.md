---
title: "Thinking in tool and multi-turn workflows - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/thinking-tool-workflows"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:37Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fthinking-tool-workflows)

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

[Overview](build-with-claude-thinking.md)[Steering and cost control](build-with-claude-thinking-steering-and-cost.md)[Tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md)[Preserved thinking](build-with-claude-preserved-thinking.md)[Troubleshooting](build-with-claude-thinking-troubleshooting.md)[Extended thinking (legacy)](build-with-claude-extended-thinking.md)

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

[Messages](../../01-Getting-Started/intro.md)Thinking

# Thinking in tool and multi-turn workflows

Copy page



Walk through a complete two-turn tool-use round trip that preserves thinking blocks correctly, and see how interleaved thinking changes the flow.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

This page walks through a complete two-turn tool-use round trip with thinking enabled: Claude thinks, requests a tool call, receives the result, and finishes its answer, with the thinking blocks handled correctly at every step. The full rules live on the [Thinking](build-with-claude-thinking.md) page, in [Thinking with tool use](build-with-claude-thinking.md#thinking-with-tool-use) and [Preserving thinking blocks](build-with-claude-thinking.md#preserving-thinking-blocks); this page shows those rules applied in runnable code.

## The rules this walkthrough applies

Each link leads to the full statement on the Thinking page:

- [Limit tool choice to `auto` or `none` in manual mode](build-with-claude-thinking.md#thinking-with-tool-use): `tool_choice` options that force tool use return an error with manual extended thinking (`thinking: {type: "enabled"}`); adaptive thinking supports forced tool use.
- [Keep one thinking configuration per assistant turn](build-with-claude-thinking.md#thinking-with-tool-use): a tool-use loop is one assistant turn, so change the configuration only between turns.
- [Pass thinking blocks back complete and unmodified](build-with-claude-thinking.md#preserving-thinking-blocks): when you return a tool result, the thinking blocks from the assistant message must come back with it.
- [Echo the assistant message exactly as received](build-with-claude-thinking.md#preserving-thinking-blocks): rebuilding the message or filtering out `redacted_thinking` blocks triggers a 400 error.

The samples use adaptive thinking; on models that support only extended thinking, substitute `thinking: {type: "enabled", budget_tokens: N}`. The round-trip rules are identical.

## Walk through a two-turn tool-use round trip

The example defines a `get_weather` tool, lets Claude think and request a tool call, then returns the tool result along with the assistant turn echoed exactly as received, thinking block included.

1.  1

    ### Make the first request with a tool available

    Send a request with adaptive thinking enabled and the tool defined. Apart from the `thinking` parameter, this is a standard [tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md) request:

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

    ``` shiki
    client = anthropic.Anthropic()

    weather_tool = {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {"location": {"type": "string", "description": "City name"}},
            "required": ["location"],
        },
    }

    # First request - Claude responds with thinking and tool request
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[weather_tool],
        messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    )
    print(response)
    ```

2.  2

    ### Capture the content array to echo back

    You should see `thinking`, `text`, and `tool_use` blocks in the response content on a run where Claude chose to think (on simpler requests, adaptive mode may skip the thinking block). Keep this content array intact: the next step sends it back verbatim.

    
    To see thinking text like this output, add `display: "summarized"` to the request. On models where display defaults to omitted, including claude-opus-4-8, the `thinking` field otherwise comes back as an empty string with only the `signature` populated. Either way, echo the content array back unchanged; see [Controlling thinking display](build-with-claude-thinking.md#controlling-thinking-display).

    Output

    

    ``` shiki
    {
      "content": [
        {
          "type": "thinking",
          "thinking": "The user wants to know the current weather in Paris. I have access to a function `get_weather`...",
          "signature": "BDaL4VrbR2Oj0hO4XpJxT28J5T...."
        },
        {
          "type": "text",
          "text": "I can help you get the current weather information for Paris. Let me check that for you"
        },
        {
          "type": "tool_use",
          "id": "toolu_01CswdEQBMshySk6Y9DFKrfq",
          "name": "get_weather",
          "input": {
            "location": "Paris"
          }
        }
      ]
    }
    ```

3.  3

    ### Return the tool result, echoing the assistant turn verbatim

    Run the tool on your side, then send a second request that appends two messages to the conversation. The first is the assistant content echoed back exactly as received, so the thinking block stays unchanged alongside the `tool_use` block. The second is a user message carrying the `tool_result`.

    Each sample is a self-contained script: it repeats the first request, then immediately sends the follow-up using the response it just received.

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

    ``` shiki
    client = anthropic.Anthropic()
    weather_tool = {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {"location": {"type": "string", "description": "City name"}},
            "required": ["location"],
        },
    }
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[weather_tool],
        messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    )
    # Extract the tool use block to get its ID for the tool result
    tool_use_block = next(block for block in response.content if block.type == "tool_use")

    # Call your actual weather API, here is where your actual API call would go
    # Let's pretend this is what we get back
    weather_data = {"temperature": 88}

    # Second request - Include the assistant turn and the tool result
    continuation = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[weather_tool],
        messages=[
            {"role": "user", "content": "What's the weather in Paris?"},
            # Echo the assistant content exactly as received. When a thinking
            # block is present, it must accompany the tool_use block.
            {"role": "assistant", "content": response.content},
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
    print(continuation)
    ```

4.  4

    ### Read the final response

    You should see Claude complete the turn with text. Because [interleaved thinking](build-with-claude-thinking.md#interleaved-thinking) is automatic in adaptive mode, the continuation can also open with a new thinking block before the final text:

    Output

    

    ``` shiki
    {
      "content": [
        {
          "type": "text",
          "text": "Currently in Paris, the temperature is 88°F (31°C)"
        }
      ]
    }
    ```

## How interleaved thinking changes the flow

Interleaved thinking lets Claude think between tool calls, reasoning about each tool result before acting on it. The concept and per-model availability are covered in [Interleaved thinking](build-with-claude-thinking.md#interleaved-thinking) on the Thinking page; interleaving changes where thinking blocks appear, not whether tool calls can chain. The following comparison shows what interleaved thinking changes in a two-tool workflow:

### Tool use without interleaved thinking

Without interleaved thinking, Claude thinks once at the start of the assistant turn. Subsequent responses after tool results continue without new thinking blocks.

``` inline-block
User: "What's the total revenue if we sold 150 units at $50 each,
       and how does this compare to our average monthly revenue?"

Response 1: [thinking] "I need to calculate 150 * $50, then check the database..."
            [tool_use: calculator] { "expression": "150 * 50" }
  ↓ tool result: "7500"

Response 2: [tool_use: database_query] { "query": "SELECT AVG(revenue)..." }
            ↑ no thinking block
  ↓ tool result: "5200"

Response 3: [text] "The total revenue is $7,500, which is 44% above your
            average monthly revenue of $5,200."
            ↑ no thinking block
```



### Tool use with interleaved thinking

With interleaved thinking enabled, Claude can think after receiving each tool result, allowing it to reason about intermediate results before continuing.

``` inline-block
User: "What's the total revenue if we sold 150 units at $50 each,
       and how does this compare to our average monthly revenue?"

Response 1: [thinking] "I need to calculate 150 * $50 first..."
            [tool_use: calculator] { "expression": "150 * 50" }
  ↓ tool result: "7500"

Response 2: [thinking] "Got $7,500. Now I should query the database to compare..."
            [tool_use: database_query] { "query": "SELECT AVG(revenue)..." }
            ↑ thinking after receiving calculator result
  ↓ tool result: "5200"

Response 3: [thinking] "$7,500 vs $5,200 average - that's a 44% increase..."
            [text] "The total revenue is $7,500, which is 44% above your
            average monthly revenue of $5,200."
            ↑ thinking before final answer
```



## Next steps



[Thinking](build-with-claude-thinking.md)

The overview: turn thinking on, read thinking output, and review the full rules for tool use, caching, and streaming.

[Steering thinking](build-with-claude-thinking-steering-and-cost.md)

Steer how often and how deeply Claude thinks with effort levels and prompt-based guidance.



[Extended thinking](build-with-claude-extended-thinking.md)

Manual thinking budgets on older models: `budget_tokens` mechanics and migration to adaptive.
