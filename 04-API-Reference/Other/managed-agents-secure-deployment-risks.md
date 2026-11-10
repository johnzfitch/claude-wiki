---
title: "Security risks and sandbox boundaries - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/secure-deployment-risks"
category: "04-API-Reference/Other"
fetched_at: "2026-11-06T06:33:50Z"
tags: ["api", "security"]
---

# Security risks and sandbox boundaries

Copy page



Why an agent’s settings matter for security, and what the Managed Agents sandbox can and cannot do.

Copy page



[Managed Agents](managed-agents-overview.md)

[Status](managed-agents-overview.md#availability-feature-support)  
Beta

[Cloud platforms](managed-agents-overview.md#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableClaude Models on Google CloudAnthropic managedAvailable

[Beta header](managed-agents-overview.md#feature-beta-headers)  
- `managed-agents-2026-04-01`
  

[Data handling](managed-agents-overview.md#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

This page explains why the settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md) matter, and what the sandbox can and cannot do.

## Why this matters

Hidden instructions in content that an agent reads can steer the agent. This is called [prompt injection](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md). Claude is inherently resilient to it, but model behavior is not a security control. The settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md) limit the effect if an attempt succeeds.

Claude can also take a step you did not expect while it keeps working to complete the task you gave it. For example, it might use a tool or credential it can reach to get past an obstacle. The same settings limit what such a step can reach, and an [offline reviewer](managed-agents-secure-deployment-monitoring.md#optionally-have-an-offline-reviewer-read-every-transcript) can flag it afterward.

| What can go wrong | Example | Controls |
|----|----|----|
| Untrusted input steers the agent | A ticket tells the agent to cancel every open order | [Smallest tool set](managed-agents-secure-deployment.md#give-the-agent-the-smallest-tool-set), [untrusted input kept away from powerful tools](managed-agents-secure-deployment.md#keep-untrusted-input-away-from-powerful-tools), [approvals for risky actions](managed-agents-secure-deployment.md#approve-risky-actions) |
| Code in the sandbox can use a credential | A script the agent was tricked into running sends the agent’s key to an outside host, or uses it to read every customer’s orders | [Credentials in vaults](managed-agents-secure-deployment.md#keep-credentials-in-vaults), [limited networking](managed-agents-secure-deployment.md#limit-the-network), [approvals for risky actions](managed-agents-secure-deployment.md#approve-risky-actions) |
| An open network lets data out | A bash command posts a file to an outside host | [Limited networking](managed-agents-secure-deployment.md#limit-the-network), the [`web_fetch` domain list](managed-agents-secure-deployment.md#restrict-web-search-and-web-fetch) |
| Claude takes a step you did not expect | To get past an obstacle, it uses a tool or credential it can reach | The settings in [Secure your Managed Agents deployment](managed-agents-secure-deployment.md). An [offline reviewer](managed-agents-secure-deployment-monitoring.md#optionally-have-an-offline-reviewer-read-every-transcript) can flag the step afterward |

These settings lower the risk but do not remove it, so do not put data in the sandbox that must never leave it. An agent can still put data it is allowed to read into its own reply or tool output. Limit a key’s permissions at the service that issued it, because these settings do not limit them. The settings do not secure your custom tools, your MCP servers, or your self-hosted infrastructure.

## What the sandbox can and cannot do

Managed Agents keeps the agent loop, session history, and vault secrets outside the sandbox by design. For the design background, see [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents).

| Part | Where it runs | What limits it |
|----|----|----|
| Agent loop | Anthropic’s servers | The tool set, permission policies, and budget that you set |
| `bash` and file tools | The sandbox. In a cloud environment, each session gets its own isolated Linux container | Environment networking, the tool set, and permission policies |
| `web_search` and `web_fetch` | Anthropic’s servers | The tool’s own domain list, your organization’s web search and web fetch settings in the Claude Console, and, in a `limited` cloud environment, the environment’s allowed hosts. `web_fetch` also opens only URLs that have already appeared in the session |
| Vault secret | Outside the sandbox. MCP credentials never enter it. For an environment variable credential, code sees a placeholder | For an MCP credential, the MCP server URL it is for. For an environment variable credential, the hosts the credential allows, its injection location, and the environment’s allowed hosts |
| Session history | Anthropic’s servers, until you delete the session | The API keys for the workspace, the Developer and Admin roles in the Claude Console, and session deletion |
| Custom tools | Your application | Your code |

In a cloud environment, sessions do not share filesystem state. A memory store attached to more than one session is shared between them.

These limits do not replace each other. For example, limiting the environment’s hosts does not stop the agent from using a credential on a host you allowed.
