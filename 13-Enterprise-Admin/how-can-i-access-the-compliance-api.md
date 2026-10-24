---
title: "Access the Compliance API | Claude Help Center"
source_url: "https://support.claude.com/en/articles/13015708-how-can-i-access-the-compliance-api"
category: "13-Enterprise-Admin"
fetched_at: "2026-10-23T06:29:00Z"
tags: ["api", "enterprise", "security"]
---

# Access the Compliance API


The Compliance API lets your organization programmatically pull activity feed events, chat data, and file content across all your Claude deployments. Use it to monitor, audit, and meet compliance requirements with your own tools.

The Compliance API is available to Enterprise plan organizations and to Claude Platform customers in Claude chats. Organizations on Anthropic’s dedicated government deployments, such as Claude for Government, use **[a separate Compliance API](https://claude.com/docs/government/org-admin/compliance-api)**.

**Important:** For Claude Enterprise organizations, only your organization's Primary Owner can enable the Compliance API, from **[Organization settings \> API](https://claude.ai/admin-settings/api-access)**. You can create a key on the same page by clicking "+Create key" under **Keys**: the Primary Owner can create a key covering every linked organization, and Owners can create keys limited to their own organization. Owners see this page but not the **Compliance API** toggle—only the Primary Owner can turn the API on or off. Admins don't see the page at all. If your organization is linked to a parent organization, the parent organization's Primary Owner enables it and the setting applies to every linked organization.

## Compliance API technical documentation

For setup instructions, endpoints, and reference material, including how to enable the API and create access keys to start pulling data, see the **[Compliance API documentation](../04-API-Reference/Other/manage-claude-compliance-api.md)** on Claude Platform Docs.

## Compliance API security integrations

Security and compliance platforms have built integrations on top of the Claude Compliance API, so your team can monitor Claude activity within the tools you already use. Learn more about **[Compliance API integrations](../14-Connectors/get-started-with-claude-compliance-api-integrations.md)**.

## Audit log events in the Compliance API

The Compliance API now includes audit log events, giving you a full view across all your Claude deployments. To see which events are recorded via audit logs, see **[How to access audit logs](how-to-access-audit-logs.md#h_41cdad187a)**.
