---
title: "Set up and manage the new unified Claude experience for your Enterprise organization | Claude Help Center"
source_url: "https://support.claude.com/en/articles/17444462"
category: "13-Enterprise-Admin"
fetched_at: "2026-11-18T06:28:08Z"
tags: ["enterprise"]
---

# Set up and manage the new unified Claude experience for your Enterprise organization


The new unified Claude experience brings chat and Cowork together on web, desktop, and mobile. Members no longer choose between chat and Cowork before they start. Every conversation starts as a chat, and when a task needs to run code or work with files, Claude continues the same conversation in an isolated cloud sandbox managed by Anthropic, then returns the finished work for review.

This article explains how admins turn on the new unified Claude experience, which settings apply to it, and how it fits your security, compliance, and data retention setup.

The new unified Claude experience is available on Enterprise plans, where it appears in admin settings as **Chat and Cowork unified**. It's off by default in existing organizations and turns on by default on November 16, 2026.

------------------------------------------------------------------------

## How the new unified Claude experience works

1.  **One conversation, two modes.** The new unified Claude experience starts as a chat and moves into a Cowork cloud session when a task needs agentic work. Members aren't asked to switch modes.

2.  **Longer tasks run in an isolated cloud environment.** Each conversation that needs one gets its own virtual machine, managed by Anthropic. After a few minutes idle, the virtual machine is stopped and its disk is saved as an encrypted snapshot. The sandbox environment expires 30 days after it was created.

3.  **The conversation stays on record.** Chat history, sharing, export, the Compliance API, and your data retention setting all work from the conversation.

4.  **Work moves across devices.** Members can start a task on the desktop app and pick it up on web or mobile.

5.  **Local access stays optional.** Through the Claude desktop app, members can link their computers so Claude can work with local folders, local MCP servers, and applications. Your Remote control and device policies govern this.

------------------------------------------------------------------------

## Before you begin

The new unified Claude experience requires two capabilities to be on for your organization:

1.  **Chat**, since chat is where every conversation starts.

2.  **Cloud code execution and file creation**, since agentic work runs remotely.

It doesn't require Cowork or Cowork in the cloud to be on. It is meant to replace both over time.

[TABLE]

The new unified Claude experience isn't available yet for organizations that use zero data retention (ZDR), the HIPAA-ready configuration, or customer-managed encryption keys (CMEK). See **[Current limitations](#h_8b973139dd)** below.

------------------------------------------------------------------------

## Turn on the new unified Claude experience

### For your whole organization

1.  Sign in to Claude as an Owner or Primary Owner.

2.  Go to **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**.

3.  Turn on **Chat and Cowork unified**.

4.  If you have eligible custom roles (roles with both Chat and code execution selected), a list opens with every eligible role selected, including roles where you turned it off. Roles without Chat or code execution are grayed out and not selected. Clear any role that shouldn’t have it, then confirm.

5.  Ask members to refresh the Claude app if they don't see the new experience right away.

This turns on the new unified Claude experience for members with the User, Admin, Owner or Primary Owner role. Members on a custom role get it only if their role also includes Chat and Cowork unified.

Scheduled tasks and session history will continue working after the change. You don’t need to update or recreate anything.

### If you haven't changed this setting

