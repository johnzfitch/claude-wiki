---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans"
---


Seat management allows Enterprise plan Owners to control their organization's seat allocation and assign users to different seat types. For pricing and billing details, see How am I billed for my Enterprise plan?

Permissions note: Only Owners and Primary Owners can purchase seats and access Admin settings > Billing. Admins and above can reassign seat types for members in Admin settings > Organization.

For information on adding and removing members from your organization, see Managing members on Team and Enterprise plans.

 

 

Understanding seat types

Usage-based Enterprise plans offer two seat types:

Seat type

 

What's included

Chat

 

Claude on web, desktop, and mobile apps

Chat + Claude Code

 

Everything in Chat, plus Claude Code access

Organizations can mix and match seat types based on team needs. Assign Chat + Claude Code seats to developers and technical team members who need terminal-based coding workflows, while keeping other team members on Chat seats.

 

Your plan has a total seat allocation (e.g., 50 Chat seats and 20 Chat + Claude Code seats). Within that allocation, you can assign and reassign users to different seat types as needed.

Note for seat-based Enterprise plans: Some Enterprise organizations on older plans may see "Standard" and "Premium" seat types instead. See Information for seat-based Enterprise plans at the end of this article.

 

 

Purchasing seats

Enterprise plans require a minimum of 20 seats. You can add seats at any time.

Log in with your Owner or Primary Owner account.

Go to Admin settings > Billing.

Click the pencil icon under Seats.

Enter your new seat counts.

Review your changes carefully before confirming.

Click "Upgrade" to finalize.

For details on how seat purchases are billed, see How am I billed for my Enterprise plan?

 

 

Reducing your seat allocation

Seats cannot be removed from your total allocation on Enterprise plans during your annual term. However, you can:

Reassign users between seat types within your existing allocation.

Remove members from your organization (the seat remains available for reassignment).

If you need to discuss adjusting your seat allocation, contact your account manager or reach out to our Sales team.

 

 

Assigning and reassigning seat types

You can move users between Chat and Chat + Claude Code seats within your existing allocation.

 

How to reassign a user's seat type

Go to Admin settings > Organization.

Find the member you want to reassign.

Click the dropdown under Seat Type.

Select Chat or Chat + Claude Code.

Members moved from Chat + Claude Code to Chat will lose Claude Code access, and vice versa.

 

Using "unassigned" to swap users between seat types

The unassigned option allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

 

Example: You have ten Chat + Claude Code seats, all assigned. You want to move User A (currently on Chat + Claude Code) to Chat, and move User B (currently on Chat) to Chat + Claude Code—without purchasing an additional seat.

Go to Admin settings > Organization.

Find User A and change their seat type to "Unassigned." This frees up one Chat + Claude Code seat.

Find User B and change their seat type to "Chat + Claude Code." They now occupy the freed seat.

Find User A and change their seat type to "Chat."

Note: Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat.

What if I don't have an available seat?

If you try to reassign a user to Chat + Claude Code but don't have any available seats of that type, you'll be prompted to purchase an additional Chat + Claude Code seat.

 

Seat assignment with JIT or SCIM provisioning

Users provisioned via JIT or SCIM are automatically assigned to the highest-available seat type when they're added. Admins and above can manually reassign seat types afterward in Admin settings > Organization.

 

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat type.

 

 

Information for seat-based Enterprise plans

Some Enterprise organizations are on seat-based plans with a different billing model than usage-based Enterprise plan. If you see "Standard" and "Premium" seats in your account, this section applies to you.

Note: Only existing Enterprise organizations use the seat-based billing model. All new Enterprise organizations will use the usage-based billing model.

 

Seat types

Seat type

 

What's included

Standard

 

Core seat-based Enterprise plan features and usage limits

Premium

 

Everything in Standard, plus access to Claude Code and higher usage limits

Managing seats

You can reassign users between Standard and Premium seats using the same process described above—just select "Standard" or "Premium" instead of "Chat" or "Chat + Claude Code" in the seat type dropdown.

 

Billing and extra usage

Seat-based Enterprise plans charge a flat monthly fee per seat that includes usage limits. Owners can enable extra usage to allow team members to continue working after reaching their seat's usage limits. Refer to Extra usage for Team and seat-based Enterprise plans for additional details about extra usage.

 

For specific information about seat-based Enterprise pricing, reach out to your Anthropic Contact or our Sales team.

 

Migrating to usage-based Enterprise

If you're on a seat-based Enterprise plan and are interested in migrating to the current usage-based billing model, reach out to your Anthropic Contact or our Sales team.

Related Articles
What is the Enterprise plan?
How am I billed for my Enterprise plan?
Using Claude Code with your Team or Enterprise plan
Purchasing and managing seats on Team plans
Extra usage for Team and seat-based Enterprise plans