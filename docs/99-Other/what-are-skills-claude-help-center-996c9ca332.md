---
category: "99-Other"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12512176-what-are-skills"
title: "What are Skills? | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_f5a87690c3)

[](#h_b3f521b778)

[](#h_139a46811b)

[](#h_8ada01c45f)

[](#h_0f5f83e7da)

[](#h_c858f8fc74)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

What are Skills?

# What are Skills?

Updated this week

Table of contents

[](#h_f5a87690c3)

[](#h_b3f521b778)

[](#h_139a46811b)

[](#h_8ada01c45f)

[](#h_0f5f83e7da)

[](#h_c858f8fc74)

Skills are available for users on free, Pro, Max, Team, and Enterprise plans. This feature requires [code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190). Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

## How do Skills work?

Skills improve Claude’s consistency, speed, and performance on many tasks. Skills work through progressive disclosure—Claude determines which Skills are relevant and loads the information it needs to complete that task, helping to prevent context window overload.

When you ask Claude to complete a task, it reviews available Skills, loads relevant ones, and applies their instructions.

## Types of Skills

### Anthropic Skills

These are Skills created and maintained by Anthropic, such as enhanced document creation for Excel, Word, PowerPoint, and PDF files. Anthropic Skills are available to all users and Claude invokes them automatically when relevant.

### Custom Skills

These are Skills you or your organization create for specialized workflows and domain-specific tasks. Here are some potential workflows you could enable using custom Skills:

- Apply brand style guidelines to documents and presentations.

- Generate communications following company email templates.

- Structure meeting notes with company-specific formats.

- Create tasks in company tools (JIRA, Asana, Linear) following team conventions.

- Execute company-specific data analysis workflows.

- Automate personal workflows and customize Claude to match your work style.

### Organization provisioned skills

For Team and Enterprise plans, organization Owners can provision skills for all users. Skills provisioned in this way appear automatically in every team member's Skills list and can be set as enabled or disabled by default. This allows organizations to:

- Distribute approved workflows consistently across all employees

- Ensure teams use standardized procedures and best practices

- Deploy new capabilities without requiring individual uploads

Learn more about provisioning skills in [Provisioning and managing Skills for your organization](https://support.claude.com/en/articles/13119606-managing-skills-as-an-admin).

### Partner skills

The Skills Directory features professionally-built skills from partners like Notion, Figma, Atlassian, and others. These skills are designed to work seamlessly with their respective MCP connectors, enabling powerful integrated workflows.

## Key Benefits

**Improvement in Claude’s performance of specific tasks**: Skills provide specialized capabilities for tasks like document creation, data analysis, and domain-specific work that requires supplementing Claude's general knowledge.

**Organizational knowledge capture**: Package your company's workflows, best practices, and institutional knowledge for Claude to use consistently across your team.

**Easy customization**: Anyone can create Skills by writing instructions in Markdown—no coding required for simple Skills, though you can attach executable scripts to custom Skills for more advanced functionality.

**Centralized management for organizations:** Team and Enterprise plan Owners can provision skills organization-wide, ensuring consistent workflows across teams without requiring individual setup from each user.

## Agent Skills Open Standard

The Agent Skills specification is published as an open standard at [agentskills.io](https://agentskills.io). This means skills you create aren't locked to Claude—the same skill format works across AI platforms and tools that adopt the standard. A reference Python SDK is also available for developers implementing skills support in their own platforms.

## Comparing Skills to other Claude capabilities

### Skills vs. Projects

[Projects](https://support.claude.com/en/articles/9517075-what-are-projects) provide static background knowledge that's always loaded when you start chats within them. Skills provide specialized procedures that activate dynamically when needed and work everywhere across Claude.

### Skills vs. MCP (Model Context Protocol)

MCP connects Claude to external services and data sources. Skills provide procedural knowledge—instructions for how to complete specific tasks or workflows. You can use both together: MCP connections give Claude access to tools, while Skills teach Claude how to use those tools effectively.

### Skills vs. Custom Instructions

[Custom instructions](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) apply broadly to all your conversations. Skills are task-specific and only load when relevant, making them better for specialized workflows.

## Learn more about Skills

For more detailed information about how Skills work, see [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) in our Claude Docs.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

Using Skills in Claude

[](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

How to create custom Skills

[](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation)

How to create a skill with Claude through conversation

[](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)

Provisioning and managing Skills for your organization

[](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

Anthropic Software Directory Policy

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
