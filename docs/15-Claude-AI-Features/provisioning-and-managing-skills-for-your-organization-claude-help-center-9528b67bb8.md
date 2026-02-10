---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:52:05Z"
source_url: "https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization"
title: "Provisioning and managing Skills for your organization | Claude Help Center"
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

[](#h_7673241237)

[](#h_4dea113421)

[](#h_3f6923f81f)

[](#h_e208b55f2f)

[](#h_091510b3f8)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Features and Capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities)

Provisioning and managing Skills for your organization

# Provisioning and managing Skills for your organization

Updated yesterday

Table of contents

[](#h_7673241237)

[](#h_4dea113421)

[](#h_3f6923f81f)

[](#h_e208b55f2f)

[](#h_091510b3f8)

Organization-wide skill management is available to Team and Enterprise plans.

This article explains how organization Owners can provision skills for all users in their organization. Provisioning skills to your team allows you to distribute approved workflows and capabilities across your entire organization from a central location.

## Prerequisites

Before you can provision skills for your organization, you must enable two capabilities by toggling them on in [Admin settings \> Capabilities](https://claude.ai/admin-settings/capabilities):

1.  **Code execution and file creation**

2.  **Skills**

Skills require code execution to function, so if code execution is disabled, skills will not be available.

## Provisioning skills for your organization

When you upload a skill through Admin settings, it automatically becomes available to all users in your organization in [Settings \> Capabilities](https://claude.ai/settings/capabilities) under **Skills**. This means that individual users no longer need to manually upload the same skills.

### To provision a skill

1.  Navigate to [Admin settings \> Capabilities](https://claude.ai/admin-settings/capabilities).

2.  Locate the **Skills** section.

3.  Click “Upload skill.”

4.  Select a .zip file containing your skill (must include a SKILL.md file).

5.  The skill is immediately provisioned to all users in your organization.

### Setting default status

When provisioning a skill, you can choose whether it should be enabled or disabled by default for users:

- **Enabled by default:** The skill is automatically active for all users. Users can still toggle it off individually if they prefer.

- **Disabled by default:** The skill appears in users' Skills list but is not active until they toggle it on.

Individual users can always toggle Owner-provisioned skills on or off based on their preferences, regardless of the default setting.

## How users see provisioned skills

Skills provisioned by an organization Owner will appear in each user's **Skills** section in [Settings \> Capabilities](https://claude.ai/settings/capabilities) alongside Anthropic skills and any skills they've uploaded themselves.

These skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

## Managing and removing provisioned skills

The **Skills** section in Admin settings displays all skills that have been provisioned for your organization. You can use search and section headings to navigate your provisioned skills.

To remove a skill from your organization, locate it in the Skills list and select the option to remove it. Once removed, the skill will no longer appear in users' Skills lists.

**Note:** Only Owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

## Best Practices

- **Test skills before provisioning:** Upload and test skills on your own account first to verify they work as expected before distributing them organization-wide.

- **Use descriptive names:** Give skills clear names that help users understand their purpose at a glance.

- **Write clear descriptions:** The skill's description helps Claude determine when to use it automatically. Ensure descriptions accurately reflect what the skill does.

- **Consider default status carefully:** Enable skills by default when they're broadly useful to most users. Use disabled by default for specialized skills that only some team members need.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12512176-what-are-skills)

What are Skills?

[](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

Using Skills in Claude

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)

Cowork for Team and Enterprise plans

[](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization)

Find and join a Team or Enterprise organization

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
