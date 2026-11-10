---
title: "Get started with Claude Managed Agents - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/quickstart"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:37:23Z"
tags: ["agents", "api", "sdk"]
---

# Get started with Claude Managed Agents

Copy page



Create your first autonomous agent.

Copy page



[Managed Agents](managed-agents-overview.md)

[Status](managed-agents-overview.md#availability-feature-support)  
Beta

[Cloud platforms](managed-agents-overview.md#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableClaude Models on Google CloudAnthropic managedAvailable

[Beta header](managed-agents-overview.md#feature-beta-headers)  
- `managed-agents-2026-04-01`
  

[Data handling](managed-agents-overview.md#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

Claude Code

Let Claude Code set up your agent for you

Run in

`❯``/claude-api`` managed-agents-onboard`



## Core concepts

| Concept | Description |
|----|----|
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

## Before you begin

1.  1

    ### Create a Claude Console account

    [Sign up](playground.md) for a Claude Console account, or sign in to the one you have.

2.  2

    ### Choose how to authenticate

    Signing in with the CLI is recommended for local development.

    CLIAPI key

1.  3

    ### Install the CLI

    Homebrew (macOS)
    curl (Linux/WSL)
    go install

    Homebrew (macOS)

    ``` shiki
    brew install anthropics/tap/ant
    ```

    

    curl (Linux/WSL)

    For Linux environments, download the release binary directly.

    ``` shiki
    VERSION=2.6.0
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
    case $(uname -m) in
      x86_64) ARCH=amd64 ;;
      aarch64) ARCH=arm64 ;;
    esac
    curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
      | sudo tar -xz -C /usr/local/bin ant
    ```

    

    You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

    go install

    You can also install the CLI from source using `go install`. Requires Go 1.25 or later.

    ``` shiki
    go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest
    ```

    

    The binary is placed in `$(go env GOPATH)/bin`. Add it to your `PATH` if it isn’t already:

    ``` shiki
    export PATH="$PATH:$(go env GOPATH)/bin"
    ```

    

2.  4

    ### Sign in

    ``` shiki
    ant auth login
    ```

    

    Once login is completed, the SDKs and CLI will pick up your credentials automatically.

1.  3

    ### Create an API key

    Create an [API key](playground.md) in the Claude Console.

2.  4

    ### Set the environment variable

    The SDKs and CLI read your key from `ANTHROPIC_API_KEY`:

    ``` shiki
    export ANTHROPIC_API_KEY="your-api-key-here"
    ```

    

To run the CLI examples, install the CLI:

Homebrew (macOS)

curl (Linux/WSL)

go install

Homebrew (macOS)

```python
brew install anthropics/tap/ant
```



curl (Linux/WSL)

For Linux environments, download the release binary directly.

```python
VERSION=2.6.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
case $(uname -m) in
  x86_64) ARCH=amd64 ;;
  aarch64) ARCH=arm64 ;;
esac
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant
```



You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

go install

You can also install the CLI from source using `go install`. Requires Go 1.25 or later.

```python
go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest
```



The binary is placed in `$(go env GOPATH)/bin`. Add it to your `PATH` if it isn’t already:

```python
export PATH="$PATH:$(go env GOPATH)/bin"
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

Python

```python
pip install anthropic
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

    CLI

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
        configs:
          - name: web_search
            enabled: false
          - name: web_fetch
            enabled: false
    ---

    You are a helpful coding assistant. Write clean, well-documented code.
    ```

    [`ant apply`](cli-sdks-libraries-cli-apply.md) prints the agent’s ID and records it in `claude-lock.json`. You’ll reference it in every session you create.

    The `agent_toolset_20260401` tool type enables the prebuilt agent tools (bash, file operations, web search, and more). This example disables web search and web fetch because the task in this guide, writing a short Python script, doesn’t use the web. Give an agent [only the tools it needs](managed-agents-secure-deployment.md#give-the-agent-the-smallest-tool-set). See [Tools](managed-agents-tools.md) for the complete list and per-tool configuration options.

2.  2

    ### Create an environment

    An environment defines the sandbox where your agent runs. This one uses `limited` [networking](managed-agents-environments.md#networking) with package managers allowed, so code running in the sandbox can reach public [package registries and code hosts](managed-agents-environments.md#package-manager-hosts). With `limited` networking, the [`allowed_hosts` list](managed-agents-environments.md#networking) also applies to web search and web fetch, even though they run outside the sandbox. With no hosts listed, as in this environment, they return no pages or search results. If your own agent uses these tools, add the hosts it needs to that list.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    CLI

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
        type: limited
        allow_package_managers: true
    ```

    [`ant apply`](cli-sdks-libraries-cli-apply.md) records the environment’s ID in `claude-lock.json` too. To create the agent and the environment with one command, pass both files: `ant apply coding-assistant.md environment.yaml`.

    
    This quickstart uses a cloud environment. To decide whether to run tools on your own infrastructure with a [self-hosted sandbox](managed-agents-self-hosted-sandboxes.md) instead, see [Choosing an agent environment](managed-agents-choosing-an-environment.md).

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

    Python

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

    Python

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

## What’s happening

When you send a user event, Claude Managed Agents:

1.  **Provisions a sandbox:** Your environment configuration determines how it’s built.
2.  **Runs the agent loop:** Claude determines which tools to use based on your message.
3.  **Runs tools:** File writes, bash commands, and other tool calls run inside the sandbox.
4.  **Streams events:** You receive real-time updates as the agent works.
5.  **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do.

## Build a complete app

Each of these quickstarts pairs Claude Managed Agents with a popular chat framework to make a complete, runnable application. In each one, the framework renders the chat surface while a managed session runs the agent loop server-side: the session holds the transcript, runs tools in a sandbox, and streams events that the front end renders.

[Chat SDK](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/chat-sdk)

A research analyst in a browser chat built with Vercel’s Chat SDK. Each conversation is one persistent session that streams its reply while a live feed shows the tool calls. Swapping the Chat SDK adapter moves the same handler to Slack, Teams, Discord, or WhatsApp.

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

Handle events and steer the agent while it runs



[Scheduled deployments](managed-agents-scheduled-deployments.md)

Run your agent on a recurring cron schedule

[Knowledge wiki quickstart](https://github.com/anthropics/claude-quickstarts/tree/main/managed-agents/knowledge-wiki)

Distill a document corpus once into a knowledge wiki, then answer repeated questions from it at a fraction of the cost
