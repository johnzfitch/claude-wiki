---
category: "13-Enterprise-Admin"
source_url: "https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning"
---


JIT provisioning is available for Team plans, Enterprise plans, and Console organizations. SCIM provisioning is available for Enterprise and Console organizations only.

This guide covers how to configure user provisioning and role assignment for your Claude or Claude Console organization.

 

Before you begin: This guide assumes you have already completed the steps in Setting up Single Sign-On (SSO), including domain verification and SSO configuration with your Identity Provider (IdP), and you have an Admin (Console) or Owner (Claude) role.

 

 

Step 1: Choose your provisioning mode

Once SSO is configured, you need to decide how users will be provisioned to your organization. This is controlled by the Provisioning mode setting in your Identity and access settings.

 

Provisioning options

Manual is the default. Users are added and removed directly in Claude or Console settings.

 

JIT (Just-in-Time): Users assigned to your Anthropic IdP app are automatically provisioned when they first log in. This option is available to all plans.

 

SCIM: Users are automatically provisioned and deprovisioned based on assignments in your IdP, without requiring them to log in first. SCIM is available for Enterprise plans and Console organizations with their own parent organization or joined to an Enterprise parent organization. SCIM is not available for Team plans or Console organizations joined to a Team plan's parent organization.

 

Provisioning behavior overview

Use this table to help decide which provisioning mode is right for your organization:

Mode

 

Provisioning

 

Role and seat tier changes

 

Removal

Manual

 

Users are manually added

 

Roles and seat tiers are manually changed

 

Users are manually removed

JIT

 

Users assigned to your IdP app are provisioned at login with the User role

 

Roles and seat tiers are manually changed

 

Manual removal required: users removed from your IdP app can no longer log in, but remain in the user list until they attempt to log in or are removed

JIT + advanced group mappings

 

Users in at least one mapped group are provisioned at login with the highest-permissioned role from their group memberships

 

Roles and seat tiers update on next login based on group membership

 

Users without group access can't log in but remain in the list until login attempt or manual removal

SCIM

 

Users assigned to your IdP app are automatically provisioned to all organizations joined to your parent org.

 

Roles and seat tiers are manually changed

 

Users removed from your IdP app are automatically removed

SCIM + advanced group mappings

 

Users in at least one mapped group are automatically provisioned with appropriate roles

 

Role and seat tier changes automatically propagate based on group membership

 

Automatic removal when group access is revoked

Both JIT and SCIM can be combined with Advanced Group Mappings to control role or seat tier assignment based on IdP group membership.

 

Available roles and seat tiers

Product

 

Roles

 

Seat tiers

Team plan / Seat-based Enterprise plan

 

Owner, Admin, User

 

Premium, Standard

Usage-based Enterprise plan

 

Owner, Admin, User

 

Chat, Chat + Claude Code

Console

 

Admin, Developer, Billing, Claude Code User, User

 

—

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for Team plans and Enterprise plans.

 

 

Step 2: Set up SCIM directory sync (if using SCIM)

Note: Skip this step if you're using Manual or JIT provisioning.

If you chose SCIM as your provisioning mode, you need to establish the connection between your Identity Provider and Anthropic before enabling it.

Navigate to your Identity and access settings in Claude (claude.ai/admin-settings/identity) or Console (platform.claude.com/settings/identity)

In the “Global SSO Configuration” section, click “Setup SCIM” (or “Manage SCIM”) next to "Directory sync (SCIM)."

Follow the WorkOS setup guide to configure SCIM in your Identity Provider. You'll need to copy values from WorkOS into your IdP's Anthropic application.

‼️ When you reach the IdP Group step, pause to review Steps 3 and 4 of this guide, alongside the other guides.

 

For IdP-specific JIT / SCIM setup instructions, see:

Okta SAML / OKTA SCIM

Entra ID SAML / Entra ID SCIM

Google SAML / Directory Sync 

OneLogin SAML / OneLogin SCIM

