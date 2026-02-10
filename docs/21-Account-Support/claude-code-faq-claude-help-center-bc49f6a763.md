---
category: "21-Account-Support"
fetched_at: "2026-02-08T20:51:53Z"
source_url: "https://support.claude.com/en/articles/12386420-claude-code-faq"
title: "Claude Code FAQ | Claude Help Center"
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

[](#h_cf672dfd7f)

[](#h_37f0e89126)

[](#h_dafdd89f9b)

[](#h_0d201f8904)

[](#h_ae9534d5f8)

[](#h_df28f8adcd)

[](#h_4349b0c230)

[](#h_6fd7d6ab56)

[](#h_322575549c)

[](#h_4792f8e35d)

[](#h_1d194be4a7)

[](#h_bdceb9f4cc)

[](#h_f756bbf783)

[](#h_ee668e1c76)

[](#h_a06e0e4a8e)

[](#h_003fb44ed5)

[](#h_1dd9345bcc)

[](#h_8c70bdf68f)

[](#h_7b6bb96ea7)

[](#h_093f1d96f5)

[All Collections](/en/)

[Claude Code](https://support.claude.com/en/collections/14445694-claude-code)

Claude Code FAQ

# Claude Code FAQ

Updated yesterday

Table of contents

[](#h_cf672dfd7f)

[](#h_37f0e89126)

[](#h_dafdd89f9b)

[](#h_0d201f8904)

[](#h_ae9534d5f8)

[](#h_df28f8adcd)

[](#h_4349b0c230)

[](#h_6fd7d6ab56)

[](#h_322575549c)

[](#h_4792f8e35d)

[](#h_1d194be4a7)

[](#h_bdceb9f4cc)

[](#h_f756bbf783)

[](#h_ee668e1c76)

[](#h_a06e0e4a8e)

[](#h_003fb44ed5)

[](#h_1dd9345bcc)

[](#h_8c70bdf68f)

[](#h_7b6bb96ea7)

[](#h_093f1d96f5)

This article is a compilation of commonly-asked questions about Claude Code related to authentication, integrations, configuration, and more. If you're interested in learning more about Claude Code, please refer to our Claude Docs here: [Claude Code overview](https://docs.claude.com/en/docs/claude-code/overview).

## How do I set up single sign-on (SSO) for Claude Code?

If you are setting up single sign-on for a Claude Console organization, we have detailed instructions here: [Setting up Single Sign-On on the Claude Console](https://support.claude.com/en/articles/10280258-setting-up-single-sign-on-on-the-claude-console). If you are using Claude Code with an Enterprise plan, see this article for SSO setup instructions: [Setting up Single Sign-On (SSO) on the Enterprise plan](https://support.claude.com/en/articles/9797544-setting-up-single-sign-on-sso-on-the-enterprise-plan).

## Is there a way to disable Opus model access across our entire organization in Claude Code?

If you are a Claude Console user, this can be configured through rate limiting in your Console organization. If you are using Bedrock or Vertex, set the Opus rate limit to 0 in your Vertex/Bedrock project settings. Note that even if disabled in Vertex, users may be able to switch models in Claude Code, so rate limiting is the most effective approach.

## Does Claude Code support Microsoft Visual Studio IDE integration (not VS Code)?

No current Visual Studio 2022 integration exists. Claude Code currently supports VS Code, Cursor (and other VS Code forks), Intellij, Pycharm (and other Jetbrains IDEs).

## How can we implement PR review automation with Claude Code?

While there isn't a turnkey PR reviewer solution yet, you can use the [Claude Code GitHub Actions integration](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code) for automated reviews. For now, you can use the security review action as a template and customize it for general PR reviews. This is also a good use case for the [Claude Code SDK](https://docs.claude.com/en/docs/claude-code/sdk/sdk-overview).

## I’m getting an error message that “Claude Max or Pro is required to connect to Claude Code” but I should have access through my organization’s Team or Enterprise plan. How can I troubleshoot?

This indicates that you selected the wrong login method from the Claude Code setup screen. Try running /login again and selecting the account associated with your primary work email address. If you’re still unable to connect, see [Having trouble using your Team or Enterprise account to access Claude Code?](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan#h_540f9e65d8)

## What data is sent to Anthropic when using Claude Code with Bedrock/Vertex API keys?

When configured with Bedrock/Vertex and CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC is set, only essential telemetry is sent. All model API requests go directly to your Bedrock/Vertex endpoints. Review the [data flow documentation](https://docs.claude.com/en/docs/claude-code/security) for complete details.

## Is there a way to access Claude Code via Bedrock/Vertex without exposing a secret key/access key?

Yes. Our setup guides for [Bedrock](https://docs.claude.com/en/docs/claude-code/amazon-bedrock) and [Vertex](https://docs.claude.com/en/docs/claude-code/google-vertex-ai) show how you can enable this. For example, in the Bedrock case you can run \`aws configure\` to configure the AWS CLI before adding the necessary [configs](https://docs.claude.com/en/docs/claude-code/amazon-bedrock#3-configure-claude-code) and running Claude Code with the Bedrock, or you can use Bedrock API keys, which is a new feature from AWS that enables API keys for Bedrock usage that don’t require full AWS credentials.

## Is the 1M context window available in Claude Code, and will users be warned about higher pricing?

Long context support is currently limited to some Claude Code users on Max 20x plans, so it’s available only to a small number of users. The 1M context window is not generally available for all Claude Code users yet, including those accessing Claude via the API.

## How can we deploy Claude Code with custom environment variables and permissions across our organization?

Create wrapper scripts that set environment variables before running Claude Code. For permissions, use .claude/settings.json files with allow/deny lists. Note that wildcard patterns (\*) don't always match as expected - test permissions thoroughly. Enterprise teams often inject standardized Claude.md files for consistent configurations.

## Does Claude Code have public code filtering or attribution capabilities on the roadmap?

No, public code filtering and attribution capabilities are not currently on the roadmap. Some customers use BlackDuck for code scanning, though feedback on cost and false positives has been mixed. We are aware that this is a blocker for scaling Claude Code to more users and are looking into solutions.

## Are subagents available in Claude Code SDK and GitHub Actions?

Subagents are available via the [Claude Code SDK](https://docs.claude.com/en/docs/claude-code/sdk/sdk-overview). They're not yet integrated into GitHub Actions, but we are considering this. The UX collapses outputs when more than three subagents run in parallel to manage complexity.

## Can subagents be configured to use specific MCP tools?

Yes, when creating a subagent, you can specify which tools it has access to using the \`tools\` field in the configuration. In the subagent configuration file, you can either omit the tools field to inherit all tools from the main thread, or you can specify individual tools as a comma-separated list for more granular control. Learn more about this in our Claude Docs: [Subagents - Available tools](https://docs.claude.com/en/docs/claude-code/sub-agents#available-tools).

## How can we manage Claude Code costs, especially for automated workflows?

For automated workflows like security reviews, switch from Opus to Sonnet using the [claude --model \<alias\|name\> configuration option](https://docs.claude.com/en/docs/claude-code/model-config) for cost savings. You can also monitor usage through your console dashboard and set appropriate rate limits. Note that you can use Workspaces to set more granular spend limits for different user groups. Read more about Workspaces here: [Creating and managing Workspaces in the Claude Console](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console). We also allow you to view spend per API key in the Console. Refer to this article for more information: [Cost and Usage Reporting in the Claude Console](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console).

## Can Claude Code work through corporate proxies like LiteLLM?

Yes, Claude Code supports corporate proxy configurations as long as they support the Anthropic API spec. Follow the proxy setup instructions in our Claude Docs: [Proxy configuration](https://docs.claude.com/en/docs/claude-code/network-config#proxy-configuration). Common issues arise from port restrictions in restricted environments.

## How do we add users to Claude Code when using a Console account?

Add users directly to your Console organization with a Claude Code User or Developer role - that's all that's needed. Users then run /login from within Claude Code and select the intended Console account. Do not try to manually create API keys in the Claude Code workspace.

## Is there team-based memory or knowledge sharing beyond Claude.md files?

Currently, Claude.md files are the primary mechanism. IT teams can inject standardized Claude.md files into every machine's .claude directory for org-wide configurations. More advanced team memory features are being explored but not yet available.

## How do permissions work in Claude Code, and why aren’t my allow lists being respected?

Permissions use pattern matching in .claude/settings.json or settings.local.json. Wildcard syntax can be tricky - "Bash(atlassian-api:\*)" should work but may need exact command matching. Use "Yes, and don't ask again for similar commands" to build up permissions incrementally. Check both global (~/.claude/settings.json) and local settings files.

## Does Claude Code index my entire codebase or use a vector database to store information about my codebase?

No. Claude Code has access to a system prompt and a series of tools that it can use to navigate your codebase on command. For example, if Claude Code needs to understand something about your codebase, it will use a search tool to search through your codebase and read files on command. We find that this is more effective and flexible than full codebase indexing: Claude Code is *really* good at knowing how to sift through a codebase to gather context it needs on the fly!

## Can Claude Code integrate with CI/CD, version control, and observability platforms?

Yes, Claude Code integrates with GitHub Actions for CI/CD, supports git operations, and can connect to various platforms via MCP servers. See our Claude Docs for more information:

- [Claude Code GitHub Actions](https://docs.claude.com/en/docs/claude-code/github-actions)

- [Claude Code GitLab CI/CD](https://docs.claude.com/en/docs/claude-code/gitlab-ci-cd)

## Why am I seeing "Workflow validation failed" errors in GitHub Actions?

This typically occurs with reusable workflows. Check that your workflow syntax is correct and that all required parameters are passed. If the error persists, file an issue here with your workflow configuration: [github.com/anthropics/claude-code-action](http://github.com/anthropics/claude-code-action).

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/7996920-how-do-i-get-access-to-claude-in-amazon-bedrock)

How do I get access to Claude in Amazon Bedrock?

[](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)

Using Claude Code with your Pro or Max plan

[](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)

Automated Security Reviews in Claude Code

[](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)

Claude Code usage analytics

[](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)

Claude Code on the web

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
