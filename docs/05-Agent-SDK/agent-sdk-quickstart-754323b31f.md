---
category: "05-Agent-SDK"
source_url: "https://platform.claude.com/docs/en/agent-sdk/quickstart"
---


Agent SDK
Quickstart
Copy page
Get started with the Python or TypeScript Agent SDK to build AI agents that work autonomously

Use the Agent SDK to build an AI agent that reads your code, finds bugs, and fixes them, all without manual intervention.

What you'll do:

Set up a project with the Agent SDK
Create a file with some buggy code
Run an agent that finds and fixes the bugs automatically
Prerequisites
Node.js 18+ or Python 3.10+
An Anthropic account (sign up here)
Setup
1

Install Claude Code

The Agent SDK uses Claude Code as its runtime. Install it for your platform:

macOS/Linux/WSL
Homebrew
WinGet
curl -fsSL https://claude.ai/install.sh | bash

After installing Claude Code onto your machine, run claude in your terminal and follow the prompts to authenticate. The SDK will use this authentication automatically.

For more information on Claude Code installation, see Claude Code setup.

2

Create a project folder

Create a new directory for this quickstart:

mkdir my-agent && cd my-agent

For your own projects, you can run the SDK from any folder; it will have access to files in that directory and its subdirectories by default.

3

Install the SDK

Install the Agent SDK package for your language:

TypeScript
Python (uv)
Python (pip)
npm install @anthropic-ai/claude-agent-sdk
4

Set your API key

If you've already authenticated Claude Code (by running claude in your terminal), the SDK uses that authentication automatically.

Otherwise, you need an API key, which you can get from the Claude Console.

Create a .env file in your project directory and store the API key there:

ANTHROPIC_API_KEY=your-api-key

Using Amazon Bedrock, Google Vertex AI, or Microsoft Azure? See the setup guides for Bedrock, Vertex AI, or Azure AI Foundry.

Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.

Create a buggy file

This quickstart walks you through building an agent that can find and fix bugs in code. First, you need a file with some intentional bugs for the agent to fix. Create utils.py in the my-agent directory and paste the following code:

def calculate_average(numbers):
 total = 0
 for num in numbers:
 total += num
 return total / len(numbers)

def get_user_name(user):
 return user["name"].upper()

This code has two bugs:

calculate_average([]) crashes with division by zero
get_user_name(None) crashes with a TypeError
Build an agent that finds and fixes bugs

Create agent.py if you're using the Python SDK, or agent.ts for TypeScript:

Python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
 # Agentic loop: streams messages as Claude works
 async for message in query(
 prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
 options=ClaudeAgentOptions(
 allowed_tools=["Read", "Edit", "Glob"], # Tools Claude can use
 permission_mode="acceptEdits" # Auto-approve file edits
 )
 ):
 # Print human-readable output
 if isinstance(message, AssistantMessage):
 for block in message.content:
 if hasattr(block, "text"):
 print(block.text) # Claude's reasoning
 elif hasattr(block, "name"):
 print(f"Tool: {block.name}") # Tool being called
 elif isinstance(message, ResultMessage):
 print(f"Done: {message.subtype}") # Final result

asyncio.run(main())

This code has three main parts:

query: the main entry point that creates the agentic loop. It returns an async iterator, so you use async for to stream messages as Claude works. See the full API in the Python or TypeScript SDK reference.

prompt: what you want Claude to do. Claude figures out which tools to use based on the task.

options: configuration for the agent. This example uses allowedTools to restrict Claude to Read, Edit, and Glob, and permissionMode: "acceptEdits" to auto-approve file changes. Other options include systemPrompt, mcpServers, and more. See all options for Python or TypeScript.

The async for loop keeps running as Claude thinks, calls tools, observes results, and decides what to do next. Each iteration yields a message: Claude's reasoning, a tool call, a tool result, or the final outcome. The SDK handles the orchestration (tool execution, context management, retries) so you just consume the stream. The loop ends when Claude finishes the task or hits an error.

The message handling inside the loop filters for human-readable output. Without filtering, you'd see raw message objects including system initialization and internal state, which is useful for debugging but noisy otherwise.

This example uses streaming to show progress in real-time. If you don't need live output (e.g., for background jobs or CI pipelines), you can collect all messages at once. See Streaming vs. single-turn mode for details.

Run your agent

Your agent is ready. Run it with the following command:

Python
TypeScript
python3 agent.py

After running, check utils.py. You'll see defensive code handling empty lists and null users. Your agent autonomously:

Read utils.py to understand the code
Analyzed the logic and identified edge cases that would crash
Edited the file to add proper error handling

This is what makes the Agent SDK different: Claude executes tools directly instead of asking you to implement them.

If you see "Claude Code not found", install Claude Code and restart your terminal. For "API key not found", set your API key. See the full troubleshooting guide for more help.

Try other prompts

Now that your agent is set up, try some different prompts:

"Add docstrings to all functions in utils.py"
"Add type hints to all functions in utils.py"
"Create a README.md documenting the functions in utils.py"
Customize your agent

You can modify your agent's behavior by changing the options. Here are a few examples:

Add web search capability:

Python
options=ClaudeAgentOptions(
 allowed_tools=["Read", "Edit", "Glob", "WebSearch"],
 permission_mode="acceptEdits"
)

Give Claude a custom system prompt:

Python
options=ClaudeAgentOptions(
 allowed_tools=["Read", "Edit", "Glob"],
 permission_mode="acceptEdits",
 system_prompt="You are a senior Python developer. Always follow PEP 8 style guidelines."
)

Run commands in the terminal:

Python
options=ClaudeAgentOptions(
 allowed_tools=["Read", "Edit", "Glob", "Bash"],
 permission_mode="acceptEdits"
)

With Bash enabled, try: "Write unit tests for utils.py, run them, and fix any failures"

Key concepts

Tools control what your agent can do:

Tools What the agent can do
Read, Glob, Grep Read-only analysis
Read, Edit, Glob Analyze and modify code
Read, Edit, Bash, Glob, Grep Full automation

Permission modes control how much human oversight you want:

Mode Behavior Use case
acceptEdits Auto-approves file edits, asks for other actions Trusted development workflows
bypassPermissions Runs without prompts CI/CD pipelines, automation
default Requires a canUseTool callback to handle approval Custom approval flows

The example above uses acceptEdits mode, which auto-approves file operations so the agent can run without interactive prompts. If you want to prompt users for approval, use default mode and provide a canUseTool callback that collects user input. For more control, see Permissions.

Next steps

Now that you've created your first agent, learn how to extend its capabilities and tailor it to your use case:

Permissions: control what your agent can do and when it needs approval
Hooks: run custom code before or after tool calls
Sessions: build multi-turn agents that maintain context
MCP servers: connect to databases, browsers, APIs, and other external systems
Hosting: deploy agents to Docker, cloud, and CI/CD
Example agents: see complete examples: email assistant, research agent, and more

Was this page helpful?