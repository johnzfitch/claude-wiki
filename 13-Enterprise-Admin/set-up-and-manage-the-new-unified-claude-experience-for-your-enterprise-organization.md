---
title: "Set up and manage the new unified Claude experience for your Enterprise organization | Claude Help Center"
source_url: "https://support.claude.com/en/articles/17444462"
category: "13-Enterprise-Admin"
fetched_at: "2026-10-23T06:29:16Z"
tags: ["enterprise"]
---

# Set up and manage the new unified Claude experience for your Enterprise organization

Updated today


The new unified Claude experience brings chat and Cowork together on web, desktop, and mobile. Members no longer choose between chat and Cowork before they start. Every conversation starts as a chat, and when a task needs to run code or work with files, Claude continues the same conversation in an isolated cloud sandbox managed by Anthropic, then returns the finished work for review.

This article explains how admins turn on the new unified Claude experience, which settings apply to it, and how it fits your security, compliance, and data retention setup.

The new unified Claude experience is in public beta for Claude Enterprise plans. In your admin settings it appears as **Chat and Cowork unified (beta)**. The new unified Claude experience is off by default. Nothing changes for your organization until an admin turns it on.

------------------------------------------------------------------------

## How the new unified Claude experience works

1.  One conversation, two modes. The new unified Claude experience starts as a chat and moves into a Cowork cloud session when a task needs agentic work, and goes back to chat when it doesn't. Members aren't asked to switch modes.

2.  Agentic work runs in an isolated cloud sandbox. Each conversation that needs one gets its own virtual machine, managed by Anthropic. After a few minutes idle, the virtual machine is stopped and its disk is saved as an encrypted snapshot. The sandbox environment expires 30 days after it was created.

3.  The conversation stays on record. Chat history, sharing, export, the Compliance API, and your data retention setting all work from the conversation.

4.  Work moves across devices. Members can start a task on the desktop app and pick it up on web or mobile.

5.  Local access stays optional. Through the Claude desktop app, members can link their computers so Claude can work with local folders, local MCP servers, and applications. Your Computer access and device policies govern this.

------------------------------------------------------------------------

## Before you begin

The new unified Claude experience requires two capabilities to be on for your organization:

1.  Chat, since chat is where every conversation starts.

2.  Cloud code execution and file creation, since agentic work runs remotely.

It doesn't require Cowork or Cowork in the cloud to be on. It is meant to replace both over time.

[TABLE]

The new unified Claude experience isn't available yet for organizations that use zero data retention (ZDR), the HIPAA-ready configuration, or customer-managed encryption keys (CMEK). See **[Current limitations](#h_8b973139dd)** below.

------------------------------------------------------------------------

## Turn on the new unified Claude experience

### For your whole organization

1.  Sign in to Claude as an Owner or Primary Owner.

2.  Go to **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**.

3.  Turn on **Chat and Cowork unified (beta)**.

4.  Ask members to refresh the Claude app if they don't see the new experience right away.

This turns on the new unified Claude experience for every member of your organization. To limit access to specific members, use roles instead.

Scheduled tasks and session history will continue working after the change. You don’t need to update or recreate anything.

### For specific members, using roles

If your organization uses custom roles, you can grant the new unified Claude experience to specific roles:

