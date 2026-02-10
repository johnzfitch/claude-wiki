---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:31Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/skills-guide"
title: "Using Agent Skills with the API - Claude API Docs"
---

Agent Skills

# Using Agent Skills with the API

Copy page

Learn how to use Agent Skills to extend Claude's capabilities through the API.

Copy page

Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.

For complete API reference including request/response schemas and all parameters, see:

- [Skill Management API Reference](/docs/en/api/skills/list-skills) - CRUD operations for Skills
- [Skill Versions API Reference](/docs/en/api/skills/list-skill-versions) - Version management

## 

Quick Links

[](/docs/en/agents-and-tools/agent-skills/quickstart)

Get started with Agent Skills

Create your first Skill

[](/docs/en/agents-and-tools/agent-skills/best-practices)

Create Custom Skills

Best practices for authoring Skills

## 

Overview

For a deep dive into the architecture and real-world applications of Agent Skills, read our engineering blog: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

Skills integrate with the Messages API through the code execution tool. Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical—both require code execution and use the same `container` structure.

### 

Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.

**You can use Skills from two sources:**

| Aspect | Anthropic Skills | Custom Skills |
|----|----|----|
| **Type value** | `anthropic` | `custom` |
| **Skill IDs** | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv` |
| **Version format** | Date-based: `20251013` or `latest` | Epoch timestamp: `1759178010641129` or `latest` |
| **Management** | Pre-built and maintained by Anthropic | Upload and manage via [Skills API](/docs/en/api/skills/create-skill) |
| **Availability** | Available to all users | Private to your workspace |

Both skill sources are returned by the [List Skills endpoint](/docs/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical—the only difference is where the Skills come from and how they're managed.

### 

Prerequisites

To use Skills, you need:

1.  **Anthropic API key** from the [Console](/settings/keys)
2.  **Beta headers**:
    - `code-execution-2025-08-25` - Enables code execution (required for Skills)
    - `skills-2025-10-02` - Enables Skills API
    - `files-api-2025-04-14` - For uploading/downloading files to/from container
3.  **Code execution tool** enabled in your requests

------------------------------------------------------------------------

## 

Using Skills in Messages

### 

Container Parameter

Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.

The structure is identical for both Anthropic and custom Skills—specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a presentation about renewable energy"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

### 

Downloading Generated Files

When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.

**How it works:**

1.  Skills create files during code execution
2.  Response includes `file_id` for each created file
3.  Use Files API to download the actual file content
4.  Save locally or process as needed

**Example: Creating and downloading an Excel file**

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create an Excel file with a simple budget spreadsheet"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# Step 2: Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == 'bash_code_execution_tool_result':
            content_item = item.content
            if content_item.type == 'bash_code_execution_result':
                for file in content_item.content:
                    if hasattr(file, 'file_id'):
                        file_ids.append(file.file_id)
    return file_ids

# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(
        file_id=file_id,
        betas=["files-api-2025-04-14"]
    )
    file_content = client.beta.files.download(
        file_id=file_id,
        betas=["files-api-2025-04-14"]
    )

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")
```

**Additional Files API operations:**

Python

``` shiki
# Get file metadata
file_info = client.beta.files.retrieve_metadata(
    file_id=file_id,
    betas=["files-api-2025-04-14"]
)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
files = client.beta.files.list(betas=["files-api-2025-04-14"])
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(
    file_id=file_id,
    betas=["files-api-2025-04-14"]
)
```

For complete details on the Files API, see the [Files API documentation](/docs/en/api/files-content).

### 

Multi-Turn Conversations

Reuse the same container across multiple messages by specifying the container ID:

Python

``` shiki
# First request creates container
response1 = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    messages=[{"role": "user", "content": "Analyze this sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Analyze this sales data"},
    {"role": "assistant", "content": response1.content},
    {"role": "user", "content": "What was the total revenue?"}
]

response2 = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

### 

Long-Running Operations

Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:

Python

``` shiki
messages = [{"role": "user", "content": "Process this large dataset"}]
max_retries = 10

response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
        ]
    },
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# Handle pause_turn for long operations
for i in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.beta.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "id": response.container.id,
            "skills": [
                {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
            ]
        },
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
    )