On November 16, 2026, **Chat and Cowork unified** turns on by default if no admin has turned it on or off for your organization. Owners and Primary Owners can turn it off at any time in **[Organization settings \> Capabilities](https://claude.ai/admin-settings/capabilities)**. If the setting was already turned on or off, that choice stays.

If **Chat** or **Cloud code execution and file creation** is off, nothing turns on. After November 16, the new experience turns on as soon as both are on.

**Custom roles on December 1, 2026:** If your organization is still on by default, the new unified Claude experience turns on for custom roles that have both Chat and code execution selected, even if an admin turned it off for that role. Admins can turn it off again by role after that. If an admin has turned it on or off for your organization, this change doesn’t apply.

### For specific members, using roles

The organization setting above must also be on. Once it is, everyone with the User, Admin, Owner or Primary Owner role has access. Before you turn it on, move anyone who shouldn’t have it to a custom role with Chat and Cowork unified turned off. New roles start with All capabilities, which includes it.

When you turn it on for your organization, clear that role in the list that opens, because every eligible role starts selected. If your organization is still on by default instead, it turns on for eligible roles on December 1, 2026, even if you turned it off for them.

If your organization uses custom roles, you can grant the new unified Claude experience to specific roles:

1.  Go to **[Organization settings \> Roles](https://claude.ai/admin-settings/roles)**.

2.  Open the role you want to update and go to “Capabilities.”

3.  Turn on **Chat and Cowork unified** for that role.

4.  Assign the role to the members who should have access. You can sync role membership through SCIM to add members in waves.

Access is checked on every request. If you remove a member's role or turn the setting off, they lose access to the new unified Claude experience.

To learn how to create a role, see **[Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458)**.

### Recommended rollout

1.  Share this article with your IT, security, and procurement teams.

2.  Complete your security review. Most teams review two components they already know: Claude chat and Cowork in the cloud. If a review of Cowork in the cloud is already underway, it carries over.

3.  Start in your sandbox organization, if you have one, or with a pilot group through a role. If you pilot through a role, clear every other role you can in the list when you turn on the organization setting. Built-in roles and roles on "All capabilities" or "All generally available" can’t be cleared, so users with those roles get it too unless you move them first.

4.  Review your network egress, connector, sharing, and remote control settings before you turn the experience on.

5.  Monitor usage and gather feedback for two to four weeks, then expand in waves.

------------------------------------------------------------------------

## Admin settings that apply to the new unified Claude experience

[TABLE]

Identity settings carry over unchanged. Members sign in to Claude as members of your organization, and your SSO (SAML/OIDC), SCIM provisioning, and tenant restrictions apply. The new unified Claude experience adds no separate sign-in.

For recommended Security settings and architecture, see **[Unified Claude and Cowork security best practices](https://trust.anthropic.com/resources?s=uukz8hyx7jmdmo80lys36s&name=claude-cowork-security-best-practices)**.

------------------------------------------------------------------------

## Data retention and deletion

1.  **Conversations.** Conversations are kept until the member deletes them or according to your organization's custom data retention setting if you’ve set one (minimum 30 days). See **[custom data retention](https://support.claude.com/en/articles/10440198)**. Conversations in a project are deleted with the project, once deleted by the user or once the project and all its conversations have been inactive for the project’s retention period. The period is measured from the most recent activity in the conversation or in any cloud session Claude started from it.

2.  **Cloud sessions started from a conversation.** When a conversation is deleted, whether by a member, by deleting its project, or under your retention period, the cloud sessions Claude started in it are deleted too, including their transcripts. Deletion finishes in the background after the conversation is removed.

3.  **Memory.** Account memory is covered by your custom data retention setting for chats, and project memory is deleted when the project is deleted, including by your project data retention period. After moving to the new experience, the memory will be moved to a new memory system and the old memory may be deleted 14 days later, or sooner if it’s past the data retention period.

4.  **Artifacts.** Artifacts, including those Claude creates in conversations, follow your retention periods for private and shared artifacts, or your period for all data, not the conversation's. These periods don't delete artifacts published with a public link. Some artifacts, such as Research reports and artifacts in some older conversations, are deleted with their conversation instead.

5.  **Files Claude gives you.** Almost all files (like documents or spreadsheets) that Claude gives you in a conversation on or after October 8, 2026 are deleted with it, including under your retention period, unless another conversation or project in your organization uses them. Older files may remain after their conversation is deleted.

6.  **Not deleted with a conversation.** Custom data retention doesn’t cover:

    1.  Cowork cloud sessions a member starts directly, including in a project. These are kept until the member deletes them.

    2.  Scheduled tasks and their runs, including tasks created from a conversation. These keep running after that conversation is deleted. To stop them from running, turn off Scheduled tasks.

    3.  Cowork history stored on a member’s computer.

    4.  Memory of members who have left your organization.

    5.  Transcripts and memory kept by Claude Code (including Claude Code on the web), Claude Tag, and other products outside chat and Cowork.

Deletion happens after the period ends rather than at an exact moment, and deleted data is removed from our back-end systems. As with chat, we may retain content flagged by our trust and safety systems or as required by law. See **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**

------------------------------------------------------------------------

## Manage access and spend

1.  Pricing stays usage-based, and the spend controls you have today apply.

2.  Spend limits can be set at the organization, group, and member level.

3.  Usage analytics break out chat, Cowork, and the new unified Claude experience.

4.  Models: The model allowlist you set applies to both chat and agentic work in the new unified Claude experience.

------------------------------------------------------------------------

## Usage and analytics

The new unified Claude experience gets its own line in your reports. When a member has access to the new unified Claude experience, their chat and Cowork usage is reported under **Chat and Cowork unified**, not under Chat or Cowork. Think of it as a new folder for the same work: only where the usage is filed changes, so moving usage to this line doesn't change how it's counted or billed.

### How usage is counted

- **Counting follows each member.** Usage counts toward the new unified Claude experience if the member has access to it when the usage happens. If you turn it on for some roles first, your reports can show Chat, Cowork, and **Chat and Cowork unified** on the same day.

- **It covers chat and Cowork.** A member's chats, their cloud sessions, and their use of the Cowork desktop app count toward the new unified Claude experience.

- **Other products keep their own line.** For example, Claude Code and Claude in Chrome usage is still reported under those products.

- **Past usage stays where it is.** Data for the new unified Claude experience starts the day a member first gets access. Usage from before then stays under Chat or Cowork. If you turn the new unified Claude experience off, past unified usage keeps its **Chat and Cowork unified** label, and new usage goes back to Chat and Cowork.

- **Include it when you add things up.** When you add up spend, tokens, or messages for Chat and Cowork, include **Chat and Cowork unified** too. Otherwise your Chat and Cowork numbers will seem to drop as members move over. For the number of people, use the overall active users count rather than adding products together, since one person can be active in more than one.

### In the analytics dashboard

**A page of its own.** Admins who can view analytics will find a Chat and Cowork unified page under Apps. It shows daily active users.


**Across the dashboard.** You can pick "Chat and Cowork unified" in the Active users, Active members, Total spend, and Spend by model charts. The See all members table on the Overview page has a "Messages in Chat and Cowork unified" column. The Top connectors and Top skills cards don't include it yet.


**Who sees it.** The page appears for every organization that can turn on the new unified Claude experience, whether or not it is on yet.

**Give it a day or two.** New activity can take up to two days to show up.

### In the APIs

**Your keys already work.** If you already use these APIs, your existing access keys work. If your scripts check responses against a fixed list of fields or products, add the new ones.

**Cost and Usage API.** Tokens and spend for the new unified Claude experience are reported under the product value `chat_cowork_unified`. You can filter to it with `products[]`. The `chat` and `cowork` values still work, and cover usage from members who didn't have the new unified Claude experience at the time.

**Analytics API.** Member, skill, and connector rows have a `chat_cowork_unified_metrics` object with two parts: `chat`, for chat activity, and `sessions`, for cloud sessions and the Cowork desktop app. Daily summaries add daily, weekly, and monthly active user counts for the new unified Claude experience, such as `chat_cowork_unified_daily_active_user_count`.

### What members see

Members with usage-based seats see their own usage of the new unified Claude experience on their usage page, listed as **Chat and Cowork unified**.

### Unified smart report and analytics chat

To learn how to create a smart report, refer to **[Get started with smart reports](../15-Claude-AI-Features/get-started-with-smart-reports.md#h_85974ef359)**. When choosing products to run the report for, choose “Chat and Cowork unified” to run the report against the new unified Claude experience.

------------------------------------------------------------------------

## Efficient mode for the new unified Claude experience

When on, org members can use only Sonnet and Haiku models in the new unified Claude experience, and new sessions start on Claude Sonnet 5.5 at low effort. Other products aren’t affected. As lower-cost models become available, Anthropic may update the default model and effort level to keep the best balance of performance and cost.

**How to access it:** Owners can turn it on for the whole org on the Models page, or for specific custom roles on each role's Models tab.

------------------------------------------------------------------------

## Current limitations

1.  **ZDR, HIPAA, and CMEK.** The new unified Claude experience isn't available to organizations with zero data retention, the HIPAA-ready configuration, or customer-managed encryption keys. These organizations keep using chat and Cowork as they do today, and admins can't turn on Chat and Cowork unified. HIPAA support is expected after general availability; CMEK support is planned for a later release. If your organization turns on CMEK after turning on the new experience, it becomes unavailable.
