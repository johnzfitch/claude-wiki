---
title: "Agent Skills - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview"
category: "04-API-Reference/Agents-Tools"
fetched_at: "2026-09-26T06:38:20Z"
tags: ["agents", "api", "security", "skills"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Fagent-skills%2Foverview)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](../Guides/build-with-claude-overview.md)[Using the Messages API](../Guides/build-with-claude-working-with-messages.md)[Stop reasons and fallback](../Guides/build-with-claude-handling-stop-reasons.md)[Refusals and fallback](../Guides/build-with-claude-refusals-and-fallback.md)[Fallback credit](../Guides/build-with-claude-fallback-credit.md)

Model capabilities

[Effort](../Guides/build-with-claude-effort.md)[Task budgets (beta)](../Guides/build-with-claude-task-budgets.md)[Fast mode (research preview)](../Guides/build-with-claude-fast-mode.md)[Structured outputs](../Guides/build-with-claude-structured-outputs.md)[Citations](../Guides/build-with-claude-citations.md)[Streaming Messages](../Guides/build-with-claude-streaming.md)[Batch processing](../Guides/build-with-claude-batch-processing.md)[Search results](../Guides/build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](../Guides/build-with-claude-multilingual-support.md)[Embeddings](../Guides/build-with-claude-embeddings.md)

[Thinking](../Guides/build-with-claude-thinking.md)

Tools

[Overview](agents-and-tools-tool-use-overview.md)[How tool use works](agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](agents-and-tools-tool-use-tool-runner.md)[Strict tool use](agents-and-tools-tool-use-strict-tool-use.md)[Server tools](agents-and-tools-tool-use-server-tools.md)[Web search tool](agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](agents-and-tools-tool-use-memory-tool.md)[Bash tool](agents-and-tools-tool-use-bash-tool.md)[Text editor tool](agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](agents-and-tools-tool-use-tool-reference.md)[Manage tool context](agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](../Guides/build-with-claude-context-windows.md)[Context editing](../Guides/build-with-claude-context-editing.md)[Prompt caching](../Guides/build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](../Guides/build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](../Guides/build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](../Guides/build-with-claude-cache-diagnostics.md)[Token counting](../Guides/build-with-claude-token-counting.md)

[Compaction](../Guides/build-with-claude-compaction.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](agents-and-tools-agent-skills-overview.md)[Quickstart](agents-and-tools-agent-skills-quickstart.md)[Best practices](agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](agents-and-tools-agent-skills-enterprise.md)[Skills in the API](../Guides/build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](agents-and-tools-remote-mcp-servers.md)[MCP connector](agents-and-tools-mcp-connector.md)

