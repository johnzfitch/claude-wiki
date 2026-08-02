---
title: "Using Agent Skills with the API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/skills-guide"
category: "04-API-Reference/Guides"
fetched_at: "2026-08-02T05:40:33Z"
tags: ["agents", "api", "skills"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

Thinking

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Compaction](/docs/en/build-with-claude/compaction)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

Images and vision

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

MCP tunnels

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[](/login)




Messages

Skills in the API

Messages/Skills

# Using Agent Skills with the API




Learn how to use Agent Skills to extend Claude's capabilities through the API.




Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.



For complete API reference including request/response schemas and all parameters, see:

- [Skill Management API Reference](/docs/en/api/beta/skills/list) - CRUD operations for Skills
- [Skill Versions API Reference](/docs/en/api/beta/skills/versions/list) - Version management



For how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).




Quick links


Get started with Agent Skills

Create your first Skill


Create custom Skills

Best practices for authoring Skills




Overview



For a detailed look at the architecture and real-world applications of Agent Skills, read the engineering blog post: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

Skills integrate with the Messages API through the [code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool). Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.




Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.

**You can use Skills from two sources:**

| Aspect             | Anthropic Skills                           | Custom Skills                                                               |
|--------------------|--------------------------------------------|-----------------------------------------------------------------------------|
| **Type value**     | `anthropic`                                | `custom`                                                                    |
| **Skill IDs**      | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`                                 |
| **Version format** | Date-based: `20251013` or `latest`         | Epoch timestamp: `1759178010641129` or `latest`                             |
| **Management**     | Pre-built and maintained by Anthropic      | Upload and manage through the [Skills API](/docs/en/api/beta/skills/create) |
| **Availability**   | Available to all users                     | Private to your workspace                                                   |

Both skill sources are returned by the [List Skills endpoint](/docs/en/api/beta/skills/list) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.




Prerequisites

To use Skills, you need:

1.  **Claude API key** from the [Claude Console](/settings/keys)
2.  **Beta headers:**
    - `code-execution-2025-08-25` - Enables code execution (required for Skills)
    - `skills-2025-10-02` - Enables Skills API
    - `files-api-2025-04-14` - For uploading/downloading files to/from container
3.  **[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)** enabled in your requests

------------------------------------------------------------------------




Using Skills in Messages




Container parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills for each request.

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

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    },
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```




Downloading generated files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1.  Skills create files during code execution.
2.  Response includes `file_id` for each created file.
3.  Use the Files API to download the actual file content.
4.  Save locally or process as needed.

**Example: Creating and downloading an Excel file**

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
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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
    file_metadata = client.beta.files.retrieve_metadata(file_id=file_id)
    file_content = client.beta.files.download(file_id=file_id)

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
file_info = client.beta.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
for file in client.beta.files.list():
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id=file_id)
```



For complete details on the Files API, see the [Files API](/docs/en/api/beta/files/download) documentation.




Multi-turn conversations

Reuse the same container across multiple messages by specifying the container ID:

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
response1 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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

response2 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```




