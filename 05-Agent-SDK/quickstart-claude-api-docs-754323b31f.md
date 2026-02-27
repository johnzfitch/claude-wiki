---
category: "05-Agent-SDK"
fetched_at: "2026-02-07T10:04:32Z"
source_url: "https://platform.claude.com/docs/en/agent-sdk/quickstart"
title: "Quickstart - Claude API Docs"
---

Agent SDK

# Quickstart

Copy page

Get started with the Python or TypeScript Agent SDK to build AI agents that work autonomously

Copy page

Use the Agent SDK to build an AI agent that reads your code, finds bugs, and fixes them, all without manual intervention.

**What you'll do:**

1.  Set up a project with the Agent SDK
2.  Create a file with some buggy code
3.  Run an agent that finds and fixes the bugs automatically

## 

Prerequisites

- **Node.js 18+** or **Python 3.10+**
- An **Anthropic account** ([sign up here](https://platform.claude.com/))

## 

Setup

1.  1

    Create a project folder

    Create a new directory for this quickstart:

    ``` shiki
    mkdir my-agent && cd my-agent
    ```

    For your own projects, you can run the SDK from any folder; it will have access to files in that directory and its subdirectories by default.

2.  2

    Install the SDK

    Install the Agent SDK package for your language:

    TypeScript

    TypeScript

    Python (uv)

    Python (uv)

    Python (pip)

    Python (pip)

    ``` shiki
    npm install @anthropic-ai/claude-agent-sdk
    ```

3.  3

    Set your API key

    Get an API key from the [Claude Console](https://platform.claude.com/), then create a `.env` file in your project directory:

    ``` shiki
    ANTHROPIC_API_KEY=your-api-key
    ```

    The SDK also supports authentication via third-party API providers:

    - **Amazon Bedrock**: set `CLAUDE_CODE_USE_BEDROCK=1` environment variable and configure AWS credentials
    - **Google Vertex AI**: set `CLAUDE_CODE_USE_VERTEX=1` environment variable and configure Google Cloud credentials
    - **Microsoft Azure**: set `CLAUDE_CODE_USE_FOUNDRY=1` environment variable and configure Azure credentials

    See the setup guides for [Bedrock](https://code.claude.com/docs/en/amazon-bedrock), [Vertex AI](https://code.claude.com/docs/en/google-vertex-ai), or [Azure AI Foundry](https://code.claude.com/docs/en/azure-ai-foundry) for details.

    Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.

## 

Create a buggy file

This quickstart walks you through building an agent that can find and fix bugs in code. First, you need a file with some intentional bugs for the agent to fix. Create `utils.py` in the `my-agent` directory and paste the following code:

``` shiki
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def get_user_name(user):
    return user["name"].upper()
```

This code has two bugs:

1.  `calculate_average([])` crashes with division by zero
2.  `get_user_name(None)` crashes with a TypeError

## 

Build an agent that finds and fixes bugs

Create `agent.py` if you're using the Python SDK, or `agent.ts` for TypeScript:

Python

``` shiki
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
    # Agentic loop: streams messages as Claude works
    async for message in query(
        prompt="Review utils.py for bugs that would cause crashes. Fix any issues you find.",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob"],  # Tools Claude can use
            permission_mode="acceptEdits"            # Auto-approve file edits
        )
    ):
        # Print human-readable output
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)              # Claude's reasoning
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")   # Tool being called
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}")      # Final result

asyncio.run(main())
```

This code has three main parts:

1.  **`query`**: the main entry point that creates the agentic loop. It returns an async iterator, so you use `async for` to stream messages as Claude works. See the full API in the [Python](/docs/en/agent-sdk/python#query) or [TypeScript](/docs/en/agent-sdk/typescript#query) SDK reference.

2.  **`prompt`**: what you want Claude to do. Claude figures out which tools to use based on the task.

3.  **`options`**: configuration for the agent. This example uses `allowedTools` to restrict Claude to `Read`, `Edit`, and `Glob`, and `permissionMode: "acceptEdits"` to auto-approve file changes. Other options include `systemPrompt`, `mcpServers`, and more. See all options for [Python](/docs/en/agent-sdk/python#claudeagentoptions) or [TypeScript](/docs/en/agent-sdk/typescript#claudeagentoptions).

The `async for` loop keeps running as Claude thinks, calls tools, observes results, and decides what to do next. Each iteration yields a message: Claude's reasoning, a tool call, a tool result, or the final outcome. The SDK handles the orchestration (tool execution, context management, retries) so you just consume the stream. The loop ends when Claude finishes the task or hits an error.

The message handling inside the loop filters for human-readable output. Without filtering, you'd see raw message objects including system initialization and internal state, which is useful for debugging but noisy otherwise.

This example uses streaming to show progress in real-time. If you don't need live output (e.g., for background jobs or CI pipelines), you can collect all messages at once. See [Streaming vs. single-turn mode](/docs/en/agent-sdk/streaming-vs-single-mode) for details.

### 

Run your agent

Your agent is ready. Run it with the following command:

Python

Python

TypeScript

TypeScript

``` shiki
python3 agent.py
```

After running, check `utils.py`. You'll see defensive code handling empty lists and null users. Your agent autonomously:

1.  **Read** `utils.py` to understand the code
2.  **Analyzed** the logic and identified edge cases that would crash
3.  **Edited** the file to add proper error handling

This is what makes the Agent SDK different: Claude executes tools directly instead of asking you to implement them.

If you see "API key not found", make sure you've set the `ANTHROPIC_API_KEY` environment variable in your `.env` file or shell environment. See the [full troubleshooting guide](https://code.claude.com/docs/en/troubleshooting) for more help.

### 

Try other prompts

Now that your agent is set up, try some different prompts:

- `"Add docstrings to all functions in utils.py"`
- `"Add type hints to all functions in utils.py"`
- `"Create a README.md documenting the functions in utils.py"`

### 

Customize your agent

You can modify your agent's behavior by changing the options. Here are a few examples:

**Add web search capability:**

Python

``` shiki
options=ClaudeAgentOptions(
    allowed_tools=["Read", "Edit", "Glob", "WebSearch"],
    permission_mode="acceptEdits"
)
```

**Give Claude a custom system prompt:**

Python

``` shiki
options=ClaudeAgentOptions(
    allowed_tools=["Read", "Edit", "Glob"],
    permission_mode="acceptEdits",
    system_prompt="You are a senior Python developer. Always follow PEP 8 style guidelines."
)
```

**Run commands in the terminal:**

Python

``` shiki
options=ClaudeAgentOptions(
    allowed_tools=["Read", "Edit", "Glob", "Bash"],
    permission_mode="acceptEdits"
)
```

With `Bash` enabled, try: `"Write unit tests for utils.py, run them, and fix any failures"`

## 

Key concepts

**Tools** control what your agent can do:

| Tools                                  | What the agent can do   |
|----------------------------------------|-------------------------|
| `Read`, `Glob`, `Grep`                 | Read-only analysis      |
| `Read`, `Edit`, `Glob`                 | Analyze and modify code |
| `Read`, `Edit`, `Bash`, `Glob`, `Grep` | Full automation         |

**Permission modes** control how much human oversight you want:

| Mode | Behavior | Use case |
|----|----|----|
| `acceptEdits` | Auto-approves file edits, asks for other actions | Trusted development workflows |
| `bypassPermissions` | Runs without prompts | CI/CD pipelines, automation |
| `default` | Requires a `canUseTool` callback to handle approval | Custom approval flows |

The example above uses `acceptEdits` mode, which auto-approves file operations so the agent can run without interactive prompts. If you want to prompt users for approval, use `default` mode and provide a [`canUseTool` callback](/docs/en/agent-sdk/user-input) that collects user input. For more control, see [Permissions](/docs/en/agent-sdk/permissions).

## 

Next steps

Now that you've created your first agent, learn how to extend its capabilities and tailor it to your use case:

- **[Permissions](/docs/en/agent-sdk/permissions)**: control what your agent can do and when it needs approval
- **[Hooks](/docs/en/agent-sdk/hooks)**: run custom code before or after tool calls
- **[Sessions](/docs/en/agent-sdk/sessions)**: build multi-turn agents that maintain context
- **[MCP servers](/docs/en/agent-sdk/mcp)**: connect to databases, browsers, APIs, and other external systems
- **[Hosting](/docs/en/agent-sdk/hosting)**: deploy agents to Docker, cloud, and CI/CD
- **[Example agents](https://github.com/anthropics/claude-agent-sdk-demos)**: see complete examples: email assistant, research agent, and more

Was this page helpful?

- 

- [Prerequisites](#prerequisites)

- [Setup](#setup)

- [Create a buggy file](#create-a-buggy-file)

- [Build an agent that finds and fixes bugs](#build-an-agent-that-finds-and-fixes-bugs)

- [Run your agent](#run-your-agent)

- [Try other prompts](#try-other-prompts)

- [Customize your agent](#customize-your-agent)

- [Key concepts](#key-concepts)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
