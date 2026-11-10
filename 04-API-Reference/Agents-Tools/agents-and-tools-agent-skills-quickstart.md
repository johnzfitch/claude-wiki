---
title: "Get started with Agent Skills in the API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-11-05T06:35:27Z"
tags: ["agents", "api", "skills"]
---

# Get started with Agent Skills in the API

Copy page



Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.

Copy page



This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You’ll learn how to enable Skills, make a request, and access the generated file.

## Before you begin

You need a [client SDK](../Other/cli-sdks-libraries-overview.md) for your language, or `curl` and `jq`, and basic familiarity with making API requests.

1.  1

    ### Create a Claude Console account

    [Sign up](../Other/playground.md) for a Claude Console account, or sign in to the one you have.

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

    Create an [API key](../Other/playground.md) in the Claude Console.

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

## Agent Skills overview

Pre-built Agent Skills extend Claude’s capabilities with specialized expertise for tasks such as creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:

- **PowerPoint (pptx):** Create and edit presentations
- **Excel (xlsx):** Create and analyze spreadsheets
- **Word (docx):** Create and edit documents
- **PDF (pdf):** Generate PDF documents



To create custom Skills, see the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) for examples of building your own Skills with domain-specific expertise.

## Step 1: List available Skills

First, check what Skills are available. Use the Skills API to list all Anthropic-managed Skills. The example is an excerpt from one continuous script, with any imports and client setup at the top:

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

```python
# List Anthropic-managed Skills
skills = client.skills.list(source="anthropic")

for skill in skills.data:
    print(f"{skill.id}: {skill.display_name}")
```

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.

This API returns each Skill’s metadata: its name and description. Claude loads this metadata at startup to determine which Skills are available. This is the first level of **progressive disclosure**, where Claude discovers Skills without loading their full instructions yet.

## Step 2: Create a presentation

Use the PowerPoint Skill to create a presentation about renewable energy. Specify Skills using the `container` parameter in the Messages API:

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

```python
# Create a message with the PowerPoint Skill
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create a presentation about renewable energy with 5 slides",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)

print(f"stop_reason={response.stop_reason}, blocks={len(response.content)}")
```

The request includes the following parts:

- **`model`:** A [model that supports the code execution tool](agents-and-tools-tool-use-code-execution-tool.md#availability-feature-support)
- **`container.skills`:** Specifies which Skills Claude can use
- **`type: "anthropic"`:** Indicates this is an Anthropic-managed Skill
- **`skill_id: "pptx"`:** The PowerPoint Skill identifier
- **`version: "latest"`:** The Skill version set to the most recently published
- **`tools`:** Enables code execution (required for Skills)



The examples use the `code_execution_20260521` tool version, and the Step 3 code parses the result types that current tool versions return. Skills also work with other [code execution tool](agents-and-tools-tool-use-code-execution-tool.md) versions such as `code_execution_20250825`: any current code execution tool version satisfies the Skills requirement. If you use a different version, use the tool `type` listed on the code execution tool page.

When you make this request, Claude automatically matches your task to the relevant Skill. Because you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude runs the Skill’s code to create your presentation.

## Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The Step 2 `response` includes a file reference with a file ID. Extract the file ID and download the file with the Files API. The example saves it to your system temp directory:

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

```python
# Extract the file ID. The code execution tool runs the Skill's code through
# its Bash sub-tool, and generated files appear as bash_code_execution_output
# items inside the bash_code_execution_tool_result block.
file_id = None
for block in response.content:
    if block.type == "bash_code_execution_tool_result":
        if block.content.type == "bash_code_execution_result":
            for output in block.content.content:
                file_id = output.file_id

if file_id:
    # Download the file and save it
    output_path = Path(tempfile.gettempdir()) / "renewable_energy.pptx"
    file_content = client.files.download(file_id=file_id)
    file_content.write_to_file(output_path)
    print(f"Presentation saved to {output_path}")
```



For complete details on working with generated files, see [Retrieve generated files](agents-and-tools-tool-use-code-execution-tool.md#retrieve-generated-files) in the code execution tool documentation.

## Try more examples

Try these variations:

### Create a spreadsheet

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

```python
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create a quarterly sales tracking spreadsheet with sample data",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

### Create a Word document

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

```python
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    container={
        "skills": [{"type": "anthropic", "skill_id": "docx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Write a 2-page report on the benefits of renewable energy",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

### Generate a PDF

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

```python
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    container={
        "skills": [{"type": "anthropic", "skill_id": "pdf", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Generate a PDF invoice template",
        }
    ],
    tools=[{"type": "code_execution_20260521", "name": "code_execution"}],
)
```

## Next steps



[Skill authoring best practices](agents-and-tools-agent-skills-best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.



[Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md)

Learn how to use Agent Skills to extend Claude’s capabilities through the API.



[Create custom Skills](../Endpoints/skills-create.md)

Upload your own Skills for specialized tasks.



[Use Skills in Claude Code](../../08-Plugins-Skills/skills.md)

Learn about Skills in Claude Code.



[Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)

Explore example Skills and implementation patterns.