Long-running operations

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

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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
    response = client.beta.messages.create(
        model="claude-opus-5",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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



The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you want to interrupt the conversation and provide additional guidance.




Using multiple Skills

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

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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




Managing custom Skills




Creating a Skill

A Skill bundle is a directory containing a `SKILL.md` file at the top level with `name` and `description` YAML frontmatter, plus any supporting scripts or resources. See [Get started with Agent Skills in the API](/docs/en/agents-and-tools/agent-skills/quickstart) to author one, and the **Requirements** list following the examples for the full constraints.

Upload your custom Skill to make it available in your workspace. You can upload a zip archive or individual file objects; the Python SDK additionally provides a `files_from_dir` helper that accepts a directory path.

Files are identified by the filename you attach. Per-file uploads must keep a common top-level directory in their paths (the `;filename=` suffix in the cURL example and the filename arguments in the SDK examples), and a zip archive must contain the skill directory as its single top-level entry.

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
ant beta:skills create \
  --file example_skill.zip \
  --beta skills-2025-10-02

# Per-file upload requires path-qualified filenames, which the CLI
# can't currently set. Upload a zip archive instead.
```

**Requirements:**

- Must include a SKILL.md file at the top level
- All files must specify a common root directory in their paths
- The top-level directory name must match the `name` in SKILL.md frontmatter (case and underscore insensitive: `Financial_Skill` matches `financial-skill`)
- `display_title` is optional: when omitted, it derives from the SKILL.md `name`; an explicit value must be unique among the custom skills in your workspace
- Total upload size must be under 30 MB
- YAML frontmatter requirements:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](/docs/en/api/beta/skills/create).




Listing Skills

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
# List all Skills
ant beta:skills list

# List only custom Skills
ant beta:skills list --source custom
```

See the [List Skills API reference](/docs/en/api/beta/skills/list) for pagination and filtering options.




Retrieving a Skill

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
ant beta:skills retrieve \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv
```




Deleting a Skill

To delete a Skill, you must first delete all its versions:

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
# Step 1: List the versions, then delete each one
ant beta:skills:versions list \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --transform version --raw-output

# Repeat for each version id the list returned
ant beta:skills:versions delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --version 1759178010641129 >/dev/null

# Step 2: Delete the Skill
ant beta:skills delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv >/dev/null
```

Attempting to delete a Skill with existing versions returns a 400 error.




Versioning

Skills support versioning to manage updates safely:

**Anthropic Skills:**

- Versions use date format: `20251013`
- New versions released as updates are made
- Specify exact versions for stability

**Custom Skills:**

- Auto-generated epoch timestamps: `1759178010641129`
- Use `"latest"` to always get the most recent version
- Create new versions when updating Skill files

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
# Create a new version
VERSION_NUMBER=$(ant beta:skills:versions create \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --file updated_skill.zip \
  --transform version --raw-output)

# Use specific version
ant beta:messages create \
  --beta code-execution-2025-08-25,skills-2025-10-02 <<YAML
model: claude-opus-5
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: $VERSION_NUMBER
messages:
  - role: user
    content: Use updated Skill
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Use latest version
ant beta:messages create \
  --beta code-execution-2025-08-25,skills-2025-10-02 <<'YAML'
model: claude-opus-5
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Use latest Skill version
tools:
  - type: code_execution_20250825
    name: code_execution
YAML
```

See the [Create Skill Version API reference](/docs/en/api/beta/skills/versions/create) for complete details.

------------------------------------------------------------------------




How Skills are loaded

When you specify Skills in a container:

1.  **Metadata discovery:** Claude sees metadata for each Skill (name, description) in the system prompt.
2.  **File loading:** Skill files are copied into the container at `/skills/{directory}/`.
3.  **Automatic use:** Claude automatically loads and uses Skills when relevant to your request.
4.  **Composition:** Multiple Skills compose together for complex workflows.

The progressive disclosure architecture ensures efficient context usage: Claude only loads full Skill instructions when needed.

------------------------------------------------------------------------




Use cases




Organizational Skills

**Brand & Communications**

- Apply company-specific formatting (colors, fonts, layouts) to documents
- Generate communications following organizational templates
- Ensure consistent brand guidelines across all outputs

**Project Management**

- Structure notes with company-specific formats (OKRs, decision logs)
- Generate tasks following team conventions
- Create standardized meeting recaps and status updates

**Business Operations**

- Create company-standard reports, proposals, and analyses
- Execute company-specific analytical procedures
- Generate financial models following organizational templates




Personal Skills

**Content Creation**

- Custom document templates
- Specialized formatting and styling
- Domain-specific content generation

**Data Analysis**

- Custom data processing pipelines
- Specialized visualization templates
- Industry-specific analytical methods

**Development & Automation**

- Code generation templates
- Testing frameworks
- Deployment workflows




Example: financial modeling

Combine Excel and custom DCF analysis Skills:

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

# Create custom DCF analysis Skill

dcf_skill = client.beta.skills.create(
    files=files_from_dir("/path/to/dcf_skill"),
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"},
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




Limits and constraints




Request limits

- **Maximum Skills per request:** 8
- **Maximum Skill upload size:** 30 MB (all files combined)
- **YAML frontmatter requirements:**
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags




Environment constraints

Skills run in the code execution container with these limitations:

- **No network access:** Cannot make external API calls
- **No runtime package installation:** Only pre-installed packages available
- **Isolated environment:** Containers are isolated; a fresh container is created unless you specify an existing container ID

See [Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool) for available packages.

------------------------------------------------------------------------




Best practices




When to use multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**

- Data analysis (Excel) + presentation creation (PowerPoint)
- Report generation (Word) + export to PDF
- Custom domain logic + document generation

**Avoid:**

- Including unused Skills (impacts performance)




Version management strategy

**For production:**

```python
# Pin to specific versions for stability
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "1759178010641129",  # Specific version
        }
    ]
}
```



**For development:**

```python
# Use latest for active development
container = {
    "skills": [
        {
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",  # Always get newest
        }
    ]
}
```






Prompt caching considerations

When using prompt caching, note that changing the Skills list in your container breaks the cache:

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

# First request creates cache
response1 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
    ],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    },
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
    ],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # Cache miss
        ]
    },
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
```

For best caching performance, keep your Skills list consistent across requests.




Error handling

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
    response = client.beta.messages.create(
        model="claude-opus-5",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
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




Data retention

Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).




Next steps




API reference

Complete API reference with all endpoints




Skill authoring best practices

Learn how to write effective Skills that Claude can discover and use successfully


Code execution tool

Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions
