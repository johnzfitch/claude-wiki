---
title: "Apple’s Xcode now supports the Claude Agent SDK \\ Anthropic"
source_url: "https://www.anthropic.com/news/apple-xcode-claude-agent-sdk"
category: "19-Reference"
fetched_at: "2026-09-10T06:46:08Z"
tags: ["agents", "sdk"]
---

# Apple’s Xcode now supports the Claude Agent SDK

Feb 3, 2026

Apple's Xcode is where developers build, test, and distribute apps for Apple platforms, including iPhone, iPad, Mac, Apple Watch, Apple Vision Pro, and Apple TV.

In September, [we announced](https://www.anthropic.com/news/claude-in-xcode) that developers would have access to Claude Sonnet 4 in Xcode 26. Claude could be used to write code, debug, and generate documentation—but it was limited to helping with individual, turn-by-turn requests.

Now, Xcode 26.3 introduces a native integration with the [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview), the same underlying harness that powers Claude Code. Developers get the full power of Claude Code directly in Xcode—including subagents, background tasks, and plugins—all without leaving the IDE.

## **Using Claude for long-running, autonomous work in Xcode**

With the Claude Agent SDK, Claude can now work autonomously on much more sophisticated, long-running coding tasks inside Xcode. Specifically, this integration supports:

- **Visual verification with Previews.** With the new integration, Claude can capture Xcode Previews to see what the interface it’s building looks like in practice, identify any issues with what it sees, and iterate from there. This is particularly useful when building SwiftUI views, where the visual output is the thing that matters most. Claude can close the loop on its own implementation, allowing it to build higher-quality interfaces that are much closer to developers’ design intent on the first try.
- **Reasoning across projects.** Building for Apple platforms means working with a wide range of frameworks and technologies, like SwiftUI, UIKit, Swift Data, and many more. Claude can explore a project's full file structure, understand how these pieces connect, and identify where changes need to be made before it starts writing code. When given a task, it works with an understanding of the whole app and its architecture – not just whichever file is currently open.
- **Autonomous task execution.** Claude can be given a *goal*, rather than a set of specific instructions. It’ll then break the task down itself, decide which files to modify, make the changes, and iterate if something doesn't work. When Claude needs to understand how an Apple API works, or how a specific framework is meant to be used, it can search Apple's documentation directly. And it can update the project as needed and continue until the task is complete or it needs a user’s input—a meaningful time saver for developers who are often working alone or on small teams.
- **Interface through the Model Context Protocol.** In addition to accessing Claude Agent directly within the IDE, Xcode 26.3 also makes its capabilities available through the Model Context Protocol. Developers using Claude Code can integrate with Xcode over MCP and capture visual Previews without leaving the CLI.

## **Availability**

Xcode 26.3 is available as a release candidate for all members of the Apple Developer Program starting today, with a release coming soon on Apple’s App Store. See Apple’s announcement [here for more](https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/).


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](/news/enterprise-frontier-safeguards)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](/news/improving-alignment-security-efforts)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](/news/model-hardware-standard-research-preview)

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Commerce](https://claude.com/solutions/commerce)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](https://academy.claude.com)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Scientists](https://claude.com/programs/team-plan-for-scientists)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Leadership](/company/leadership)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
