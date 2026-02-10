::: {.cell .markdown}
# Tool Search: Alternate Approaches

**Recommend first reading see the cookbook: Tool Search with
Embeddings.**

The goal of this cookbook is to show of some alternate approaches to
using tool search (or really \"tool discovery\") with Claude. In this
cookbook we\'ll demonstrate two useful techniques:

1.  Tools can be discovered without \"Search\". In this cookbook, we\'ll
    include all of the tool names in Claude\'s system prompt and provide
    Claude with decribe_tool_tool to load the tool fully into Claude\'s
    context.
2.  Tools do not have to be passed in the request\'s `tools` list if
    they have not been loaded into Claude\'s context yet. This can be a
    bit more application complexity to manage, but can allow your
    application to keep requests small, even while Claude has potential
    access to thousands of tools.

Users have a lot of flexibility to design tool search to keep Claude\'s
context (and Messages requests) as focused as possible.

## Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

- Python fundamentals - comfortable with functions, dictionaries, and
  basic data structures
- Basic understanding of Claude tool use - we recommend reading the
  [Tool Use
  Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
  first

**Required Tools**

- Python 3.11 or higher
- Anthropic API key ([get one
  here](https://docs.anthropic.com/claude/reference/getting-started-with-the-api))
:::

::: {.cell .code}
``` python
%pip install -q anthropic python-dotenv
```
:::

::: {.cell .code}
``` python
import anthropic
import json
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-sonnet-4-5-20250929"
client = anthropic.Anthropic()

print("✓ Client initialized")
```
:::

::: {.cell .markdown}
## Define Tool Library

We\'ll define 5 simple tools. In production, this could be hundreds or
thousands of tools stored in a database or configuration file.
:::

::: {.cell .code}
``` python
TOOL_LIBRARY = {
    "get_weather": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
            },
            "required": ["city"],
        },
    },
    "get_stock_price": {
        "name": "get_stock_price",
        "description": "Get current stock price for a ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string", "description": "Stock ticker (e.g., AAPL)"},
            },
            "required": ["ticker"],
        },
    },
    "convert_currency": {
        "name": "convert_currency",
        "description": "Convert amount between currencies",
        "input_schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "from_currency": {"type": "string"},
                "to_currency": {"type": "string"},
            },
            "required": ["amount", "from_currency", "to_currency"],
        },
    },
    "calculate_tip": {
        "name": "calculate_tip",
        "description": "Calculate tip amount for a bill",
        "input_schema": {
            "type": "object",
            "properties": {
                "bill_amount": {"type": "number"},
                "tip_percent": {"type": "number", "default": 20},
            },
            "required": ["bill_amount"],
        },
    },
    "send_email": {
        "name": "send_email",
        "description": "Send an email to a recipient",
        "input_schema": {
            "type": "object",
            "properties": {
                "to": {"type": "string", "description": "Recipient email"},
                "subject": {"type": "string"},
                "body": {"type": "string"},
            },
            "required": ["to", "subject", "body"],
        },
    },
}

print(f"✓ Defined {len(TOOL_LIBRARY)} tools: {list(TOOL_LIBRARY.keys())}")
```
:::

::: {.cell .markdown}
## The `describe_tool` Tool

Instead of semantic search, we give Claude a simple `describe_tool`
tool. Claude calls this with a tool name to load that tool into context.

The system prompt lists all available tool names, so Claude knows
what\'s available without needing embeddings or search.
:::

::: {.cell .code}
``` python
DESCRIBE_TOOL = {
    "name": "describe_tool",
    "description": "Load a tool's full definition into context. Call this before using any tool for the first time.",
    "input_schema": {
        "type": "object",
        "properties": {
            "tool_name": {
                "type": "string",
                "description": "Name of the tool to load",
            },
        },
        "required": ["tool_name"],
    },
}

# Build system prompt with tool catalog
tool_names = list(TOOL_LIBRARY.keys())
SYSTEM_PROMPT = f"""You are a helpful assistant with access to various tools.

Available tools: {', '.join(tool_names)}

Before using any tool, you must first call describe_tool with the tool name to load it."""

print("System prompt:")
print(SYSTEM_PROMPT)
```
:::

::: {.cell .markdown}
## Mock Tool Execution

Simple mock responses for demonstration:
:::

::: {.cell .code}
``` python
def execute_tool(name: str, inputs: dict) -> str:
    """Mock tool execution."""
    if name == "get_weather":
        return json.dumps({"city": inputs["city"], "temp": "72°F", "conditions": "Sunny"})
    elif name == "get_stock_price":
        return json.dumps({"ticker": inputs["ticker"], "price": 185.50, "change": "+1.2%"})
    elif name == "convert_currency":
        rate = 0.92 if inputs["to_currency"] == "EUR" else 1.0
        converted = inputs["amount"] * rate
        return json.dumps({"converted": round(converted, 2), "to": inputs["to_currency"]})
    elif name == "calculate_tip":
        tip = inputs["bill_amount"] * (inputs.get("tip_percent", 20) / 100)
        return json.dumps({"tip": round(tip, 2), "total": round(inputs["bill_amount"] + tip, 2)})
    elif name == "send_email":
        return json.dumps({"status": "sent", "to": inputs["to"]})
    return json.dumps({"error": f"Unknown tool: {name}"})

print("✓ Mock execution ready")
```
:::

::: {.cell .markdown}
## Conversation Loop with Dynamic Tool Loading

The key pattern here:

1.  **Start with only `describe_tool`** in the tools list
2.  **When Claude calls `describe_tool`**, return a `tool_reference` AND
    add the tool to `active_tools` with `defer_loading=True`
3.  **`defer_loading=True` is critical** - it keeps the tool definition
    out of the cached prompt prefix, avoiding cache invalidation when
    tools are discovered

Every time Claude sees a `tool_reference` in the conversation, the full
tool definition is loaded into Claude\'s context at that point in the
conversation.
:::

::: {.cell .code}
``` python
def run_conversation(user_message: str, max_turns: int = 10):
    """Run a conversation with dynamic tool loading."""
    print(f"\n{'='*60}")
    print(f"USER: {user_message}")
    print(f"{'='*60}\n")

    messages = [{"role": "user", "content": user_message}]
    
    # Start with ONLY describe_tool - no other tools in the request
    active_tools = [DESCRIBE_TOOL]
    loaded_tools = set()  # Track which tools we've added

    for turn in range(max_turns):
        print(f"--- Turn {turn + 1} (tools in request: {len(active_tools)}) ---")

        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=active_tools,
            messages=messages,
            extra_headers={"anthropic-beta": "advanced-tool-use-2025-11-20"},
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            for block in response.content:
                if block.type == "text":
                    print(f"\nASSISTANT: {block.text}")
            break

        # Process tool calls
        tool_results = []
        for block in response.content:
            if block.type == "text" and block.text:
                print(f"ASSISTANT: {block.text}")
            
            elif block.type == "tool_use":
                tool_name = block.name
                tool_input = block.input

                if tool_name == "describe_tool":
                    requested_tool = tool_input["tool_name"]
                    print(f"🔍 describe_tool({requested_tool})")

                    if requested_tool in TOOL_LIBRARY:
                        # Add tool to active_tools with defer_loading=True
                        # This is critical for prompt caching!
                        if requested_tool not in loaded_tools:
                            tool_def = {**TOOL_LIBRARY[requested_tool], "defer_loading": True}
                            active_tools.append(tool_def)
                            loaded_tools.add(requested_tool)
                            print(f"   ✓ Added {requested_tool} to tools (defer_loading=True)")

                        # Return tool_reference so Claude can use it
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": [{"type": "tool_reference", "tool_name": requested_tool}],
                        })
                    else:
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": f"Tool '{requested_tool}' not found.",
                        })
                else:
                    # Execute discovered tool
                    print(f"🔧 {tool_name}({json.dumps(tool_input)})")
                    result = execute_tool(tool_name, tool_input)
                    print(f"   → {result}")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

        if tool_results:
            messages.append({"role": "user", "content": tool_results})

    print(f"\n{'='*60}\n")

print("✓ Conversation loop ready")
```
:::

::: {.cell .markdown}
## Example: Weather Query

Watch how Claude:

1.  Sees `get_weather` in the system prompt\'s tool list
2.  Calls `describe_tool("get_weather")` to load it
3.  Receives the `tool_reference` and can now use the tool
:::

::: {.cell .code}
``` python
run_conversation("What's the weather in Tokyo?")
```
:::

::: {.cell .markdown}
## Example: Multi-Tool Query

Claude can load multiple tools as needed:
:::

::: {.cell .code}
``` python
run_conversation("Convert $100 to EUR, then calculate a 20% tip on a $85 dinner bill.")
```
:::

::: {.cell .markdown}
## Why `defer_loading=True` Matters

When you add a tool to the `tools` list, the tool definition is normally
loaded into the very beginning of Claude\'s context window. If you add
new tools, you will lose most of the cache because the very beginning of
the context window has changed.

**With `defer_loading=True`:**

- The tool definition is NOT included into the beginning of Claude\'s
  context window.
- Instead, it\'s loaded into context when Claude sees the
  `tool_reference`
- This means your system prompt and initial tools stay cached even as
  you discover new tools

**The pattern:**

``` python
# Initial request - only describe_tool, system prompt is cached
tools = [DESCRIBE_TOOL]

# After Claude calls describe_tool("get_weather")
# Add with defer_loading to preserve cache
tools.append({**TOOL_LIBRARY["get_weather"], "defer_loading": True})

# Return tool_reference so Claude knows it's available
tool_result = [{"type": "tool_reference", "tool_name": "get_weather"}]
```

This is essential for applications with hundreds or thousands of tools
where you want to:

- Keep initial request size small
- Preserve prompt caching across tool discoveries
- Only load tools Claude actually needs
:::

::: {.cell .markdown}
## Conclusion

The key insight from this cookbook: **tools don\'t need to be in the
`tools` list until Claude needs them**. Combined with
`defer_loading=True` and `tool_reference`, this lets you scale to
thousands of tools while keeping requests small and preserving prompt
caching. However, in this case your client will need to provide a tool
discovery mechanism.

The `describe_tool` approach shown here is just one flavor. Other
patterns include:

- **`list_tools`** - Returns tool names matching a category or keyword
- **Hierarchical discovery** - Browse tool categories, then load
  specific tools
- **Hybrid** - Combine listing with semantic search for large catalogs

The core pattern is always:

1.  Return `tool_reference` when a tool is discovered
2.  Add the tool with `defer_loading=True` to preserve caching
3.  Claude can then use the tool immediately

See [Tool Search with Embeddings](./tool_search_with_embeddings.ipynb)
for the embeddings-based approach.
:::