```

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.

### 

Using Multiple Skills

Combine multiple Skills in a single request to handle complex workflows:

Python

``` shiki
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {
                "type": "anthropic",
                "skill_id": "xlsx",
                "version": "latest"
            },
            {
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest"
            },
            {
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Analyze sales data and create a presentation"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

------------------------------------------------------------------------

## 

Managing Custom Skills

### 

Creating a Skill

Upload your custom Skill to make it available in your workspace. You can upload using either a directory path or individual file objects.

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

# Option 1: Using files_from_dir helper (Python only, recommended)
from anthropic.lib import files_from_dir

skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=files_from_dir("/path/to/financial_analysis_skill"),
    betas=["skills-2025-10-02"]
)

# Option 2: Using a zip file
skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=[("skill.zip", open("financial_analysis_skill.zip", "rb"))],
    betas=["skills-2025-10-02"]
)

# Option 3: Using file tuples (filename, file_content, mime_type)
skill = client.beta.skills.create(
    display_title="Financial Analysis",
    files=[
        ("financial_skill/SKILL.md", open("financial_skill/SKILL.md", "rb"), "text/markdown"),
        ("financial_skill/analyze.py", open("financial_skill/analyze.py", "rb"), "text/x-python"),
    ],
    betas=["skills-2025-10-02"]
)

print(f"Created skill: {skill.id}")
print(f"Latest version: {skill.latest_version}")
```

**Requirements:**

- Must include a SKILL.md file at the top level
- All files must specify a common root directory in their paths
- Total upload size must be under 8MB
- YAML frontmatter requirements:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
  - `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](/docs/en/api/skills/create-skill).

### 

Listing Skills

Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:

Python

``` shiki
# List all Skills
skills = client.beta.skills.list(
    betas=["skills-2025-10-02"]
)

for skill in skills.data:
    print(f"{skill.id}: {skill.display_title} (source: {skill.source})")

# List only custom Skills
custom_skills = client.beta.skills.list(
    source="custom",
    betas=["skills-2025-10-02"]
)
```

See the [List Skills API reference](/docs/en/api/skills/list-skills) for pagination and filtering options.

### 

Retrieving a Skill

Get details about a specific Skill:

Python

``` shiki
skill = client.beta.skills.retrieve(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    betas=["skills-2025-10-02"]
)

print(f"Skill: {skill.display_title}")
print(f"Latest version: {skill.latest_version}")
print(f"Created: {skill.created_at}")
```

### 

Deleting a Skill

To delete a Skill, you must first delete all its versions:

Python

``` shiki
# Step 1: Delete all versions
versions = client.beta.skills.versions.list(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    betas=["skills-2025-10-02"]
)

for version in versions.data:
    client.beta.skills.versions.delete(
        skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
        version=version.version,
        betas=["skills-2025-10-02"]
    )

# Step 2: Delete the Skill
client.beta.skills.delete(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    betas=["skills-2025-10-02"]
)
```

Attempting to delete a Skill with existing versions will return a 400 error.

### 

Versioning

Skills support versioning to manage updates safely:

**Anthropic-Managed Skills**:

- Versions use date format: `20251013`
- New versions released as updates are made
- Specify exact versions for stability

**Custom Skills**:

- Auto-generated epoch timestamps: `1759178010641129`
- Use `"latest"` to always get the most recent version
- Create new versions when updating Skill files

Python

``` shiki
# Create a new version
from anthropic.lib import files_from_dir

new_version = client.beta.skills.versions.create(
    skill_id="skill_01AbCdEfGhIjKlMnOpQrStUv",
    files=files_from_dir("/path/to/updated_skill"),
    betas=["skills-2025-10-02"]
)

# Use specific version
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": new_version.version
        }]
    },
    messages=[{"role": "user", "content": "Use updated Skill"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# Use latest version
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest"
        }]
    },
    messages=[{"role": "user", "content": "Use latest Skill version"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

See the [Create Skill Version API reference](/docs/en/api/skills/create-skill-version) for complete details.

------------------------------------------------------------------------

## 

How Skills Are Loaded

When you specify Skills in a container:

1.  **Metadata Discovery**: Claude sees metadata for each Skill (name, description) in the system prompt
2.  **File Loading**: Skill files are copied into the container at `/skills/{directory}/`
3.  **Automatic Use**: Claude automatically loads and uses Skills when relevant to your request
4.  **Composition**: Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage—Claude only loads full Skill instructions when needed.

------------------------------------------------------------------------

## 

Use Cases

### 

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

### 

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

### 

Example: Financial Modeling

Combine Excel and custom DCF analysis Skills:

Python

``` shiki
# Create custom DCF analysis Skill
from anthropic.lib import files_from_dir

