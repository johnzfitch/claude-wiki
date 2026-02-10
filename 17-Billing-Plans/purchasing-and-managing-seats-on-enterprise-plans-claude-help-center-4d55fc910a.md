---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:36Z"
source_url: "https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans"
title: "Purchasing and managing seats on Enterprise plans | Claude Help Center"
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

[](#h_62a37addb3)

[](#h_4d24b6ef7c)

[](#h_1e1e38fa47)

[](#h_4e79d93003)

[](#h_0918f7f456)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Enterprise Plan](https://support.claude.com/en/collections/10351014-enterprise-plan)

Purchasing and managing seats on Enterprise plans

# Purchasing and managing seats on Enterprise plans

Updated this week

Table of contents

[](#h_62a37addb3)

[](#h_4d24b6ef7c)

[](#h_1e1e38fa47)

[](#h_4e79d93003)

[](#h_0918f7f456)

Seat management allows Enterprise plan Owners to control their organization's seat allocation and assign users to different seat types. For pricing and billing details, see **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-usage-based-enterprise-plans)**

**Permissions note:** Only Owners and Primary Owners can purchase seats and access **[Admin settings \> Billing](https://claude.ai/admin-settings/billing)**. Admins and above can reassign seat types for members in **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

For information on adding and removing members from your organization, see [**Managing members on Team and Enterprise plans**](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans).

------------------------------------------------------------------------

## Understanding seat types

Usage-based Enterprise plans offer two seat types:

[TABLE]

Organizations can mix and match seat types based on team needs. Assign Chat + Claude Code seats to developers and technical team members who need terminal-based coding workflows, while keeping other team members on Chat seats.

Your plan has a total seat allocation (e.g., 50 Chat seats and 20 Chat + Claude Code seats). Within that allocation, you can assign and reassign users to different seat types as needed.

**Note for seat-based Enterprise plans:** Some Enterprise organizations on older plans may see "Standard" and "Premium" seat types instead. See **[Information for seat-based Enterprise plans](#h_0918f7f456)** at the end of this article.

------------------------------------------------------------------------

## Purchasing seats

Enterprise plans require a minimum of 20 seats. You can add seats at any time.

1.  Log in with your Owner or Primary Owner account.

2.  Go to **[Admin settings \> Billing](https://claude.ai/admin-settings/billing)**.

3.  Click the pencil icon under **Seats**.

4.  Enter your new seat counts.

5.  Review your changes carefully before confirming.

6.  Click "Upgrade" to finalize.

For details on how seat purchases are billed, see **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-usage-based-enterprise-plans)**

------------------------------------------------------------------------

## Reducing your seat allocation

Seats cannot be removed from your total allocation on Enterprise plans during your annual term. However, you can:

- Reassign users between seat types within your existing allocation.

- Remove members from your organization (the seat remains available for reassignment).

If you need to discuss adjusting your seat allocation, contact your account manager or **[reach out to our Sales team](https://claude.com/contact-sales)**.

------------------------------------------------------------------------

## Assigning and reassigning seat types

You can move users between Chat and Chat + Claude Code seats within your existing allocation.

### How to reassign a user's seat type

1.  Go to **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

2.  Find the member you want to reassign.

3.  Click the dropdown under **Seat Type**.

4.  Select Chat or Chat + Claude Code.

Members moved from Chat + Claude Code to Chat will lose Claude Code access, and vice versa.

### Using "unassigned" to swap users between seat types

The unassigned option allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

**Example:** You have ten Chat + Claude Code seats, all assigned. You want to move User A (currently on Chat + Claude Code) to Chat, and move User B (currently on Chat) to Chat + Claude Code—without purchasing an additional seat.

1.  Go to Admin settings \> Organization.

2.  Find User A and change their seat type to "Unassigned." This frees up one Chat + Claude Code seat.

3.  Find User B and change their seat type to "Chat + Claude Code." They now occupy the freed seat.

4.  Find User A and change their seat type to "Chat."

**Note:** Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat.

### What if I don't have an available seat?

If you try to reassign a user to Chat + Claude Code but don't have any available seats of that type, you'll be prompted to purchase an additional Chat + Claude Code seat.

### Seat assignment with JIT or SCIM provisioning

**[Users provisioned via JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans)** are automatically assigned to the highest-available seat type when they're added. Admins and above can manually reassign seat types afterward in **[Admin settings \> Organization](https://claude.ai/admin-settings/organization)**.

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat type.

------------------------------------------------------------------------

## Information for seat-based Enterprise plans

Some Enterprise organizations are on seat-based plans with a different billing model than usage-based Enterprise plan. If you see "Standard" and "Premium" seats in your account, this section applies to you.

**Note:** Only existing Enterprise organizations use the seat-based billing model. All new Enterprise organizations will use the usage-based billing model.

### Seat types

[TABLE]

### Managing seats

You can reassign users between Standard and Premium seats using the **[same process described above](#h_4e79d93003)**—just select "Standard" or "Premium" instead of "Chat" or "Chat + Claude Code" in the seat type dropdown.

### Billing and extra usage

Seat-based Enterprise plans charge a flat monthly fee per seat that includes usage limits. Owners can enable extra usage to allow team members to continue working after reaching their seat's usage limits. Refer to **[Extra usage for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)** for additional details about extra usage.

For specific information about seat-based Enterprise pricing, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.

### Migrating to usage-based Enterprise

If you're on a seat-based Enterprise plan and are interested in migrating to the current usage-based billing model, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)

What is the Enterprise plan?

[](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)

How am I billed for my Enterprise plan?

[](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)

Using Claude Code with your Team or Enterprise plan

[](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats-on-team-plans)

Purchasing and managing seats on Team plans

[](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)

Extra usage for Team and seat-based Enterprise plans

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
