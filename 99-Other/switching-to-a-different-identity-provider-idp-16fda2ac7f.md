---
category: "99-Other"
source_url: "https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp"
---


This guide walks you through the process of migrating your Claude or Console organization from one identity provider to another while preserving user access and avoiding disruption.

Note: This process applies to organizations that already have SSO configured. If you're setting up SSO for the first time, see Setting up Single Sign-On (SSO).

 

Before you begin

Confirm you have the required role:

For Team or Enterprise plans: You must be an Owner or Primary Owner.

For Claude Console: You must be an Admin.

Notify your users in advance that they will be temporarily signed out during the migration.

Schedule the switch during a low-disruption period.

Ensure that the SSO and SCIM email attribute for all users in your new IdP exactly matches what was used with your previous IdP. If these email addresses don't match exactly, users will be provisioned with duplicate accounts.

 

Steps to switch your IdP

Disable SCIM pushes from your current IdP (if applicable): Stop Create/Update events on your current IdP's side to prevent any sync signals from being sent during the migration.

For more information about SCIM, see Setting up JIT or SCIM provisioning.

Switch provisioning mode to Manual (if applicable): Wait approximately one hour after disabling SCIM pushes, then navigate to the "Identity and access" page on all connected Claude (claude.ai/admin-settings/identity) or Console (platform.claude.com/settings/identity) organizations. Under Global SSO Configuration, set the provisioning mode to Manual.

This stops SCIM from automatically managing users—users remain in the organization but are no longer subject to SCIM events.

Delete the SCIM directory (if applicable): Click "Manage SCIM" > "Delete Directory." When in Manual mode, deleting the directory will not trigger directory sync events, including user deprovisioning.

Reset the SSO connection: Click "Manage SSO" > "Reset Connection."

Important: This will sign out all users. They will be able to sign in via email link until the new IdP is configured for SSO.

Verify the reset: Refresh the "Identity and access" page and confirm that the button state has changed from "Manage SSO" to "Setup SSO."

Set up your new IdP for SSO and provisioning: Follow the SSO setup steps and configure JIT or SCIM with Advanced Group Mappings (if needed) to ensure all users are assigned in the new IdP with the correct groups for all your connected Claude and/or Console organizations. If applicable, after setup you can click "Manage SCIM" to verify which users have synced to the directory and confirm they're associated with the correct groups.

Re-enable provisioning (if applicable): Switch the provisioning mode to Just-in-Time (JIT) or Directory Sync (SCIM) and click "Save Changes" to apply.

Related Articles
Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning
Getting Started with Claude for Education at Your University (for Owners/Admins)
Setting up Single Sign-on (SSO)
Setting up JIT or SCIM provisioning
Managing members on Team and Enterprise plans