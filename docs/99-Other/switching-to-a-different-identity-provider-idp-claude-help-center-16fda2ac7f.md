---
category: "99-Other"
fetched_at: "2026-02-10T10:49:36Z"
source_url: "https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp"
title: "Switching to a different Identity Provider (IdP) | Claude Help Center"
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

[](#h_382efe77a7)

[](#h_92a0a82c14)

[All Collections](/en/)

[Identity Management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)

Switching to a different Identity Provider (IdP)

# Switching to a different Identity Provider (IdP)

Updated today

Table of contents

[](#h_382efe77a7)

[](#h_92a0a82c14)

This guide walks you through the process of migrating your Claude or Console organization from one identity provider to another while preserving user access and avoiding disruption.

**Note:** This process applies to organizations that already have SSO configured. If you're setting up SSO for the first time, see **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**.

## Before you begin

- Confirm you have the required role:

  - **For Team or Enterprise plans:** You must be an Owner or Primary Owner.

  - **For Claude Console:** You must be an Admin.

- Notify your users in advance that they will be temporarily signed out during the migration.

- Schedule the switch during a low-disruption period.

- Ensure that the SSO and SCIM email attribute for all users in your new IdP exactly matches what was used with your previous IdP. If these email addresses don't match exactly, users will be provisioned with duplicate accounts.

## Steps to switch your IdP

1.  **Disable SCIM pushes from your current IdP** (if applicable): Stop Create/Update events on your current IdP's side to prevent any sync signals from being sent during the migration.

    1.  For more information about SCIM, see **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**.

2.  **Switch provisioning mode to Manual** (if applicable): Wait approximately one hour after disabling SCIM pushes, then navigate to the "Identity and access" page on **all** connected Claude (claude.ai/admin-settings/identity) or Console (platform.claude.com/settings/identity) organizations. Under **Global SSO Configuration**, set the provisioning mode to Manual.

    1.  This stops SCIM from automatically managing users—users remain in the organization but are no longer subject to SCIM events.

3.  **Delete the SCIM directory** (if applicable): Click "Manage SCIM" \> "Delete Directory." When in Manual mode, deleting the directory will not trigger directory sync events, including user deprovisioning.

4.  **Reset the SSO connection**: Click "Manage SSO" \> "Reset Connection."

    1.  **Important:** This will sign out all users. They will be able to **[sign in via email link](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account#h_869b162f56)** until the new IdP is configured for SSO.

5.  **Verify the reset**: Refresh the "Identity and access" page and confirm that the button state has changed from "Manage SSO" to "Setup SSO."

6.  **Set up your new IdP for SSO and provisioning**: Follow the **[SSO setup steps](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** and **[configure JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)** with group mappings enabled (if needed) to ensure all users are assigned in the new IdP with the correct groups for all your connected Claude and/or Console organizations. If applicable, after setup you can click "Manage SCIM" to verify which users have synced to the directory and confirm they're associated with the correct groups.

7.  **Re-enable provisioning** (if applicable): Switch the provisioning mode to Just-in-Time (JIT) or Directory Sync (SCIM) and click "Save Changes" to apply.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)

Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

[](https://support.claude.com/en/articles/11139094-getting-started-with-claude-for-education-at-your-university-for-owners-admins)

Getting Started with Claude for Education at Your University (for Owners/Admins)

[](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)

Setting up single sign-on (SSO)

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)

Managing members on Team and Enterprise plans

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
