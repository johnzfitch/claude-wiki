---
category: "99-Other"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation"
title: "How to create a skill with Claude through conversation | Claude Help Center"
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

[](#h_31fb4ffa32)

[](#h_297c3cec23)

[](#h_37932beb75)

[](#h_bf474b2cfc)

[All Collections](/en/)

[Video Tutorials](https://support.claude.com/en/collections/10548294-video-tutorials)

How to create a skill with Claude through conversation

# How to create a skill with Claude through conversation

Updated this week

Table of contents

[](#h_31fb4ffa32)

[](#h_297c3cec23)

[](#h_37932beb75)

[](#h_bf474b2cfc)

With Skills, you are able to teach Claude specific workflows, tools, and processes. By creating a skill, you're giving Claude a playbook it can reference whenever you need a particular type of help—whether that's generating reports in your company's format, cleaning and using data the way you normally do, or pulling and analyzing CRM data your way.

\
There are two paths for creating skills. You can create skills by writing the files yourself for full control over structure and implementation. See *[How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills) and [Skills authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)* for that approach.

\
This guide focuses on the other path: creating skills through conversation with Claude. You describe your process naturally, and Claude handles the formatting and structure. This approach makes Skills accessible to anyone, regardless of technical background.

\
​*New to skills? See [What are Skills](https://support.claude.com/en/articles/12512176-what-are-skills) and [Skills user guide](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)* to get started learning about Skills.\
​

# An error occurred.

Unable to execute JavaScript.

## **Creating a skill through conversation**

Creating a skill with Claude means having a conversation where you explain your approach and share any materials you want included. Claude translates this into a properly formatted skill that can work in future chats.

### 1. Start a conversation

Open a new chat and say something like "I want to create a skill for quarterly business reviews" or "I need a skill that knows how to analyze customer feedback."\
​

If you have materials that show your approach—templates you use, examples of work you're proud of, brand guidelines you follow, data files you reference—upload them. You can also mention any connected tools Claude should use. If you are unsure of what else to include, ask Claude for guidance.\
​

### 2. Answer Claude's questions

Claude will ask about your process. Provide enough detail that someone capable but unfamiliar could follow your approach.\
​

You'll get questions about concrete usage ("Can you give examples of when you'd use this skill?") or about your process ("What makes output good for this type of work?").\
​

### 3. Claude builds the Skill

In Claude's thinking, you will see it read a *skill-creator* skill to follow best practices in creating a properly structured skill*.* Claude will create a SKILL.md file (the instruction file every skill needs), organize any materials you've provided, and generate code for operations you've described that need to happen consistently. Claude then packages everything into a skill file.\
​

### 4. Activate and test the skill

Save the the skill file that Claude creates. In [Settings \> Capabilities \> Skills](https://claude.ai/settings/capabilities), you can view your library of skills and turn them on or off as needed.\
​

Try using your skill by describing a task the skill should address. See if Claude recognizes the situation (you'll see "Using \[skill name\]" in Claude's thinking) and whether it produces the expected outcome. If something's off, ask Claude to update the skill with your desired changes. Repeat this process until your skill works effectively.\
​

## **Skills you can build**

You can build skills for a range of tasks. Skills can capture how your organization works, enable specialized expertise you don't personally have, or work together to handle complex workflows.

- **CRM automation skill:** creates contacts, updates opportunities, maintains data standards to eliminate repetitive entry

- **Legal contract review skill:** evaluates agreements against standard terms, identifies risky clauses, suggests protective language

- **Sprint planning skill:** calculates team velocity, estimates work accounting for patterns, allocates capacity, generates planning docs

- **SEO content skill:** analyzes opportunities, structures for search intent, optimizes while maintaining brand voice

- **Music composition skill:** creates original tracks with realistic instruments, applies genre conventions, exports for production

- **Report automation skill:** gathers monthly data, applies calculations, generates visualizations, formats in template, distributes to stakeholders

- **Skill reviewer skill:** evaluates another skill's effectiveness, suggests improvements to instructions, identifies missing edge cases, recommends structure changes

## **What you can include within a skill**

Skills bundle three types of content together—instructions, reference materials, and scripts. Knowing these components helps you articulate what you need when creating a skill with Claude.\
​

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781727755/40d01224cb2a1653189d5211e731/380d5eae-c159-4643-80e3-ce1be19b6d57?expires=1770722100&signature=2b192c1fef2cce4a448a26038781936f03ba70516ca4851797800ba8985b9729&req=dScvF858moZaXPMW1HO4zRjaA46Zjw%2Bcf1HwTII0D0HSqYhz4fVV934W2Tje%0AYv3%2BnYpwpHbDjpD5VdI%3D%0A)

\
​**Instructions —** Every skill needs a SKILL.md file that explains your process. When asking Claude to create a skill, describe your process for Claude to structure it into proper instructions. At the top of your [SKILL.md](http://skill.md) file, will be the skill's name and what it does. Claude scans this information first to decide whether or not to load and use the full skill during your conversations. Below that are clear instructions on how to do the task.

**Reference materials and assets —** Sometimes instructions alone aren't enough and Claude needs actual files to reference or use in the output. To include these, upload any relevant files or information when creating your Skill. Claude determines whether to embed guidance in the SKILL.md instructions or bundle it as a reference file.

- **Brand assets:** font files, logos, color palettes, design templates

- **Reference documents:** policy guides, workflow procedures, database schemas

- **Templates:** spreadsheet with formulas, presentation layouts, document styles

- **Data files:** CSV lookup tables, JSON configurations, pricing databases

- **Media files:** audio samples, images, video clips

**Scripts —** These are executable code files that Claude can run to handle complex operations more reliably than instructions alone. You don't need to write these yourself. When you describe tasks that need scripts, Claude recognizes them and creates the code automatically. Examples include:

- **Data work** for tasks like cleaning data, running calculations, and creating charts or dashboards

- **Document work** to handle file processing tasks like batch editing and applying formatting

- **Integrations** to connect your skill to other tools you use, such fetching data from external sources

- **Media processing** to transform images, edit videos, and generate audio

## **Additional Resources**

#### Getting started

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)

- [Teach Claude your way of working using skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

#### Going deeper

- [Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)

- [Skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)

- [Skill cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/skills)

- [Agent skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/12512176-what-are-skills)

What are Skills?

[](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

Using Skills in Claude

[](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

How to create custom Skills

[](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

Teach Claude your way of working using skills

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