dcf_skill = client.beta.skills.create(
    display_title="DCF Analysis",
    files=files_from_dir("/path/to/dcf_skill"),
    betas=["skills-2025-10-02"]
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"}
        ]
    },
    messages=[{
        "role": "user",
        "content": "Build a DCF valuation model for a SaaS company with the attached financials"
    }],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

------------------------------------------------------------------------

## 

Limits and Constraints

### 

Request Limits

- **Maximum Skills per request**: 8
- **Maximum Skill upload size**: 8MB (all files combined)
- **YAML frontmatter requirements**:
  - `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words
  - `description`: Maximum 1024 characters, non-empty, no XML tags

### 

Environment Constraints

Skills run in the code execution container with these limitations:

- **No network access** - Cannot make external API calls
- **No runtime package installation** - Only pre-installed packages available
- **Isolated environment** - Each request gets a fresh container

See the [code execution tool documentation](/docs/en/agents-and-tools/tool-use/code-execution-tool) for available packages.

------------------------------------------------------------------------

## 

Best Practices

### 

When to Use Multiple Skills

Combine Skills when tasks involve multiple document types or domains:

**Good use cases:**

- Data analysis (Excel) + presentation creation (PowerPoint)
- Report generation (Word) + export to PDF
- Custom domain logic + document generation

**Avoid:**

- Including unused Skills (impacts performance)

### 

Version Management Strategy

**For production:**

``` shiki
# Pin to specific versions for stability
container={
    "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "1759178010641129"  # Specific version
    }]
}
```

**For development:**

``` shiki
# Use latest for active development
container={
    "skills": [{
        "type": "custom",
        "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
        "version": "latest"  # Always get newest
    }]
}
```

### 

Prompt Caching Considerations

When using prompt caching, note that changing the Skills list in your container will break the cache:

Python

``` shiki
# First request creates cache
response1 = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02", "prompt-caching-2024-07-31"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}  # Cache miss
        ]
    },
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
)
```

For best caching performance, keep your Skills list consistent across requests.

### 

Error Handling

Handle Skill-related errors gracefully:

Python

``` shiki
try:
    response = client.beta.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "skills": [
                {"type": "custom", "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv", "version": "latest"}
            ]
        },
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}]
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise
```

------------------------------------------------------------------------

## 

Next Steps

[](/docs/en/api/skills/create-skill)

API Reference

Complete API reference with all endpoints

[](/docs/en/agents-and-tools/agent-skills/best-practices)

Authoring Guide

Best practices for writing effective Skills

[](/docs/en/agents-and-tools/tool-use/code-execution-tool)

Code Execution Tool

Learn about the code execution environment

Was this page helpful?

- 

- [Quick Links](#quick-links)

- [Overview](#overview)

- [Using Skills](#using-skills)

- [Prerequisites](#prerequisites)

- [Using Skills in Messages](#using-skills-in-messages)

- [Container Parameter](#container-parameter)

- [Downloading Generated Files](#downloading-generated-files)

- [Multi-Turn Conversations](#multi-turn-conversations)

- [Long-Running Operations](#long-running-operations)

- [Using Multiple Skills](#using-multiple-skills)

- [Managing Custom Skills](#managing-custom-skills)

- [Creating a Skill](#creating-a-skill)

- [Listing Skills](#listing-skills)

- [Retrieving a Skill](#retrieving-a-skill)

- [Deleting a Skill](#deleting-a-skill)

- [Versioning](#versioning)

- [How Skills Are Loaded](#how-skills-are-loaded)

- [Use Cases](#use-cases)

- [Organizational Skills](#organizational-skills)

- [Personal Skills](#personal-skills)

- [Example: Financial Modeling](#example-financial-modeling)

- [Limits and Constraints](#limits-and-constraints)

- [Request Limits](#request-limits)

- [Environment Constraints](#environment-constraints)

- [Best Practices](#best-practices)

- [When to Use Multiple Skills](#when-to-use-multiple-skills)

- [Version Management Strategy](#version-management-strategy)

- [Prompt Caching Considerations](#prompt-caching-considerations)

- [Error Handling](#error-handling)

- [Next Steps](#next-steps)

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
