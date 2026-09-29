---
title: "Using Agent Skills with the API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/skills-guide"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:26Z"
tags: ["agents", "api", "skills"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fskills-guide)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Skills

# Using Agent Skills with the API

Copy page



Learn how to use Agent Skills to extend Claude's capabilities through the API.

Copy page



Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.



For complete API reference including request/response schemas and all parameters, see:

- [Skill Management API Reference](../Endpoints/skills-list.md) - CRUD operations for Skills
- [Skill Versions API Reference](../Endpoints/skills-versions-list.md) - Version management



To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

## Quick links

[Get started with Agent Skills in the API](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.



[Skill authoring best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.

## Overview



For a detailed look at the architecture and real-world applications of Agent Skills, read the engineering blog post: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

Skills integrate with the Messages API through the [code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md). Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.

### Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they run in the code execution environment.

You can use Skills from two sources:

| Aspect             | Anthropic Skills                           | Custom Skills                                                          |
|--------------------|--------------------------------------------|------------------------------------------------------------------------|
| **Type value**     | `anthropic`                                | `custom`                                                               |
| **Skill IDs**      | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`                            |
| **Version format** | Date-based: `20251013` or `latest`         | Version ID: `skver_01AbCdEfGhIjKlMnOpQrStUv` or `latest`               |
| **Management**     | Pre-built and maintained by Anthropic      | Upload and manage through the [Skills API](../Endpoints/skills-create.md) |
| **Availability**   | Available to all users                     | Private to your workspace                                              |

Both skill sources are returned by the [List Skills endpoint](../Endpoints/skills-list.md) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.

### Prerequisites

To use Skills, you need:

1.  **Claude API key** from the [Claude Console](../Other/usage-limits.md)
2.  **[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)** enabled in your requests

Skills require the code execution tool, so use a model from its [model compatibility list](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#compatibility).

------------------------------------------------------------------------

## Using Skills in Messages

### Container parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 20 Skills for each request.

The structure is identical for both Anthropic and custom Skills. Specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:

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

```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

### Downloading generated files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1.  Skills create files during code execution.
2.  The response includes a `file_id` for each created file, inside code-execution tool result blocks (see [Response format](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#response-format)).
3.  Use the Files API to download the actual file content.
4.  Save locally or process as needed.

To provide input files for Skills to work on, [upload them with the Files API](build-with-claude-files.md#uploading-a-file) and reference them in your request with a [container upload block](build-with-claude-files.md#container-upload-blocks).

**Example: creating and downloading an Excel file**

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

```python
client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {
            "role": "user",
            "content": "Create an Excel file with a simple budget spreadsheet",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)


# Step 2: Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == "bash_code_execution_tool_result":
            content_item = item.content
            if content_item.type == "bash_code_execution_result":
                # each content item is a bash_code_execution_output block carrying a file_id
                for file in content_item.content:
                    file_ids.append(file.file_id)
    return file_ids


# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.files.retrieve_metadata(file_id=file_id)
    file_content = client.files.download(file_id=file_id)

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

**Additional Files API operations:**

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

```python
client = anthropic.Anthropic()
file_id = "file_011CNha8iCJcU1wXNR6q4V8w"
# Get file metadata
file_info = client.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
for file in client.files.list():
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.files.delete(file_id=file_id)
```



For complete details, see [Files API](build-with-claude-files.md).

### Multi-turn conversations

The response's `container` object carries the container's `id` and `expires_at` timestamp (see [Container reuse](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md#container-reuse) for lifetime details). Reuse the same container across multiple messages by specifying the container ID:

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

```python
client = anthropic.Anthropic()

# First request creates container
response1 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a sample sales dataset and analyze it"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Create a sample sales dataset and analyze it"},
    {
        # Carry the assistant's text forward; container.id carries the execution state
        "role": "assistant",
        "content": "\n".join(
            block.text for block in response1.content if block.type == "text"
        ),
    },
    {"role": "user", "content": "What was the total revenue?"},
]

response2 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

### Long-running operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:

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

```python
client = anthropic.Anthropic()

messages = [{"role": "user", "content": "Generate and process a large sample dataset"}]
max_retries = 10

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            }
        ]
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Handle pause_turn for long operations
for _ in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=4096,
        container={
            "id": response.container.id,
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ],
        },
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
```



The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you want to interrupt the conversation and provide additional guidance.

### Using multiple Skills

Combine multiple Skills in a single request to handle complex workflows:

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

```python
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            },
        ]
    },
    messages=[
        {"role": "user", "content": "Analyze sales data and create a presentation"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

------------------------------------------------------------------------

## Managing custom Skills



**Custom Skills are accessible to your entire workspace, not scoped to an end user, conversation, or session.** Any API key with access to a workspace can read, invoke, and delete every custom Skill uploaded to that workspace. Every service account, and every user whose organization role allows API access, can use the Default Workspace in addition to any workspace you add them to, so keep Skills that must stay separate in their own [workspace](../Other/manage-claude-workspaces.md#api-keys-and-resource-scoping) and access them only with keys scoped to that workspace.

If you are building a multi-tenant platform on the Skills API, create a separate [workspace](../Other/manage-claude-workspaces.md) for each tenant. The workspace is the isolation boundary for custom Skills, so a workspace per tenant gives each tenant's Skills hard isolation from every other tenant. Each organization can have up to 100 workspaces by default (see [How workspaces work](../Other/manage-claude-workspaces.md#how-workspaces-work)); if you need more for tenant isolation, contact your account team.

### Creating a Skill

A Skill bundle is a directory containing a `SKILL.md` file at the top level with `name` and `description` YAML frontmatter, plus any supporting scripts or resources. See [Get started with Agent Skills in the API](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md) to author one, and the **Requirements** list following the examples for the full constraints.

Upload your custom Skill to make it available in your workspace. You can upload a zip archive or individual file objects. The Python SDK also provides a `files_from_dir` helper that accepts a directory path, and the CLI's `ant apply` uploads the directory itself.

Files are identified by the filename you attach (the `;filename=` suffix in the cURL example and the filename arguments in the SDK examples). For the walkthrough's skill, create a zip with `zip -r financial_skill.zip financial_skill/` and substitute it for the `example_skill.zip` placeholder in the zip-upload options.

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

```python
ant apply financial_skill
```

financial_skill/SKILL.md





```python
---
name: financial-skill
description: Docs example skill.
---
```

financial_skill/analyze.py





```python
print("financial analysis helper")
```

**Requirements:**

- Must include a `SKILL.md` file at the upload root (or at the top of a single enclosing folder)
- `display_name` is optional: when omitted, it derives from the `SKILL.md` `name`; an explicit value may be up to 255 characters and does not need to be unique within the workspace
- Total upload size must be under 30 MB (uncompressed)
- YAML frontmatter requirements:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](../Endpoints/skills-create.md).

### Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:

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

```python
client = anthropic.Anthropic()

# List all Skills
for skill in client.skills.list():
    print(f"{skill.id}: {skill.display_name} (source: {skill.source.type})")

# List only custom Skills
custom_skills = client.skills.list(source="custom")
```

See the [List Skills API reference](../Endpoints/skills-list.md) for pagination and filtering options.

### Retrieving a Skill

Get details about a specific Skill:

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

```python
client = anthropic.Anthropic()

skill = client.skills.retrieve(skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv")

print(f"Skill: {skill.display_name}")
print(f"Latest version: {skill.latest_version_id}")
print(f"Created: {skill.created_at}")
```

### Deleting a Skill

Deleting a Skill also removes all of its versions.

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

```python
client = anthropic.Anthropic()

client.skills.delete(skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv")
```

### Versioning

Skills support versioning to manage updates safely:

**Anthropic Skills:**

- Versions use date format: `20251013`
- New versions released as updates are made
- Specify exact versions for stability

**Custom Skills:**

- Auto-generated version IDs: `skver_01AbCdEfGhIjKlMnOpQrStUv`
- Use `"latest"` to always get the most recent version
- Create new versions when updating Skill files

A new version is a complete snapshot, not a delta: upload the Skill's full file set each time. Files you omit are not carried over, and the `name` in the new version's `SKILL.md` must match the Skill's existing name. The following examples re-upload the complete `financial_skill/` bundle from [Creating a Skill](#creating-a-skill).

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

```python
from anthropic.lib import files_from_dir

client = anthropic.Anthropic()

# Create a new version

new_version = client.skills.versions.create(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    files=files_from_dir("financial_skill"),
)

# Use specific version
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": new_version.id,
            }
        ]
    },
    messages=[{"role": "user", "content": "Use updated Skill"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Use latest version
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
            }
        ]
    },
    messages=[{"role": "user", "content": "Use latest Skill version"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

See the [Create Skill Version API reference](../Endpoints/skills-versions-create.md) for complete details.

------------------------------------------------------------------------

## How Skills are loaded

When you specify Skills in a container:

1.  **Metadata discovery:** Claude sees metadata for each Skill (name, description) in the system prompt.
2.  **File loading:** Skill files are copied into the container at `/skills/{skill-name}/`. The directory is the Skill's name (`pptx` for an Anthropic Skill, the `SKILL.md` `name` for a custom Skill), not its `skill_01...` ID.
3.  **Automatic use:** Claude automatically loads and uses Skills when relevant to your request.
4.  **Composition:** Multiple Skills compose together for complex workflows.

Claude loads full Skill instructions only when needed.

------------------------------------------------------------------------

## Use cases

Skills fit both organizational and personal work. Organizations use them to apply brand formatting to documents, structure notes and reports around company templates, and run company-specific analytical procedures. Individuals use them for custom document templates, specialized data pipelines, and code generation or deployment conventions.

### Example: financial modeling

Combine Excel and custom DCF analysis Skills. First, create the custom DCF analysis Skill:

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

```python
ant apply dcf_skill
```

Then use it with the Excel Skill to create a financial model. Pass the ID of the Skill you created as the custom Skill's `skill_id`:

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

```python
client = anthropic.Anthropic()

# Custom DCF analysis Skill (ID obtained from Skills API create response)
dcf_skill_id = "skill_01AbCdEfGhIjKlMnOpQrStUv"

# Use with Excel to create financial model
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill_id, "version": "latest"},
        ]
    },
    messages=[
        {
            "role": "user",
            "content": "Build a DCF valuation model for a SaaS company",
        }
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
print(response)
```

------------------------------------------------------------------------

## Limits and constraints

### Request limits

- **Maximum Skills per request:** 20
- **Maximum Skill upload size:** 30 MB (all files combined, uncompressed)
- **YAML frontmatter requirements:**
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

### Environment constraints

Skills run in the code execution container with these limitations:

- **No network access:** Cannot make external API calls
- **No runtime package installation:** Only pre-installed packages available
- **Isolated environment:** A fresh container is created unless you specify an existing container ID

See [Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md) for available packages.

------------------------------------------------------------------------

## Best practices

### When to use multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**

- Data analysis (Excel) + presentation creation (PowerPoint)
- Report generation (Word) + export to PDF
- Custom domain logic + document generation

**Avoid:**

- Including unused Skills (impacts performance)

### Version management strategy

The SDK tabs in this section show the `container` value to include in a Messages request. The cURL and CLI tabs show the full request.

**For production:** pin a specific version, so Skill updates never change your deployed behavior. If you omit `version` or set it to `"latest"`, requests use the newest version of the Skill, so a version uploaded by anyone in the [workspace](#workspace-scoped-access) immediately changes what your production agents run. The version ID comes from the create-version response in [Versioning](#versioning) or from the [List Skill Versions API](../Endpoints/skills-versions-list.md). The ID is always a string, so quote it in JSON or YAML even when it looks numeric.

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

```python
# Pin to specific versions for stability
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "skver_01AbCdEfGhIjKlMnOpQrStUv",
        }
    ]
}
```

**For development:** use `latest` to pick up the newest version automatically as you iterate.

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

```python
# Use latest for active development
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",
        }
    ]
}
```

### Prompt caching considerations

If you use [Prompt caching](build-with-claude-prompt-caching.md), changing the Skills list in your container breaks the cache. Skills render into the system prompt in a fixed order, so the same list produces the same cacheable prefix:

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

```python
client = anthropic.Anthropic()

# Skills render into the system prompt in a fixed, cache-friendly order
response1 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Changing the Skills list ([xlsx] vs [xlsx, pptx]) changes the prefix: a cache miss, while an identical list is a cache hit
response2 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # prefix change: cache miss
        ]
    },
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

For best caching performance, keep your Skills list, including its order, consistent across requests. Pinning custom Skill versions also helps: with `"latest"`, publishing a new version can invalidate the cached prefix if it changes the Skill's description.

### Error handling

Handle Skill-related errors gracefully:

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

```python
client = anthropic.Anthropic()

try:
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=4096,
        container={
            "skills": [
                {
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
                }
            ]
        },
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise
```

------------------------------------------------------------------------

## Migrate from `skills-2025-10-02`

The Skills API is out of beta and needs no beta header. Migrating off `skills-2025-10-02` is optional: requests that still send it keep working and keep returning the beta response shapes, so an existing integration keeps working until you change it. Removing the header switches those requests to the shapes documented on this page:

|                                 | With `skills-2025-10-02`                                                        | Without the header                                                                                                                                |
|---------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Skill label                     | `display_title` (up to 64 characters, unique per workspace)                     | `display_name` (up to 255 characters, not unique); derived from the `SKILL.md` `name` when omitted                                                |
| Newest version pointer          | `latest_version`, an epoch-microsecond string such as `"1759178010641129"`      | `latest_version_id`, a version ID such as `"skver_01AbCdEfGhIjKlMnOpQrStUv"`; `GET /v1/skills/{skill_id}/versions/latest` resolves it in one call |
| Version identifier in URLs      | Epoch-microsecond string                                                        | Version ID (`skver_...`). IDs captured under the beta with the `skill_version_` prefix are accepted as input.                                     |
| Version object                  | Includes `directory` (always equal to the Skill `name`)                         | No `directory` field                                                                                                                              |
| `source`                        | A string, `"custom"` or `"anthropic"`                                           | An object, for example `{"type": "custom"}`; the example catalog value is `"anthropic_example"`                                                   |
| List responses                  | `{ data, has_more, next_page }`                                                 | `{ data, next_page }`; `limit` from 1 to 1,000 (default 20)                                                                                       |
| Versions list order             | Oldest first                                                                    | Newest first, default `limit` 20. Page cursors from one shape are not valid on the other.                                                         |
| Deleting a Skill                | Returns a 400 error while any version exists                                    | Deletes the Skill and all of its versions                                                                                                         |
| Deleting a Skill's only version | Allowed, leaving a Skill with no versions                                       | Returns a 400 error; upload a replacement version first, or delete the Skill                                                                      |
| Upload layout                   | Files must sit inside a top-level directory whose name matches the Skill `name` | `SKILL.md` may sit at the root of the upload; stored paths are the same either way                                                                |
| Response types                  | `CreateSkillResponse`, `GetSkillResponse`, and one type per operation           | `Skill`, `SkillVersion`, `DeletedSkill`, `DeletedSkillVersion`                                                                                    |

To migrate:

1.  **Remove the beta header.** Drop `anthropic-beta: skills-2025-10-02` from your requests. In the SDKs, call `client.skills` instead of `client.beta.skills`; keeping `client.beta.skills` works only on the [SDK releases that no longer send the header](#sdk-beta-namespace). Earlier releases send it from `client.beta.skills` even with no `betas` argument.
2.  **Rename fields** in your code: `display_title` to `display_name`, `latest_version` to `latest_version_id`, and read `source.type` instead of comparing `source` to a string.
3.  **Use version IDs.** Wherever you stored an epoch-microsecond version, store the version's `id` instead, or use `latest`. Skill references in Messages requests accept a version ID, `latest`, or (for Anthropic Skills) the catalog version.
4.  **Review delete calls.** `DELETE /v1/skills/{skill_id}` now removes every version with the Skill. If you relied on the beta's refusal as a safeguard, add your own check.



After migrating, `client.skills.delete(skill_id)` and `client.beta.skills.delete(skill_id)` delete the Skill together with all of its versions in one call.

A Skill whose versions were all deleted under the beta has no current version to return: `GET /v1/skills/{skill_id}` returns a 400 error and the Skill is omitted from list responses until you upload a version to it. You can still delete it.

### SDK beta namespace

Starting with Python SDK 1.2.0, TypeScript SDK 0.122.0, Go SDK 1.68.0, Java SDK 2.59.0, Ruby SDK 1.67.0, and C# SDK 12.44.0, `client.beta.skills` no longer sends `skills-2025-10-02` and returns the same shapes as `client.skills`, with `Beta`-prefixed type names (`BetaSkill`, `BetaSkillVersion`, `BetaDeletedSkill`, `BetaDeletedSkillVersion`). It accepts a `betas` argument for Skills features that are still in beta. In the beta Messages types, the container Skill reference type is renamed from `BetaSkill` to `BetaContainerSkill` (same fields: `type`, `skill_id`, `version`); `BetaSkill` now names the Skill resource, matching `Skill` and `ContainerSkill` in the non-beta types. Earlier SDK releases are typed to the beta shapes; if you depend on those types, stay on an earlier release until you migrate.

## Data retention

Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

## Audit logging

If your organization has the [Compliance API](../Other/manage-claude-compliance-api.md) enabled, its [Activity Feed](../Other/manage-claude-compliance-activity-feed.md) records the creation and deletion of Skills and Skill versions made with a Claude API key or from the Claude Console. Operations that occur while the Compliance API is off are not recorded and cannot be recovered later, so [set up the Compliance API](../Other/manage-claude-compliance-api-access.md) before you rely on this audit trail.

## Next steps



[API reference](../Endpoints/skills-create.md)

Complete API reference with all endpoints



[Skill authoring best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.



[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.
