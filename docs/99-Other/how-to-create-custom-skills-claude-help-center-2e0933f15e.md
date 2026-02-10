---
category: "99-Other"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12512198-how-to-create-custom-skills"
title: "How to create custom Skills | Claude Help Center"
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

[](#h_db275d1972)

[](#h_4e4ace21a0)

[](#h_0e125af124)

[](#h_e53a50417c)

[](#h_3909d72078)

[](#h_9e1cfbb21e)

[](#h_0e8242504a)

[](#h_175380ddad)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

How to create custom Skills

# How to create custom Skills

Updated this week

Table of contents

[](#h_db275d1972)

[](#h_4e4ace21a0)

[](#h_0e125af124)

[](#h_e53a50417c)

[](#h_3909d72078)

[](#h_9e1cfbb21e)

[](#h_0e8242504a)

[](#h_175380ddad)

Skills are available for users on Pro, Max, Team, and Enterprise plans. This feature requires [code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190). Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Custom Skills let you enhance Claude with specialized knowledge and workflows specific to your organization or personal work style. This article explains how to create, structure, and test your own Skills.

Skills can be as simple as a few lines of instructions or as complex as multi-file packages with executable code. The best Skills:

- Solve a specific, repeatable task

- Have clear instructions that Claude can follow

- Include examples when helpful

- Define when they should be used

- Are focused on one workflow rather than trying to do everything

## Creating a Skill.md File

Every Skill consists of a directory containing at minimum a Skill.md file, which is the core of the Skill. This file must start with a YAML frontmatter to hold name and description fields, which are required metadata. It can also contain additional metadata, instructions for Claude or reference files, executable scripts, or tools.

### Required metadata fields

**name:** A human-friendly name for your Skill (64 characters maximum)

- **Example:** Brand Guidelines

**description:** A clear description of what the Skill does and when to use it.

- This is critical—Claude uses this to determine when to invoke your Skill (200 characters maximum).

- **Example:** Apply Acme Corp brand guidelines to presentations and documents, including official colors, fonts, and logo usage.

### Optional Metadata Fields

**dependencies:** Software packages required by your Skill.

- **Example:** python\>=3.8, pandas\>=1.5.0

The metadata in the Skill.md file serves as the first level of a progressive disclosure system, providing just enough information for Claude to know when the Skill should be used without having to load all of the content.

### Markdown Body

The Markdown body is the second level of detail after the metadata, so Claude will access this if needed after reading the metadata. Depending on your task, Claude can access the Skill.md file and use the Skill.

### Example Skill.md

**Brand Guidelines Skill**

    ## Metadata
    name: Brand Guidelines
    description: Apply Acme Corp brand guidelines to all presentations and documents

    ## Overview
    This Skill provides Acme Corp's official brand guidelines for creating consistent, professional materials. When creating presentations, documents, or marketing materials, apply these standards to ensure all outputs match Acme's visual identity. Claude should reference these guidelines whenever creating external-facing materials or documents that represent Acme Corp.

    ## Brand Colors

    Our official brand colors are:
    - Primary: #FF6B35 (Coral)
    - Secondary: #004E89 (Navy Blue)
    - Accent: #F7B801 (Gold)
    - Neutral: #2E2E2E (Charcoal)

    ## Typography

    Headers: Montserrat Bold
    Body text: Open Sans Regular
    Size guidelines:
    - H1: 32pt
    - H2: 24pt
    - Body: 11pt

    ## Logo Usage

    Always use the full-color logo on light backgrounds. Use the white logo on dark backgrounds. Maintain minimum spacing of 0.5 inches around the logo.

    ## When to Apply

    Apply these guidelines whenever creating:
    - PowerPoint presentations
    - Word documents for external sharing
    - Marketing materials
    - Reports for clients

    ## Resources

    See the resources folder for logo files and font downloads.

## Adding Resources

If you have too much information to add to a single [Skill.md](http://skill.md) file (e.g., sections that only apply to specific scenarios), you can add more content by adding files within your Skill directory. For example, add a REFERENCE.md file containing supplemental and reference information to your Skill directory. Referencing it in [Skill.md](http://skill.md) will help Claude decide if it needs to access that resource when executing the Skill.

## Adding Scripts

For more advanced Skills, attach executable code files to [Skill.md](http://skill.md), allowing Claude to run code. For example, our document skills use the following programming languages and packages:

- Python (pandas, numpy, matplotlib)

- JavaScript/[Node.js](http://node.js)

- Packages to help with file editing

- visualization tools

**Note:** Claude and Claude Code can install packages from standard repositories (Python PyPI, JavaScript npm) when loading Skills. It’s not possible to install additional packages at runtime with API Skills—all dependencies must be pre-installed in the container.

## Packaging Your Skill

Once your Skill folder is complete:

1.  Ensure the folder name matches your Skill's name.

2.  Create a ZIP file of the folder.

3.  The ZIP should contain the Skill folder as its root (not a subfolder).

**Correct structure:**

my-Skill.zip

└── my-Skill/

├── Skill.md

└── resources/

**Incorrect structure:**

my-Skill.zip

└── (files directly in ZIP root)

## Testing Your Skill

### Before Uploading

1\. Review your Skill.md for clarity

2\. Check that the description accurately reflects when Claude should use the Skill

3\. Verify all referenced files exist in the correct locations

4\. Test with example prompts to ensure Claude invokes it appropriately

### After Uploading to Claude

1\. Enable the Skill in [Settings \> Capabilities](https://claude.ai/settings/capabilities).

2\. Try several different prompts that should trigger it

3\. Review Claude's thinking to confirm it's loading the Skill

4\. Iterate on the description if Claude isn't using it when expected

**Note for Team and Enterprise plans:** To make a skill available to all users in your organization, see Provisioning and managing Skills for your organization.

## Best Practices

**Keep it focused:** Create separate Skills for different workflows. Multiple focused Skills compose better than one large Skill.

**Write clear descriptions:** Claude uses descriptions to decide when to invoke your Skill. Be specific about when it applies.

**Start simple:** Begin with basic instructions in Markdown before adding complex scripts. You can always expand on the Skill later.

**Use examples:** Include example inputs and outputs in your Skill.md file to help Claude understand what success looks like.

**Test incrementally:** Test after each significant change rather than building a complex Skill all at once.

**Skills can build on each other:** While Skills can't explicitly reference other Skills, Claude can use multiple Skills together automatically. This composability is one of the most powerful parts of the Skills feature.

**Review the open Agent Skills specification:** Follow the guidelines at [agentskills.io](http://agentskills.io), so skills you create can work across platforms that adopt the standard.

For a more in-depth guide to skill creation, refer to [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) in our Claude Docs.

## Security Considerations

- Exercise caution when adding scripts to your Skill.md file.

- Don't hardcode sensitive information (API keys, passwords).

- Review any Skills you download before enabling them.

- Use appropriate MCP connections for external service access.

## Example Skills to Reference

Visit our repository on GitHub for example Skills you can use as templates: [https://github.com/anthropics/skills/tree/main/skills](https://github.com/anthropics/skills/tree/main/skills).

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12512176-what-are-skills)

What are Skills?

[](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

Using Skills in Claude

[](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

Teach Claude your way of working using skills

[](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation)

How to create a skill with Claude through conversation

[](https://support.claude.com/en/articles/12663107-claude-for-financial-services-skills)

Claude for Financial Services Skills

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
