---
category: "05-Skills"
fetched_at: "2026-02-22T14:29:38Z"
source_url: "https://agentskills.io/integrate-skills"
title: "Integrate skills into your agent - Agent Skills"
---

[Skip to main content](#content-area)

[Agent Skills home page](/)

Agent Skills

Search...

⌘K

Ask AI

- [](https://github.com/agentskills/agentskills "agentskills/agentskills")
  agentskills/agentskills
- [](https://github.com/agentskills/agentskills "agentskills/agentskills")
  agentskills/agentskills

Search...

Navigation

Integrate skills into your agent

- [](/home)
  Overview

&nbsp;

- [](/what-are-skills)
  What are skills?

&nbsp;

- [](/specification)
  Specification

&nbsp;

- [](/integrate-skills)
  Integrate skills

On this page

- [Integration approaches](#integration-approaches)
- [Overview](#overview)
- [Skill discovery](#skill-discovery)
- [Loading metadata](#loading-metadata)
- [Parsing frontmatter](#parsing-frontmatter)
- [Injecting into context](#injecting-into-context)
- [Security considerations](#security-considerations)
- [Reference implementation](#reference-implementation)

# Integrate skills into your agent

Copy page

How to add Agent Skills support to your agent or tool.

Copy page

This guide explains how to add skills support to an AI agent or development tool.

## 

[​](#integration-approaches)

Integration approaches

The two main approaches to integrating skills are: **Filesystem-based agents** operate within a computer environment (bash/unix) and represent the most capable option. Skills are activated when models issue shell commands like `cat /path/to/my-skill/SKILL.md`. Bundled resources are accessed through shell commands. **Tool-based agents** function without a dedicated computer environment. Instead, they implement tools allowing models to trigger skills and access bundled assets. The specific tool implementation is up to the developer.

## 

[​](#overview)

Overview

A skills-compatible agent needs to:

1.  **Discover** skills in configured directories
2.  **Load metadata** (name and description) at startup
3.  **Match** user tasks to relevant skills
4.  **Activate** skills by loading full instructions
5.  **Execute** scripts and access resources as needed

## 

[​](#skill-discovery)

Skill discovery

Skills are folders containing a `SKILL.md` file. Your agent should scan configured directories for valid skills.

## 

[​](#loading-metadata)

Loading metadata

At startup, parse only the frontmatter of each `SKILL.md` file. This keeps initial context usage low.

### 

[​](#parsing-frontmatter)

Parsing frontmatter

Report incorrect code

Copy

Ask AI

``` shiki
function parseMetadata(skillPath):
    content = readFile(skillPath + "/SKILL.md")
    frontmatter = extractYAMLFrontmatter(content)

    return {
        name: frontmatter.name,
        description: frontmatter.description,
        path: skillPath
    }
```

### 

[​](#injecting-into-context)

Injecting into context

Include skill metadata in the system prompt so the model knows what skills are available. Follow your platform’s guidance for system prompt updates. For example, for Claude models, the recommended format uses XML:

Report incorrect code

Copy

Ask AI

``` shiki
<available_skills>
  <skill>
    <name>pdf-processing</name>
    <description>Extracts text and tables from PDF files, fills forms, merges documents.</description>
    <location>/path/to/skills/pdf-processing/SKILL.md</location>
  </skill>
  <skill>
    <name>data-analysis</name>
    <description>Analyzes datasets, generates charts, and creates summary reports.</description>
    <location>/path/to/skills/data-analysis/SKILL.md</location>
  </skill>
</available_skills>
```

For filesystem-based agents, include the `location` field with the absolute path to the SKILL.md file. For tool-based agents, the location can be omitted. Keep metadata concise. Each skill should add roughly 50-100 tokens to the context.

## 

[​](#security-considerations)

Security considerations

Script execution introduces security risks. Consider:

- **Sandboxing**: Run scripts in isolated environments
- **Allowlisting**: Only execute scripts from trusted skills
- **Confirmation**: Ask users before running potentially dangerous operations
- **Logging**: Record all script executions for auditing

## 

[​](#reference-implementation)

Reference implementation

The [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) library provides Python utilities and a CLI for working with skills. For example: **Validate a skill directory:**

Report incorrect code

Copy

Ask AI

``` shiki
skills-ref validate <path>
```

**Generate `<available_skills>` XML for agent prompts:**

Report incorrect code

Copy

Ask AI

``` shiki
skills-ref to-prompt <path>...
```

Use the library source code as a reference implementation.

[Specification](/specification)

[Powered by](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=agent-skills)

Assistant

Responses are generated using AI and may contain mistakes.
