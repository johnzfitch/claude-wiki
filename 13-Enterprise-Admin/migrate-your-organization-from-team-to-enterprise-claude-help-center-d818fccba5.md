---
category: "13-Enterprise-Admin"
fetched_at: "2026-02-28T11:22:18Z"
source_url: "https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise"
title: "Migrate your organization from Team to Enterprise | Claude Help Center"
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

    1.  We only support credit card payments for self-serve Enterprise plans. For more information, see **[Self-serve vs. sales-assisted Enterprise](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan#h_3058c781c5)**.

6.  Review your order summary and click "Confirm upgrade."

**Important:** Migrating an organization from Team to Enterprise via this pathway is not reversible; please ensure that an Enterprise plan is the right fit for your organization before initiating this change.

## Seat assignment

During migration, some users may appear as "Unassigned" rather than being automatically mapped to seat tiers. Admins should verify all users have correct seat assignments after the cutover.

For detailed guidance, refer to **[Purchasing and managing seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

## SSO and identity setup timeline

- **Domain verification (DNS):** Allow 24–48 hours for DNS changes to propagate globally, though many changes take effect within 10 minutes.

- **SCIM provisioning sync:** Microsoft Entra ID pushes changes approximately every 40 minutes. Okta syncs more frequently.

For detailed setup instructions, refer to **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** and **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning).**

**Note:** Once you turn on SSO, existing users will be forced to log out and log back in.

## Billing and usage configuration

For usage-based Enterprise plans, usage is billed based on actual consumption. For more detailed information, refer to **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

If you had purchased extra usage for your Team plan, any unused credits will roll over and become available on your new usage-based Enterprise plan.

## Provisioning process

On the start date, you'll be provisioned and able to use the new features by the end of the day. After initial setup, Owners and Primary Owners can self-serve additional seats by navigating to **[Organization settings \> Organization](https://claude.ai/admin-settings/organization)** and clicking "Manage" under **Total seats**.

## Helpful resources

- **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**

- **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**

- **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)**

- **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)**

- **[Enterprise billing information](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

- **[Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)**

------------------------------------------------------------------------

Related Articles


What is the Team plan?


Purchasing and managing seats on Team plans


Set up JIT or SCIM provisioning


Manage members on Team and Enterprise plans


Purchase and manage seats on Enterprise plans
