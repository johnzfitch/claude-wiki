---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats-on-team-plans"
---


Seat management allows Team plan owners to control their organization's seat allocation, assign users to different seat types, and manage billing. For pricing and billing details, see How is my Team plan bill calculated?

Permissions note: Only Owners and Primary Owners can purchase seats and access Admin settings > Billing. Admins and above can reassign seat types for members in Admin settings > Organization.

For information on adding and removing members from your organization, see Managing members on Team and Enterprise plans.

 

 

Understanding seat types

Team plans offer two seat types:

Seat type

 

What's included

Standard

 

Base features, usage limits, and Claude Code access

Premium

 

Everything in Standard, plus higher usage limits

Organizations can mix and match seat types based on team needs. Assign Premium seats to power users who need more capacity, while keeping other team members on Standard seats.

 

Your plan has a total seat allocation (e.g., 30 Standard seats and 10 Premium seats). Within that allocation, you can assign and reassign users to different seat types as needed.

 

 

Purchasing new seats

Important: If you want to upgrade an existing member from Standard to Premium, you don't need to purchase a new seat. Use the seat tier reassignment in Admin settings > Organization instead — see Upgrading a Standard seat to Premium below.

Follow these steps to add seats to your plan's total allocation:

Log in with your Owner or Primary Owner account.

Navigate to Admin settings > Organization.

Click "Manage" under "Total seats."

In the "Seat breakdown" modal, click "Add or change seats."

Click the "+" next to the seat type you want to add (Standard or Premium).

Click "Next" to review your purchase details and confirm the billing impact.

Check the confirmation box before continuing.

Click "Confirm & purchase" to complete the transaction.

Note: You can also purchase seats while adding a new member. If you don't have an available seat of the selected type, you'll be prompted to purchase one.

 

 

Reducing your seat allocation

You can reduce the total number of seats on your Team plan:

Log in with your Owner or Primary Owner account.

Navigate to Admin settings > Organization.

If needed, remove members or reassign them to free up the seats you want to eliminate.

Click “Manage” under Total seats.

Click “Add or change seats” in the Seat breakdown modal.

Click the "-" next to the seat type you want to reduce.

Click “Next” to review the changes.

Check the confirmation box and click "Confirm & purchase" to complete the change.

 

 

Assigning and reassigning seat types

You can move users between Standard and Premium seats within your existing allocation.

 

To reassign a user's seat type:

Go to Admin settings > Organization.

Find the member you want to reassign.

Click the dropdown under Seat Tier.

Select Standard or Premium.

Members moved from Premium to Standard will have lower usage limits, and vice versa.

 

Upgrading a Standard seat to Premium

Upgrading a member from Standard to Premium is a reassignment, not a new purchase. You don't need to buy an additional seat unless your Premium allocation is already full.

 

1. Go to Admin settings > Organization.

2. Find the member assigned to a Standard seat you want to upgrade.

3. Click the dropdown under Seat Tier.

4. Select "Premium."

 

If you have no available Premium seats, you'll be prompted to purchase one at this point.

 

The upgrade is prorated based on your billing cycle, and you'll be charged the price difference immediately.

 

What if I don't have an available seat?

If you try to reassign a user to Premium but don't have any available Premium seats, you'll then be prompted to purchase an additional Premium seat.

 

Using "unassigned" to swap users between seat types

The unassigned option allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

 

Example: You have five Premium seats, all assigned. You want to move User A (currently on Premium) to Standard, and move User B (currently on Standard) to Premium—without purchasing an additional seat.

Go to Admin settings > Organization.

Find User A and change their seat tier to "Unassigned." This frees up one Premium seat.

Find User B and change their seat tier to "Premium." They now occupy the available Premium seat.

Find User A and change their seat tier to "Standard."

Note: Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat.

 

Seat assignment with JIT or SCIM provisioning

Users provisioned via JIT or SCIM are automatically assigned to the highest-available seat type when they're added. Admins and above can manually reassign seat types afterward in Admin settings > Organization.

 

You can also use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific seat type.

 

 

Understanding billing

New seats are prorated based on your billing cycle and charged immediately.

Seat type upgrades (Standard → Premium) are prorated and charged immediately for the price difference.

Removing members does not trigger an immediate credit or refund. The seat becomes available to assign to another member. To reduce your bill, you'll need to reduce your plan's total seat allocation.

For detailed billing calculations and examples, see How is my Team plan bill calculated?

Related Articles
What is the Team plan?
How am I billed for my Enterprise plan?
Extra usage for Team and seat-based Enterprise plans
Managing members on Team and Enterprise plans
Purchasing and managing seats on Enterprise plans