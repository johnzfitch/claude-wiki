---
category: "02-Claude-Code-CLI"
source_url: "https://support.claude.com/en/articles/12512180-using-skills-in-claude"
---


Skills are available for users on free, Pro, Max, Team, and Enterprise plans. This feature requires code execution to be enabled. Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Skills extend Claude's capabilities by giving it access to specialized knowledge and workflows. This guide shows you how to enable, discover, and use Skills in Claude.

 

Prerequisites

For Enterprise plans: Owners must first enable both Code execution and file creation and Skills in Admin settings > Capabilities. Owners can also upload skills to provision them organization-wide — these skills automatically appear for all users. Once Skills are enabled at the organization level, individual members can toggle on example skills, access provisioned skills, and upload their own personal skills in Settings > Capabilities.

 

For Team plans: This feature is enabled by default at the organization level. Once enabled, individual members can toggle on example skills and upload their own in Settings > Capabilities.

 

For Max, Pro, and free plans: You can enable example skills and upload your own in Settings > Capabilities.

 

How to enable Skills

Navigate to Settings > Capabilities.

Ensure that Code execution and file creation is enabled.

Scroll to the Skills section.

Toggle individual skills on or off as needed.

To add custom skills, click "Upload skill" and upload a ZIP file containing your skill folder.

 

Organization provisioned skills (Team and Enterprise plans)

Organization Owners can provision skills for all users. These skills appear in your individual Skills list with a team indicator — you can toggle them on or off based on your preferences. For information on provisioning skills for your organization, see Provisioning and managing Skills for your organization.

 

Using Anthropic Skills

Anthropic provides several built-in skills that are available to all users, including:

Enhanced Excel spreadsheet creation and manipulation

Professional Word document creation

PowerPoint presentation generation

PDF creation and processing

With Code execution and file creation on, Claude will automatically use these tools when relevant. You don't need to explicitly invoke them—Claude determines when each skill is needed based on your request.

 

For example, if you ask Claude to "Create a PowerPoint presentation about Q3 results," Claude will automatically use the PowerPoint skill if the capability is enabled.

 

Adding and using custom skills

You can also create and upload your own skills to teach Claude your specific workflows:

Create a skill following the skill structure (see Creating Custom Skills for detailed instructions).

Package your skill folder as a ZIP file.

Navigate to Settings > Capabilities.

In the Skills section, click "Upload skill."

Upload your ZIP file.

Your skill will appear in your Skills list and can be toggled on or off.

Note: Custom skills you upload are private to your individual account. If you’re on a Team or Enterprise plan and want to share skills with your organization, see Provisioning skills for your organization.

 

How Claude uses Skills

Claude automatically identifies and loads relevant skills based on your task. Refer to What are Skills? to learn how this works.

 

Discovering skills from the Skills Directory

The Skills Directory features professionally-built skills from leading platforms like Notion, Figma, and Atlassian. These partner skills are designed to work with their respective MCP connectors, enabling powerful workflows that combine Claude's capabilities with your existing tools.

 

To install a skill from the Skills Directory:

Visit the Skills Directory at claude.com/connectors.

Browse available skills or filter by category.

Click on a skill to view its details and download link.

Download the skill package from the linked repository (typically GitHub).

Upload the downloaded ZIP file in Settings > Capabilities under Skills.

 

Managing your Skills
Viewing your Skills

All your skills are listed in Settings > Capabilities under the Skills section. You can see:

Anthropic skills (created, tested, and maintained by Anthropic)

Custom skills you've uploaded

When each skill was enabled or uploaded

A brief description of what each skill does

 

Enabling and disabling your Skills

Toggle any skill on or off using the switch next to it. Disabled skills won't be available to Claude.

 

Removing custom Skills

To remove a custom skill you've uploaded:

Navigate to Settings > Capabilities.

Find the skill in your Skills list.

Click the delete or remove option.

Confirm deletion.

Privacy and security details

For Team and Enterprise plans, organization Owners can provision skills for all users through Admin settings. Individual peer-to-peer skill sharing is not currently available — users cannot directly share skills with specific colleagues. For personal skills, each individual must upload them to their own account. Skills in Claude and the API operate in Claude's secure sandboxed environment with no data persistence between sessions.

 

Note that skills may include, or instruct Claude to install, third-party packages and software for Claude to use when completing a task. See here for details onClaude’s container environment and here for API’s container environment.

 

What are the primary risks of using Skills?

The most significant risks are prompt injection, which allows Claude to be manipulated to execute unintended actions, and data exfiltration, caused by malicious package code or prompt-injected data leaks. We’ve implemented several mitigations to these risks. Refer to our security considerations for code execution for more information.

Important: Only install skills only from trusted sources. 

When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

 

Troubleshooting
Skills section not visible

Ensure code execution is enabled in Settings > Capabilities. Skills require the code execution environment to function.

 

Claude isn’t using a Skill

Verify the Skill is toggled on in Settings > Capabilities.

Check that the Skill's description field clearly explains when it should be used.

Ensure the Skill's instructions are clear and well-structured.

Try being more explicit in your request (e.g., "Use my brand guidelines skill to create a presentation").

Upload errors

Common reasons for upload failures:

ZIP file exceeds size limits

Skill folder name doesn't match the skill name

Missing required Skill.md file

Invalid characters in skill name or description

Skills greyed out

If Skills appear greyed out, code execution or Skills may be disabled at the organization level (for Team and Enterprise plans) or individually. Check with your organization's Owner or make sure to enable code execution in your settings.

 

Best Practices
Start Simple

Begin with Anthropic's pre-built Skills to understand how they work before creating custom skills.

 

Be Specific

Write clear descriptions when writing custom skills. A specific description tells Claude when to invoke your skill.

 

Test Your Skills

After uploading a custom skill, test it with a few different prompts to ensure it works as expected.

 

Organize by Purpose

Create separate skills for different purposes rather than a single skill that’s meant to do everything.

 

Learn more about using Skills

Refer to Teach Claude your way of working using Skills for more information and video demonstrations.

Related Articles
Create and edit files with Claude
What are Skills?
How to create custom Skills
How to use the single-cell-rna-qc skill with Claude
Provisioning and managing Skills for your organization