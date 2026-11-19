---
title: "Get started with Claude - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/get-started"
category: "01-Getting-Started"
fetched_at: "2026-11-13T06:36:41Z"
tags: ["api", "getting-started"]
---

# Get started with Claude

Copy page



Make your first API call to Claude and build a simple web search assistant.

Copy page



## Before you begin

1.  1

    ### Create a Claude Console account

    [Sign up](../04-API-Reference/Other/playground.md) for a Claude Console account, or sign in to the one you have.

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
    VERSION=2.9.0
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

    You can also install the CLI from source with `go install`, which requires Go 1.26.10 or later.

    ``` shiki
    go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest
    ```

    

    `go install` places the binary in `$(go env GOPATH)/bin`. Add that directory to your `PATH` if it isn’t already there:

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

    Create an [API key](../04-API-Reference/Other/playground.md) in the Claude Console.

2.  4

    ### Set the environment variable

    The SDKs and CLI read your key from `ANTHROPIC_API_KEY`:

    ``` shiki
    export ANTHROPIC_API_KEY="your-api-key-here"
    ```

    

## Call the API

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

1.  5

    ### Create a project and install the SDK

    ``` shiki
    mkdir claude-quickstart && cd claude-quickstart
    python3 -m venv .venv && source .venv/bin/activate
    pip install anthropic
    ```

    

2.  6

    ### Create your code

    Create a file called `quickstart.py`:

    Python

    

    ``` shiki
    import anthropic

    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": "What should I search for to find the latest developments in renewable energy?",
            }
        ],
    )

    for block in message.content:
        if block.type == "text":
            print(block.text)
    ```

3.  7

    ### Run your code

    ``` shiki
    python quickstart.py
    ```

    

    Output

    

    ``` block
    Here are some effective search strategies to find the latest developments in renewable energy:

    ## General Search Terms
    - "Renewable energy news 2025"
    - ...
    ```

## Next steps

You made your first API call. Next, learn the Messages API patterns you’ll use in every Claude integration.



[Working with the Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md)

Learn multi-turn conversations, system prompts, stop reasons, and other core patterns.

Once you’re comfortable with the basics, explore further:



[Models overview](../20-Models/about-claude-models-overview.md)

Compare Claude models by capability and cost.



[Features overview](../04-API-Reference/Guides/build-with-claude-overview.md)

Browse all Claude capabilities: tools, context management, structured outputs, and more.



[Client SDKs](../04-API-Reference/Other/cli-sdks-libraries-overview.md)

Reference documentation for Python, TypeScript, C#, and other client libraries.



[Authentication](../04-API-Reference/Other/manage-claude-authentication.md)

Compare API keys and Workload Identity Federation, and set key expiration.
