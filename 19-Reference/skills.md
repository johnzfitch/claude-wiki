---
title: "Introducing Agent Skills | Claude by Anthropic"
source_url: "https://www.anthropic.com/news/skills"
category: "19-Reference"
fetched_at: "2026-10-21T06:29:57Z"
tags: ["agents", "news-research", "skills"]
---

# Introducing Agent Skills

- 

  Category[Announcements](https://www.anthropic.com/resources/product-announcements)
- 

  ProductClaude Platform
- 

  DateOctober 16, 2025
- 

  Reading time4 min
- 


***Update:** We've added [organization-wide management for skills](https://www.anthropic.com/resources/articles/organization-skills-and-directory), a [directory](../04-API-Reference/Other/partners-mcp.md) featuring partner-built skills, and published [Agent Skills](https://agentskills.io) as an open standard for cross-platform portability. (December 18, 2025)*

Claude can now use *Skills* to improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed.

Claude will only access a skill when it's relevant to the task at hand. When used, skills make Claude better at specialized tasks like working with Excel or following your organization's brand guidelines.

You've already seen Skills at work in Claude apps, where Claude uses them to create files like spreadsheets and presentations. Now, you can build your own skills and use them across Claude apps, Claude Code, and our API.

## How Skills work

While working on tasks, Claude scans available skills to find relevant matches. When one matches, it loads only the minimal information and files needed—keeping Claude fast while accessing specialized expertise.

Skills are:

- **Composable**: Skills stack together. Claude automatically identifies which skills are needed and coordinates their use.
- **Portable**: Skills use the same format everywhere. Build once, use across Claude apps, Claude Code, and API.
- **Efficient**: Only loads what's needed, when it's needed.
- **Powerful**: Skills can include executable code for tasks where traditional programming is more reliable than token generation.

Think of Skills as custom onboarding materials that let you package expertise, making Claude a specialist on what matters most to you. For a technical deep-dive on the Agent Skills design pattern, architecture, and development best practices, read our [engineering blog.](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Skills work with every Claude product

### **Claude apps**

Skills are available to Pro, Max, Team and Enterprise users. We provide skills for common tasks like document creation, examples you can customize, and the ability to create your own custom skills.

Claude automatically invokes relevant skills based on your task—no manual selection needed. You'll even see skills in Claude's chain of thought as it works.  
  
Creating skills is simple. The "skill-creator" skill provides interactive guidance: Claude asks about your workflow, generates the folder structure, formats the SKILL.md file, and bundles the resources you need. No manual file editing required.

Enable Skills in [Settings](https://claude.ai/redirect/website.v1.51f73c97-b077-44e7-85ba-8b27a025dfdf/settings/features). For Team and Enterprise users, admins must first enable Skills organization-wide.

### **Claude Developer Platform (API)**

Agent Skills, which we often refer to simply as Skills, can now be added to Messages API requests and the new `/v1/skills` endpoint gives developers programmatic control over custom skill versioning and management. Skills require the [Code Execution Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool) beta, which provides the secure environment they need to run.

Use Anthropic-created skills to have Claude read and generate professional Excel spreadsheets with formulas, PowerPoint presentations, Word documents, and fillable PDFs. Developers can create custom Skills to extend Claude's capabilities for their specific use cases.

Developers can also easily create, view, and upgrade skill versions through the Claude Console.

Explore the [documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) , our [skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction), or [Anthropic Academy](https://www.anthropic.com/learn/build-with-claude) to learn more.


> “Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.”

Anwar Haneef, GM & Head of Ecosystem

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

> “Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.”

Yusuke Kaji, General Manager AI

> “Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.”

Yashodha Bhavnani, Head of AI

> “Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.”

Anwar Haneef, GM & Head of Ecosystem

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

> “Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.”

Yusuke Kaji, General Manager AI

> “Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.”

Yashodha Bhavnani, Head of AI

> “Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.”

Anwar Haneef, GM & Head of Ecosystem

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

1/4

### **Claude Code**

Skills extend Claude Code with your team's expertise and workflows. Install skills via plugins from the anthropics/skills marketplace. Claude loads them automatically when relevant. Share skills through version control with your team. You can also manually install skills by adding them to `~/.claude/skills`. The Claude Agent SDK provides the same Agent Skills support for building custom agents.

## Getting started

- **Claude apps:** [User Guide](../15-Claude-AI-Features/teach-claude-your-way-of-working-using-skills.md) & [Help Center](../02-Claude-Code-CLI/what-are-skills.md)
- **API developers:** [Documentation](https://docs.claude.com/en/api/skills-guide)
- **Claude Code:** [Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- **Example Skills to customize:** [GitHub repository](https://github.com/anthropics/skills)

## What's next

We're working toward simplified skill creation workflows and enterprise-wide deployment capabilities, making it easier for organizations to distribute skills across teams.

Keep in mind, this feature gives Claude access to execute code. While powerful, it means being mindful about which skills you use—stick to trusted sources to keep your data safe. [Learn more](../02-Claude-Code-CLI/using-skills-in-claude.md#h_2746475e70).

## Related articles

Explore more product news and best practices for teams building with Claude.


ArticleOct 15, 2026

### Code Review is now generally available

Catch more bugs before they reach production.

Claude Code


ArticleOct 8, 2026

### Build live dashboards and animate explainers with Claude 

Claude Dashboards and Claude Motion are now in beta. Docs, Slides, and Design are out of beta and on every Claude plan, including Free.

Claude appsClaude Design

2 more: Claude Cowork and Claude CodeClaude CoworkClaude Code


ArticleOct 7, 2026

### Claude Haiku 5.5

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.

(opens in new tab)[](https://www.anthropic.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)

ArticleOct 6, 2026

### Claude now works with Google Docs, Sheets, and Slides

Teams that run on Google Workspace can now bring Claude into their files or work on their files directly from Claude, with our new add-on and Google Docs, Sheets, and Slides connectors (in beta).

Claude Enterprise
