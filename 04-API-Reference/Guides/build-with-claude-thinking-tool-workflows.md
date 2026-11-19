---
title: "Thinking in tool and multi-turn workflows - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/thinking-tool-workflows"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-13T06:34:00Z"
tags: ["api"]
---

# Thinking in tool and multi-turn workflows

Copy page



Walk through a complete two-turn tool-use round trip that preserves thinking blocks correctly, and see how interleaved thinking changes the flow.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

This page walks through a complete two-turn tool-use round trip with thinking enabled. Claude thinks, requests a tool call, receives the result, and finishes its answer. At every step, your code handles the thinking blocks correctly. The full rules are on the Thinking page, in [Thinking with tool use](build-with-claude-thinking.md#thinking-with-tool-use) and [Preserving thinking blocks](build-with-claude-thinking.md#preserving-thinking-blocks).

## The rules this walkthrough applies

Each rule links to its full statement:

- [Limit tool choice to `auto` or `none` in manual mode](build-with-claude-thinking.md#thinking-with-tool-use): with manual extended thinking (`thinking: {type: "enabled"}`), `tool_choice` options that force tool use return an error.
- [Check forced tool use on your model in adaptive mode](build-with-claude-thinking.md#thinking-with-tool-use): with adaptive thinking, the result depends on the model:
  - **Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.2, Claude Mythos 5.2, Claude Fable 5.1, and Claude Mythos 5.1:** Forced tool use returns a 400 error.
  - **Other models:** Forced tool use is accepted, and it skips thinking. The response starts with the tool call.
- [Keep one thinking configuration per assistant turn](build-with-claude-thinking.md#thinking-with-tool-use): a tool-use loop is one assistant turn, so change the configuration only between turns.
- [Pass thinking blocks back complete and unmodified](build-with-claude-thinking.md#preserving-thinking-blocks): when you return a tool result, the thinking blocks from the assistant message must come back with it.
- [Echo the assistant message exactly as received](build-with-claude-thinking.md#preserving-thinking-blocks): dropping thinking blocks loses the reasoning in them, even without an error.

The samples use adaptive thinking. On Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, and earlier Claude 4 models, substitute `thinking: {type: "enabled", budget_tokens: N}`. Echo the assistant turn the same way.

## Walk through a two-turn tool-use round trip

The example defines a `get_weather` tool, lets Claude think and request a tool call, then returns the tool result with the assistant turn echoed exactly as received, thinking block included.

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

    Python

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

    # First request: Claude responds with thinking and tool request
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[weather_tool],
        messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    )
    print(response)
    ```

2.  2

    ### Capture the content array to echo back

    You should see `thinking` and `tool_use` blocks in the response content on a run that includes thinking (on simpler requests, adaptive mode might skip the thinking block). A note Claude writes before the tool call comes back as a `text` block or, on models that write [progress updates](build-with-claude-thinking.md#progress-updates), as another `thinking` block. Keep this content array intact: the next step sends it back verbatim.

    
    To see thinking text like this output, add `display: "summarized"` to the request. On models where display defaults to omitted, including Claude Opus 5.5, the `thinking` field otherwise comes back as an empty string with only the `signature` populated. Either way, echo the content array back unchanged; see [Controlling thinking display](build-with-claude-thinking.md#controlling-thinking-display).

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

    Python

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
        model="claude-opus-5-5",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        tools=[weather_tool],
        messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    )
    # Extract the tool use block to get its ID for the tool result
    tool_use_block = next(block for block in response.content if block.type == "tool_use")

    # This is where your actual weather API call would go
    # Pretend this is what the weather API returns
    weather_data = {"temperature": 88}

    # Second request: include the assistant turn and the tool result
    continuation = client.messages.create(
        model="claude-opus-5-5",
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

### Tool use without interleaved thinking

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

### Tool use with interleaved thinking

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

Manual thinking budgets: `budget_tokens` mechanics and migration to adaptive thinking.
