---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans"
---


This guide covers how to add, remove, and manage the people on your Team or Enterprise plan.

Permissions note: Organization Admins can manage members in Admin settings > Organization, but only Owners and Primary Owners can access Admin settings > Billing. See our article about roles and permissions for more information.

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for Team plans and Enterprise plans.

 

 

Adding members
Adding members by invitation

Note: Pending invitations occupy your available seats immediately; a new member does not need to accept the invite to take up a seat.

Admins and above can add members by following these steps:

Navigate to Admin settings > Organization and click “Add member.”

Enter the person's email address (it must use one of your organization's allowed email domains).

Select the appropriate seat type.

Set the role and permissions for the member.

Click “Add members.”

This sends an email invitation to the person. The invitation expires after 21 days, so you'll need to re-invite them if they don't accept within that time period.

 

Adding multiple members at once: You can invite multiple members by clicking "Bulk add" and typing or pasting email addresses separated by commas or new lines.

Note: If you don't have an available seat of the selected type, you'll be prompted to purchase one. See our guides for Team plans and Enterprise plans for more information.

 

Automated provisioning with SSO

Organizations with single sign-on (SSO) configured can automate member provisioning. Learn more about setting up SSO.

Just-in-time (JIT) provisioning: Members assigned to the Anthropic app in your Identity Provider will have accounts created automatically the first time they log in. Users are assigned to the highest-available seat tier upon first login. Admins and above can manually reassign seat types afterward in Admin settings > Organization.

SCIM provisioning (Enterprise plan only): With SCIM directory sync enabled, members assigned to the Anthropic app in your Identity Provider are provisioned automatically, up to the number of total seats on your plan. Seat tiers are distributed from highest to lowest available. Primary Owners and Owners can reassign seat types afterward in Admin settings > Organization.

Important: An Owner or Primary Owner must ensure seats are available before new users can be provisioned. We recommend monitoring your seat usage and adding seats proactively to ensure uninterrupted access for your team. You can use Advanced Group Mappings with JIT or SCIM to provision users directly to a specific role and seat tier.

 

 

Removing members

You can remove a member by navigating to Admin settings > Organization, clicking the menu button to the right of the member, then selecting "Remove from team."

 

For Enterprise organizations using SCIM provisioning, members are automatically removed from Claude when they are removed from your Identity Provider.

 

When a member is removed:

They lose access to the organization immediately.

The seat they occupied becomes available to assign to another user.

If you re-add the member later using the same email address, their account history will be maintained.

Removing a member frees up their seat for reassignment, but does not automatically reduce your plan's total seat count. See our guides for Team plans and Enterprise plans for information on reducing seats.

Note: You cannot remove yourself as a Primary Owner or Owner. Another Primary Owner or Owner must remove you from the team.

 

 

Managing invitations
Resending an expired invitation

You can resend an invite from Admin settings > Organization. Find the member and select to resend the invite.

 

Revoking a pending invitation

You can revoke a pending invite from Admin settings > Organization. Find the member and select "Remove from team."

 

 

Frequently Asked Questions
Can I invite someone who already uses Claude personally with their work email?

Yes. Once they join your team, they'll have both a personal account and a Team or Enterprise plan account. They can toggle between accounts through the menu by clicking their initials or name in the lower left corner.

 

How do I add a member that I previously removed?

To add a member that you previously removed, follow the same steps as adding a new member. Their account history will be maintained.

 

How do I change the Primary Owner?

The current Primary Owner can transfer ownership by:

Navigate to Admin settings > Organization.

Click the Role dropdown next to the new user and select "Primary Owner."

Type the new Primary Owner's email address in the modal to confirm and transfer ownership.

Important: There can only be one Primary Owner per organization. Following these steps transfers the role to a different user.

What happens to the initial invitation for a new Enterprise organization?

When Anthropic provides a new Enterprise organization and invites the Primary Owner, the same 21-day expiration period applies to that initial invitation. If your invitation has expired, please reach out to your account manager.

Related Articles
Roles and Permissions
Purchasing and managing seats on Team plans
Extra usage for Team and seat-based Enterprise plans
Setting up JIT or SCIM provisioning
Purchasing and managing seats on Enterprise plans