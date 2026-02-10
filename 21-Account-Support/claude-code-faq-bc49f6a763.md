---
category: "21-Account-Support"
source_url: "https://support.claude.com/en/articles/12386420-claude-code-faq"
---


This article is a compilation of commonly-asked questions about Claude Code related to authentication, integrations, configuration, and more. If you're interested in learning more about Claude Code, please refer to our Claude Docs here: Claude Code overview.

 

How do I set up single sign-on (SSO) for Claude Code?

If you are setting up single sign-on for a Claude Console organization, we have detailed instructions here: Setting up Single Sign-On on the Claude Console. If you are using Claude Code with an Enterprise plan, see this article for SSO setup instructions: Setting up Single Sign-On (SSO) on the Enterprise plan.

 

Is there a way to disable Opus model access across our entire organization in Claude Code?

If you are a Claude Console user, this can be configured through rate limiting in your Console organization. If you are using Bedrock or Vertex, set the Opus rate limit to 0 in your Vertex/Bedrock project settings. Note that even if disabled in Vertex, users may be able to switch models in Claude Code, so rate limiting is the most effective approach.

 

Does Claude Code support Microsoft Visual Studio IDE integration (not VS Code)?

No current Visual Studio 2022 integration exists. Claude Code currently supports VS Code, Cursor (and other VS Code forks), Intellij, Pycharm (and other Jetbrains IDEs).

 

How can we implement PR review automation with Claude Code?

While there isn't a turnkey PR reviewer solution yet, you can use the Claude Code GitHub Actions integration for automated reviews. For now, you can use the security review action as a template and customize it for general PR reviews. This is also a good use case for the Claude Code SDK.

 

I’m getting an error message that “Claude Max or Pro is required to connect to Claude Code” but I should have access through my organization’s Team or Enterprise plan. How can I troubleshoot?

This indicates that you selected the wrong login method from the Claude Code setup screen. Try running /login again and selecting the account associated with your primary work email address. If you’re still unable to connect, see Having trouble using your Team or Enterprise account to access Claude Code?

 

What data is sent to Anthropic when using Claude Code with Bedrock/Vertex API keys?

When configured with Bedrock/Vertex and CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC is set, only essential telemetry is sent. All model API requests go directly to your Bedrock/Vertex endpoints. Review the data flow documentation for complete details.

 

Is there a way to access Claude Code via Bedrock/Vertex without exposing a secret key/access key?

Yes. Our setup guides for Bedrock and Vertex show how you can enable this. For example, in the Bedrock case you can run `aws configure` to configure the AWS CLI before adding the necessary configs and running Claude Code with the Bedrock, or you can use Bedrock API keys, which is a new feature from AWS that enables API keys for Bedrock usage that don’t require full AWS credentials.

 

Is the 1M context window available in Claude Code, and will users be warned about higher pricing?

Long context support is currently limited to some Claude Code users on Max 20x plans, so it’s available only to a small number of users. The 1M context window is not generally available for all Claude Code users yet, including those accessing Claude via the API.

 

How can we deploy Claude Code with custom environment variables and permissions across our organization?

Create wrapper scripts that set environment variables before running Claude Code. For permissions, use .claude/settings.json files with allow/deny lists. Note that wildcard patterns (*) don't always match as expected - test permissions thoroughly. Enterprise teams often inject standardized Claude.md files for consistent configurations.

 

Does Claude Code have public code filtering or attribution capabilities on the roadmap?

No, public code filtering and attribution capabilities are not currently on the roadmap. Some customers use BlackDuck for code scanning, though feedback on cost and false positives has been mixed. We are aware that this is a blocker for scaling Claude Code to more users and are looking into solutions.

 

Are subagents available in Claude Code SDK and GitHub Actions? 

Subagents are available via the Claude Code SDK. They're not yet integrated into GitHub Actions, but we are considering this. The UX collapses outputs when more than three subagents run in parallel to manage complexity.

 

Can subagents be configured to use specific MCP tools?

Yes, when creating a subagent, you can specify which tools it has access to using the `tools` field in the configuration. In the subagent configuration file, you can either omit the tools field to inherit all tools from the main thread, or you can specify individual tools as a comma-separated list for more granular control. Learn more about this in our Claude Docs: Subagents - Available tools.

 

How can we manage Claude Code costs, especially for automated workflows?

For automated workflows like security reviews, switch from Opus to Sonnet using the claude --model <alias|name> configuration option for cost savings. You can also monitor usage through your console dashboard and set appropriate rate limits. Note that you can use Workspaces to set more granular spend limits for different user groups. Read more about Workspaces here: Creating and managing Workspaces in the Claude Console. We also allow you to view spend per API key in the Console. Refer to this article for more information: Cost and Usage Reporting in the Claude Console.

 

Can Claude Code work through corporate proxies like LiteLLM? 

Yes, Claude Code supports corporate proxy configurations as long as they support the Anthropic API spec. Follow the proxy setup instructions in our Claude Docs: Proxy configuration. Common issues arise from port restrictions in restricted environments.

 

How do we add users to Claude Code when using a Console account?

Add users directly to your Console organization with a Claude Code User or Developer role - that's all that's needed. Users then run /login from within Claude Code and select the intended Console account. Do not try to manually create API keys in the Claude Code workspace.

 

Is there team-based memory or knowledge sharing beyond Claude.md files?

Currently, Claude.md files are the primary mechanism. IT teams can inject standardized Claude.md files into every machine's .claude directory for org-wide configurations. More advanced team memory features are being explored but not yet available.

 

How do permissions work in Claude Code, and why aren’t my allow lists being respected?

Permissions use pattern matching in .claude/settings.json or settings.local.json. Wildcard syntax can be tricky - "Bash(atlassian-api:*)" should work but may need exact command matching. Use "Yes, and don't ask again for similar commands" to build up permissions incrementally. Check both global (~/.claude/settings.json) and local settings files.

 

Does Claude Code index my entire codebase or use a vector database to store information about my codebase?

No. Claude Code has access to a system prompt and a series of tools that it can use to navigate your codebase on command. For example, if Claude Code needs to understand something about your codebase, it will use a search tool to search through your codebase and read files on command. We find that this is more effective and flexible than full codebase indexing: Claude Code is really good at knowing how to sift through a codebase to gather context it needs on the fly!

 

Can Claude Code integrate with CI/CD, version control, and observability platforms?

Yes, Claude Code integrates with GitHub Actions for CI/CD, supports git operations, and can connect to various platforms via MCP servers. See our Claude Docs for more information:

Claude Code GitHub Actions

Claude Code GitLab CI/CD

Why am I seeing "Workflow validation failed" errors in GitHub Actions?

This typically occurs with reusable workflows. Check that your workflow syntax is correct and that all required parameters are passed. If the error persists, file an issue here with your workflow configuration: github.com/anthropics/claude-code-action.

Related Articles
How do I get access to Claude in Amazon Bedrock?
Using Claude Code with your Pro or Max plan
Automated Security Reviews in Claude Code
Claude Code usage analytics
Claude Code on the web