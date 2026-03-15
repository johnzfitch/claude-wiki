---
category: "21-Account-Support"
fetched_at: "2026-03-15T04:10:35Z"
source_url: "https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans"
title: "Set up JIT or SCIM provisioning | Claude Help Center"
---

# Set up JIT or SCIM provisioning

Updated yesterday


JIT provisioning is available for Team plans, Enterprise plans, and Console organizations. SCIM provisioning is available for Enterprise and Console organizations only.

This guide covers how to configure user provisioning and role assignment for your Claude or Claude Console organization.

**Before you begin:** This guide assumes you have already completed the steps in **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**, including domain verification and SSO configuration with your Identity Provider (IdP), and you have an Admin (Console) or Owner (Claude) role.

------------------------------------------------------------------------

## Step 1: Choose your provisioning mode

Once SSO is configured, you need to decide how users will be provisioned to your organization. This is controlled by the **Provisioning mode** setting in **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Identity and access](https://claude.ai/admin-settings/identity)**.

### Provisioning options

**Invite only** is the default. Users are added and removed directly in Claude or Console settings.

**Approve automatically (JIT):** Users assigned to your Anthropic IdP app are automatically provisioned when they first log in. This option is available to all plans.

**Sync with SCIM:** Users are automatically provisioned and deprovisioned based on assignments in your IdP, without requiring them to log in first. SCIM is available for Enterprise plans and Console organizations with their own parent organization or joined to an Enterprise parent organization. SCIM is not available for Team plans or Console organizations joined to a Team plan's parent organization.

### Provisioning behavior overview

Use this table to help decide which provisioning mode is right for your organization:

[TABLE]

Both JIT and SCIM can be combined with **Enable group mappings** to control role or seat tier assignment based on IdP group membership.

### Available roles and seat tiers

[TABLE]

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

------------------------------------------------------------------------

## Step 2: Set up SCIM directory sync (if using SCIM)

**Note:** Skip this step if you're using Invite only or JIT provisioning.

If you chose SCIM as your provisioning mode, you need to establish the connection between your Identity Provider and Anthropic before enabling it.

1.  Navigate to your Identity and access settings in Claude (**[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)**) or Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identit)**)

2.  In the **Global access settings** section, click “Setup SCIM” (or “Manage SCIM”) next to **Directory sync (SCIM)**.

3.  Follow the WorkOS setup guide to configure SCIM in your Identity Provider. You'll need to copy values from WorkOS into your IdP's Anthropic application.

**‼️ When you reach the IdP Group step, pause to review Steps 3 and 4 of this guide, alongside the other guides.**

For IdP-specific JIT / SCIM setup instructions, see:

