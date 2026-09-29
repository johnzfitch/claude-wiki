---
title: "Get started with Claude Managed Agents - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
tags: ["agents", "api", "cli", "sdk"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fquickstart)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)First steps

# Get started with Claude Managed Agents

Copy page



Create your first autonomous agent.

Copy page



[Managed Agents](managed-agents-overview.md)

[Beta](../Guides/build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

managed-agents-2026-04-01

This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.



**Prefer an interactive walkthrough?** Run `/claude-api managed-agents-onboard` in the latest version of [Claude Code](../../15-Claude-AI-Features/claude-com-product-claude-code.md) for a guided setup and interactive question-answering.

## Core concepts

| Concept         | Description                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Agent**       | The model, system prompt, tools, MCP servers, and skills                                                                      |
| **Environment** | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure |
| **Session**     | A running agent instance within an environment, performing a specific task and generating outputs                             |
| **Events**      | Messages exchanged between your application and the agent (user turns, tool results, status updates)                          |

## Prerequisites

- A [Claude Console account](usage-limits.md)
- An [API key](usage-limits.md)

## Install the CLI

Homebrew (macOS)

curl (Linux/WSL)

Go

```python
brew install anthropics/tap/ant
```



Check the installation:

```python
ant --version
```



## Install the SDK

Python

TypeScript

Java

Go

C#

Ruby

PHP

```python
pip install anthropic
```



Set your API key as an environment variable:

```python
export ANTHROPIC_API_KEY="your-api-key-here"
```



## Create your first session

1.  1

    ### Create an agent

    Create an agent that defines the model, system prompt, and available tools.

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
    ant apply coding-assistant.md
    ```

    coding-assistant.md
    
    

    ``` shiki
    ---
    name: Coding Assistant
    model: claude-opus-5-5
    tools:
      - type: agent_toolset_20260401
    ---

    You are a helpful coding assistant. Write clean, well-documented code.
    ```

    [`ant apply`](cli-sdks-libraries-cli-apply.md) prints the agent's ID and records it in `claude-lock.json`. You'll reference it in every session you create.

    The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](managed-agents-tools.md) for the complete list and per-tool configuration options.

2.  2

    ### Create an environment

    An environment defines the sandbox where your agent runs.

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
    ant apply environment.yaml
    ```

    environment.yaml
    
    

    ``` shiki
    # yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
    name: quickstart-env
    config:
      type: cloud
      networking:
        type: unrestricted
    ```

    [`ant apply`](cli-sdks-libraries-cli-apply.md) records the environment's ID in `claude-lock.json` too. To create the agent and the environment with one command, pass both files: `ant apply coding-assistant.md environment.yaml`.

    
    To run the sandbox on your own infrastructure instead of a cloud sandbox, see [Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md).

3.  3

    ### Start a session

    Create a session that references your agent and environment.

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
    session = client.beta.sessions.create(
        agent=agent.id,
        environment_id=environment.id,
        title="Quickstart session",
    )

    print(f"Session ID: {session.id}")
    ```

4.  4

    ### Send a message and stream the response

    Open a stream, send a user event, then process events as they arrive:

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
    with client.beta.sessions.events.stream(session.id) as stream:
        # Send the user message after the stream opens
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.message",
                    "content": [
                        {
                            "type": "text",
                            "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                        },
                    ],
                },
            ],
        )

        # Process streaming events
        for event in stream:
            match event.type:
                case "agent.message":
                    for block in event.content:
                        if block.type == "text":
                            print(block.text, end="")
                case "agent.tool_use":
                    print(f"\n[Using tool: {event.name}]")
                case "session.status_idle":
                    print("\n\nAgent finished.")
                    break
    ```

    The agent writes a Python script, runs it in the sandbox, and verifies the output file was created. Your output looks similar to this:

    ``` block
    I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
    [Using tool: write]
    [Using tool: bash]
    The script ran successfully. Let me verify the output file.
    [Using tool: bash]
    fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

    Agent finished.
    ```

    

## What's happening

When you send a user event, Claude Managed Agents:

1.  **Provisions a sandbox:** Your environment configuration determines how it's built.
2.  **Runs the agent loop:** Claude determines which tools to use based on your message.
3.  **Runs tools:** File writes, bash commands, and other tool calls run inside the sandbox.
4.  **Streams events:** You receive real-time updates as the agent works.
5.  **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do.

## Build a complete app

Each of these quickstarts pairs Claude Managed Agents with a popular chat framework to make a complete, runnable application. In each one, the framework renders the chat surface while a managed session runs the agent loop server-side: the session holds the transcript, runs tools in a sandbox, and streams events that the front end renders.

[Chat SDK](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/chat-sdk)

A research analyst in a browser chat built with Vercel's Chat SDK. Each conversation is one persistent session that streams its reply while a live feed shows the tool calls. Swapping the Chat SDK adapter moves the same handler to Slack, Teams, Discord, or WhatsApp.

[assistant-ui](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/assistant-ui)

A spreadsheet analyst in a chat built from assistant-ui primitives. Sessions are the thread list, one reducer turns the session event log into messages and tool cards, and each bash command renders an inline Allow/Deny gate before it runs.

[CopilotKit (AG-UI)](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/copilot-kit-ag-ui)

A personal finance assistant in a CopilotKit chat. The AG-UI adapter for Claude Managed Agents maps each chat thread to a managed session and streams replies token by token, and custom tools render interactive charts inline in the conversation.

## Next steps



[Define your agent](managed-agents-agent-setup.md)

Create reusable, versioned agent configurations



[Configure environments](managed-agents-environments.md)

Customize networking and sandbox settings



[Agent tools](managed-agents-tools.md)

Enable specific tools for your agent



[Session event stream](managed-agents-events-and-streaming.md)

Handle events and steer the agent mid-execution



[Scheduled deployments](managed-agents-scheduled-deployments.md)

Run your agent on a recurring cron schedule

[Knowledge wiki quickstart](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/knowledge-wiki)

Distill a document corpus once into a knowledge wiki, then answer repeated questions from it at a fraction of the cost
