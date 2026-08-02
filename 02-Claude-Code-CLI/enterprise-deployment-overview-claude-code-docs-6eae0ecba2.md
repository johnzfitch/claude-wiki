---
title: "Enterprise deployment overview - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/third-party-integrations"
category: "02-Claude-Code-CLI"
fetched_at: "2026-08-02T05:36:32Z"
tags: ["claude-code", "enterprise"]
---

## On this page

- [Compare deployment options](#compare-deployment-options)
- [Configure proxies and gateways](#configure-proxies-and-gateways)
  - [Amazon Bedrock](#amazon-bedrock)
  - [Microsoft Foundry](#microsoft-foundry)
  - [Google Cloud’s Agent Platform](#google-cloud%E2%80%99s-agent-platform)
- [Best practices for organizations](#best-practices-for-organizations)
  - [Invest in documentation and memory](#invest-in-documentation-and-memory)
  - [Simplify deployment](#simplify-deployment)
  - [Start with guided usage](#start-with-guided-usage)
  - [Pin model versions for cloud providers](#pin-model-versions-for-cloud-providers)
  - [Configure security policies](#configure-security-policies)
  - [Leverage MCP for integrations](#leverage-mcp-for-integrations)
- [Next steps](#next-steps)

Deployment

# Enterprise deployment overview

Copy pageCopy page

Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.

Copy pageCopy page

Organizations can deploy Claude Code through Anthropic directly or through a cloud provider. This page helps you choose the right configuration.


[​](#compare-deployment-options)

Compare deployment options

For most organizations, Claude for Teams or Claude for Enterprise provides the best experience. Team members get access to both Claude Code and Claude on the web with a single subscription, centralized billing, and no infrastructure setup required. **Claude for Teams** is self-service and includes collaboration features, admin tools, and billing management. Best for smaller teams that need to get started quickly. **Claude for Enterprise** adds SSO and domain capture, role-based permissions, compliance API access, and managed policy settings for deploying organization-wide Claude Code configurations. Best for larger organizations with security and compliance requirements. Learn more about [Team plans](https://support.claude.com/en/articles/9266767-what-is-the-team-plan) and [Enterprise plans](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan). If your organization has specific infrastructure requirements, compare the options below:

[TABLE]

For a feature-by-feature breakdown of what’s available on each option, see [Feature availability](/docs/en/feature-availability). Select a deployment option to view setup instructions:

- [Claude for Teams or Enterprise](/docs/en/authentication#claude-for-teams-or-enterprise)
- [Anthropic Console](/docs/en/authentication#claude-console-authentication)
- [Claude apps gateway](/docs/en/claude-apps-gateway), a self-hosted gateway that adds IdP sign-in in front of Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, Microsoft Foundry, or the Anthropic API
- [Amazon Bedrock](/docs/en/amazon-bedrock)
- [Claude Platform on AWS](/docs/en/claude-platform-on-aws)
- [Google Cloud’s Agent Platform](/docs/en/google-vertex-ai)
- [Microsoft Foundry](/docs/en/microsoft-foundry)

For Amazon Bedrock and Google Vertex AI, you can also run `claude` and select **3rd-party platform** at the login prompt to launch an interactive setup wizard.


[​](#configure-proxies-and-gateways)

Configure proxies and gateways

Most organizations can use a cloud provider directly without additional configuration. However, you may need to configure a corporate proxy or LLM gateway if your organization has specific network or management requirements. These are different configurations that can be used together:

- **Corporate proxy**: Routes traffic through an HTTP/HTTPS proxy. Use this if your organization requires all outbound traffic to pass through a proxy server for security monitoring, compliance, or network policy enforcement. Configure with the `HTTPS_PROXY` or `HTTP_PROXY` environment variables. Learn more in [Enterprise network configuration](/docs/en/network-config).
- **LLM Gateway**: A service that sits between Claude Code and the cloud provider to handle authentication and routing. Use this if you need centralized usage tracking across teams, custom rate limiting or budgets, or centralized authentication management. Configure with the `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_AWS_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, or `ANTHROPIC_FOUNDRY_BASE_URL` environment variables. Learn more in [LLM gateways](/docs/en/llm-gateway).

The following examples show the environment variables to set in your shell or shell profile (`.bashrc`, `.zshrc`). See [Settings](/docs/en/settings) for other configuration methods.


[​](#amazon-bedrock)

Amazon Bedrock

- Corporate proxy

- LLM Gateway

Route Amazon Bedrock traffic through your corporate proxy by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Amazon Bedrock traffic through your LLM gateway by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Bedrock
export CLAUDE_CODE_USE_BEDROCK=1

# Configure LLM gateway
export ANTHROPIC_BEDROCK_BASE_URL='https://your-llm-gateway.com/bedrock'
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1  # If gateway handles AWS auth
```


[​](#microsoft-foundry)

Microsoft Foundry

- Corporate proxy

- LLM Gateway

Route Microsoft Foundry traffic through your corporate proxy by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1
export ANTHROPIC_FOUNDRY_RESOURCE=your-resource
export ANTHROPIC_FOUNDRY_API_KEY=your-api-key  # Or omit for Entra ID auth

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Microsoft Foundry traffic through your LLM gateway by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Microsoft Foundry
export CLAUDE_CODE_USE_FOUNDRY=1

# Configure LLM gateway
export ANTHROPIC_FOUNDRY_BASE_URL='https://your-llm-gateway.com'
export ANTHROPIC_FOUNDRY_API_KEY=your-gateway-key  # Sent as x-api-key
```


[​](#google-cloud’s-agent-platform)

Google Cloud’s Agent Platform

- Corporate proxy

- LLM Gateway

Route Google Cloud’s Agent Platform traffic through your corporate proxy by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Agent Platform
export CLAUDE_CODE_USE_VERTEX=1
export CLOUD_ML_REGION=us-east5
export ANTHROPIC_VERTEX_PROJECT_ID=your-project-id

# Configure corporate proxy
export HTTPS_PROXY='https://proxy.example.com:8080'
```

Route Google Cloud’s Agent Platform traffic through your LLM gateway by setting the following [environment variables](/docs/en/env-vars):

```python
# Enable Agent Platform
export CLAUDE_CODE_USE_VERTEX=1

# Configure LLM gateway
export ANTHROPIC_VERTEX_BASE_URL='https://your-llm-gateway.com/vertex'
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1  # If gateway handles GCP auth
export ANTHROPIC_VERTEX_PROJECT_ID=your-gcp-project-id
export CLOUD_ML_REGION=us-east5
```

Use `/status` in Claude Code to verify your proxy and gateway configuration is applied correctly. For example, with the Bedrock gateway configuration above, the output includes lines like:

```python
API provider: Amazon Bedrock
Bedrock base URL: https://your-llm-gateway.com/bedrock
AWS region: us-east-1
AWS auth skipped
```

If you configured a corporate proxy, `/status` also shows a `Proxy` line with your proxy URL.


[​](#best-practices-for-organizations)

Best practices for organizations


[​](#invest-in-documentation-and-memory)

Invest in documentation and memory

We strongly recommend investing in documentation so that Claude Code understands your codebase. Organizations can deploy CLAUDE.md files at multiple levels:

- **Organization-wide**: Deploy to system directories such as `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux and WSL), or `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows) for company-wide standards
- **Repository-level**: Create `CLAUDE.md` files in repository roots containing project architecture, build commands, and contribution guidelines. Check these into source control so all users benefit

Learn more in [Memory and CLAUDE.md files](/docs/en/memory).


[​](#simplify-deployment)

Simplify deployment

If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.


[​](#start-with-guided-usage)

Start with guided usage

Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.


[​](#pin-model-versions-for-cloud-providers)

Pin model versions for cloud providers

If you deploy through [Amazon Bedrock](/docs/en/amazon-bedrock), [Google Cloud’s Agent Platform](/docs/en/google-vertex-ai), [Microsoft Foundry](/docs/en/microsoft-foundry), or [Claude Platform on AWS](/docs/en/claude-platform-on-aws), pin specific model versions using `ANTHROPIC_DEFAULT_FABLE_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL`. Without pinning, model aliases resolve to Claude Code’s built-in default for that provider, which can lag the newest release and may not yet be enabled in your account. Pinning lets you control when your users move to a new model. See [Model configuration](/docs/en/model-config#pin-models-for-third-party-deployments) for what each provider does when the default is unavailable.


[​](#configure-security-policies)

Configure security policies

Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration. [Learn more](/docs/en/security).


[​](#leverage-mcp-for-integrations)

Leverage MCP for integrations

MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit. [Learn more](/docs/en/mcp). At Anthropic, we trust Claude Code to power development across every Anthropic codebase. We hope you enjoy using Claude Code as much as we do.


[​](#next-steps)

Next steps

Once you’ve chosen a deployment option and configured access for your team:

1.  **Roll out to your team**: Share installation instructions and have team members [install Claude Code](/docs/en/setup) and authenticate with their credentials.
2.  **Set up shared configuration**: Create a [CLAUDE.md file](/docs/en/memory) in your repositories to help Claude Code understand your codebase and coding standards.
3.  **Configure permissions**: Review [security settings](/docs/en/security) to define what Claude Code can and cannot do in your environment.