- **[Okta SAML](https://workos.com/docs/integrations/okta-saml)** / **[OKTA SCIM](https://workos.com/docs/integrations/okta-scim)**

- **[Entra ID SAML](https://workos.com/docs/integrations/entra-id-saml)** / **[Entra ID SCIM](https://workos.com/docs/integrations/entra-id-scim)**

- **[Google SAML](https://workos.com/docs/integrations/google-saml)** / **[Directory Sync](https://workos.com/docs/integrations/google-directory-sync)**

- **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)** / **[OneLogin SCIM](https://workos.com/docs/integrations/onelogin-scim)**

- **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)** / **[JumpCloud SCIM](https://workos.com/docs/integrations/jumpcloud-scim)**

- See additional IdPs **[here](https://workos.com/docs/integrations)**

Once your IdP is connected, continue to Step 3.

------------------------------------------------------------------------

## Step 3: Configure provisioning mode and enable group mappings

1.  In the **Global access settings** section of your Identity and access settings, find **Provisioning mode**.

2.  Select your chosen option from the dropdown:

    1.  **Invite only**: New members can only join if manually invited by an existing member. SSO access alone won't add them to your org.

    2.  **Approve automatically (JIT)**: Allow people with SSO access to join when they first log in. Each new member uses one of your available seats.

    3.  **Sync with SCIM**: Add or remove members automatically as your directory changes. Your org always stays current.

3.  Toggle on **Enable group mappings** if using.

    1.  **Important:** Do NOT click “Save changes” yet. You must first ensure all users are assigned to your Anthropic application in your IdP. When you enable group mappings, users must also be assigned to the appropriate groups (Steps 4 and 5). Saving before users are properly assigned will result in those users being deprovisioned from the organization.

4.  **If you are not using group mappings:** Ensure all users are assigned to your Anthropic application in your IdP for SCIM provisioning, then click “Save changes” to complete your setup.

------------------------------------------------------------------------

## Step 4: Configure groups and assign users in your Identity Provider for group mappings

1.  Create groups in your IdP for each role you want to assign. Unless you're on the single-seat Enterprise plan, create groups for each seat type as well.

    1.  While there are no longer naming requirements for these groups, we recommend including something in the group name (e.g., `anthropic-claude-` or `anthropic-console-`) to make them easier to identify.

2.  Add users to the groups you created, ensuring at least one user (including yourself) is in a group that will be mapped to an Admin (Console) or Owner (Claude) role.

**Important:** All users who need access must be assigned to the appropriate groups before you save your group mappings configuration in the next step. These users should already be assigned to your Anthropic application in your IdP from when you enabled SSO.

------------------------------------------------------------------------

## Step 5: Map groups to roles and seat types

1.  Return to your Identity and access settings in Claude or Console, and toggle **Enable group mappings** on (if it’s not already).

2.  In the **Enable group mappings** section, click “Add” next to each role and select the corresponding group from your IdP in the dropdown.

3.  **For all plans except single-seat Enterprise:** In the **Assign seat tiers to IdP groups** section, click "Add" next to each seat type and select the corresponding group from your IdP. If a user isn't assigned to a seat type group, they will be assigned to the highest available type by default.

    1.  **For single-seat Enterprise:** Seat type mapping does not apply. All provisioned users are automatically assigned an Enterprise seat, provided one is available in your organization.

4.  Verify all necessary groups are mapped to the appropriate roles and seat types.

5.  Click “Save changes.”

**Note:** Microsoft Entra only pushes SCIM changes every 40 minutes, so there may be a delay before changes appear.

------------------------------------------------------------------------

## Troubleshooting

### Users assigned correctly and showing in the directory but aren’t being added to the Claude as members?

Verify you have enough seats purchased and available to add members to your org.

1.  Check the number of available seats shown in **[Organization](https://claude.ai/admin-settings/organization)** **[settings \> Billing](https://claude.ai/admin-settings/billing)** and purchase additional seats if needed (see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**).

2.  Once you have available seats, go back to the Identity and access page and click “Sync now,” next to **Directory sync (SCIM)**. This will trigger a sync to provision accounts for those users not yet added as members.

### Users aren't being provisioned with the correct role

1.  Verify the user is assigned to the correct group in your IdP.

2.  Verify the group is mapped to the correct role in your Identity and access settings.

3.  **For JIT:** The user needs to log out and log back in for role changes to take effect.

4.  **For SCIM:** Click "Sync Now" to prompt an immediate sync, or wait for the automatic sync cycle.

### I lost Admin/Owner access after enabling group mappings

This happens when the person configuring group mappings isn't assigned to a group mapped to an Admin or Owner role, causing their permissions to be downgraded to User.

To fix this:

**Option 1: Have another Admin/Owner reinstate your role**

1.  Contact another Admin or Owner of your organization.

2.  Ask them to navigate to **[Organization settings \> Organization](https://claude.ai/admin-settings/organization)** (for Claude) or **[Settings \> Members](https://platform.claude.com/settings/members)** (for Console).

3.  Have them change your role back to Admin or Owner.

**Option 2: Fix via your Identity Provider**

1.  In your IdP, assign yourself to a group with the correct prefix that maps to an Admin or Owner role.

2.  **For JIT:** Log out and log back in to regain access.

3.  **For SCIM:** Ask another Admin or Owner to click "Sync Now" in the Identity and access settings, or wait for the automatic sync cycle.

------------------------------------------------------------------------

Related Articles


Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning


Set up single sign-on (SSO)


Manage members on Team and Enterprise plans


Purchase and manage seats on Enterprise plans


Switching to a different Identity Provider (IdP)
