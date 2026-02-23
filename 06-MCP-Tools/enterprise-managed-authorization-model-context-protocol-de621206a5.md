---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:20Z"
source_url: "https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization"
title: "Enterprise-Managed Authorization - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Authorization Extensions

Enterprise-Managed Authorization

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/extensions/overview)
  Extensions Overview

&nbsp;

- [](/extensions/client-matrix)
  Extension Support Matrix

##### MCP Apps

- [](/extensions/apps/overview)
  MCP Apps
- [](/extensions/apps/build)
  Build an MCP App

##### Authorization Extensions

- [](/extensions/auth/overview)
  Authorization Extensions
- [](/extensions/auth/oauth-client-credentials)
  OAuth Client Credentials
- [](/extensions/auth/enterprise-managed-authorization)
  Enterprise-Managed Authorization

On this page

- [What it is](#what-it-is)
- [When to use it](#when-to-use-it)
- [How it works](#how-it-works)

Authorization Extensions

# Enterprise-Managed Authorization

Copy page

Centralized access control for MCP in enterprise environments via identity providers

Copy page

The Enterprise-Managed Authorization extension (`io.modelcontextprotocol/enterprise-managed-authorization`) enables organizations to control MCP server access centrally through their existing identity provider (IdP). Instead of each employee authorizing each MCP server individually, the organization’s IT or security team manages access policies in one place. [](https://github.com/modelcontextprotocol/ext-auth/blob/main/specification/draft/enterprise-managed-authorization.mdx)

## Specification

Full technical specification for the Enterprise-Managed Authorization extension.

## 

[​](#what-it-is)

What it is

In a standard MCP deployment, each user independently authorizes an MCP client to access each MCP server. For consumer applications, this user-driven model is ideal — it gives individuals control over what accesses their data. In enterprise environments, this model creates friction and security gaps:

- Employees shouldn’t need to understand the authorization details of every MCP server their organization uses
- Security teams can’t enforce consistent access policies if each user authorizes independently
- Onboarding new employees requires them to manually authorize dozens of services
- Offboarding requires revoking access across every service individually

Enterprise-Managed Authorization solves this by introducing the organization’s IdP as the authoritative decision-maker. The IdP (such as Okta, Azure AD, or a corporate SSO system) controls which MCP servers employees can access, and under what conditions. Employees authenticate with their corporate identity — the same credentials they use for email, Slack, and other work tools — and the IdP grants or denies MCP server access based on organizational policy.

## 

[​](#when-to-use-it)

When to use it

Use Enterprise-Managed Authorization when:

- **Deploying MCP in a corporate environment** where IT manages access to all business applications
- **Enforcing organizational access policies** — you need to ensure only authorized employees access specific MCP servers
- **Centralizing access control** — you want to add or revoke access to MCP servers from a single admin console
- **Meeting compliance requirements** — your organization needs an auditable authorization trail for all MCP server access
- **Simplifying employee experience** — employees should access MCP tools with their existing corporate SSO credentials, without per-service authorization flows

## 

[​](#how-it-works)

How it works

The extension establishes a delegated authorization flow where the enterprise IdP acts as an intermediary between the MCP client and the MCP server:

Was this page helpful?

Yes

No

[OAuth Client Credentials](/extensions/auth/oauth-client-credentials)

[github](https://github.com/modelcontextprotocol)
