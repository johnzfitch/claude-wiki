---
category: "22-Safety-Policy"
fetched_at: "2026-03-03T15:08:29Z"
source_url: "https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization"
title: "Provision and manage Skills for your organization | Claude Help Center"
---

4.  Provision and manage Skills for your organization

# Provision and manage Skills for your organization


Organization-wide skill management is available to Team and Enterprise plans.

This article explains how organization owners can provision skills for all users in their organization. Provisioning skills to your team allows you to distribute approved workflows and capabilities across your entire organization from a central location.

## Prerequisites

Before you can provision skills for your organization, you must enable two capabilities by toggling them on:

1.  **Code execution and file creation** in **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**

2.  **Skills** in **[Organization settings \> Skills](https://claude.ai/admin-settings/skills)**

Skills require code execution to function, so if code execution is disabled, skills will not be available.

------------------------------------------------------------------------

## Provision skills for your organization

When you upload a skill through organization settings, it automatically becomes available to all users in your organization in **[Customize \> Skills](https://claude.ai/customize/skills)**. This means that individual users no longer need to manually upload the same skills.

**To provision a skill:**

1.  Navigate to **[Organization settings \> Skills](https://claude.ai/admin-settings/skills)**.

2.  In the **Organization skills** section, click "+ Add."

3.  Select a .zip file containing your skill (must include a SKILL.md file).

4.  The skill is immediately provisioned to all users in your organization.

### Set default status

When provisioning a skill, you can choose whether it should be enabled or disabled by default for users:

- **Enabled by default:** The skill is automatically active for all users. Users can still toggle it off individually if they prefer.

- **Disabled by default:** The skill appears in users' Skills lists but is not active until they toggle it on.

Individual users can always toggle owner-provisioned skills on or off based on their preferences, regardless of the default setting.

------------------------------------------------------------------------

## How users see provisioned skills

Skills provisioned by an organization owner will appear for each user in **[Customize \> Skills](https://claude.ai/customize/skills)** alongside Anthropic skills and any skills they've uploaded themselves.

These skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

------------------------------------------------------------------------

## Manage and remove provisioned skills

The **Organization skills** section in **[Organization settings \> Skills](https://claude.ai/admin-settings/skills)** displays all skills that have been provisioned for your organization. You can use search and section headings to navigate your provisioned skills.

To remove a skill from your organization, locate it in the **Organization skills** list and select the option to remove it. Once removed, the skill will no longer appear in users' Skills lists in **[Customize \> Skills](https://claude.ai/customize/skills).**

**Note:** Only owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

------------------------------------------------------------------------

## Best practices

- **Test skills before provisioning:** Upload and test skills on your own account first to verify they work as expected before distributing them organization-wide.

- **Use descriptive names:** Give skills clear names that help users understand their purpose at a glance.

- **Write clear descriptions:** The skill's description helps Claude determine when to use it automatically. Ensure descriptions accurately reflect what the skill does.

- **Consider default status carefully:** Enable skills by default when they're broadly useful to most users. Use disabled by default for specialized skills that only some team members need.

------------------------------------------------------------------------

Related Articles


How can I disable public projects?


What are Skills?


Use Skills in Claude


Cowork for Team and Enterprise plans


Find and join a Team or Enterprise organization
