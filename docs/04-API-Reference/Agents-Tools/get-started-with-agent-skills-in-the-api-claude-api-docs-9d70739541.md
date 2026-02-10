---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:29Z"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart"
title: "Get started with Agent Skills in the API - Claude API Docs"
---

Agent Skills

# Get started with Agent Skills in the API

Copy page

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.

Copy page

This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a simple request, and access the generated file.

## 

Prerequisites

- [Anthropic API key](/settings/keys)
- Python 3.7+ or curl installed
- Basic familiarity with making API requests

## 

What are Agent Skills?

Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks like creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:

- **PowerPoint (pptx)**: Create and edit presentations
- **Excel (xlsx)**: Create and analyze spreadsheets
- **Word (docx)**: Create and edit documents
- **PDF (pdf)**: Generate PDF documents

**Want to create custom Skills?** See the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) for examples of building your own Skills with domain-specific expertise.

## 

Step 1: List available Skills

First, let's see what Skills are available. We'll use the Skills API to list all Anthropic-managed Skills:

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

# List Anthropic-managed Skills
skills = client.beta.skills.list(
    source="anthropic",
    betas=["skills-2025-10-02"]
)

for skill in skills.data:
    print(f"{skill.id}: {skill.display_title}")
```

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.

This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of **progressive disclosure**, where Claude discovers Skills without loading their full instructions yet.

## 

Step 2: Create a presentation

Now we'll use the PowerPoint Skill to create a presentation about renewable energy. We specify Skills using the `container` parameter in the Messages API:

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

# Create a message with the PowerPoint Skill
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
        "content": "Create a presentation about renewable energy with 5 slides"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)

print(response.content)
```

Let's break down what each part does:

- **`container.skills`**: Specifies which Skills Claude can use
- **`type: "anthropic"`**: Indicates this is an Anthropic-managed Skill
- **`skill_id: "pptx"`**: The PowerPoint Skill identifier
- **`version: "latest"`**: The Skill version set to the most recently published
- **`tools`**: Enables code execution (required for Skills)
- **Beta headers**: `code-execution-2025-08-25` and `skills-2025-10-02`

When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.

## 

Step 3: Download the created file

The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:

Python

``` shiki
# Extract file ID from response
file_id = None
for block in response.content:
    if block.type == 'tool_use' and block.name == 'code_execution':
        # File ID is in the tool result
        for result_block in block.content:
            if hasattr(result_block, 'file_id'):
                file_id = result_block.file_id
                break

if file_id:
    # Download the file
    file_content = client.beta.files.download(
        file_id=file_id,
        betas=["files-api-2025-04-14"]
    )

    # Save to disk
    with open("renewable_energy.pptx", "wb") as f:
        file_content.write_to_file(f.name)

    print(f"Presentation saved to renewable_energy.pptx")
```

For complete details on working with generated files, see the [code execution tool documentation](/docs/en/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files).

## 

Try more examples

Now that you've created your first document with Skills, try these variations:

### 

Create a spreadsheet

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
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Create a quarterly sales tracking spreadsheet with sample data"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

### 

Create a Word document

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
                "skill_id": "docx",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Write a 2-page report on the benefits of renewable energy"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

### 

Generate a PDF

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
                "skill_id": "pdf",
                "version": "latest"
            }
        ]
    },
    messages=[{
        "role": "user",
        "content": "Generate a PDF invoice template"
    }],
    tools=[{
        "type": "code_execution_20250825",
        "name": "code_execution"
    }]
)
```

## 

Next steps

Now that you've used pre-built Agent Skills, you can:

[](/docs/en/build-with-claude/skills-guide)

API Guide

Use Skills with the Claude API

[](/docs/en/api/skills/create-skill)

Create Custom Skills

Upload your own Skills for specialized tasks

[](/docs/en/agents-and-tools/agent-skills/best-practices)

Authoring Guide

Learn best practices for writing effective Skills

[](https://code.claude.com/docs/en/skills)

Use Skills in Claude Code

Learn about Skills in Claude Code

[](/docs/en/agent-sdk/skills)

Use Skills in the Agent SDK

Use Skills programmatically in TypeScript and Python

[](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)

Agent Skills Cookbook

Explore example Skills and implementation patterns

Was this page helpful?

- 

- [Prerequisites](#prerequisites)

- [What are Agent Skills?](#what-are-agent-skills)

- [Step 1: List available Skills](#step-1-list-available-skills)

- [Step 2: Create a presentation](#step-2-create-a-presentation)

- [Step 3: Download the created file](#step-3-download-the-created-file)

- [Try more examples](#try-more-examples)

- [Create a spreadsheet](#create-a-spreadsheet)

- [Create a Word document](#create-a-word-document)

- [Generate a PDF](#generate-a-pdf)

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
