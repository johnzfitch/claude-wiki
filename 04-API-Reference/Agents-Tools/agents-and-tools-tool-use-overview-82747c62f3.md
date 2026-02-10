---
category: "04-API-Reference"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview"
---


Tools
Tool use with Claude
Copy page

Claude is capable of interacting with tools and functions, allowing you to extend Claude's capabilities to perform a wider variety of tasks.

Learn everything you need to master tool use with Claude as part of our new courses! Please continue to share your ideas and suggestions using this form.

Guarantee schema conformance with strict tool use

Structured Outputs provides guaranteed schema validation for tool inputs. Add strict: true to your tool definitions to ensure Claude's tool calls always match your schema exactly—no more type mismatches or missing fields.

Perfect for production agents where invalid tool parameters would cause failures. Learn when to use strict tool use →

Here's an example of how to provide tools to Claude using the Messages API:

Shell
curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -d '{
 "model": "claude-sonnet-4-5",
 "max_tokens": 1024,
 "tools": [
 {
 "name": "get_weather",
 "description": "Get the current weather in a given location",
 "input_schema": {
 "type": "object",
 "properties": {
 "location": {
 "type": "string",
 "description": "The city and state, e.g. San Francisco, CA"
 }
 },
 "required": ["location"]
 }
 }
 ],
 "messages": [
 {
 "role": "user",
 "content": "What is the weather like in San Francisco?"
 }
 ]
 }'
How tool use works

Claude supports two types of tools:

Client tools: Tools that execute on your systems, which include:

User-defined custom tools that you create and implement
Anthropic-defined tools like computer use and text editor that require client implementation

Server tools: Tools that execute on Anthropic's servers, like the web search and web fetch tools. These tools must be specified in the API request but don't require implementation on your part.

Anthropic-defined tools use versioned types (e.g., web_search_20250305, text_editor_20250124) to ensure compatibility across model versions.

Client tools

Integrate client tools with Claude in these steps:

1

Provide Claude with tools and a user prompt

Define client tools with names, descriptions, and input schemas in your API request.
Include a user prompt that might require these tools, e.g., "What's the weather in San Francisco?"
2

Claude decides to use a tool

Claude assesses if any tools can help with the user's query.
If yes, Claude constructs a properly formatted tool use request.
For client tools, the API response has a stop_reason of tool_use, signaling Claude's intent.
3

Execute the tool and return results

Extract the tool name and input from Claude's request
Execute the tool code on your system
Return the results in a new user message containing a tool_result content block
4

Claude uses tool result to formulate a response

Claude analyzes the tool results to craft its final response to the original user prompt.

Note: Steps 3 and 4 are optional. For some workflows, Claude's tool use request (step 2) might be all you need, without sending results back to Claude.

Server tools

Server tools follow a different workflow:

1

Provide Claude with tools and a user prompt

Server tools, like web search and web fetch, have their own parameters.
Include a user prompt that might require these tools, e.g., "Search for the latest news about AI" or "Analyze the content at this URL."
2

Claude executes the server tool

Claude assesses if a server tool can help with the user's query.
If yes, Claude executes the tool, and the results are automatically incorporated into Claude's response.
3

Claude uses the server tool result to formulate a response

Claude analyzes the server tool results to craft its final response to the original user prompt.
No additional user interaction is needed for server tool execution.
Using MCP tools with Claude

If you're building an application that uses the Model Context Protocol (MCP), you can use tools from MCP servers directly with Claude's Messages API. MCP tool definitions use a schema format that's similar to Claude's tool format. You just need to rename inputSchema to input_schema.

Don't want to build your own MCP client? Use the MCP connector to connect directly to remote MCP servers from the Messages API without implementing a client.

Converting MCP tools to Claude format

When you build an MCP client and call list_tools() on an MCP server, you'll receive tool definitions with an inputSchema field. To use these tools with Claude, convert them to Claude's format:

Python
from mcp import ClientSession

async def get_claude_tools(mcp_session: ClientSession):
 """Convert MCP tools to Claude's tool format."""
 mcp_tools = await mcp_session.list_tools()

 claude_tools = []
 for tool in mcp_tools.tools:
 claude_tools.append({
 "name": tool.name,
 "description": tool.description or "",
 "input_schema": tool.inputSchema # Rename inputSchema to input_schema
 })

 return claude_tools

Then pass these converted tools to Claude:

Python
import anthropic

client = anthropic.Anthropic()
claude_tools = await get_claude_tools(mcp_session)

response = client.messages.create(
 model="claude-sonnet-4-5",
 max_tokens=1024,
 tools=claude_tools,
 messages=[{"role": "user", "content": "What tools do you have available?"}]
)

When Claude responds with a tool_use block, execute the tool on your MCP server using call_tool() and return the result to Claude in a tool_result block.

For a complete guide to building MCP clients, see Build an MCP client.

Tool use examples

Here are a few code examples demonstrating various tool use patterns and techniques. For brevity's sake, the tools are simple tools, and the tool descriptions are shorter than would be ideal to ensure best performance.

Single tool example
Parallel tool use
Multiple tool example
Missing information
Sequential tools
Chain of thought tool use
Pricing

Tool use requests are priced based on:

The total number of input tokens sent to the model (including in the tools parameter)
The number of output tokens generated
For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.

The additional tokens from tool use come from:

The tools parameter in API requests (tool names, descriptions, and schemas)
tool_use content blocks in API requests and responses
tool_result content blocks in API requests

When you use tools, we also automatically include a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no tools are provided, then a tool choice of none uses 0 additional system prompt tokens.

Model Tool choice Tool use system prompt token count
Claude Opus 4.5 auto, none
any, tool 346 tokens
313 tokens
Claude Opus 4.1 auto, none
any, tool 346 tokens
313 tokens
Claude Opus 4 auto, none
any, tool 346 tokens
313 tokens
Claude Sonnet 4.5 auto, none
any, tool 346 tokens
313 tokens
Claude Sonnet 4 auto, none
any, tool 346 tokens
313 tokens
Claude Sonnet 3.7 (deprecated) auto, none
any, tool 346 tokens
313 tokens
Claude Haiku 4.5 auto, none
any, tool 346 tokens
313 tokens
Claude Haiku 3.5 auto, none
any, tool 264 tokens
340 tokens
Claude Opus 3 (deprecated) auto, none
any, tool 530 tokens
281 tokens
Claude Sonnet 3 auto, none
any, tool 159 tokens
235 tokens
Claude Haiku 3 auto, none
any, tool 264 tokens
340 tokens

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

Refer to our models overview table for current per-model prices.

When you send a tool use prompt, just like any other API request, the response will output both input and output token counts as part of the reported usage metrics.

Next Steps

Explore our repository of ready-to-implement tool use code examples in our cookbooks:

Calculator Tool

Learn how to integrate a simple calculator tool with Claude for precise numerical computations.

Customer Service Agent

Build a responsive customer service bot that leverages client tools to enhance support.

JSON Extractor

See how Claude and tool use can extract structured data from unstructured text.

Was this page helpful?