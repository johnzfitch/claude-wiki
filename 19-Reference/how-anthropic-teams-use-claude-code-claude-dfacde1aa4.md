---
category: "19-Reference"
fetched_at: "2026-03-15T04:10:47Z"
last_modified: "Sat, 14 Mar 2026 03:47:02 GMT"
source_url: "https://www.anthropic.com/news/how-anthropic-teams-use-claude-code"
title: "How Anthropic teams use Claude Code | Claude"
---

# How Anthropic teams use Claude Code

Teams across Anthropic use Claude Code for everything from debugging production issues and navigating unfamiliar codebases to building custom automation tools. Here's how.

[](#)

[](#)

- 

  Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

- 

  Product

  Claude Code

- 

  Date

  July 24, 2025

- 

  Reading time

  5

  min

- 

  Share

  [Copy link](#)
  https://claude.com/blog/how-anthropic-teams-use-claude-code

Agentic coding tools like [Claude Code](https://www.anthropic.com/claude-code) help developers accelerate workflows, automate repetitive tasks, and tackle complex programming projects. As the field evolves, we're learning about new applications everyday from users, including our own employees.

To learn more, we sat down with employees across Anthropic to understand how they use Claude Code at work.

While many of their use cases were predictable—debugging, navigating codebases, managing workflows—others surprised us. Lawyers built phone tree systems. Marketers generated hundreds of ad variations in seconds. Data scientists created complex visualizations without knowing JavaScript.

The pattern became clear: agentic coding isn't just accelerating traditional development. It's dissolving the boundary between technical and non-technical work, turning anyone who can describe a problem into someone who can build a solution.

Here’s what we learned.

### **Codebase navigation and understanding**

Teams across the company use Claude Code to help new hires and even long-time employees get up to speed on our codebases.

New data scientists on our Infrastructure team feed Claude Code their entire codebase to get productive quickly. Claude reads the codebase’s [CLAUDE.md](http://claude.md) files, identifies relevant ones, explains data pipeline dependencies, and shows which upstream sources feed into dashboards, replacing traditional data catalog tools.

Our Product Engineering team refers to Claude Code as their "first stop" for any programming task. They ask it to identify which files to examine for bug fixes, features, or analysis, eliminating the time-consuming process of manually gathering context before building new features.

### **Testing and code review**

Agentic coding tools are particularly popular for their ability to automate two critical but tedious programming tasks: writing unit tests and reviewing code.

The Product Design team uses Claude Code to write comprehensive tests for new features. They've automated Pull Request comments through GitHub Actions, with Claude handling formatting issues and test case refactoring automatically.

The Security Engineering team transformed their workflow from "design doc → janky code → refactor → give up on tests" to asking Claude for pseudocode, guiding it through test-driven development, and checking in periodically. This results in more reliable, testable code.

Agentic coding can also be used to translate tests into other programming languages. For instance, when the Inference team needs to test functionality in unfamiliar languages like Rust, they explain what they want to test and Claude writes the logic in the native language of the codebase.

### **Debugging and troubleshooting**

Production issues demand quick resolution, but trying to reason about unfamiliar code under pressure often leads to delays. For many teams at the company, Claude Code accelerates diagnosis and fixes by analyzing stack traces, documentation, and system behavior in real-time.

During incidents, the Security Engineering team feeds Claude Code stack traces and documentation to trace control flow through the codebase. Problems that typically take 10-15 minutes of manual scanning now resolve 3x as quickly.

With Claude Code, the Product Engineering team gained confidence to tackle bugs in unfamiliar codebases. They ask Claude: "Can you fix this bug? This is the behavior I'm seeing" and review the proposed solution without needing to rely on other engineering teams for assistance.

In one instance, when Kubernetes clusters stopped scheduling pods, the Data Infrastructure team used Claude Code to diagnose the issue. They fed it dashboard screenshots, and Claude guided them menu-by-menu through Google Cloud's UI until they found pod IP address exhaustion. Claude then provided the exact commands to create a new IP pool and add it to the cluster, saving them 20 minutes of valuable time during a system outage.

### **Prototyping and feature development**

Building new features traditionally requires deep technical knowledge and significant time investment. Claude Code enables rapid prototyping and even full application development, letting teams validate ideas quickly regardless of their programming expertise.

Members of the Product Design team would feed Figma design files to Claude Code and then set up autonomous loops where Claude Code writes the code for the new feature, runs tests, and iterates continuously. They give Claude abstract problems, let it work autonomously, then review solutions before final refinements. In one case, they had Claude build Vim key bindings for itself with minimal human review.

With Claude Code, the Product Design team discovered an unexpected use: mapping out error states, logic flows, and system statuses to identify edge cases during design rather than discovering them in development. This fundamentally improves their initial design quality and saves them hours of debugging later on.

Despite not being fluent in TypeScript, data scientists use Claude Code to build entire React applications for visualizing RL model performance. After one-shot prompting in a sandbox environment, the tool writes entire TypeScript visualizations from scratch without understanding the code themselves. Given the simplicity of the task, if the first prompt isn’t sufficient, they’ll make slight tweaks and try again.

### **Documentation and knowledge management**

Technical documentation often sits scattered across wikis, code comments, and team members' heads. Claude Code consolidates this knowledge via MCP and CLAUDE.md files into accessible formats, making expertise available to everyone who needs it.

Inference team members without ML backgrounds depend on Claude to explain model-specific functions. What normally requires an hour of Google searching now takes 10-20 minutes—an 80% reduction in research time.

The Security Engineering team has Claude ingest multiple documentation sources to create markdown runbooks and troubleshooting guides. These condensed documents become context for debugging real production issues, which is often more efficient than searching through full knowledge bases.

### **Automation and workflow optimization**

Agentic coding tools help teams build custom automation that would traditionally require dedicated developer resources or expensive software.

The Growth Marketing team built an agentic workflow that processes CSV files with hundreds of ads, identifies underperformers, and generates new variations within strict character limits. Using two specialized sub-agents, the system generates hundreds of new ads in minutes instead of hours.

They also developed a Figma plugin that identifies frames and programmatically generates up to 100 ad variations by swapping headlines and descriptions, reducing hours of copy-pasting to half a second per batch of ads.

In a particularly unique use case, the Legal team created prototype "phone tree" systems to help team members connect with the right lawyer at Anthropic, demonstrating how departments can build custom tools without traditional development resources.

### **Unlocking new possibilities with Claude Code**

These stories reveal a pattern: Claude Code works best when you focus on the human workflows that it can augment. The most successful teams treat Claude Code as a thought partner rather than a code generator.

They explore possibilities, prototype rapidly, and share discoveries across technical and non-technical users. This collaborative approach between humans and AI creates opportunities we're only beginning to understand.

No items found.

[Prev](#)

Prev

0/5

[Next](#)

Next

eBook

## Building trusted AI in the enterprise

Anthropic’s guide to starting, scaling, and succeeding based on real-world examples and best practices

Download now

[Download now](https://assets.anthropic.com/m/66daaa23018ab0fd/original/Anthropic-enterprise-ebook-digital.pdf)

Download now

FAQ

No items found.

Get started with Claude Code.

Learn more.

[Learn more.](#)

Learn more.

## Related posts

Explore more product news and best practices for teams building with Claude.

Mar 13, 2026

### 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Product announcements

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](#)

1M context is now generally available for Opus 4.6 and Sonnet 4.6

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](/blog/1m-context-ga)

1M context is now generally available for Opus 4.6 and Sonnet 4.6

Mar 11, 2026

### Advancing Claude for Excel and PowerPoint

Enterprise AI

[Advancing Claude for Excel and PowerPoint](#)

Advancing Claude for Excel and PowerPoint

[Advancing Claude for Excel and PowerPoint](/blog/claude-excel-powerpoint-updates)

Advancing Claude for Excel and PowerPoint

Feb 24, 2026

### Cowork and plugins for finance

Enterprise AI

[Cowork and plugins for finance ](#)

Cowork and plugins for finance

[Cowork and plugins for finance ](/blog/cowork-plugins-finance)

Cowork and plugins for finance

Feb 24, 2026

### Cowork and plugins for teams across the enterprise

Agents

[Cowork and plugins for teams across the enterprise](#)

Cowork and plugins for teams across the enterprise

[Cowork and plugins for teams across the enterprise](/blog/cowork-plugins-across-enterprise)

Cowork and plugins for teams across the enterprise

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