[MCP tunnels](agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](../Guides/build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](../Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)[Google Cloud](../Guides/build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Skills

# Agent Skills

Copy page



Agent Skills are modular capabilities that extend Claude's functionality. Each Skill packages instructions, metadata, and optional resources (scripts, templates) that Claude uses automatically when relevant.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

## Why use Skills

Skills are reusable, filesystem-based resources that give Claude domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Unlike prompts (conversation-level instructions for one-off tasks), Skills load on demand, so you don't have to repeat the same guidance across conversations.

**Key benefits:**

- **Specialize Claude:** Tailor capabilities for domain-specific tasks
- **Reduce repetition:** Create once, use automatically
- **Compose capabilities:** Combine Skills for complex, multistep tasks



For more on the architecture and real-world applications of Agent Skills, see the engineering blog post [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

## Using Skills

Anthropic provides pre-built Agent Skills for common document tasks (PowerPoint, Excel, Word, PDF), and you can create your own custom Skills. Both work the same way: once a Skill is available in your environment, Claude uses it automatically when relevant to your request.

**Pre-built Agent Skills** are available on claude.ai, the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md). On Microsoft Foundry, Agent Skills require a [Hosted on Anthropic deployment](../Guides/build-with-claude-claude-in-microsoft-foundry.md#additional-features-not-supported-when-hosted-on-azure). See [Available Skills](#available-skills) for the complete list.

**Custom Skills** let you package domain expertise and organizational knowledge. They're available across Claude's products: create them in Claude Code, upload them through the Claude API, or add them in claude.ai settings. On [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) and [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), upload custom Skills through the Skills API.



**Get started:**

- For pre-built Agent Skills: See the [quickstart tutorial](agents-and-tools-agent-skills-quickstart.md) to start using PowerPoint, Excel, Word, and PDF Skills in the API
- For custom Skills: See the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) to learn how to create your own Skills

## How Skills work

Skills use Claude's VM environment to provide capabilities beyond what's possible with prompts alone. Claude operates in a virtual machine with filesystem access, allowing Skills to exist as directories containing instructions, executable code, and reference materials, organized like an onboarding guide you'd create for a new team member.

This filesystem-based architecture enables **progressive disclosure:** Claude loads information in stages as needed, rather than consuming context upfront.

Skills can contain three types of content, each loaded at a different time:

### Level 1: Metadata (always loaded)

The Skill's YAML frontmatter provides discovery information:

```python
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```



Claude loads this metadata at startup and includes it in the system prompt. The `description` is what Claude matches your request against when determining whether to trigger the Skill, so it must say both what the Skill does and when to use it. This lightweight approach means you can install many Skills without context penalty: until a Skill is triggered, only its name and description occupy context.

### Level 2: Instructions (loaded when triggered)

The main body of SKILL.md contains procedural knowledge: workflows, best practices, and guidance:

```` shiki
# PDF Processing

## Quick start

Use pdfplumber to extract text from PDFs:

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For advanced form filling, see [FORMS.md](FORMS.md).
````



When you request something that matches a Skill's description, Claude reads SKILL.md from the filesystem using bash. Only then does this content enter the context window.

### Level 3: Resources and code (loaded as needed)

Skills can bundle additional materials:

- `pdf-processing/`
  - `SKILL.md` (main instructions)
  - `FORMS.md` (form-filling guide)
  - `REFERENCE.md` (detailed API reference)
  - `scripts/`
    - `fill_form.py` (utility script)

**Instructions:** Additional markdown files (FORMS.md, REFERENCE.md) containing specialized guidance and workflows

**Code:** Executable scripts (fill_form.py, validate.py) that Claude runs using bash, providing deterministic operations without loading their code into context

**Resources:** Reference materials such as database schemas, API documentation, templates, or examples

Claude accesses these files only when referenced. The filesystem model means each content type has different strengths: instructions for flexible guidance, code for reliability, resources for factual lookup.

| Level                     | When loaded             | Token cost            | Content                                                                                                                    |
|---------------------------|-------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Level 1: Metadata**     | Always (at startup)     | ~100 tokens per Skill | `name` and `description` from YAML frontmatter                                                                             |
| **Level 2: Instructions** | When Skill is triggered | Under 5k tokens       | SKILL.md body with instructions and guidance                                                                               |
| **Level 3+: Resources**   | As needed               | None until accessed   | Bundled files. Reference files load into context when read. Scripts run through bash, and only their output enters context |

Progressive disclosure ensures only relevant content occupies the context window at any given time.

### The Skills architecture

Skills run in a code execution environment where Claude has filesystem access, bash commands, and code execution capabilities. Skills exist as directories on a virtual machine, and Claude interacts with them using the same bash commands you'd use to navigate files on your computer.

**How Claude accesses Skill content:**

When a Skill is triggered, Claude uses bash to read SKILL.md from the filesystem, bringing its instructions into the context window. If those instructions reference other files (such as FORMS.md or a database schema), Claude reads those files too using additional bash commands. When instructions mention executable scripts, Claude runs them through bash and receives only the output (the script code itself never enters context).

**What this architecture enables:**

- **On-demand file access:** Claude reads only the files each task needs. A Skill can include dozens of reference files, but if your task only needs the sales schema, that's the one file Claude loads. The rest stay on the filesystem and cost zero tokens.
- **Efficient script execution:** When Claude runs `validate_form.py`, the script's code never loads into the context window. Only its output (such as "Validation passed" or a specific error message) consumes tokens, which makes scripts far more efficient than having Claude generate equivalent code on the fly.
- **No practical limit on bundled content:** Files don't consume context until accessed, so Skills can include comprehensive API documentation, large datasets, or extensive examples. There's no context penalty for bundled content that isn't used.

### Example: Loading a PDF processing Skill

Here's how Claude loads and uses the custom `pdf-processing` Skill from the earlier examples (not the pre-built `pdf` Skill):

1.  **Startup:** System prompt includes: `pdf-processing - Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.`
2.  **User request:** "Extract the text from this PDF and summarize it"
3.  **Claude invokes:** `bash: cat pdf-processing/SKILL.md` → Instructions loaded into context
4.  **Claude determines:** Form filling is not needed, so FORMS.md is not read
5.  **Claude executes:** Uses instructions from SKILL.md to complete the task

## Where Skills work

Skills are available across Claude's agent products:



Claude Platform on AWS and Microsoft Foundry inherit the same Skills behavior as the Claude API in all following sections, except where [Limitations and constraints](#limitations-and-constraints) says otherwise.

### Claude API

The Claude API supports both pre-built Agent Skills and custom Skills. Both work identically: specify the relevant `skill_id` in the `container` parameter along with the [code execution tool](agents-and-tools-tool-use-code-execution-tool.md).

**Prerequisites:** Using Skills through the API requires the [code execution tool](agents-and-tools-tool-use-code-execution-tool.md), whose container Skills run in.

Use pre-built Agent Skills by referencing their `skill_id` (`pptx`, `xlsx`, `docx`, or `pdf`), or create and upload your own through the Skills API (`/v1/skills` endpoints). Custom Skills are shared workspace-wide: all workspace members can access them.

Skills on the API run in a sandboxed container with no network access and no runtime package installation. See [Limitations and constraints](#limitations-and-constraints) for details.

To learn more, see [Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md).

### Claude Code

[Claude Code](https://platform.claude.com/docs/en/01-Getting-Started/overview.md) supports custom Skills. The pre-built document Skills (PowerPoint, Excel, Word, PDF) are not available in Claude Code, though the open-source [Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md) comes bundled with it. See the full list of [built-in commands and Skills](https://platform.claude.com/docs/en/02-Claude-Code-CLI/built-in-commands-claude-code-docs.md) that ship with Claude Code.

**Custom Skills:** Create Skills as directories with SKILL.md files. Claude discovers and uses them automatically.

Custom Skills in Claude Code are filesystem-based and don't require API uploads: place them in `~/.claude/skills/` (personal) or `.claude/skills/` (project).

To learn more, see [Use Skills in Claude Code](../../08-Plugins-Skills/skills.md).

### claude.ai

[claude.ai](https://claude.ai) supports both pre-built Agent Skills and custom Skills.

**Pre-built Agent Skills:** These Skills are active when you create documents. Claude uses them with no setup required.

**Custom Skills:** Upload your own Skills as zip files through Settings \> Features. Available on Pro, Max, Team, and Enterprise plans with [code execution enabled](../../15-Claude-AI-Features/create-and-edit-files-with-claude.md). Custom Skills are individual to each user. They are not shared organization-wide and cannot be centrally managed by admins.

To learn more about using Skills in claude.ai, see the following resources in the Claude Help Center:

- [What are Skills?](../../02-Claude-Code-CLI/what-are-skills.md)
- [Using Skills in Claude](https://platform.claude.com/docs/en/99-Other/using-skills-in-claude-a1bdb5a95a.md)
- [How to create custom Skills](https://platform.claude.com/docs/en/02-Claude-Code-CLI/creating-custom-skills-eb687e04e2.md)
- [Teach Claude your way of working using Skills](../../15-Claude-AI-Features/teach-claude-your-way-of-working-using-skills.md)

## Skill structure

Every Skill requires a `SKILL.md` file with YAML frontmatter:

```python
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
[Clear, step-by-step guidance for Claude to follow]

## Examples
[Concrete examples of using this Skill]
```



**Required fields:** `name` and `description`

**Field requirements:**

`name`:

- Maximum 64 characters
- Must contain only lowercase letters, numbers, and hyphens
- Cannot contain XML tags
- Cannot contain reserved words: "anthropic", "claude"

`description`:

- Must be non-empty
- Maximum 1024 characters
- Cannot contain XML tags

The `description` must include both what the Skill does and when Claude should use it. For complete authoring guidance, see [Skill authoring best practices](agents-and-tools-agent-skills-best-practices.md).

## Security considerations

Use Skills only from trusted sources: those you created yourself or obtained from Anthropic. Skills give Claude new capabilities through instructions and code, which also means a malicious Skill can direct Claude to invoke tools or execute code in ways that don't match the Skill's stated purpose.



If you must use a Skill from an untrusted or unknown source, exercise extreme caution and thoroughly audit it before use. Depending on what access Claude has when executing the Skill, malicious Skills could lead to data exfiltration, unauthorized system access, or other security risks.

**Key security considerations:**

- **Audit thoroughly:** Review all files bundled in the Skill: SKILL.md, scripts, images, and other resources. Look for unusual patterns such as unexpected network calls, file access patterns, or operations that don't match the Skill's stated purpose
- **External sources are risky:** Skills that fetch data from external URLs pose particular risk, as fetched content may contain malicious instructions. Even trustworthy Skills can be compromised if their external dependencies change over time
- **Tool misuse:** Malicious Skills can invoke tools (file operations, bash commands, code execution) in harmful ways
- **Data exposure:** Skills with access to sensitive data could be designed to leak information to external systems
- **Treat like installing software:** Be especially careful when integrating Skills into production systems with access to sensitive data or critical operations

For organization-scale governance, vetting, and deployment guidance, see [Skills for enterprise](agents-and-tools-agent-skills-enterprise.md). Claude Enterprise organizations can also turn on [Skill content scanning](agents-and-tools-agent-skills-enterprise.md#skill-content-scanning) for custom Skills uploaded in claude.ai and Claude Cowork. Scanning doesn't cover Skills uploaded through the Skills API or the Claude Console.

## Available Skills

### Pre-built Agent Skills

The following pre-built Agent Skills are available for immediate use:

- **PowerPoint (pptx):** Create presentations, edit slides, analyze presentation content
- **Excel (xlsx):** Create spreadsheets, analyze data, generate reports with charts
- **Word (docx):** Create documents, edit content, format text
- **PDF (pdf):** Generate formatted PDF documents and reports

These Skills are available on the Claude API, [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), and claude.ai. See the [quickstart tutorial](agents-and-tools-agent-skills-quickstart.md) to start using them in the API.

### Open-source Skills

Anthropic also publishes open-source Skills in the [skills repository](https://github.com/anthropics/skills):

- **[Claude API skill](agents-and-tools-agent-skills-claude-api-skill.md):** Provides Claude with up-to-date API reference material, SDK documentation, and best practices for eight programming languages. Bundled with Claude Code and also available for installation from the skills repository.

### Custom Skills examples

For complete examples of custom Skills, see the [Skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction).

## Data retention

Agent Skills is not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.

For ZDR eligibility across all features, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

For audit logging of Skills API operations, see [Audit logging](../Guides/build-with-claude-skills-guide.md#audit-logging) in Using Agent Skills with the API.

## Limitations and constraints

Claude Platform on AWS and Microsoft Foundry follow the same limitations as the Claude API in the following subsections. In addition, on Microsoft Foundry, the [Skill version download endpoint](../Endpoints/beta-skills-versions-download.md) (`GET /v1/skills/{skill_id}/versions/{version}/content`) is not supported.

### Cross-surface availability

**Custom Skills do not sync across surfaces**. Skills uploaded to one surface are not automatically available on others:

- Skills uploaded to claude.ai must be separately uploaded to the API
- Skills uploaded through the API are not available on claude.ai
- Claude Code Skills are filesystem-based and separate from both claude.ai and API

Manage and upload Skills separately for each surface where you want to use them.

### Sharing scope

Skills have different sharing models depending on where you use them:

- **claude.ai:** Individual user only. Each team member must upload separately.
- **Claude API:** Workspace-wide. All workspace members can access uploaded Skills.
- **Claude Code:** Personal (`~/.claude/skills/`) or project-based (`.claude/skills/`). Can also be shared through Claude Code Plugins.

claude.ai does not support centralized admin management or org-wide distribution of custom Skills.

### Runtime environment constraints

The exact runtime environment available to your Skill depends on the product surface where you use it.

- **claude.ai:**
  - **Varying network access:** Depending on user/admin settings, Skills may have full, partial, or no network access. For more details, see the [Create and Edit Files](../../15-Claude-AI-Features/create-and-edit-files-with-claude.md#h_6b7e833898) support article.
- **Claude API:**
  - **No network access:** Skills cannot make external API calls or access the internet.
  - **No runtime package installation:** Only pre-installed packages are available. You cannot install new packages during execution.
  - **Pre-configured dependencies only:** Check the [Code execution tool](agents-and-tools-tool-use-code-execution-tool.md) documentation for the list of available packages.
- **Claude Code:**
  - **Full network access:** Skills have the same network access as any other program on the user's computer.
  - **Global package installation discouraged:** Skills should only install packages locally to avoid interfering with the user's computer.

Plan your Skills to work within these constraints.

## Next steps



[Get started with Agent Skills in the API](agents-and-tools-agent-skills-quickstart.md)

Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.



[Using Agent Skills with the API](../Guides/build-with-claude-skills-guide.md)

Learn how to use Agent Skills to extend Claude's capabilities through the API.



[Use Skills in Claude Code](../../08-Plugins-Skills/skills.md)

Create and manage custom Skills in Claude Code.



[Skill authoring best practices](agents-and-tools-agent-skills-best-practices.md)

Learn how to write effective Skills that Claude can discover and use successfully.
