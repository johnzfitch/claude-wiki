---
title: "Compliance API FAQ - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/compliance-faq"
category: "04-API-Reference/Other"
fetched_at: "2026-08-02T05:40:32Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management (beta)](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

Encryption keys

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[](/login)




Admin


Admin/Compliance API

# Compliance API FAQ




Answers to common questions about Compliance API access, scopes, retention, and integration.






To enable the Compliance API, see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).




Access and scopes

### Why doesn't my parent organization appear in Claude Console when creating an Admin API key?

### Can I use my regular Claude API key with the Compliance API?

### Why does my Admin API key return 403 on chat or file endpoints?




Data coverage and retention

### How far back does the Activity Feed go?

### Does the Activity Feed include prompt or message content?

### Is deleted content recoverable through the Compliance API?

### What does the Compliance API not capture?




Integration and pagination

### How do I correlate Compliance API records with my SIEM?

### Can one customer have multiple organizations under one parent?

### Are activities returned in order, and how do I detect when I have caught up to real time?

### How do I get a sandbox to test the Compliance API?
