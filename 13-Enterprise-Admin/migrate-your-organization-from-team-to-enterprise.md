---
title: "Migrate your organization from Team to Enterprise | Claude Help Center"
source_url: "https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise"
category: "13-Enterprise-Admin"
fetched_at: "2026-03-22T09:01:45Z"
tags: ["billing", "enterprise"]
---

4.  Migrate your organization from Team to Enterprise

# Migrate your organization from Team to Enterprise


When upgrading from a Team plan to an Enterprise plan, we recommend you keep the same Team organization and follow the upgrade path to change it to Enterprise. This way your data (memberships/roles, conversations and projects) and settings will be preserved. If a you create a brand new Enterprise organization, then you'll need to set up everything from scratch.

## What's retained (same organization upgrade)

- All chat history and conversations

- Projects and shared content

- User memberships and roles

## Migrate from Team to Enterprise

You can migrate from a Team plan to a self-serve Enterprise plan by following these steps:

1.  Navigate to **[claude.ai/upgrade](https://claude.ai/upgrade)** and click "Get Enterprise plan."

2.  When prompted, choose "Upgrade an existing organization" and select your Team plan organization.

3.  Add the number of seats needed for all your team members (Enterprise organizations have a 20 seat minimum).

4.  Set a per-user spend limit and a starting usage balance for the whole team.

5.  Your payment information will be saved from previous Team plan payments, but you can click the pencil icon to change it if needed.

    1.  We only support credit card payments for self-serve Enterprise plans. For more information, see **[Self-serve vs. sales-assisted Enterprise](../17-Billing-Plans/what-is-the-enterprise-plan.md#h_3058c781c5)**.

6.  Review your order summary and click "Confirm upgrade."

**Important:** Migrating an organization from Team to Enterprise via this pathway is not reversible; please ensure that an Enterprise plan is the right fit for your organization before initiating this change.

## Seat assignment

During migration, some users may appear as "Unassigned" rather than being automatically mapped to seat tiers. Admins should verify all users have correct seat assignments after the cutover.

For detailed guidance, refer to **[Purchasing and managing seats on Enterprise plans](../17-Billing-Plans/purchasing-and-managing-seats-on-enterprise-plans.md)**.

## SSO and identity setup timeline

- **Domain verification (DNS):** Allow 24–48 hours for DNS changes to propagate globally, though many changes take effect within 10 minutes.

- **SCIM provisioning sync:** Microsoft Entra ID pushes changes approximately every 40 minutes. Okta syncs more frequently.

For detailed setup instructions, refer to **[Setting up single sign-on (SSO)](../21-Account-Support/setting-up-single-sign-on-sso.md)** and **[Setting up JIT or SCIM provisioning](setting-up-jit-or-scim-provisioning.md).**

**Note:** Once you turn on SSO, existing users will be forced to log out and log back in.

## Billing and usage configuration

For usage-based Enterprise plans, usage is billed based on actual consumption. For more detailed information, refer to **[How am I billed for my Enterprise plan?](../17-Billing-Plans/how-am-i-billed-for-my-enterprise-plan.md)**

If you had purchased extra usage for your Team plan, any unused credits will roll over and become available on your new usage-based Enterprise plan.

## Provisioning process

On the start date, you'll be provisioned and able to use the new features by the end of the day. After initial setup, Owners and Primary Owners can self-serve additional seats by navigating to **[Organization settings \> Organization](https://claude.ai/admin-settings/organization)** and clicking "Manage" under **Total seats**.

## Helpful resources

- **[Set up single sign-on (SSO)](../21-Account-Support/set-up-single-sign-on-sso.md)**

- **[Set up JIT or SCIM provisioning](set-up-jit-or-scim-provisioning.md)**

- **[Purchase and manage seats on Enterprise plans](../17-Billing-Plans/purchase-and-manage-seats-on-enterprise-plans.md)**

- **[Manage members on Team and Enterprise plans](../17-Billing-Plans/manage-members-on-team-and-enterprise-plans.md)**

- **[Enterprise billing information](../17-Billing-Plans/how-am-i-billed-for-my-enterprise-plan.md)**

- **[Use Claude Code with your Team or Enterprise plan](../17-Billing-Plans/use-claude-code-with-your-team-or-enterprise-plan.md)**
