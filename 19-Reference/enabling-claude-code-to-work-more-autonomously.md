---
title: "Enabling Claude Code to work more autonomously \\ Anthropic"
source_url: "https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:32Z"
tags: ["claude-code", "news-research"]
---

# Enabling Claude Code to work more autonomously

Sep 29, 2025

We’re introducing several upgrades to [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md): a native VS Code extension, version 2.0 of our terminal interface, and checkpoints for autonomous operation. Powered by [Sonnet 4.5](claude-sonnet-4-5.md), Claude Code now handles longer, more complex development tasks in your terminal and IDE.

## Claude Code on more surfaces

**VS Code extension**

We’re introducing a [native VS Code extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) in beta that brings Claude Code directly into your IDE. You can now see Claude’s changes in real-time through a dedicated sidebar panel with inline diffs. The extension provides a richer, graphical Claude Code experience for users who prefer to work in IDEs over terminals.

**Enhanced terminal experience**

We’ve also refreshed Claude Code’s terminal interface. The updated interface features improved status visibility and searchable prompt history (Ctrl+r), making it easier to reuse or edit previous prompts.

**Claude Agent SDK**

For teams who want to create custom agentic experiences, the Claude Agent SDK (formerly the Claude Code SDK) gives access to the same core tools, context management systems, and permissions frameworks that power Claude Code. We’ve also released SDK support for subagents and hooks, making it more customizable for building agents for your specific workflows.

Developers are [already building agents](https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) for a broad range use cases with the SDK, including financial compliance agents, cybersecurity agents, and code debugging agents.

## Execute long-running tasks with confidence

As Claude Code takes on increasingly complex tasks, we're releasing a checkpointing feature to help delegate tasks to Claude Code with confidence while maintaining control. Combined with recent feature releases, Claude Code is now more capable of handling sophisticated tasks.

**Checkpoints**

Complex development often involves exploration and iteration. Our new checkpoint system automatically saves your code state before each change, and you can instantly rewind to previous versions by tapping Esc twice or using the /rewind command. Checkpoints let you pursue more ambitious and wide-scale tasks knowing you can always return to a prior code state.

When you rewind to a checkpoint, you can choose to restore the code, the conversation, or both to the prior state. Checkpoints apply to Claude’s edits and not user edits or bash commands, and we recommend using them in combination with version control.

**Subagents, hooks, and background tasks**

Checkpoints are especially useful when combined with Claude Code’s latest features that power autonomous work:

- **Subagents** delegate specialized tasks—like spinning up a backend API while the main agent builds the frontend—allowing parallel development workflows
- **Hooks** automatically trigger actions at specific points, such as running your test suite after code changes or linting before commits
- **Background** **tasks** keep long-running processes like dev servers active without blocking Claude Code’s progress on other work

Together, these capabilities let you confidently delegate broad tasks like extensive refactors or feature exploration to Claude Code.

## Getting started

These updates are available now for Claude Code users.

- **Claude Sonnet 4.5** is the new default model in Claude Code. Run /model to switch models
- **VS Code extension** (beta)**:** Download from the [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) to get started
- **Terminal updates**, including the visual refresh and checkpoints, are available to all Claude Code users—just update your local installation
- **Claude Agent SDK:** [See the docs](https://docs.claude.com/en/api/agent-sdk/overview) to get started


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](investigating-incidents-cybersecurity-evals.md)

### Our position on open-weights models

[Read more](position-open-weights-models.md)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](cognizant-anthropic.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://www.anthropic.com/learn)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
