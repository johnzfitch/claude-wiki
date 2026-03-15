---
category: "17-Billing-Plans"
fetched_at: "2026-03-15T04:10:31Z"
source_url: "https://support.claude.com/en/articles/12005970-manage-extra-usage-for-team-and-seat-based-enterprise-plans"
title: "Manage extra usage for Team and seat-based Enterprise plans | Claude Help Center"
---

4.  Manage extra usage for Team and seat-based Enterprise plans

# Manage extra usage for Team and seat-based Enterprise plans

Updated yesterday


This article explains how Team and seat-based Enterprise plan Owners and Primary Owners can purchase extra usage, allowing members to continue using Claude, Cowork, and Claude Code after reaching usage limits for their assigned seat.

## What is extra usage?

Enabling extra usage allows Team and seat-based Enterprise plan members on Standard and Premium seats to continue working with Claude, Cowork, and Claude Code after reaching their included usage limits. Instead of being blocked upon hitting limits, members can keep working without interruption by purchasing extra usage.

**Important:** Extra usage doesn't apply to current usage-based Enterprise plans. On those plans, there's no included usage allowance to run out of—all usage is billed at API rates from the first token. For details on how usage and spend limits work on usage-based plans, see **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

------------------------------------------------------------------------

## How extra usage works

After an organization Owner or Primary Owner configures your account for extra usage, you’ll start using this as soon as you reach your seat's usage limit. Your subsequent usage will be billed at standard API pricing rates as you continue working.

**For Team plans:** Owners can pre-purchase extra usage that they can control using spend limits.

**For seat-based Enterprise plans:** Extra usage is billed at the end of each month based on your actual usage during the billing period.

------------------------------------------------------------------------

## Enable extra usage

### For Team owners

1.  Log in to your Team organization as an Owner or Primary Owner.

2.  Navigate to **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Usage](https://claude.ai/admin-settings/usage)**.

3.  Click “Enable” in **Extra usage** to turn this on for your organization.

4.  You’ll be prompted to pay for extra usage.

5.  Next, you’ll see the option to enable auto-reload; choose “Reload when balance reaches” and enter the amount to reload.

6.  Set a monthly spend limit to apply organization-wide.

7.  Enable extra usage for specific users or the entire organization.

### For seat-based Enterprise owners

1.  Log in to your seat-based Enterprise organization as an Owner or Primary Owner.

2.  Navigate to **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Usage](https://claude.ai/admin-settings/usage)**.

3.  Click “Enable” in **Extra usage** to turn this on for your organization.

4.  You’ll be prompted to set monthly spend limits for the organization as a whole, by seat tier, or for individual members.

### How can members switch to extra usage once it's enabled?

Once an organization owner has enabled extra usage:

1.  Continue using Claude or Claude Code normally.

2.  When you reach your usage limit and choose to continue working, your extra usage will be tracked and billed according to your plan type.

------------------------------------------------------------------------

## Organization-wide spend limits

Owners and Primary Owners of Team and seat-based Enterprise plans can set organization-wide spend limits to ensure predictable costs while providing flexibility for critical work.

### Spend limits

After navigating to **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Usage](https://claude.ai/admin-settings/usage)** and enabling this feature, Owners can set a monthly spend limit on the entire organization's extra usage. Setting a limit here controls total extra usage spend across your whole organization, regardless of individual or seat limits.

The **Usage and spend limits** section will show the current limit (if any) or **Unlimited**. Clicking on “Adjust limit” opens a modal where you can either input an amount and click “Set spend limit,” or click “Set to unlimited” to remove the organization-wide monthly spend limit:


Changes to your organization’s overall spend limit go into effect immediately.

### Seat spend limits for seat-based Enterprise plans

Owners and Primary Owners on **seat-based Enterprise plans only** can set spend limits that apply to all users within a specific seat tier. Clicking the pencil icon next to the current limit for either Standard or Premium users allows you to edit this:


Clicking that icon opens a modal where you can either input an amount and click “Set limit,” or click “Set to unlimited” to remove the limit for that seat type:


------------------------------------------------------------------------

## User-level spend limits

Owners and Primary Owners can also set individual monthly spend limits for each member by finding **Spend limits by user** and clicking the “...” button next to the user, then “Edit limit”:


Enter the amount and click “Set limit.” Alternatively, selecting “Set to unlimited” will remove that member’s monthly spend limit (they will still be subject to any organization or seat-level spend limits).


This allows owners fine control over extra usage, so you can set limits for different members based on their roles or individual needs. Once a user reaches their defined spend limit, this will automatically pause their extra usage until the end of the month. They will need to wait for their usage limits to reset before using Claude again.

Note that the **Spend limits by user** section has a **MTD Spend** column, so you can track members’ usage patterns and optimize seat assignments.

------------------------------------------------------------------------

## Extra usage pricing

Extra usage is billed at standard API rates; see our **[pricing page](https://claude.com/pricing#api)** for details.

------------------------------------------------------------------------

## Request extra usage for seat-based Enterprise plans

Members of seat-based Enterprise plans will see a "Request extra usage" link upon hitting their included usage limit:


Click this to send a request to organization Admins to either switch you to a Premium seat (if you're currently assigned to a Standard seat) or enable extra usage for your user account. This will change to **Request sent to admin** after clicking it, indicating that you submitted a request for a seat tier increase or extra usage to an organization Admin.

Admins and Owners can review these requests in **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Usage](https://claude.ai/admin-settings/usage)**. Clicking into "Review requests" will open a modal where each requester is listed, along with their current seat, and the time they asked for more usage. Click "Increase limit" next to each request you want to approve. Admins and above will also receive a daily email including all your organization's outstanding requests.

### Disable extra usage requests

If you want to prevent users from submitting requests for extra usage, an organization owner can follow these steps:

1.  Navigate to **[Organization settings \> Usage](https://claude.ai/admin-settings/usage)**.

2.  Scroll to the bottom of the page and find **Extra usage requests**.

3.  Toggle it off:


------------------------------------------------------------------------

## Frequently asked questions

### What happens when I reach my extra usage limit?

If your account is configured for extra usage and you exceed your set spend limit, you won’t be able to use Claude, Cowork, or Claude Code again until the next billing period, or until your limits are adjusted.

### Why was I able to exceed my extra usage limit?

It's possible to slightly exceed your defined usage limit. Our system checks if you're within your limit before you're allowed to make a single request or send a message. Once the request is processed, we calculate your token consumption, which means you may bypass your limit with that request. Once this happens, any subsequent requests will be blocked.

### Does extra usage apply to Claude, Cowork, and Claude Code?

Yes, extra usage applies to Claude, Cowork, and Claude Code.

### Can extra usage be disabled completely?

Yes, Owners and Primary Owners can choose to disable extra usage entirely, which means that members of the organization will be unable to continue working once they reach their usage limits and will need to wait for them to reset.\
​

------------------------------------------------------------------------

Related Articles


What is the Enterprise plan?


How am I billed for my Enterprise plan?


Use Claude Code with your Team or Enterprise plan


View usage analytics for Team and Enterprise plans


Purchase and manage seats on Enterprise plans
