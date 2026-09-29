---
title: "Enterprise deployment overview - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/third-party-integrations"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-22T06:30:24Z"
tags: ["claude-code", "enterprise"]
---

## On this page

- [Compare deployment options](#compare-deployment-options)
- [Configure proxies and gateways](#configure-proxies-and-gateways)
- [Best practices for organizations](#best-practices-for-organizations)
  - [Invest in documentation and memory](#invest-in-documentation-and-memory)
  - [Simplify deployment](#simplify-deployment)
  - [Start with guided usage](#start-with-guided-usage)
  - [Pin model versions for cloud providers](#pin-model-versions-for-cloud-providers)
  - [Configure security policies](#configure-security-policies)
  - [Use MCP for integrations](#leverage-mcp-for-integrations)
- [Next steps](#next-steps)

Deployment

# Enterprise deployment overview

Copy pageCopy page

Learn how Claude Code can integrate with various third-party services and infrastructure to meet enterprise deployment requirements.

Copy pageCopy page

Organizations can deploy Claude Code through Anthropic directly or through a cloud provider. This page helps you choose the right configuration.


[​](#compare-deployment-options)

Compare deployment options

For most organizations, Claude for Teams or Claude for Enterprise provides the best experience. Team members get access to both Claude Code and Claude on the web with a single subscription, centralized billing, and no infrastructure setup required. **Claude for Teams** is self-service and includes collaboration features, admin tools, SSO, billing management, and [server-managed settings](../13-Enterprise-Admin/server-managed-settings.md) for organization-wide Claude Code configuration. Best for smaller teams that need to get started quickly. **Claude for Enterprise** adds domain capture, role-based permissions, and compliance API access. Best for larger organizations with security and compliance requirements. Learn more about [Team plans](../17-Billing-Plans/what-is-the-team-plan.md) and [Enterprise plans](../17-Billing-Plans/what-is-the-enterprise-plan.md). The deployment options compared below cover where model inference runs. To run Claude Code [cloud sessions](claude-code-on-the-web.md) on compute your organization operates, see [self-hosted environments](../13-Enterprise-Admin/self-hosted-environments.md). If your organization has specific infrastructure requirements, compare the options below:

[TABLE]

For a feature-by-feature breakdown of what’s available on each option, see [Feature availability](feature-availability.md). Select a deployment option to view setup instructions:

- [Claude for Teams or Enterprise](../13-Enterprise-Admin/iam.md#claude-for-teams-or-enterprise)
- [Anthropic Console](../13-Enterprise-Admin/iam.md#claude-console-authentication)
- [Claude apps gateway](../13-Enterprise-Admin/claude-apps-gateway.md), a self-hosted gateway that adds IdP sign-in in front of Amazon Bedrock, Claude Platform on AWS, Google Cloud’s Agent Platform, Microsoft Foundry, or the Anthropic API
- [Amazon Bedrock](amazon-bedrock.md)
- [Claude Platform on AWS](claude-platform-on-aws.md)
- [Google Cloud’s Agent Platform](google-vertex-ai.md)
- [Microsoft Foundry](microsoft-foundry.md)

For Amazon Bedrock and Google Vertex AI, you can also run `claude` and select **3rd-party platform** at the login prompt to launch an interactive setup wizard.


[​](#configure-proxies-and-gateways)

Configure proxies and gateways

Most organizations can use a cloud provider directly without additional configuration. However, you may need to configure a corporate proxy or LLM gateway if your organization has specific network or management requirements. These are different configurations that can be used together:

- **Corporate proxy**: Routes traffic through an HTTP/HTTPS proxy. Use this if your organization requires all outbound traffic to pass through a proxy server for security monitoring, compliance, or network policy enforcement. Configure with the `HTTPS_PROXY` or `HTTP_PROXY` environment variables. Learn more in [Enterprise network configuration](../13-Enterprise-Admin/network-config.md).
- **LLM Gateway**: A service that sits between Claude Code and the cloud provider to handle authentication and routing. Use this if you need centralized usage tracking across teams, custom rate limiting or budgets, or centralized authentication management. Configure with the `ANTHROPIC_BASE_URL`, `ANTHROPIC_BEDROCK_BASE_URL`, `ANTHROPIC_AWS_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, or `ANTHROPIC_FOUNDRY_BASE_URL` environment variables. Learn more in [LLM gateways](../13-Enterprise-Admin/llm-gateway.md).

For the per-provider environment variables that route Amazon Bedrock, Microsoft Foundry, or Google Cloud’s Agent Platform through an LLM gateway, see [route to a cloud provider through a gateway](../13-Enterprise-Admin/llm-gateway-connect.md#route-to-a-cloud-provider-through-a-gateway). Run `/status` in Claude Code to verify which provider, base URL, and proxy a session is using. If your organization uses [customer-managed encryption keys](../04-API-Reference/Other/manage-claude-cmek.md) (CMEK) and routes Claude Code through an LLM gateway or a custom `ANTHROPIC_BASE_URL`, CMEK doesn’t apply to Claude Code’s operational telemetry on those sessions. To turn telemetry off for every developer, deliver `DISABLE_TELEMETRY` through managed settings as shown in [Turn telemetry off for your organization](../13-Enterprise-Admin/managed-settings.md#turn-telemetry-off-for-your-organization).


[​](#best-practices-for-organizations)

Best practices for organizations


[​](#invest-in-documentation-and-memory)

Invest in documentation and memory

We strongly recommend investing in documentation so that Claude Code understands your codebase. Organizations can deploy CLAUDE.md files at multiple levels. See [where CLAUDE.md files can live](memory.md#choose-where-to-put-claude-md-files) and [how to deploy an organization-wide CLAUDE.md](memory.md#deploy-organization-wide-claude-md).


[​](#simplify-deployment)

Simplify deployment

If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.


[​](#start-with-guided-usage)

Start with guided usage

Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.


[​](#pin-model-versions-for-cloud-providers)

Pin model versions for cloud providers

If you deploy through [Amazon Bedrock](amazon-bedrock.md), [Google Cloud’s Agent Platform](google-vertex-ai.md), [Microsoft Foundry](microsoft-foundry.md), or [Claude Platform on AWS](claude-platform-on-aws.md), pin specific model versions using `ANTHROPIC_DEFAULT_FABLE_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL`. Without pinning, model aliases resolve to Claude Code’s built-in default for that provider, which can lag the newest release and may not yet be enabled in your account. Pinning lets you control when your users move to a new model. See [Model configuration](model-config.md#pin-models-for-third-party-deployments) for what each provider does when the default is unavailable.


[​](#configure-security-policies)

Configure security policies

Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration. [Learn more](../13-Enterprise-Admin/security.md).


[​](#leverage-mcp-for-integrations)

Use MCP for integrations

MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a `.mcp.json` configuration into the codebase so that all users benefit. [Learn more](../06-MCP-Tools/General/mcp.md).


[​](#next-steps)

Next steps

Once you’ve chosen a deployment option and configured access for your team:

1.  **Roll out to your team**: Share installation instructions and have team members [install Claude Code](../01-Getting-Started/setup.md) and authenticate with their credentials.
2.  **Set up shared configuration**: Create a [CLAUDE.md file](memory.md) in your repositories to help Claude Code understand your codebase and coding standards.
3.  **Configure permissions**: Review [security settings](../13-Enterprise-Admin/security.md) to define what Claude Code can and cannot do in your environment.
