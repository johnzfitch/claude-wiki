---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-15T04:10:27Z"
source_url: "https://support.claude.com/en/articles/12512180-use-skills-in-claude"
title: "Use Skills in Claude | Claude Help Center"
---

# Use Skills in Claude

Updated yesterday


Skills are available for users on free, Pro, Max, Team, and Enterprise plans. This feature requires **[code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)**. Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Skills extend Claude's capabilities by giving it access to specialized knowledge and workflows. This guide shows you how to enable, discover, and use Skills in Claude.

## Prerequisites

**For Enterprise plans:** Owners must first enable both **Code execution and file creation** in **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)** and **Skills** in **[Organization settings \> Skills](https://claude.ai/admin-settings/skills)**. Owners can also upload skills to provision them organization-wide — these skills automatically appear for all users. Once Skills are enabled at the organization level, individual members can toggle on example skills, access provisioned skills, and upload their own personal skills in **[Customize \> Skills](https://claude.ai/customize/skills)**.

**For Team plans:** This feature is enabled by default at the organization level. Once enabled, individual members can toggle on example skills and upload their own in **[Customize \> Skills](https://claude.ai/customize/skills)**.

**For Max, Pro, and free plans:** You can enable example skills and upload your own in **[Customize \> Skills](https://claude.ai/customize/skills)**.

------------------------------------------------------------------------

## How to enable Skills

1.  Navigate to **[Settings \> Capabilities](https://claude.ai/settings/capabilities)** and ensure that **Code execution and file creation** is enabled.

2.  Go to **[Customize \> Skills](https://claude.ai/customize/skills)**.

3.  Toggle individual skills on or off as needed.

## Provision skills organization-wide

Owners of Team and Enterprise organizations can provision skills for all users. These skills appear in your individual Skills list with a team indicator — you can toggle them on or off based on your preferences. For information on provisioning skills for your organization, see **[Provision and manage Skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization#h_4dea113421)**.

## Use Anthropic Skills

Anthropic provides several built-in skills that are available to all users, including:

- Enhanced Excel spreadsheet creation and manipulation

- Professional Word document creation

- PowerPoint presentation generation

- PDF creation and processing

With **Code execution and file creation** on, Claude will automatically use these tools when relevant. You don't need to explicitly invoke them—Claude determines when each skill is needed based on your request.

For example, if you ask Claude to "Create a PowerPoint presentation about Q3 results," Claude will automatically use the PowerPoint skill if the capability is enabled.

## Add and use custom skills

You can also create and upload your own skills to teach Claude your specific workflows:

1.  Create a skill following the skill structure (see **[How to create custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)** for detailed instructions).

2.  Package your skill folder as a ZIP file.

3.  Navigate to **[Customize \> Skills](https://claude.ai/customize/skills).**

4.  To add custom skills, click the "+" button, then select "Upload a skill":


5.  Upload a ZIP file containing your skill folder.

6.  Your skill will appear in your Skills list and can be toggled on or off.

**Note:** Custom skills you upload are private to your individual account. If you’re on a Team or Enterprise plan and want to share skills with your organization, see **[Provision skills for your organization](https://support.claude.com/en/articles/13119606-managing-skills-as-an-admin#h_4dea113421)**.

## How Claude uses Skills

Claude automatically identifies and loads relevant skills based on your task. Refer to **[What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)** to learn how this works.

------------------------------------------------------------------------

## Use Skills in Excel and PowerPoint

Skills you've enabled in your Claude settings are also available in the Claude for Excel and Claude for PowerPoint add-ins. Claude applies relevant Skills automatically while you work—you don't need to invoke them separately.

**How triggering works in the add-ins:**

- Type `/` in the sidebar to see available Skills and select one (for example, `/debug` or `/deck-check`).

- Or describe your task naturally—Claude recognizes when a Skill applies and uses it.

Claude adapts skills to the surface it’s in. A research skill may produce a Word document in Cowork, but detailed data breakdowns in Excel.

Some skills may work better on one surface than others. If you let Claude work across apps, Claude can orchestrate another app to apply the skill.

If you build a Skill with a specific Excel or PowerPoint template, Claude for Excel and Powerpoint can load that template exactly into the current open file.

### Instructions

Each add-in also has an **Instructions** field for persistent preferences — see **[Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-in-excel)** and **[Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-in-powerpoint)** for details.

------------------------------------------------------------------------

## Discover skills from the Skills Directory

The Skills Directory features professionally-built skills from leading platforms like Notion, Figma, and Atlassian. These partner skills are designed to work with their respective MCP connectors, enabling powerful workflows that combine Claude's capabilities with your existing tools.

**To install a skill from the Skills Directory:**

1.  Visit the Skills Directory at **[claude.com/connectors](http://claude.com/connectors)**.

2.  Browse available skills or filter by category.

3.  Click on a skill to view its details and download link.

4.  Download the skill package from the linked repository (typically GitHub).

5.  Upload the downloaded ZIP file in **[Customize \> Skills](https://claude.ai/customize/skills).**

------------------------------------------------------------------------

## Manage your Skills

### View your Skills

All your skills are listed in **[Customize \> Skills](https://claude.ai/customize/skills)**. You can see:

- Anthropic skills (created, tested, and maintained by Anthropic)

- Custom skills you've uploaded

- When each skill was enabled or uploaded

- A brief description of what each skill does

### Enable/disable your Skills

Toggle any skill on or off using the switch next to it. Disabled skills won't be available to Claude.

### Delete custom Skills

To remove a custom skill you've uploaded:

1.  Navigate to **[Customize \> Skills](https://claude.ai/customize/skills)**.

2.  Find the skill in your Skills list and click on it to view the details.

3.  Use the toggle in the upper right corner to disable the skill.

4.  To delete the custom skill entirely, click the "..." button next to the toggle, then select "Delete":


5.  Click "Delete" in the confirmation prompt.

If you change your mind, you can add the skill again by re-uploading the file.

------------------------------------------------------------------------

## Privacy and security details

For Team and Enterprise plans, organization Owners can provision skills for all users through organization settings. Individual peer-to-peer skill sharing is not currently available — users cannot directly share skills with specific colleagues. For personal skills, each individual must upload them to their own account. Skills in Claude and the API operate in Claude's secure sandboxed environment with no data persistence between sessions.

Note that skills may include, or instruct Claude to install, third-party packages and software for Claude to use when completing a task. See **[here](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1)** for details on Claude’s container environment and **[here](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool#containers)** for API’s container environment.

### What are the primary risks of using Skills?

The most significant risks are prompt injection, which allows Claude to be manipulated to execute unintended actions, and data exfiltration, caused by malicious package code or prompt-injected data leaks. We’ve implemented several mitigations to these risks. Refer to **[our security considerations for code execution](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1)** for more information.

**Important:** Only install skills only from trusted sources.

When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

------------------------------------------------------------------------

## Troubleshooting

### Skills section not visible

Ensure code execution is enabled in **[Settings \> Capabilities](https://claude.ai/settings/capabilities)**. Then navigate to **[Customize \> Skills](https://claude.ai/customize/skills)** to access your skills. Skills require the code execution environment to function.

### Claude isn’t using a Skill

- Verify the Skill is toggled on in **[Customize \> Skills](https://claude.ai/customize/skills)**.

- Check that the Skill's description field clearly explains when it should be used.

- Ensure the Skill's instructions are clear and well-structured.

- Try being more explicit in your request (e.g., "Use my brand guidelines skill to create a presentation").

### Upload errors

Common reasons for upload failures:

- ZIP file exceeds size limits

- Skill folder name doesn't match the skill name

- Missing required Skill.md file

- Invalid characters in skill name or description

### Skills greyed out

If Skills appear greyed out, code execution may be disabled at the organization level (for Team and Enterprise plans) or individually. Check with your organization's Owner or make sure to enable code execution in **[Settings \> Capabilities](https://claude.ai/settings/capabilities)**.

------------------------------------------------------------------------

## Best practices

### Start simple

Begin with Anthropic's pre-built Skills to understand how they work before creating custom skills.

### Be specific

Write clear descriptions when writing custom skills. A specific description tells Claude when to invoke your skill.

### Test your skills

After uploading a custom skill, test it with a few different prompts to ensure it works as expected.

### Organize by purpose

Create separate skills for different purposes rather than a single skill that’s meant to do everything.

------------------------------------------------------------------------

## Learn more about using Skills

Refer to **[Teach Claude your way of working using Skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)** for more information and video demonstrations.

------------------------------------------------------------------------

Related Articles


Create and edit files with Claude


What are Skills?


Claude for Financial Services Skills


Provision and manage Skills for your organization


Use Claude for Excel and PowerPoint with an LLM gateway
