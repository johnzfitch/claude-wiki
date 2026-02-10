::: {#4126045b .cell .markdown}
# Programatic Tool Calling (PTC) with the Claude API

Programmatic Tool Calling (PTC) allows Claude to write code that calls
tools programmatically within the Code Execution environment, rather
than requiring round-trips through the model for each tool invocation.
This substantially reduces end-to-end latency for multiple tool calls,
and can dramatically reduce token consumption by allowing the model to
write code that removes irrelevant context before it hits the model's
context window (for example, by grepping for key information within
large and noisy files).

When faced with third-party APIs and tools that you may not be able to
modify directly, PTC can help reduce usage of context by allowing Claude
to write code that can be invoked in the Code Execution environment.

In this cookbook, we will work with a mock API for team expense
management. The API is designed to require multiple invocations and will
return large results which help illustrate the benefits of Programmatic
Tool Calling.
:::

::: {#4d7e647f .cell .markdown}
## By the end of this cookbook, you\'ll be able to:

- Understand the difference between regular tool calling and programatic
  tool calling (PTC)
- Write agents that leverage PTC
:::

::: {#e0e31236 .cell .markdown}
## Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

- Python fundamentals - comfortable with async/await, functions, and
  basic data structures
- Basic understanding of agentic patterns and tool calling

**Required Tools**

- Python 3.11 or higher
- Anthropic API key
- Anthropic Python SDK \>= 0.72
:::

::: {#43e53178 .cell .markdown}
## Setup

First, install the required dependencies:
:::

::: {#fa190a78 .cell .code}
``` python
# %pip install -r requirements.txt
```
:::

::: {#5d24e94e .cell .markdown}
Note: Ensure your .env file contains:

`ANTHROPIC_API_KEY=your_key_here`

Load your environment variables and configure the client. We also load a
helper utility to visualize Claude message responses.
:::

::: {#3a1f5033 .cell .code execution_count="2"}
``` python
from dotenv import load_dotenv
from utils.visualize import visualize

load_dotenv()

MODEL = "claude-sonnet-4-5"

viz = visualize(auto_show=True)
```
:::

::: {#8d0fc3df .cell .markdown}
## Understanding the Third-Party API

In [utils/team_expense_api.py](utils/team_expense_api.py), there are
three functions defined: `get_team_members`, `get_expenses`, and
`get_custom_budget`. The `get_team_members` function allows us to
retrieve all employees in a given department with their role, level, and
contact information. The `get_expenses` function returns all expense
line items for an employee in a specific quarter---this can be several
hundred records per employee, with each record containing extensive
metadata including receipt URLs, approval chains, merchant details, and
more. The `get_custom_budget` function checks if a specific employee has
a custom travel budget exception (otherwise they use the standard
\$5,000 quarterly limit).

In this scenario, we need to analyze team expenses and identify which
employees have exceeded their budgets. Traditionally, we might manually
pull expense reports for each person, sum up their expenses by category,
compare against budget limits (checking for custom budget exceptions),
and compile a report. Instead, we will ask Claude to perform this
analysis for us, using the available tools to retrieve team data, fetch
potentially hundreds of expense line items with rich metadata, and
determine who has gone over budget.

The key challenge here is that each employee may have 100+ expense line
items that need to be fetched, parsed, and aggregated---and the
`get_custom_budget` tool can only be called after analyzing expenses to
see if someone exceeded the standard budget. This creates a sequential
dependency chain that makes this an ideal use case for demonstrating the
benefits of Programmatic Tool Calling.

We\'ll pass our tool definitions to the messages API and ask Claude to
perform the analysis. Read the docs on [implementing tool
use](https://docs.claude.com/en/docs/agents-and-tools/tool-use/implement-tool-use)
if you are not familiar with how tool use works with Claude\'s API.
:::

::: {#af013fcc .cell .code execution_count="3"}
``` python
import json

import anthropic
from utils.team_expense_api import get_custom_budget, get_expenses, get_team_members

client = anthropic.Anthropic()

# Tool definitions for the team expense API
tools = [
    {
        "name": "get_team_members",
        "description": 'Returns a list of team members for a given department. Each team member includes their ID, name, role, level (junior, mid, senior, staff, principal), and contact information. Use this to get a list of people whose expenses you want to analyze. Available departments are: engineering, sales, and marketing.\n\nRETURN FORMAT: Returns a JSON string containing an ARRAY of team member objects (not wrapped in an outer object). Parse with json.loads() to get a list. Example: [{"id": "ENG001", "name": "Alice", ...}, {"id": "ENG002", ...}]',
        "input_schema": {
            "type": "object",
            "properties": {
                "department": {
                    "type": "string",
                    "description": "The department name. Case-insensitive.",
                }
            },
            "required": ["department"],
        },
        "input_examples": [
            {"department": "engineering"},
            {"department": "sales"},
            {"department": "marketing"},
        ],
    },
    {
        "name": "get_expenses",
        "description": "Returns all expense line items for a given employee in a specific quarter. Each expense includes extensive metadata: date, category, description, amount (in USD), currency, status (approved, pending, rejected), receipt URL, approval chain, merchant name and location, payment method, and project codes. An employee may have 20-50+ expense line items per quarter, and each line item contains substantial metadata for audit and compliance purposes. Categories include: 'travel' (flights, trains, rental cars, taxis, parking), 'lodging' (hotels, airbnb), 'meals', 'software', 'equipment', 'conference', 'office', and 'internet'. IMPORTANT: Only expenses with status='approved' should be counted toward budget limits.\n\nRETURN FORMAT: Returns a JSON string containing an ARRAY of expense objects (not wrapped in an outer object with an 'expenses' key). Parse with json.loads() to get a list directly. Example: [{\"expense_id\": \"ENG001_Q3_001\", \"amount\": 1250.50, \"category\": \"travel\", ...}, {...}]",
        "input_schema": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "The unique employee identifier",
                },
                "quarter": {
                    "type": "string",
                    "description": "Quarter identifier: 'Q1', 'Q2', 'Q3', or 'Q4'",
                },
            },
            "required": ["employee_id", "quarter"],
        },
        "input_examples": [
            {"employee_id": "ENG001", "quarter": "Q3"},
            {"employee_id": "SAL002", "quarter": "Q1"},
            {"employee_id": "MKT001", "quarter": "Q4"},
        ],
    },
    {
        "name": "get_custom_budget",
        "description": 'Get the custom quarterly travel budget for a specific employee. Most employees have a standard $5,000 quarterly travel budget. However, some employees have custom budget exceptions based on their role requirements. This function checks if a specific employee has a custom budget assigned.\n\nRETURN FORMAT: Returns a JSON string containing a SINGLE OBJECT (not an array). Parse with json.loads() to get a dict. Example: {"user_id": "ENG001", "has_custom_budget": false, "travel_budget": 5000, "reason": "Standard", "currency": "USD"}',
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The unique employee identifier",
                }
            },
            "required": ["user_id"],
        },
        "input_examples": [
            {"user_id": "ENG001"},
            {"user_id": "SAL002"},
            {"user_id": "MKT001"},
        ],
    },
]

tool_functions = {
    "get_team_members": get_team_members,
    "get_expenses": get_expenses,
    "get_custom_budget": get_custom_budget,
}
```
:::

::: {#ae7a7b68 .cell .markdown}
## Traditional Tool Calling (Baseline)

In this first example, we\'ll use traditional tool calling to establish
our baseline.

We\'ll call the `messages.create` API with our initial query. When the
model stops with a `tool_use` reason, we will execute the tool as
requested, and then add the output from the tool to the messages and
call the model again.
:::

::: {#dff83920 .cell .code execution_count="4"}
``` python
import time

from anthropic.types import TextBlock, ToolUseBlock
from anthropic.types.beta import (
    BetaMessageParam as MessageParam,
)
from anthropic.types.beta import (
    BetaTextBlock,
    BetaToolUseBlock,
)

messages: list[MessageParam] = []


def run_agent_without_ptc(user_message):
    """Run agent using traditional tool calling"""
    messages.append({"role": "user", "content": user_message})
    total_tokens = 0
    start_time = time.time()
    api_counter = 0

    while True:
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=4000,
            tools=tools,
            messages=messages,
            betas=["advanced-tool-use-2025-11-20"],
        )

        api_counter += 1

        # Track token usage
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        viz.capture(response)
        if response.stop_reason == "end_turn":
            # Extract the first text block from the response
            final_response = next(
                (
                    block.text
                    for block in response.content
                    if isinstance(block, (BetaTextBlock, TextBlock))
                ),
                None,
            )
            elapsed_time = time.time() - start_time
            return final_response, messages, total_tokens, elapsed_time, api_counter

        # Process tool calls
        if response.stop_reason == "tool_use":
            # First, add the assistant's response to messages
            messages.append({"role": "assistant", "content": response.content})

            # Collect all tool results
            tool_results = []

            for block in response.content:
                if isinstance(block, (BetaToolUseBlock, ToolUseBlock)):
                    tool_name = block.name
                    tool_input = block.input
                    tool_use_id = block.id

                    result = tool_functions[tool_name](**tool_input)

                    content = str(result)

                    tool_result = {
                        "type": "tool_result",
                        "tool_use_id": tool_use_id,
                        "content": content,
                    }
                    tool_results.append(tool_result)

            # Append all tool results at once after collecting them
            messages.append({"role": "user", "content": tool_results})

        else:
            print(f"\nUnexpected stop reason: {response.stop_reason}")
            elapsed_time = time.time() - start_time

            final_response = next(
                (
                    block.text
                    for block in response.content
                    if isinstance(block, (BetaTextBlock, TextBlock))
                ),
                f"Stopped with reason: {response.stop_reason}",
            )
            return final_response, messages, total_tokens, elapsed_time, api_counter
```
:::

::: {#db2d30d4 .cell .markdown}
Our initial query to the model provides some instructions to help guide
the model. For brevity, we\'ve asked the model to only call each tool
once. For deeper investigations, the model may wish to look into
multiple systems or time spans.
:::

::: {#6d4bb83a .cell .code execution_count="5"}
``` python
query = "Which engineering team members exceeded their Q3 travel budget? Standard quarterly travel budget is $5,000. However, some employees have custom budget limits. For anyone who exceeded the $5,000 standard budget, check if they have a custom budget exception. If they do, use that custom limit instead to determine if they truly exceeded their budget."
```
:::

:::::::: {#ac08a17f .cell .code execution_count="6"}
``` python
# Run the agent
result, conversation, total_tokens, elapsed_time, api_count_without_ptc = run_agent_without_ptc(
    query
)

print(f"Result: {result}")
print(f"API calls made: {api_count_without_ptc}")
print(f"Total tokens used: {total_tokens:,}")
print(f"Total time taken: {elapsed_time:.2f}s")
```

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ──────────────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">1,859</span> in • <span style="color: #008000; text-decoration-color: #008000">85</span> out • <span style="color: #808000; text-decoration-color: #808000">1,944</span> total                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (2 blocks)                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">I'll help you identify which engineering team members exceeded their Q3 travel budget. Let me </span>  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">start by getting the list of engineering team members.</span>                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_team_members</span>                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01LuouuJYp1sSvBe2Du7EG7v                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"department"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"engineering"</span><span style="background-color: #272822">                                                              </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ───────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">2,473</span> in • <span style="color: #008000; text-decoration-color: #008000">497</span> out • <span style="color: #808000; text-decoration-color: #808000">2,970</span> total            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                                        <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (9 blocks)                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Now let me get the Q3 expenses for all engineering team members:</span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01Wu8LLTT2sKTTqpVwGT65Lj                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG001"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 3</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01KzjQ5mQJa9ocWjCGzYkD9F                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG002"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 4</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01RjjhZTg9JsKXE5E9S6Foho                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG003"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 5</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_013xqpxpfc2N9rP5W5uMLAo9                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG004"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 6</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_019zfzG6Wox8iDqy1dUXiH3t                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG005"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 7</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01RxfTz11tzvbVE7oEtqHaVB                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG006"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 8</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01FsFEtK1gTEPxg56eVrhhf6                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG007"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 9</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01Ctq9dZbvzaVSLSZe86MTzb                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG008"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰──────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ──────────────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">51,744</span> in • <span style="color: #008000; text-decoration-color: #008000">290</span> out • <span style="color: #808000; text-decoration-color: #808000">52,034</span> total                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (7 blocks)                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Now let me calculate the approved travel expenses for each engineer and identify who exceeded </span>  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">$5,000:</span>                                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_013oegKwjvToLwEW1daDD8av                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG001"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 3</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_0162W4Ycr9FcVVED65exjAj4                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG003"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 4</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01JcTX5rnwFxA99Am33gXmh6                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG005"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 5</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01QwNJz1wGeV5VeZoCd4ByER                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG006"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 6</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01KoJ4gzfiu1TPccLJB86Wiq                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG007"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 7</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01MxeFPzHot9aE5fPuniFkui                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> model (direct)                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG008"</span><span style="background-color: #272822">                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ──────────────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">52,533</span> in • <span style="color: #008000; text-decoration-color: #008000">992</span> out • <span style="color: #808000; text-decoration-color: #808000">53,525</span> total                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> end_turn                                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (1 blocks)                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Now let me analyze the data. I'll calculate the approved travel expenses for each engineer:</span>     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**Analysis of Q3 Travel Expenses:**</span>                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**ENG001 - Alice Chen (Senior Software Engineer)**</span>                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Approved travel expenses: $1,161.04 + $18.63 + $13.21 + $36.55 + $1,440.42 + $166.46 + $48.43</span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">+ $1,124.56 + $1,245.90 + $1,498.42 = **$6,753.62**</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Budget: $5,000 (Standard)</span>                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- **EXCEEDED by $1,753.62** ❌</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**ENG002 - Bob Martinez (Staff Engineer)**</span>                                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Approved travel expenses: $180.16 + $10.07 + $20.76 = **$210.99**</span>                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Budget: $5,000 (Standard)</span>                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Under budget ✓</span>                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**ENG003 - Carol White (Software Engineer)**</span>                                                    <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Approved travel expenses: $24.75 + $424.74 + $1,397.17 + $1,026.12 + $1,288.36 + $1,128.90 + </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">$1,148.42 + $45.03 = **$6,483.49**</span>                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Budget: $5,000 (Standard)</span>                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- **EXCEEDED by $1,483.49** ❌</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**ENG004 - David Kim (Principal Engineer)**</span>                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Approved travel expenses: $21.68 + $46.12 + $1,008.68 + $46.43 = **$1,122.91**</span>                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Budget: $5,000 (Standard)</span>                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">- Under budget ✓</span>                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**ENG005 - Emma Johnson (Junior Software Engineer)</span>                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">... (truncated)</span>                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .stream .stdout}
    Result: Now let me analyze the data. I'll calculate the approved travel expenses for each engineer:

    **Analysis of Q3 Travel Expenses:**

    **ENG001 - Alice Chen (Senior Software Engineer)**
    - Approved travel expenses: $1,161.04 + $18.63 + $13.21 + $36.55 + $1,440.42 + $166.46 + $48.43 + $1,124.56 + $1,245.90 + $1,498.42 = **$6,753.62**
    - Budget: $5,000 (Standard)
    - **EXCEEDED by $1,753.62** ❌

    **ENG002 - Bob Martinez (Staff Engineer)**
    - Approved travel expenses: $180.16 + $10.07 + $20.76 = **$210.99**
    - Budget: $5,000 (Standard)
    - Under budget ✓

    **ENG003 - Carol White (Software Engineer)**
    - Approved travel expenses: $24.75 + $424.74 + $1,397.17 + $1,026.12 + $1,288.36 + $1,128.90 + $1,148.42 + $45.03 = **$6,483.49**
    - Budget: $5,000 (Standard)
    - **EXCEEDED by $1,483.49** ❌

    **ENG004 - David Kim (Principal Engineer)**
    - Approved travel expenses: $21.68 + $46.12 + $1,008.68 + $46.43 = **$1,122.91**
    - Budget: $5,000 (Standard)
    - Under budget ✓

    **ENG005 - Emma Johnson (Junior Software Engineer)**
    - Approved travel expenses: $450.00 + $1,376.36 + $1,164.49 + $151.55 + $1,253.88 = **$4,396.28**
    - Budget: $5,000 (Standard)
    - Under budget ✓

    **ENG006 - Frank Liu (Senior Software Engineer)**
    - Approved travel expenses: $596.48 + $1,018.71 + $1,193.82 + $159.08 + $1,112.11 + $24.97 = **$4,105.17**
    - Budget: $5,000 (Standard)
    - Under budget ✓

    **ENG007 - Grace Taylor (Software Engineer)**
    - Approved travel expenses: $1,476.63 + $39.85 + $1,220.19 + $189.16 + $1,032.52 + $1,331.00 = **$5,289.35**
    - Budget: $5,000 (Standard)
    - **EXCEEDED by $289.35** ❌

    **ENG008 - Henry Park (Staff Engineer)**
    - Approved travel expenses: $15.63 + $166.05 + $1,018.94 + $1,224.34 + $1,120.32 + $1,345.90 = **$4,891.18**
    - Budget: $5,000 (Standard)
    - Under budget ✓

    ---

    ## Summary: Engineering Team Members Who Exceeded Their Q3 Travel Budget

    **3 team members exceeded their quarterly travel budget:**

    1. **Alice Chen (ENG001)** - Senior Software Engineer
       - Travel expenses: **$6,753.62**
       - Budget: $5,000
       - **Over budget by $1,753.62 (35% over)**

    2. **Carol White (ENG003)** - Software Engineer
       - Travel expenses: **$6,483.49**
       - Budget: $5,000
       - **Over budget by $1,483.49 (30% over)**

    3. **Grace Taylor (ENG007)** - Software Engineer
       - Travel expenses: **$5,289.35**
       - Budget: $5,000
       - **Over budget by $289.35 (6% over)**

    All three employees have the standard $5,000 quarterly travel budget with no custom exceptions.
    API calls made: 4
    Total tokens used: 110,473
    Total time taken: 35.38s
:::
::::::::

::: {#6a3fedb1 .cell .markdown}
Great! We can see that Claude was able to use the available tools
successfully to identify which team members exceeded their travel
budgets. However, we can also see that we used a lot of tokens to
accomplish this task. Claude had to ingest all the expense line items
through its context window---potentially 100+ records per employee, each
with extensive metadata including receipt URLs, approval chains,
merchant information, and more---in order to parse them, sum up the
totals by category, and compare against budget limits.

Additionally, the traditional tool calling approach requires multiple
sequential round trips: first fetching team members, then expenses for
each person, then checking custom budgets for those who exceeded the
standard limit. Each round trip adds latency, and all the rich metadata
from expense records flows through the model\'s context.

Let\'s see if we can use PTC to improve performance by allowing Claude
to write code that processes these large datasets in the code execution
environment instead.
:::

::: {#f9c2500e .cell .markdown}
To enable PTC on tools, we must first add the `allowed_callers` field to
any tool that should be callable via code execution.

**Key points to consider**

- Tools without allowed_callers default to model-only invocation
- Tools can be invoked by both the model AND code execution by including
  multiple callers: `["direct", "code_execution_20250825"]`
- Only opt in tools that are safe for programmatic/repeated execution.
:::

::: {#yg1hozsmgz9 .cell .code execution_count="7"}
``` python
import copy

ptc_tools = copy.deepcopy(tools)
for tool in ptc_tools:
    tool["allowed_callers"] = ["code_execution_20250825"]  # type: ignore


# Add the code execution tool
ptc_tools.append(
    {
        "type": "code_execution_20250825",  # type: ignore
        "name": "code_execution",
    }
)
```
:::

::: {#c9d1c138 .cell .markdown}
Now that we\'ve updated our tool definitions to allow programmatic tool
calling, we can run our agent with PTC. In order to do so, we\'ve had to
make a few changes to our function. We must use the `beta` messages API.

1.  We\'ve added `"advanced-tool-use-2025-11-20"` to betas.
2.  We pass in the `container_id` if it is defined with our request.
    This is only necessary for stateful workflows like ours. In
    single-turn workflows this is not required.
3.  We can check the `caller` field in the `tool_use` block to determine
    if this tool call is from a direct model invocation or from
    programmatic invocation.

Note that in either case, we send our tool results via the Claude API,
however only `direct` invocations will be \"seen\" by the model.
`code_execution_20250825` types will only be seen my the code execution
container.
:::

::: {#dq3gj54mlv .cell .code execution_count="8"}
``` python
messages = []


def run_agent_with_ptc(user_message):
    """Run agent using PTC"""
    messages.append({"role": "user", "content": user_message})
    total_tokens = 0
    start_time = time.time()
    container_id = None
    api_counter = 0

    while True:
        # Build request with PTC beta headers
        request_params = {
            "model": MODEL,
            "max_tokens": 4000,
            "tools": ptc_tools,
            "messages": messages,
        }

        response = client.beta.messages.create(
            **request_params,
            betas=[
                "advanced-tool-use-2025-11-20",
            ],
            extra_body={"container": container_id} if container_id else None,
        )
        viz.capture(response)
        api_counter += 1

        # Track container for stateful execution
        if hasattr(response, "container") and response.container:
            container_id = response.container.id
            print(f"\n[Container] ID: {container_id}")
            if hasattr(response.container, "expires_at"):
                # If the container has expired, we would need to restart our workflow. In our case, it completes before expiration.
                print(f"[Container] Expires at: {response.container.expires_at}")

        # Track token usage
        total_tokens += response.usage.input_tokens + response.usage.output_tokens

        if response.stop_reason == "end_turn":
            # Extract the first text block from the response
            final_response = next(
                (block.text for block in response.content if isinstance(block, BetaTextBlock)),
                None,
            )
            elapsed_time = time.time() - start_time
            return final_response, messages, total_tokens, elapsed_time, api_counter

        # As before, we process tool calls
        if response.stop_reason == "tool_use":
            # First, add the assistant's response to messages
            messages.append({"role": "assistant", "content": response.content})

            # Collect all tool results
            tool_results = []

            for block in response.content:
                if isinstance(block, BetaToolUseBlock):
                    tool_name = block.name
                    tool_input = block.input
                    tool_use_id = block.id

                    # We can use caller type to understand how the tool was invoked
                    caller_type = block.caller["type"]  # type: ignore

                    if caller_type == "code_execution_20250825":
                        print(f"[PTC] Tool called from code execution environment: {tool_name}")

                    elif caller_type == "direct":
                        print(f"[Direct] Tool called by model: {tool_name}")

                    result = tool_functions[tool_name](**tool_input)

                    # Format result as proper content for the API
                    if isinstance(result, list) and result and isinstance(result[0], str):
                        content = "\n".join(result)
                    elif isinstance(result, (dict, list)):
                        content = json.dumps(result)
                    else:
                        content = str(result)

                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use_id,
                            "content": content,
                        }
                    )

            messages.append({"role": "user", "content": tool_results})

        else:
            print(f"\nUnexpected stop reason: {response.stop_reason}")
            elapsed_time = time.time() - start_time

            final_response = next(
                (block.text for block in response.content if isinstance(block, BetaTextBlock)),
                f"Stopped with reason: {response.stop_reason}",
            )
            return final_response, messages, total_tokens, elapsed_time, api_counter
```
:::

:::::::::: {#640d2e02 .cell .code execution_count="9"}
``` python
# Run the PTC agent
result_ptc, conversation_ptc, total_tokens_ptc, elapsed_time_ptc, api_count_with_ptc = (
    run_agent_with_ptc(query)
)
```

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ──────────────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">4,134</span> in • <span style="color: #008000; text-decoration-color: #008000">539</span> out • <span style="color: #808000; text-decoration-color: #808000">4,673</span> total                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (3 blocks)                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">I'll help you identify which engineering team members exceeded their Q3 travel budget. Let me </span>  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">start by getting the engineering team members and their expenses.</span>                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Server Tool Use</span>                                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> srvtoolu_015mWPqaFni4B313UieCxbny                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> direct                                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Code:</span>                                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 1 </span><span style="background-color: #272822">                                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 2 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">import</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> asyncio</span><span style="background-color: #272822">                                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 3 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">import</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> json</span><span style="background-color: #272822">                                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 4 </span><span style="background-color: #272822">                                                                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 5 </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">async</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #a6e22e; text-decoration-color: #a6e22e; background-color: #272822">main</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">():</span><span style="background-color: #272822">                                                                     </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 6 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># First, get all engineering team members</span><span style="background-color: #272822">                                         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 7 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    team_members_json </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">await</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> get_team_members({</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'department'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'engineering'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">})</span><span style="background-color: #272822">         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 8 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    team_members </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> json</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">.</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">loads(team_members_json)</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 9 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">10 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    print(</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">f"Found {</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">len(team_members)</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">} engineering team members"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">)</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">11 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">12 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Get Q3 expenses for all team members in parallel</span><span style="background-color: #272822">                                </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">13 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    expense_tasks </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> [</span><span style="background-color: #272822">                                                                 </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">14 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        get_expenses({</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'employee_id'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: member[</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'id'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">], </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'quarter'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'Q3'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">})</span><span style="background-color: #272822">                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">15 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">for</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> member </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">in</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> team_members</span><span style="background-color: #272822">                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">16 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    ]</span><span style="background-color: #272822">                                                                                 </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">17 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">18 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    expenses_results </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">await</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> asyncio</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">.</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">gather(</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">*</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">expense_tasks)</span><span style="background-color: #272822">                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">19 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">20 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Calculate travel expenses for each member</span><span style="background-color: #272822">                                       </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">21 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    travel_spending </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> {}</span><span style="background-color: #272822">                                                              </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">22 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">for</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> i, member </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">in</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> enumerate(team_members):</span><span style="background-color: #272822">                                         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">23 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        expenses </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> json</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">.</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">loads(expenses_results[i])</span><span style="background-color: #272822">                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">24 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Only count approved expenses in travel category</span><span style="background-color: #272822">                             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">25 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        travel_total </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> sum(</span><span style="background-color: #272822">                                                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">26 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">            expense[</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'amount'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">] </span><span style="background-color: #272822">                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">27 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">            </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">for</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> expense </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">in</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> expenses </span><span style="background-color: #272822">                                                  </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">28 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">            </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">if</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> expense[</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'category'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">] </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">==</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">and</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> expense[</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'status'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">] </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">==</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'approved'</span><span style="background-color: #272822">    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">29 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        )</span><span style="background-color: #272822">                                                                             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">30 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        travel_spending[member[</span><span style="background-color: #272822">                                                       </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">31 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">...</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> (truncated)</span><span style="background-color: #272822">                                                                       </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 3</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_team_members</span>                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_016EtCE7G5rH645G3gvjzrP6                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"department"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"engineering"</span><span style="background-color: #272822">                                                              </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .stream .stdout}

    [Container] ID: container_011CVSAwq5J4vNPi3A4P2Rwh
    [Container] Expires at: 2025-11-24 05:41:17.467494+00:00
    [PTC] Tool called from code execution environment: get_team_members
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭──────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">0</span> in • <span style="color: #008000; text-decoration-color: #008000">0</span> out • <span style="color: #808000; text-decoration-color: #808000">0</span> total <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (8 blocks)                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01Nq2au3W69RmDFZaSdqe6u1          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG007"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01YYw9cuTSXk7bu7P38qBz6P          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG005"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 3</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01Fyxxe2KmVpVmw4jJL2CXSz          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG008"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 4</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01J4ovDu2UJa9Se19vxKTa6y          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG006"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 5</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01T24CrvQYA3LqGfZftCmueC          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG003"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 6</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01HotYZN6sk3gMLkpdWXbdz4          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG004"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 7</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01AxvEqi3AKqdnH44kGH1U6E          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG002"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 8</span>                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_expenses</span>                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01A4agznkK1jA4AyJo3H2jpg          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"employee_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG001"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">,</span><span style="background-color: #272822">             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"quarter"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"Q3"</span><span style="background-color: #272822">                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .stream .stdout}

    [Container] ID: container_011CVSAwq5J4vNPi3A4P2Rwh
    [Container] Expires at: 2025-11-24 05:41:19.266670+00:00
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
    [PTC] Tool called from code execution environment: get_expenses
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭─────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ───────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">4,751</span> in • <span style="color: #008000; text-decoration-color: #008000">679</span> out • <span style="color: #808000; text-decoration-color: #808000">5,430</span> total                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> tool_use                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (6 blocks)                                                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Code Execution Result:</span> <span style="color: #008000; text-decoration-color: #008000">Success (exit 0)</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">stdout:</span>                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Found 8 engineering team members</span>                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Employees who exceeded $5,000 standard budget: 3</span>                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">ENG001: Alice Chen - $9177.88</span>                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">ENG003: Carol White - $6483.49</span>                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">ENG007: Grace Taylor - $5289.35</span>                                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Now let me check if any of these three employees have custom budget exceptions:</span>   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 3</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Server Tool Use</span>                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> srvtoolu_015GTpFmCbd2JPAQLAioB4Qb                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> direct                                                                    <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Code:</span>                                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 1 </span><span style="background-color: #272822">                                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 2 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">import</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> asyncio</span><span style="background-color: #272822">                                                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 3 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">import</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> json</span><span style="background-color: #272822">                                                             </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 4 </span><span style="background-color: #272822">                                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 5 </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">async</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">def</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #a6e22e; text-decoration-color: #a6e22e; background-color: #272822">main</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">():</span><span style="background-color: #272822">                                                       </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 6 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Check custom budgets for the three employees who exceeded standard</span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 7 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    exceeded_ids </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> [</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG001'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">, </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG003'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">, </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG007'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">]</span><span style="background-color: #272822">                       </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 8 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    exceeded_amounts </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> {</span><span style="background-color: #272822">                                                </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822"> 9 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG001'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: {</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'name'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'Alice Chen'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">, </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel_total'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #ae81ff; text-decoration-color: #ae81ff; background-color: #272822">9177.88</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">},</span><span style="background-color: #272822">      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">10 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG003'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: {</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'name'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'Carol White'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">, </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel_total'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #ae81ff; text-decoration-color: #ae81ff; background-color: #272822">6483.49</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">},</span><span style="background-color: #272822">     </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">11 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'ENG007'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: {</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'name'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'Grace Taylor'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">, </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel_total'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #ae81ff; text-decoration-color: #ae81ff; background-color: #272822">5289.35</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">     </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">12 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    }</span><span style="background-color: #272822">                                                                   </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">13 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">14 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Get custom budgets in parallel</span><span style="background-color: #272822">                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">15 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    budget_tasks </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> [</span><span style="background-color: #272822">                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">16 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        get_custom_budget({</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'user_id'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: emp_id})</span><span style="background-color: #272822">                          </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">17 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">for</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> emp_id </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">in</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> exceeded_ids</span><span style="background-color: #272822">                                      </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">18 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    ]</span><span style="background-color: #272822">                                                                   </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">19 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">20 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    budget_results </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">await</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> asyncio</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">.</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">gather(</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">*</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">budget_tasks)</span><span style="background-color: #272822">                </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">21 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">22 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #959077; text-decoration-color: #959077; background-color: #272822"># Analyze who truly exceeded their budget</span><span style="background-color: #272822">                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">23 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    truly_exceeded </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> []</span><span style="background-color: #272822">                                                 </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">24 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="background-color: #272822">                                                                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">25 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">    </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">for</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> i, emp_id </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">in</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> enumerate(exceeded_ids):</span><span style="background-color: #272822">                           </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">26 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        budget_info </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> json</span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">.</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">loads(budget_results[i])</span><span style="background-color: #272822">                     </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">27 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        actual_budget </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> budget_info[</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel_budget'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">]</span><span style="background-color: #272822">                    </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">28 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        travel_total </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> exceeded_amounts[emp_id][</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'travel_total'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">]</span><span style="background-color: #272822">         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">29 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        name </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">=</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> exceeded_amounts[emp_id][</span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">'name'</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">]</span><span style="background-color: #272822">                         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">30 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="background-color: #272822">                                                                </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">31 </span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">        </span><span style="color: #66d9ef; text-decoration-color: #66d9ef; background-color: #272822">if</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> travel_total </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">&gt;</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> actua</span><span style="background-color: #272822">                                         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #e3e3dd; text-decoration-color: #e3e3dd; background-color: #272822; font-weight: bold">  </span><span style="color: #656660; text-decoration-color: #656660; background-color: #272822">32 </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">...</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822"> (truncated)</span><span style="background-color: #272822">                                                         </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 4</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01EaaJ3SikeniibPsEdAqXo8                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG003"</span><span style="background-color: #272822">                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 5</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01E5bqQ4xKX7FTdhh6xLkw4E                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG001"</span><span style="background-color: #272822">                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 6</span>                                                                                   <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #808000; text-decoration-color: #808000">Tool Use:</span> <span style="color: #808000; text-decoration-color: #808000; font-weight: bold">get_custom_budget</span>                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">ID:</span> toolu_01PLF38q7ndVQB4mqdqaFt7u                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Caller:</span> code execution environment                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #008000; text-decoration-color: #008000">Input:</span>                                                                            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 └── <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">{</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">  </span><span style="color: #ff4689; text-decoration-color: #ff4689; background-color: #272822">"user_id"</span><span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">: </span><span style="color: #e6db74; text-decoration-color: #e6db74; background-color: #272822">"ENG007"</span><span style="background-color: #272822">                                                        </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                     <span style="color: #f8f8f2; text-decoration-color: #f8f8f2; background-color: #272822">}</span><span style="background-color: #272822">                                                                            </span> <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰───────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::

::: {.output .stream .stdout}

    [Container] ID: container_011CVSAwq5J4vNPi3A4P2Rwh
    [Container] Expires at: 2025-11-24 05:41:33.430636+00:00
    [PTC] Tool called from code execution environment: get_custom_budget
    [PTC] Tool called from code execution environment: get_custom_budget
    [PTC] Tool called from code execution environment: get_custom_budget
:::

::: {.output .display_data}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">╭────────────────────────────────────────────── </span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude API Response</span><span style="color: #008080; text-decoration-color: #008080"> ──────────────────────────────────────────────╮</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">Claude Message</span> (<span style="color: #008000; text-decoration-color: #008000">assistant</span>) <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">│</span> <span style="color: #800080; text-decoration-color: #800080">tokens:</span> <span style="color: #008080; text-decoration-color: #008080">5,611</span> in • <span style="color: #008000; text-decoration-color: #008000">205</span> out • <span style="color: #808000; text-decoration-color: #808000">5,816</span> total                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Model:</span> claude-sonnet-4-5-20250929                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Stop Reason:</span> end_turn                                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span> └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">Content</span> (2 blocks)                                                                                          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     ├── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 1</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │   └── <span style="color: #808000; text-decoration-color: #808000">Code Execution Result:</span> <span style="color: #008000; text-decoration-color: #008000">Success (exit 0)</span>                                                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │       └── <span style="color: #008000; text-decoration-color: #008000">stdout:</span>                                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │           └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">ENGINEERING TEAM MEMBERS WHO EXCEEDED THEIR Q3 TRAVEL BUDGET:</span>                               <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">================================================================================</span>            <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Alice Chen (ENG001)</span>                                                                         <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Budget Limit: $5,000.00 (Standard)</span>                                                        <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Travel Spending: $9,177.88</span>                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Exceeded By: $4,177.88</span>                                                                    <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Carol White (ENG003)</span>                                                                        <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Budget Limit: $5,000.00 (Standard)</span>                                                        <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Travel Spending: $6,483.49</span>                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Exceeded By: $1,483.49</span>                                                                    <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">Grace Taylor (ENG007)</span>                                                                       <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Budget Limit: $5,000.00 (Standard)</span>                                                        <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Travel Spending: $5,289.35</span>                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │               <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">  Exceeded By: $289.35</span>                                                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     │                                                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>     └── <span style="color: #dfdfdf; text-decoration-color: #dfdfdf">Block 2</span>                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>         └── <span style="color: #008080; text-decoration-color: #008080">Text</span>                                                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>             └── <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">## Summary</span>                                                                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">**Three engineering team members exceeded their Q3 travel budget:**</span>                             <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">1. **Alice Chen (ENG001)**</span>                                                                      <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Budget: $5,000 (Standard)</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Spent: $9,177.88</span>                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Over budget by: **$4,177.88**</span>                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">2. **Carol White (ENG003)**</span>                                                                     <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Budget: $5,000 (Standard)</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Spent: $6,483.49</span>                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Over budget by: **$1,483.49**</span>                                                              <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">3. **Grace Taylor (ENG007)**</span>                                                                    <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Budget: $5,000 (Standard)</span>                                                                  <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Spent: $5,289.35</span>                                                                           <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">   - Over budget by: **$289.35**</span>                                                                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                                                                                                                 <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">All three employees are on the standard $5,000 quarterly travel budget with no custom </span>          <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">│</span>                 <span style="color: #c0c0c0; text-decoration-color: #c0c0c0">exceptions, so they all genuinely exceeded their allocated travel budget for Q3.</span>                <span style="color: #008080; text-decoration-color: #008080">│</span>
<span style="color: #008080; text-decoration-color: #008080">╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯</span>
</pre>
:::
::::::::::

:::: {#da1a0d5d .cell .code execution_count="10"}
``` python
print(f"\n{'=' * 60}")
print(f"Result: {result_ptc}")
print(f"\n{'=' * 60}")
print("Performance Metrics:")
print(
    f"  Total API calls to Claude: {len([m for m in conversation_ptc if m['role'] == 'assistant'])}"
)
print(f"  Total tokens used: {total_tokens_ptc:,}")
print(f"  Total time taken: {elapsed_time_ptc:.2f}s")
```

::: {.output .stream .stdout}

    ============================================================
    Result: ## Summary

    **Three engineering team members exceeded their Q3 travel budget:**

    1. **Alice Chen (ENG001)**
       - Budget: $5,000 (Standard)
       - Spent: $9,177.88
       - Over budget by: **$4,177.88**

    2. **Carol White (ENG003)**
       - Budget: $5,000 (Standard)
       - Spent: $6,483.49
       - Over budget by: **$1,483.49**

    3. **Grace Taylor (ENG007)**
       - Budget: $5,000 (Standard)
       - Spent: $5,289.35
       - Over budget by: **$289.35**

    All three employees are on the standard $5,000 quarterly travel budget with no custom exceptions, so they all genuinely exceeded their allocated travel budget for Q3.

    ============================================================
    Performance Metrics:
      Total API calls to Claude: 3
      Total tokens used: 15,919
      Total time taken: 34.88s
:::
::::

::: {#xevg4ich93m .cell .markdown}
## Performance Comparison

Let\'s compare the performance between traditional tool calling and PTC:

**Note on API Call Count:** You may notice that PTC requires more API
calls in this example. This is because PTC writes more structured,
sequential code that follows best practices---for instance, separating
the expense fetching step from the budget checking step. Traditional
tool calling can sometimes batch operations together in a single turn,
but at the cost of sending all raw data through the model\'s context.
The token efficiency gains from PTC far outweigh the minimal increase in
round trips, especially when working with large, metadata-rich datasets.
:::

:::: {#fun83cq4bmq .cell .code execution_count="11"}
``` python
import pandas as pd

# Create comparison dataframe
comparison_data = {
    "Metric": [
        "API Calls",
        "Total Tokens",
        "Elapsed Time (s)",
        "Token Reduction",
        "Time Reduction",
    ],
    "Traditional": [
        api_count_without_ptc,
        f"{total_tokens:,}",
        f"{elapsed_time:.2f}",
        "-",
        "-",
    ],
    "PTC": [
        api_count_with_ptc,
        f"{total_tokens_ptc:,}",
        f"{elapsed_time_ptc:.2f}",
        f"{((total_tokens - total_tokens_ptc) / total_tokens * 100):.1f}%",
        f"{((elapsed_time - elapsed_time_ptc) / elapsed_time * 100):.1f}%",
    ],
}

df = pd.DataFrame(comparison_data)
print(df.to_string(index=False))
```

::: {.output .stream .stdout}
              Metric Traditional    PTC
           API Calls           4      4
        Total Tokens     110,473 15,919
    Elapsed Time (s)       35.38  34.88
     Token Reduction           -  85.6%
      Time Reduction           -   1.4%
:::
::::

::: {#90jm6y08ua7 .cell .markdown}
## Key Takeaways

In this example, PTC demonstrated significant performance improvements
through three core capabilities:

### 1. Context Preservation Through Large Data Parsing {#1-context-preservation-through-large-data-parsing}

This was the primary benefit demonstrated in our workflow. Claude wrote
code to fetch and process hundreds of expense line items within the code
execution environment. By processing this data programmatically, Claude
parsed JSON, filtered by status, summed amounts by category, and
compared against budget limits---all without sending the raw expense
data and metadata through the model\'s context window. This resulted in
a **significant reduction in token usage**.

### 2. Sequential Dependency Optimization {#2-sequential-dependency-optimization}

The API has a sequential dependency: `get_custom_budget(user_id)` which
can only be called after analyzing expenses to identify who exceeded the
standard \$5,000 budget. In traditional tool calling, this requires
multiple round trips---fetch team members, fetch expenses for each
person, identify those over budget, then check their custom budgets one
by one. With PTC, Claude writes code that orchestrates this entire
workflow in the code execution environment, making programmatic tool
calls in a loop and maintaining state across calls. This transforms what
would be many sequential API round trips into fewer calls with smarter
orchestration.

### 3. Computational Logic in Code Execution {#3-computational-logic-in-code-execution}

Rather than requiring the model to mentally track and sum dozens of
expenses with complex metadata, Claude delegated the arithmetic and
aggregation logic to Python code. This reduced cognitive load on the
model, ensured precise calculations, and kept irrelevant metadata (like
receipt URLs and merchant locations) out of the model\'s context
entirely.

------------------------------------------------------------------------

## When to Use PTC

PTC is most beneficial when:

- **Working with large, metadata-rich datasets** that need filtering,
  parsing, or aggregation (like our expense analysis with receipt URLs,
  approval chains, merchant details, etc.)
- **Sequential dependencies exist** where one tool call depends on the
  results of previous calls (like checking custom budgets only for
  employees who exceeded standard limits)
- **Multiple tool calls are needed** in sequence or in loops across
  similar entities (checking expenses and budgets for each team member)
- **Computational logic** can reduce what needs to flow through the
  model\'s context
- **Tools are safe** for programmatic/repeated execution without human
  oversight

## Conclusion

Our team expense analysis demonstrated PTC\'s strengths: **dramatically
reducing context consumption when working with large, metadata-rich
datasets** and **optimizing workflows with sequential dependencies**. By
allowing Claude to write code that orchestrates tool calls and processes
results programmatically, we achieved substantial token savings while
maintaining accuracy and insight quality.

PTC is particularly valuable for workflows involving bulk data
processing with rich metadata, repeated tool invocations with
dependencies, or scenarios where raw tool outputs would otherwise
pollute the model\'s context.

## Next Steps

Try adapting this pattern to your own use cases:

- Financial data analysis and reporting with sequential lookups
- Multi-entity health checks that depend on initial scan results\
- Large file processing with metadata (CSV, JSON, XML parsing)
- Database query result aggregation with follow-up queries
- Batch API operations with conditional logic based on initial results
:::
