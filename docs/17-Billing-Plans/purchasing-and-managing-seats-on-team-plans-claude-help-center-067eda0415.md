---
category: "17-Billing-Plans"
fetched_at: "2026-02-10T10:49:23Z"
source_url: "https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats-on-team-plans"
title: "Purchasing and managing seats on Team plans | Claude Help Center"
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

[](#h_0c44d72ac9)

[](#h_f05a756e78)

[](#h_fb3ba7a230)

[](#h_33a6424e9b)

[](#h_e7a7f4f396)

[](#h_0a21473316)

[](#h_38e04e90d1)

[](#h_b806e2e3f3)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Team Plan](https://support.claude.com/en/collections/9811436-team-plan)

Purchasing and managing seats on Team plans

# Purchasing and managing seats on Team plans

Updated this week

Table of contents

[](#h_0c44d72ac9)

[](#h_f05a756e78)

[](#h_fb3ba7a230)

[](#h_33a6424e9b)

[](#h_e7a7f4f396)

[](#h_0a21473316)

[](#h_38e04e90d1)

[](#h_b806e2e3f3)

Seat management allows Team plan owners to control their organization's seat allocation, assign users to different seat types, and manage billing. For pricing and billing details, see [How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)

**Permissions note:** Only Owners and Primary Owners can purchase seats and access [Admin settings \> Billing](https://claude.ai/admin-settings/billing). Admins and above can reassign seat types for members in [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

For information on adding and removing members from your organization, see [Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans).

------------------------------------------------------------------------

## Understanding seat types

Team plans offer two seat types:

[TABLE]

Organizations can mix and match seat types based on team needs. Assign Premium seats to power users who need more capacity, while keeping other team members on Standard seats.

Your plan has a total seat allocation (e.g., 30 Standard seats and 10 Premium seats). Within that allocation, you can assign and reassign users to different seat types as needed.

------------------------------------------------------------------------

## Purchasing new seats

**Important:** If you want to upgrade an existing member from Standard to Premium, you don't need to purchase a new seat. Use the seat tier reassignment in [Admin settings \> Organization](https://claude.ai/admin-settings/organization) instead — see [Upgrading a Standard seat to Premium](#h_e7a7f4f396) below.

Follow these steps to add seats to your plan's total allocation:

1.  Log in with your Owner or Primary Owner account.

2.  Navigate to [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

3.  Click "Manage" under "Total seats."

4.  In the "Seat breakdown" modal, click "Add or change seats."

5.  Click the "**+**" next to the seat type you want to add (Standard or Premium).

6.  Click "Next" to review your purchase details and confirm the billing impact.

7.  Check the confirmation box before continuing.

8.  Click "Confirm & purchase" to complete the transaction.

**Note:** You can also purchase seats while adding a new member. If you don't have an available seat of the selected type, you'll be prompted to purchase one.

------------------------------------------------------------------------

## Reducing your seat allocation

You can reduce the total number of seats on your Team plan:

1.  Log in with your Owner or Primary Owner account.

2.  Navigate to [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

3.  If needed, remove members or reassign them to free up the seats you want to eliminate.

4.  Click “Manage” under **Total seats**.

5.  Click “Add or change seats” in the **Seat breakdown** modal.

6.  Click the "**-**" next to the seat type you want to reduce.

7.  Click “Next” to review the changes.

8.  Check the confirmation box and click "Confirm & purchase" to complete the change.

------------------------------------------------------------------------

## Assigning and reassigning seat types

You can move users between Standard and Premium seats within your existing allocation.

To reassign a user's seat type:

1.  Go to [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

2.  Find the member you want to reassign.

3.  Click the dropdown under **Seat Tier**.

4.  Select Standard or Premium.

Members moved from Premium to Standard will have lower usage limits, and vice versa.

## Upgrading a Standard seat to Premium

Upgrading a member from Standard to Premium is a reassignment, not a new purchase. You don't need to buy an additional seat unless your Premium allocation is already full.

1\. Go to [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

2\. Find the member assigned to a Standard seat you want to upgrade.

3\. Click the dropdown under **Seat Tier**.

4\. Select "Premium."

If you have no available Premium seats, you'll be prompted to purchase one at this point.

The upgrade is prorated based on your billing cycle, and you'll be charged the price difference immediately.

### What if I don't have an available seat?

If you try to reassign a user to Premium but don't have any available Premium seats, you'll then be prompted to purchase an additional Premium seat.

## Using "unassigned" to swap users between seat types

The unassigned option allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

**Example:** You have five Premium seats, all assigned. You want to move User A (currently on Premium) to Standard, and move User B (currently on Standard) to Premium—without purchasing an additional seat.

1.  Go to [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

2.  Find User A and change their seat tier to "Unassigned." This frees up one Premium seat.

3.  Find User B and change their seat tier to "Premium." They now occupy the available Premium seat.

4.  Find User A and change their seat tier to "Standard."

**Note:** Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat.

## Seat assignment with JIT or SCIM provisioning

[Users provisioned via JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans) are automatically assigned to the highest-available seat type when they're added. Admins and above can manually reassign seat types afterward in [Admin settings \> Organization](https://claude.ai/admin-settings/organization).

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat type.

------------------------------------------------------------------------

## Understanding billing

- **New seats** are prorated based on your billing cycle and charged immediately.

- **Seat type upgrades** (Standard → Premium) are prorated and charged immediately for the price difference.

- **Removing members** does not trigger an immediate credit or refund. The seat becomes available to assign to another member. To reduce your bill, you'll need to reduce your plan's total seat allocation.

For detailed billing calculations and examples, see [How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)

What is the Team plan?

[](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)

How am I billed for my Enterprise plan?

[](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)

Extra usage for Team and seat-based Enterprise plans

[](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)

Managing members on Team and Enterprise plans

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
