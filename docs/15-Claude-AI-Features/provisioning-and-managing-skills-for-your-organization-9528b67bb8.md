---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization"
---


Organization-wide skill management is available to Team and Enterprise plans.

This article explains how organization Owners can provision skills for all users in their organization. Provisioning skills to your team allows you to distribute approved workflows and capabilities across your entire organization from a central location.

 

Prerequisites

Before you can provision skills for your organization, you must enable two capabilities by toggling them on in Admin settings > Capabilities:

Code execution and file creation

Skills

Skills require code execution to function, so if code execution is disabled, skills will not be available.

 

Provisioning skills for your organization

When you upload a skill through Admin settings, it automatically becomes available to all users in your organization in Settings > Capabilities under Skills. This means that individual users no longer need to manually upload the same skills.

 

To provision a skill

Navigate to Admin settings > Capabilities.

Locate the Skills section.

Click “Upload skill.”

Select a .zip file containing your skill (must include a SKILL.md file).

The skill is immediately provisioned to all users in your organization.

Setting default status

When provisioning a skill, you can choose whether it should be enabled or disabled by default for users:

Enabled by default: The skill is automatically active for all users. Users can still toggle it off individually if they prefer.

Disabled by default: The skill appears in users' Skills list but is not active until they toggle it on.

Individual users can always toggle Owner-provisioned skills on or off based on their preferences, regardless of the default setting.

 

How users see provisioned skills

Skills provisioned by an organization Owner will appear in each user's Skills section in Settings > Capabilities alongside Anthropic skills and any skills they've uploaded themselves.

 

These skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

 

Managing and removing provisioned skills

The Skills section in Admin settings displays all skills that have been provisioned for your organization. You can use search and section headings to navigate your provisioned skills.

 

To remove a skill from your organization, locate it in the Skills list and select the option to remove it. Once removed, the skill will no longer appear in users' Skills lists.

Note: Only Owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

 

Best Practices

Test skills before provisioning: Upload and test skills on your own account first to verify they work as expected before distributing them organization-wide.

Use descriptive names: Give skills clear names that help users understand their purpose at a glance.

Write clear descriptions: The skill's description helps Claude determine when to use it automatically. Ensure descriptions accurately reflect what the skill does.

Consider default status carefully: Enable skills by default when they're broadly useful to most users. Use disabled by default for specialized skills that only some team members need.

Related Articles
Create and edit files with Claude
What are Skills?
Using Skills in Claude
Setting up JIT or SCIM provisioning
Cowork for Team and Enterprise plans