1.  Go to **[Organization settings \> Roles](https://claude.ai/admin-settings/roles)**.

2.  Open the role you want to update and go to “Capabilities.”

3.  Turn on **Chat and Cowork unified (beta)** for that role.

4.  Assign the role to the members who should have access. You can sync role membership through SCIM to add members in waves.

Access is checked on every request. If you remove a member's role or turn the setting off, they lose access to the new unified Claude experience.

To learn how to create a role, see **[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458)**.

### Recommended rollout

1.  Share this article with your IT, security, and procurement teams.

2.  Complete your security review. Most teams review two components they already know: Claude chat and Cowork in the cloud. If a review of Cowork in the cloud is already underway, it carries over.

3.  Start in your sandbox organization, if you have one, or with a pilot group through a role.

4.  Review your network egress, connector, sharing, and Computer access settings before you turn the experience on.

5.  Monitor usage and gather feedback for two to four weeks, then expand in waves.

------------------------------------------------------------------------

## Admin settings that apply to the new unified Claude experience

[TABLE]

Identity settings carry over unchanged. Members sign in to Claude as members of your organization, and your SSO (SAML/OIDC), SCIM provisioning, and tenant restrictions apply. The new unified Claude experience adds no separate sign-in.

For recommended Security settings and architecture, see **[Unified Claude and Cowork security best practices](https://trust.anthropic.com/resources?s=uukz8hyx7jmdmo80lys36s&name=claude-cowork-security-best-practices)**.

------------------------------------------------------------------------

## Data retention and deletion

1.  **Conversations.** Conversations are kept until the member deletes them or according to your organization's custom data retention setting if you’ve set one (minimum 30 days). See **[custom data retention](https://support.claude.com/en/articles/10440198)**. Conversations in a project follow the project’s retention period. The period is measured from the most recent activity in the conversation or in any cloud session Claude started from it, so a conversation isn’t deleted while one of its cloud sessions is in use.

2.  **Cloud sessions started from a conversation.** When a conversation is deleted, whether by a member, by deleting its project, or under your retention period, the cloud sessions Claude started in it are deleted too, including their transcripts.

3.  **Artifacts.** When a conversation is deleted under your retention period, the artifacts made in it aren't deleted with it. They follow the retention period that covers artifacts, if you have one. Research reports and artifacts in some older chats are the exception, and they're deleted with their conversation.

4.  **Not deleted with a conversation.** Custom data retention doesn’t cover:

    1.  Cowork cloud sessions a member starts directly, including in a project. These are kept until the member deletes them.

    2.  Scheduled tasks and their runs, including tasks created from a conversation. These keep running after that conversation is deleted. To prevent this, turn off Scheduled tasks.

    3.  Cowork history stored on a member’s computer.

5.  **Memory during the public beta.** Memory isn’t covered by your retention setting during the beta. When you turn on the new experience, each member’s existing memory is copied into it, and memory from conversations that are later deleted can remain. If you turn the experience off, that memory is kept. We plan to apply your retention setting to memory, including memory created during the beta, at general availability, and will update this article.

As with chat, we may retain content flagged by our trust and safety systems or as required by law. See **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**

------------------------------------------------------------------------

## Manage access and spend

1.  Pricing stays usage-based, and the spend controls you have today apply.

2.  Spend limits can be set at the organization, group, and member level.

3.  Usage analytics break out chat, Cowork, and the new unified Claude experience.

4.  Models: The model allowlist you set applies to both chat and agentic work in the new unified Claude experience.

------------------------------------------------------------------------

## Usage and analytics

The new unified Claude experience gets its own line in your reports. When a member has access to the new unified Claude experience, their chat and Cowork usage is reported under **Chat and Cowork unified (beta)**, not under Chat or Cowork. Think of it as a new folder for the same work: only where the usage is filed changes, so moving usage to this line doesn't change how it's counted or billed.

### How usage is counted

- **Counting follows each member.** Usage counts toward the new unified Claude experience if the member has access to it when the usage happens. If you turn it on for some roles first, your reports can show Chat, Cowork, and **Chat and Cowork unified (beta)** on the same day.

- **It covers chat and Cowork.** A member's chats, their cloud sessions, and their use of the Cowork desktop app count toward the new unified Claude experience.

- **Other products keep their own line.** For example, Claude Code and Claude in Chrome usage is still reported under those products.

- **Past usage stays where it is.** Data for the new unified Claude experience starts the day a member first gets access. Usage from before then stays under Chat or Cowork. If you turn the new unified Claude experience off, past unified usage keeps its **Chat and Cowork unified (beta)** label, and new usage goes back to Chat and Cowork.

- **Include it when you add things up.** When you add up spend, tokens, or messages for Chat and Cowork, include **Chat and Cowork unified (beta)** too. Otherwise your Chat and Cowork numbers will seem to drop as members move over. For the number of people, use the overall active users count rather than adding products together, since one person can be active in more than one.

### In the analytics dashboard

- **A page of its own.** Admins who can view analytics will find a Chat and Cowork unified page under Apps, marked Beta. It shows daily active users.


- **Across the dashboard.** You can pick "Chat and Cowork unified (beta)" in the Active users, Active members, Total spend, and Spend by model charts. The See all members table on the Overview page has a "Messages in Chat and Cowork unified (beta)" column. The Top connectors and Top skills cards don't include it yet.


- **Who sees it.** The page appears for every organization that can turn on the new unified Claude experience, whether or not it is on yet.

- **Give it a day or two.** New activity can take up to two days to show up.

### In the APIs

- **Your keys already work.** If you already use these APIs, your existing access keys work. If your scripts check responses against a fixed list of fields or products, add the new ones.

- **Cost and Usage API.** Tokens and spend for the new unified Claude experience are reported under the product value `chat_cowork_unified`. You can filter to it with `products[]`. The `chat` and `cowork` values still work, and cover usage from members who didn't have the new unified Claude experience at the time.

- **Analytics API.** Member, skill, and connector rows have a `chat_cowork_unified_metrics` object with two parts: `chat`, for chat activity, and `sessions`, for cloud sessions and the Cowork desktop app. Daily summaries add daily, weekly, and monthly active user counts for the new unified Claude experience, such as `chat_cowork_unified_daily_active_user_count`.

### What members see

Members with usage-based seats see their own usage of the new unified Claude experience on their usage page, listed as **Chat and Cowork unified (beta)**.

### Unified smart report and analytics chat

To learn how to create a smart report, refer to **[Get started with smart reports](../15-Claude-AI-Features/get-started-with-smart-reports.md#h_85974ef359)**. When choosing products to run the report for, choose “Chat and Cowork unified (beta)” to run the report against the new unified Claude experience.

------------------------------------------------------------------------

## Efficient mode for the new unified Claude experience

When on, org members can use only Sonnet and Haiku models in the new unified Claude experience, and new sessions start on Claude Sonnet 5.5 at low effort. Other products aren’t affected. As lower-cost models become available, Anthropic may update the default model and effort level to keep the best balance of performance and cost.

**How to access it:** Owners can turn it on for the whole org on the Models page, or for specific custom roles on each role's Models tab.

------------------------------------------------------------------------

## Current limitations

1.  **ZDR, HIPAA, and CMEK.** The new unified Claude experience isn't available to organizations with zero data retention, the HIPAA-ready configuration, or customer-managed encryption keys. These organizations stay on their current configuration. HIPAA and CMEK support is expected after general availability.

2.  **Per-role access for Computer access and scheduled tasks.** These are set for the whole organization, not per role.
