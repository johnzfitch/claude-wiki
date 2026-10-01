---
title: "Set up SCIM in Claude for Government | Claude Help Center"
source_url: "https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government"
category: "13-Enterprise-Admin"
fetched_at: "2026-09-30T06:32:52Z"
tags: ["enterprise"]
---

# Set up SCIM in Claude for Government

August 6, 2026


System for Cross-domain Identity Management (SCIM) lets your identity provider automatically manage user accounts in Claude for Government. With SCIM, your IdP controls who has access, what role they hold, and what seat tier they're assigned—without manual intervention in the Claude admin console.

For SCIM setup on Claude Enterprise, see **[Set up JIT or SCIM provisioning](setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans.md)**.

## How SCIM differs for Claude for Government

Claude for Government uses a first-party SCIM implementation hosted within the FedRAMP-authorized environment. The commercial Claude Enterprise plan uses a different SCIM backend.

[TABLE]

## Prerequisites

Before setting up SCIM, you must complete:

1.  **SSO configuration** — Complete the steps outlined in the SSO setup guide.

2.  **Domain verification** — Your login domain must be verified (this is completed during SSO setup).

3.  **IdP admin access** — Permission to configure a SCIM integration in your identity provider.

## How provisioning works with and without SCIM

Without SCIM, Claude for Government uses just-in-time (JIT) provisioning: any user who authenticates through SSO is automatically assigned a seat, as long as licenses are available. You control who can authenticate by managing membership in the SAML application within your IdP.

With SCIM, login and provisioning are separate. Your IdP tells Anthropic who should have access and at what role/tier. SSO is used only for authentication. This gives you fine-grained control over roles, seat tiers, and offboarding.

### Step 1: Generate a SCIM API key

1.  Navigate to claude.fedstart.com/admin-settings/identity.

2.  In the SCIM section, generate a new API key.

3.  Copy the key — you'll need it when configuring your IdP.

**Important**: Store this key securely. It cannot be retrieved after you leave the page.


### Step 2: Configure SCIM in your Identity Provider

1.  In your IdP (e.g., Entra ID, Okta), create or open a SCIM provisioning integration.

2.  Enter the following values:

    1.  **SCIM endpoint URL:** `https://claude.fedstart.com/v1/scim/v2`

    2.  **API key / Bearer token:** The key generated in Step 1

3.  Configure the user attributes your IdP will sync (typically name and email).

4.  Assign users and groups to the SCIM integration within your IdP.

### Step 3: Verify sync status

After enabling the integration in your IdP:

1.  Return to the identity settings page at claude.fedstart.com/admin-settings/identity.

2.  Check the SCIM sync status indicator to confirm users are syncing.

**Warning**: When you fully enable SCIM provisioning, any users who were **not** synced via SCIM will be removed from the organization. Confirm that all expected users appear in the sync before proceeding.


### Step 4: Map groups to roles and seat tiers

SCIM provisioning uses IdP groups to assign roles and seat tiers within Claude for Government.

1.  On the identity settings page, open the role mappings table.

2.  For each IdP group, assign:

    1.  Role — The user's role within the organization (e.g., Member, Owner).

    2.  Seat tier — The license tier, if your organization has purchased multiple tiers.

3.  Save your mappings.


If you manage multiple organizations under a single parent (see below), each organization maintains its own role and seat tier mappings. Switch between organizations using the organization selector in the bottom-left corner of the page.

### Parent organizations (multi-org setups)

Every Claude for Government organization belongs to a **parent organization**. For most customers, this is transparent—a parent is created automatically during provisioning and contains a single child organization.

Parent organizations become relevant when multiple organizations share a login domain. Common scenarios include:

- **Regional offices** that purchase Claude for Government independently but share an email domain.

- **Sub-departments** within an agency that require data separation (e.g., preventing cross-org sharing of chats or projects).

In a multi-org setup:

- Identity settings (IdP configuration and SCIM) are managed at the **parent organization** level.

- Role and seat tier mappings are configured **per child organization**, allowing different groups to map to different orgs.

- Any Owner or Primary Owner in a child organization can manage IdP settings. Restrict these roles to centralized IT staff.

**Note:** Anthropic support will work with you during provisioning to configure parent/child organization relationships. Contact your account representative or **[our Support team](../15-Claude-AI-Features/how-to-get-support-for-claude-for-government-claude-help-center.md)** if you need to set up a multi-org structure.
