---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:35Z"
source_url: "https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans"
title: "Managing members on Team and Enterprise plans | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_c3d323f637)

[](#h_f0d094f30d)

[](#h_b2cd7a8ce2)

[](#h_c5cdd3437a)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Account and Member Management](https://support.claude.com/en/collections/9811449-account-and-member-management)

Managing members on Team and Enterprise plans

# Managing members on Team and Enterprise plans

Updated this week

Table of contents

[](#h_c3d323f637)

[](#h_f0d094f30d)

[](#h_b2cd7a8ce2)

[](#h_c5cdd3437a)

This guide covers how to add, remove, and manage the people on your Team or Enterprise plan.

**Permissions note:** Organization Admins can manage members in **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**, but only Owners and Primary Owners can access **[Admin settings \> Billing](https://claude.ai/admin-settings/billing)**. For more information, see our article about **[roles and permissions](https://support.claude.com/en/articles/9267276-roles-and-permissions)**.

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

------------------------------------------------------------------------

## Adding members

### Adding members by invitation

**Note:** Pending invitations occupy your available seats immediately; a new member does not need to accept the invite to take up a seat.

Admins and above can add members by following these steps:

1.  Navigate to [**Admin settings \> Organization**](https://claude.ai/admin-settings/organization) and click “Add member.”

2.  Enter the person's email address (it must use one of your organization's **[allowed email domains](https://support.claude.com/en/articles/13325567-account-management-faqs#h_b54c41c86c)**).

3.  Select the appropriate seat type.

4.  Set the role and permissions for the member.

5.  Click “Add members.”

This sends an email invitation to the person. The invitation expires after 21 days, so you'll need to re-invite them if they don't accept within that time period.

**Adding multiple members at once:** You can invite multiple members by clicking "Bulk add" and typing or pasting email addresses separated by commas or new lines.

**Note:** If you don't have an available seat of the selected type, you'll be prompted to purchase one. See our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)** for more information.

### Adding members via organization discovery

Members can also join your organization on their own through organization discovery. When you enable discoverability, colleagues with a matching email domain can find your organization during signup and request to join—no invitation needed. You can configure whether they're added automatically or require your approval. See **[Find and join a Team or Enterprise organization](https://support.claude.com/en/articles/13566435-organization-discovery)** for details.

### Automated provisioning with SSO

Organizations with single sign-on (SSO) configured can automate member provisioning. Learn more about **[setting up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso-for-claude-and-claude-console)**.

- **Just-in-time (JIT) provisioning:** Members assigned to the Anthropic app in your Identity Provider will have accounts created automatically the first time they log in. Users are assigned to the highest-available seat tier upon first login. Admins and above can manually reassign seat types afterward in **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

- **SCIM provisioning (Enterprise plan only):** With SCIM directory sync enabled, members assigned to the Anthropic app in your Identity Provider are provisioned automatically, up to the number of total seats on your plan. Seat tiers are distributed from highest to lowest available. Primary Owners and Owners can reassign seat types afterward in **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

**Important:** An Owner or Primary Owner must ensure seats are available before new users can be provisioned. We recommend monitoring your seat usage and adding seats proactively to ensure uninterrupted access for your team. You can **use [Advanced Group Mappings with JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans) to provision users directly to a specific role and seat tier**.

------------------------------------------------------------------------

## Removing members

You can remove a member by navigating to **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**, clicking the menu button to the right of the member, then selecting "Remove from team."

For Enterprise organizations using SCIM provisioning, members are automatically removed from Claude when they are removed from your Identity Provider.

When a member is removed:

- They lose access to the organization immediately.

- The seat they occupied becomes available to assign to another user.

- If you re-add the member later using the same email address, their account history will be maintained.

Removing a member frees up their seat for reassignment, but does not automatically reduce your plan's total seat count. See our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)** for information on reducing seats.

**Note:** You cannot remove yourself as a Primary Owner or Owner. Another Primary Owner or Owner must remove you from the team.

------------------------------------------------------------------------

## Managing invitations

### Resending an expired invitation

You can resend an invite from **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**. Find the member and select to resend the invite.

### Revoking a pending invitation

You can revoke a pending invite from **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**. Find the member and select "Remove from team."

------------------------------------------------------------------------

## Frequently Asked Questions

### Can I invite someone who already uses Claude personally with their work email?

Yes. Once they join your team, they'll have both a personal account and a Team or Enterprise plan account. They can toggle between accounts through the menu by clicking their initials or name in the lower left corner.

### How do I add a member that I previously removed?

To add a member that you previously removed, follow the same steps as adding a new member. Their account history will be maintained.

### How do I change the Primary Owner?

The current Primary Owner can transfer ownership by:

1.  Navigate to **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

2.  Click the Role dropdown next to the new user and select "Primary Owner."

3.  Type the new Primary Owner's email address in the modal to confirm and transfer ownership.

**Important:** There can only be one Primary Owner per organization. Following these steps transfers the role to a different user.

### What happens to the initial invitation for a new Enterprise organization?

When Anthropic provides a new Enterprise organization and invites the Primary Owner, the same 21-day expiration period applies to that initial invitation. If your invitation has expired, please reach out to your account manager.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9267276-roles-and-permissions)

Roles and Permissions

[](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats-on-team-plans)

Purchasing and managing seats on Team plans

[](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)

Extra usage for Team and seat-based Enterprise plans

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)

Purchasing and managing seats on Enterprise plans

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
