---
title: "Get started with Claude Managed Agents - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
tags: ["agents", "api", "cli", "sdk"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fquickstart)





SearchCtrlK

First steps

[Overview](/docs/en/managed-agents/overview)[Quickstart](/docs/en/managed-agents/quickstart)[Build in Console](/docs/en/managed-agents/onboarding)[Migration](/docs/en/managed-agents/migration)

Define your agent

[Agent setup](/docs/en/managed-agents/agent-setup)[Tools](/docs/en/managed-agents/tools)[MCP connector](/docs/en/managed-agents/mcp-connector)[Permission policies](/docs/en/managed-agents/permission-policies)[Agent Skills](/docs/en/managed-agents/skills)

Configure agent environment

[Cloud environment setup](/docs/en/managed-agents/environments)[Cloud sandbox reference](/docs/en/managed-agents/cloud-sandboxes-reference)

[Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes)

Delegate work to your agent

[Start a session](/docs/en/managed-agents/sessions)[Session operations](/docs/en/managed-agents/session-operations)[Session event stream](/docs/en/managed-agents/events-and-streaming)[Session budgets](/docs/en/managed-agents/budgets)[Subscribe to webhooks](/docs/en/managed-agents/webhooks)[Define outcomes](/docs/en/managed-agents/define-outcomes)[Authenticate with vaults](/docs/en/managed-agents/vaults)

Manage agent context

[Access GitHub](/docs/en/managed-agents/github)[Attach and download files](/docs/en/managed-agents/files)

Build persistent memory

Advanced orchestration

[Multiagent orchestration](/docs/en/managed-agents/multiagent-orchestration)[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Reference

[Managed Agents reference](/docs/en/managed-agents/reference)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)

[Console](/)

[Managed Agents](/docs/en/managed-agents/overview)First steps

# Get started with Claude Managed Agents

Copy page



Create your first autonomous agent.

Copy page



[Managed Agents](/docs/en/managed-agents/overview)

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

managed-agents-2026-04-01

This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.



**Prefer an interactive walkthrough?** Run `/claude-api managed-agents-onboard` in the latest version of [Claude Code](https://claude.com/product/claude-code) for a guided setup and interactive question-answering.

## Core concepts

| Concept         | Description                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Agent**       | The model, system prompt, tools, MCP servers, and skills                                                                      |
| **Environment** | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure |
| **Session**     | A running agent instance within an environment, performing a specific task and generating outputs                             |
| **Events**      | Messages exchanged between your application and the agent (user turns, tool results, status updates)                          |

## Prerequisites

- A [Claude Console account](https://platform.claude.com)
- An [API key](/settings/keys)

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

    [`ant apply`](/docs/en/cli-sdks-libraries/cli/apply) prints the agent's ID and records it in `claude-lock.json`. You'll reference it in every session you create.

    The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](/docs/en/managed-agents/tools) for the complete list and per-tool configuration options.

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

    [`ant apply`](/docs/en/cli-sdks-libraries/cli/apply) records the environment's ID in `claude-lock.json` too. To create the agent and the environment with one command, pass both files: `ant apply coding-assistant.md environment.yaml`.

    
    To run the sandbox on your own infrastructure instead of a cloud sandbox, see [Self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes).

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

[Define your agent](/docs/en/managed-agents/agent-setup)

Create reusable, versioned agent configurations



[Configure environments](/docs/en/managed-agents/environments)

Customize networking and sandbox settings



[Agent tools](/docs/en/managed-agents/tools)

Enable specific tools for your agent



[Session event stream](/docs/en/managed-agents/events-and-streaming)

Handle events and steer the agent mid-execution



[Scheduled deployments](/docs/en/managed-agents/scheduled-deployments)

Run your agent on a recurring cron schedule

[Knowledge wiki quickstart](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/knowledge-wiki)

Distill a document corpus once into a knowledge wiki, then answer repeated questions from it at a fraction of the cost
