---
source_url: "https://platform.claude.com/docs/en/managed-agents/quickstart"
category: "Agents-Patterns"
fetched_at: "2026-04-08"
---

# Get started with Claude Managed Agents

Create your first autonomous agent.

---

This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

## Core concepts

| Concept | Description |
|---------|-------------|
| **Agent** | The model, system prompt, tools, MCP servers, and skills |
| **Environment** | A configured container template (packages, network access) |
| **Session** | A running agent instance within an environment, performing a specific task and generating outputs |
| **Events** | Messages exchanged between your application and the agent (user turns, tool results, status updates) |

## Prerequisites

- An Anthropic [Console account](/)
- An [API key](/settings/keys)

## Install the CLI

### Homebrew (macOS)

```bash
brew install anthropics/tap/ant
```

On macOS, unquarantine the binary:

```bash
xattr -d com.apple.quarantine "$(brew --prefix)/bin/ant"
```

### curl (Linux/WSL)

For Linux environments, download the release binary directly.

```bash
VERSION=1.0.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant
```

You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).

### Go

You may also install the CLI from source using `go install`. Requires Go 1.22 or later.

```bash
go install github.com/anthropics/anthropic-cli/cmd/ant@latest
```

The binary is placed in `$(go env GOPATH)/bin`. Add it to your `PATH` if it isn't already:

```bash
export PATH="$PATH:$(go env GOPATH)/bin"
```

Check the installation:

```bash
ant --version
```

## Install the SDK

### Python
```bash
pip install anthropic
```

### TypeScript
```bash
npm install @anthropic-ai/sdk
```

### Java
```groovy
implementation("com.anthropic:anthropic-java:2.20.0")
```

### Go
```bash
go get github.com/anthropics/anthropic-sdk-go
```

### C#
```bash
dotnet add package Anthropic
```

### Ruby
```bash
bundle add anthropic
```

### PHP
```bash
composer require anthropic-ai/sdk
```

Set your API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Create your first session

> All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

### Step 1: Create an agent

Create an agent that defines the model, system prompt, and available tools.

```python
from anthropic import Anthropic

client = Anthropic()

agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-sonnet-4-6",
    system="You are a helpful coding assistant. Write clean, well-documented code.",
    tools=[
        {"type": "agent_toolset_20260401"},
    ],
)

print(f"Agent ID: {agent.id}, version: {agent.version}")
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const agent = await client.beta.agents.create({
  name: "Coding Assistant",
  model: "claude-sonnet-4-6",
  system: "You are a helpful coding assistant. Write clean, well-documented code.",
  tools: [
    { type: "agent_toolset_20260401" },
  ],
});

console.log(`Agent ID: ${agent.id}, version: ${agent.version}`);
```

The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](/docs/en/managed-agents/tools) for the complete list and per-tool configuration options.

Save the returned `agent.id`. You'll reference it in every session you create.

### Step 2: Create an environment

An environment defines the container where your agent runs.

```python
environment = client.beta.environments.create(
    name="quickstart-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)

print(f"Environment ID: {environment.id}")
```

```typescript
const environment = await client.beta.environments.create({
  name: "quickstart-env",
  config: {
    type: "cloud",
    networking: { type: "unrestricted" },
  },
});

console.log(`Environment ID: ${environment.id}`);
```

Save the returned `environment.id`. You'll reference it in every session you create.

### Step 3: Start a session

Create a session that references your agent and environment.

```python
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)

print(f"Session ID: {session.id}")
```

```typescript
const session = await client.beta.sessions.create({
  agent: agent.id,
  environment_id: environment.id,
  title: "Quickstart session",
});

console.log(`Session ID: ${session.id}`);
```

### Step 4: Send a message and stream the response

Open a stream, send a user event, then process events as they arrive:

```python
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
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
                break
```

```typescript
const stream = await client.beta.sessions.events.stream(session.id);

// Send the user message after the stream opens
await client.beta.sessions.events.send(session.id, {
  events: [
    {
      type: "user.message",
      content: [
        {
          type: "text",
          text: "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
        },
      ],
    },
  ],
});

// Process streaming events
for await (const event of stream) {
  if (event.type === "agent.message") {
    for (const block of event.content) {
      process.stdout.write(block.text);
    }
  } else if (event.type === "agent.tool_use") {
    console.log(`\n[Using tool: ${event.name}]`);
  } else if (event.type === "session.status_idle") {
    console.log("\n\nAgent finished.");
    break;
  }
}
```

The agent will write a Python script, execute it in the container, and verify the output file was created. Your output will look similar to this:

```text
I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
[Using tool: write]
[Using tool: bash]
The script ran successfully. Let me verify the output file.
[Using tool: bash]
fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

Agent finished.
```

## What's happening

When you send a user event, Claude Managed Agents:

1. **Provisions a container:** Your environment configuration determines how it's built.
2. **Runs the agent loop:** Claude decides which tools to use based on your message
3. **Executes tools:** File writes, bash commands, and other tool calls run inside the container
4. **Streams events:** You receive real-time updates as the agent works
5. **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do

## Next steps

- [Define your agent](/docs/en/managed-agents/agent-setup) - Create reusable, versioned agent configurations
- [Configure environments](/docs/en/managed-agents/environments) - Customize networking and container settings
- [Agent tools](/docs/en/managed-agents/tools) - Enable specific tools for your agent
- [Events and streaming](/docs/en/managed-agents/events-and-streaming) - Handle events and steer the agent mid-execution