JumpCloud SAML / JumpCloud SCIM 

See additional IdPs here

Once your IdP is connected, continue to Step 3.

 

 

Step 3: Configure provisioning mode and Advanced Group Mappings

In the Organization SSO Configuration section of your Identity and access settings, find Provisioning mode.

Select your chosen option from the dropdown (“Just in time (JIT)” or “Directory sync (SCIM)”).

Toggle on Advanced group mappings if using.

Important: Do NOT click “Save changes” yet. You must first ensure all users are assigned to your Anthropic application in your IdP. For Advanced Group Mappings, users must also be assigned to the appropriate groups (Steps 4 and 5). Saving before users are properly assigned will result in those users being deprovisioned from the organization.

If you are not using Advanced Group Mappings: Ensure all users are assigned to your Anthropic application in your IdP for SCIM provisioning, then click “Save changes” to complete your setup.

 

 

Step 4: Configure groups and assign users in your Identity Provider for Advanced Group Mappings

Create groups in your IdP for each role and seat tier you want to assign. 

While there are no longer naming requirements for these groups, we recommend including something in the group name (e.g., anthropic-claude- or anthropic-console-) to make them easier to identify.

Add users to the groups you created, ensuring at least one user (including yourself) is in a group that will be mapped to an Admin (Console) or Owner (Claude) role.

Important: All users who need access must be assigned to the appropriate groups before you save your Advanced Group Mappings configuration in the next step. These users should already be assigned to your Anthropic application in your IdP from when you enabled SSO.

 

 

Step 5: Map groups to roles and seat tiers

Return to your Identity and access settings in Claude or Console, and toggle Advanced group mappings on (if it’s not already).

In the Role mappings section, click “Add” next to each role and select the corresponding group from your IdP in the dropdown.

For Claude organizations: In the Seat tier mappings section, click “Add” next to each tier (Premium, Standard) and select the corresponding group. If a user isn't assigned to a seat tier group, they will be assigned to the highest available tier by default.

Verify all necessary groups are mapped to the appropriate roles and seat tiers.

Click “Save changes.”

Note: Microsoft Entra only pushes SCIM changes every 40 minutes, so there may be a delay before changes appear.

 

 

Troubleshooting
Users assigned correctly and showing in the directory but aren’t being added to the Claude as members? 

Verify you have enough seats purchased and available to add members to your org. 

Check “Total seats” shown on the Organization page and purchase additional seats if needed (see our guides for Team plans and Enterprise plans).

Once you have available seats, go back to the Identity and access page and click “Sync now,” next to Directory sync (SCIM). This will trigger a sync to provision accounts for those users not yet added as members.

 

Users aren't being provisioned with the correct role

Verify the user is assigned to the correct group in your IdP.

Verify the group is mapped to the correct role in your Identity and access settings.

For JIT: The user needs to log out and log back in for role changes to take effect.

For SCIM: Click "Sync Now" to prompt an immediate sync, or wait for the automatic sync cycle.

 

I lost Admin/Owner access after enabling Advanced Group Mappings

This happens when the person configuring Advanced Group Mappings isn't assigned to a group mapped to an Admin or Owner role, causing their permissions to be downgraded to User. To fix this:

 

Option 1: Have another Admin/Owner reinstate your role

Contact another Admin or Owner of your organization.

Ask them to navigate to Admin settings > Organization (for Claude) or Settings > Members (for Console).

Have them change your role back to Admin or Owner.

 

Option 2: Fix via your Identity Provider

In your IdP, assign yourself to a group with the correct prefix that maps to an Admin or Owner role.

For JIT: Log out and log back in to regain access.

For SCIM: Ask another Admin or Owner to click "Sync Now" in the Identity and access settings, or wait for the automatic sync cycle.

Related Articles
Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning
Setting up Single Sign-on (SSO)
Managing members on Team and Enterprise plans
Purchasing and managing seats on Enterprise plans
Switching to a different Identity Provider (IdP)