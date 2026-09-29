---
title: "What are skills? | Claude Help Center"
source_url: "https://support.claude.com/en/articles/12512176-what-are-skills"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-29T06:31:52Z"
tags: ["agents", "claude-code", "skills"]
---

# What are skills?



Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

Skills are available for users on Free, Pro, Max, Team, and Enterprise plans. This feature requires **[code execution to be enabled](../15-Claude-AI-Features/create-and-edit-files-with-claude.md#h_1c99382190)**. Skills are also available in Claude Code, and in beta for all API users using the code execution tool.

------------------------------------------------------------------------

## How do skills work?

Skills improve Claude’s consistency, speed, and performance on many tasks. Skills work through progressive disclosure—Claude determines which skills are relevant and loads the information it needs to complete that task, helping to prevent context window overload.

When you ask Claude to complete a task, it reviews available skills, loads relevant ones, and applies their instructions.

------------------------------------------------------------------------

## Types of skills

### Anthropic skills

These are skills created and maintained by Anthropic, such as enhanced document creation for Excel, Word, PowerPoint, and PDF files. Anthropic skills are available to all users and Claude invokes them automatically when relevant.

### Custom skills

These are skills you or your organization create for specialized workflows and domain-specific tasks. Here are some potential workflows you could enable using custom skills:

- Apply brand style guidelines to documents and presentations.

- Generate communications following company email templates.

- Structure meeting notes with company-specific formats.

- Create tasks in company tools (JIRA, Asana, Linear) following team conventions.

- Execute company-specific data analysis workflows.

- Automate personal workflows and customize Claude to match your work style.

### Organization provisioned skills

For Team and Enterprise plans, organization Owners can provision skills for all users. Skills provisioned in this way appear automatically in every team member's skills list and can be set as enabled or disabled by default. This allows organizations to:

- Distribute approved workflows consistently across all employees

- Ensure teams use standardized procedures and best practices

- Deploy new capabilities without requiring individual uploads

Learn more about provisioning skills in **[Provision and manage skills for your organization](../22-Safety-Policy/provisioning-and-managing-skills-for-your-organization.md)**.

### Partner skills

The Skills Directory features professionally-built skills from partners like Notion, Figma, Atlassian, and others. These skills are designed to work seamlessly with their respective MCP connectors, enabling powerful integrated workflows.

------------------------------------------------------------------------

## Key benefits

**Improvement in Claude’s performance of specific tasks**: Skills provide specialized capabilities for tasks like document creation, data analysis, and domain-specific work that requires supplementing Claude's general knowledge.

**Organizational knowledge capture**: Package your company's workflows, best practices, and institutional knowledge for Claude to use consistently across your team.

**Easy customization**: Anyone can create skills by writing instructions in Markdown—no coding required for simple skills, though you can attach executable scripts to custom skills for more advanced functionality.

**Centralized management for organizations:** Team and Enterprise plan Owners can provision skills organization-wide, ensuring consistent workflows across teams without requiring individual setup from each user.

------------------------------------------------------------------------

## Agent Skills open standard

The Agent Skills specification is published as an open standard at **[agentskills.io](https://agentskills.io)**. This means skills you create aren't locked to Claude—the same skill format works across AI platforms and tools that adopt the standard. A reference Python SDK is also available for developers implementing skills support in their own platforms.

------------------------------------------------------------------------

## Skills compared to other Claude capabilities

### Skills vs. projects

**[Projects](../15-Claude-AI-Features/what-are-projects.md)** provide static background knowledge that's always loaded when you start chats within them. Skills provide specialized procedures that activate dynamically when needed and work everywhere across Claude.

### Skills vs. MCP (Model Context Protocol)

MCP connects Claude to external services and data sources. Skills provide procedural knowledge—instructions for how to complete specific tasks or workflows. You can use both together: MCP connections give Claude access to tools, while skills teach Claude how to use those tools effectively.

### Skills vs. custom instructions

**[Custom instructions](../15-Claude-AI-Features/understanding-claude-s-personalization-features.md)** apply broadly to all your conversations. Skills are task-specific and only load when relevant, making them better for specialized workflows.

------------------------------------------------------------------------

## Learn more about skills

To discover available skills, check out the directory by clicking "Customize" in your account and navigating to "Skills." You can click "+" then "Browse skills" to open the directory. For more information, see **[Browse skills, connectors, and plugins in one directory](../14-Connectors/browse-skills-connectors-and-plugins-in-one-directory.md)**.

On the Enterprise plan, organizations can turn on skill scanning to check uploaded skills and plugins for malicious content. Learn more about **[skill and plugin scanning](get-started-with-skill-and-plugin-scanning.md)**.

For more details about how skills work, see **[Agent Skills](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-overview.md)** in our Claude Docs.
