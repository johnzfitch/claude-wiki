---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-23T00:45:02Z"
last_modified: "Sat, 21 Feb 2026 19:44:57 GMT"
source_url: "https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills"
title: "Equipping agents for the real world with Agent Skills \\ Anthropic | Claude"
---

# Equipping agents for the real world with Agent Skills

Claude is powerful, but real work requires procedural knowledge and organizational context. Introducing Agent Skills, a new way to build specialized agents using files and folders.

[](#)

[](#)

- 

  Category

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Agents](https://claude.com/blog/category/agents)

- 

  Product

  Claude Code

  Claude Developer Platform

- 

  Date

  October 16, 2025

- 

  Reading time

  5

  min

- 

  Share

  [Copy link](#)
  https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

*Update: We've published* [*Agent Skills*](https://agentskills.io/) *as an open standard for cross-platform portability. (December 18, 2025)*

As model capabilities improve, we can now build general-purpose agents that interact with full-fledged computing environments. [Claude Code](https://claude.com/product/claude-code), for example, can accomplish complex tasks across domains using local code execution and filesystems. But as these agents become more powerful, we need more composable, scalable, and portable ways to equip them with domain-specific expertise.

This led us to create [**Agent Skills**](https://www.anthropic.com/news/skills): organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks. Skills extend Claude’s capabilities by packaging your expertise into composable resources for Claude, transforming general-purpose agents into specialized agents that fit your needs.

Building a skill for an agent is like putting together an onboarding guide for a new hire. Instead of building fragmented, custom-designed agents for each use case, anyone can now specialize their agents with composable capabilities by capturing and sharing their procedural knowledge. In this article, we explain what Skills are, show how they work, and share best practices for building your own.

## The anatomy of a skill

To see Skills in action, let’s walk through a real example: one of the skills that powers [Claude’s recently launched document editing abilities](https://www.anthropic.com/news/create-files). Claude already knows a lot about understanding PDFs, but is limited in its ability to manipulate them directly (e.g. to fill out a form). This [PDF skill](https://github.com/anthropics/skills/tree/main/document-skills/pdf) lets us give Claude these new abilities.

At its simplest, a skill is a directory that contains a `SKILL.md file`. This file must start with YAML frontmatter that contains some required metadata: `name` and `description`. At startup, the agent pre-loads the `name` and `description` of every installed skill into its system prompt.

This metadata is the **first level** of *progressive disclosure*: it provides just enough information for Claude to know when each skill should be used without loading all of it into context. The actual body of this file is the **second level** of detail. If Claude thinks the skill is relevant to the current task, it will load the skill by reading its full `SKILL.md` into context.

As skills grow in complexity, they may contain too much context to fit into a single `SKILL.md`, or context that’s relevant only in specific scenarios. In these cases, skills can bundle additional files within the skill directory and reference them by name from `SKILL.md`. These additional linked files are the **third level** (and beyond) of detail, which Claude can choose to navigate and discover only as needed.

In the PDF skill shown below, the `SKILL.md` refers to two additional files (`reference.md` and `forms.md`) that the skill author chooses to bundle alongside the core `SKILL.md`. By moving the form-filling instructions to a separate file (`forms.md`), the skill author is able to keep the core of the skill lean, trusting that Claude will read `forms.md` only when filling out a form.

Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed:

Agents with a filesystem and code execution tools don’t need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded.

### Skills and the context window

The following diagram shows how the context window changes when a skill is triggered by a user’s message.

The sequence of operations shown:

1.  To start, the context window has the core system prompt and the metadata for each of the installed skills, along with the user’s initial message;
2.  Claude triggers the PDF skill by invoking a Bash tool to read the contents of `pdf/SKILL.md`;
3.  Claude chooses to read the `forms.md` file bundled with the skill;
4.  Finally, Claude proceeds with the user’s task now that it has loaded relevant instructions from the PDF skill.

### Skills and code execution

Skills can also include code for Claude to execute as tools at its discretion.

Large language models excel at many tasks, but certain operations are better suited for traditional code execution. For example, sorting a list via token generation is far more expensive than simply running a sorting algorithm. Beyond efficiency concerns, many applications require the deterministic reliability that only code can provide.

In our example, the PDF skill includes a pre-written Python script that reads a PDF and extracts all form fields. Claude can run this script without loading either the script or the PDF into context. And because code is deterministic, this workflow is consistent and repeatable.

## Developing and evaluating skills

Here are some helpful guidelines for getting started with authoring and testing skills:

- **Start with evaluation:** Identify specific gaps in your agents’ capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.
- **Structure for scale:** When the `SKILL.md` file becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage. Finally, code can serve as both executable tools and as documentation. It should be clear whether Claude should run scripts directly or read them into context as reference.
- **Think from Claude’s perspective:** Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts. Pay special attention to the `name` and `description` of your skill. Claude will use these when deciding whether to trigger the skill in response to its current task.
- **Iterate with Claude:** As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

### Security considerations when using Skills

Skills provide Claude with new capabilities through instructions and code. While this makes them powerful, it also means that malicious skills may introduce vulnerabilities in the environment where they’re used or direct Claude to exfiltrate data and take unintended actions.

We recommend installing skills only from trusted sources. When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

## The future of Skills

Agent Skills are [supported today](https://www.anthropic.com/news/skills) across [Claude.ai](http://claude.ai/redirect/website.v1.bdb29daa-1a07-41ec-87f6-579dc33634bd), Claude Code, the Claude Agent SDK, and the Claude Developer Platform.

In the coming weeks, we’ll continue to add features that support the full lifecycle of creating, editing, discovering, sharing, and using Skills. We’re especially excited about the opportunity for Skills to help organizations and individuals share their context and workflows with Claude. We’ll also explore how Skills can complement [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) servers by teaching agents more complex workflows that involve external tools and software.

Looking further ahead, we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.

Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and give them new capabilities.

We’re excited to see what people build with Skills. Get started today by checking out our Skills [docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) and [cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills).

## Acknowledgements

Written by Barry Zhang, Keith Lazuka, and Mahesh Murag, who all really like folders. Special thanks to the many others across Anthropic who championed, supported, and built Skills.

No items found.

[Prev](#)

Prev

0/5

[Next](#)

Next

eBook

## 

[](#)

FAQ

No items found.

[](#)

Get Claude Code

- [](https://claude.ai/code)
  On the web
- [](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
  VS Code
- [](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
  JetBrains
- [](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)
  Slack

curl -fsSL https://claude.ai/install.sh \| bash

Copy command to clipboard

irm https://claude.ai/install.ps1 \| iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)

Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)

Developer docs

## Related posts

Explore more product news and best practices for teams building with Claude.

Feb 20, 2026

### Bringing automated preview, review, and merge to Claude Code on desktop

Claude Code

[Bringing automated preview, review, and merge to Claude Code on desktop](#)

Bringing automated preview, review, and merge to Claude Code on desktop

[Bringing automated preview, review, and merge to Claude Code on desktop](/blog/preview-review-and-merge-with-claude-code)

Bringing automated preview, review, and merge to Claude Code on desktop

Jan 12, 2026

### Cowork: Claude Code for the rest of your work

Product announcements

[Cowork: Claude Code for the rest of your work](#)

Cowork: Claude Code for the rest of your work

[Cowork: Claude Code for the rest of your work](/blog/cowork-research-preview)

Cowork: Claude Code for the rest of your work

Jan 23, 2026

### Building multi-agent systems: When and how to use them

Agents

[Building multi-agent systems: When and how to use them](#)

Building multi-agent systems: When and how to use them

[Building multi-agent systems: When and how to use them](/blog/building-multi-agent-systems-when-and-how-to-use-them)

Building multi-agent systems: When and how to use them

Nov 17, 2025

### How three YC startups built their companies with Claude Code

Claude Code

[How three YC startups built their companies with Claude Code](#)

How three YC startups built their companies with Claude Code

[How three YC startups built their companies with Claude Code](/blog/building-companies-with-claude-code)

How three YC startups built their companies with Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)

See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)

Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

[Subscribe](#)

Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
