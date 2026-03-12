---
category: "06-MCP-Tools"
fetched_at: "2026-03-12T08:19:08Z"
source_url: "https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization"
title: "Enterprise-Managed Authorization - Model Context Protocol"
---

# Enterprise-Managed Authorization


Centralized access control for MCP in enterprise environments via identity providers


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
