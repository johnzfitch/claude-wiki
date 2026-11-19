---
title: "Plan identity and sign-in | Claude Help Center"
source_url: "https://support.claude.com/en/articles/18466091-plan-identity-and-sign-in"
category: "21-Account-Support"
fetched_at: "2026-11-18T06:28:10Z"
tags: ["account"]
---

# Plan identity and sign-in


A Claude Desktop on 3P deployment has several separate sign-ins, and most can use a different identity system. List them before you schedule your move. If you're also changing identity providers (IdPs), the order of the two projects matters, because by default claude.ai accepts one IdP at a time.

This guide is for admins of organizations on Claude Enterprise plans.

This article is part of **[Move from Claude Enterprise to Claude Desktop on a cloud provider](https://support.claude.com/en/articles/18426225)**, which defines the terms wave, overlap period, and cutoff date.

## Sign-ins your users will see

[TABLE]

## Connect your IdP to your cloud provider

Each provider's setup guide explains how to connect your IdP.

- **Amazon Bedrock:** Make your IdP **[the identity source for IAM Identity Center](https://claude.com/docs/third-party/claude-desktop/bedrock)**. AWS allows **[only one identity source per organization in AWS Organizations](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html)**. Before you change it, read AWS's **[considerations for changing your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-considerations.html)**.

- **Google Cloud:** Use **[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)** with **[an OIDC provider in the pool](https://claude.com/docs/third-party/claude-desktop/vertex)**. A pool can federate one or more IdPs.

- **Microsoft Foundry:** Foundry uses **[Entra ID directly](https://claude.com/docs/third-party/claude-desktop/foundry)**. If you have Conditional Access rules, see **[Sign in through the OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker)**.

- **LLM gateway:** Users sign in to **[your IdP](https://claude.com/docs/third-party/claude-desktop/gateway)**, and your gateway checks each user's token.

## If you're changing IdPs

- **By default, claude.ai takes one IdP.** **[Each parent organization links to one IdP](important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning.md)**, and **[all verified domains must use it](set-up-single-sign-on-sso.md)**. The exception is a beta: parent organizations enrolled in centralized management can **[connect more than one IdP](../15-Claude-AI-Features/set-up-multiple-identity-providers-and-split-domains.md)**. A domain can't get a second IdP while any organization uses JIT provisioning, or while Microsoft Login is turned on for that domain. Outside the beta, you can't run the old and new IdPs side by side there.

- **Follow our steps for switching IdPs.** See **[Switching to a different Identity Provider (IdP)](../15-Claude-AI-Features/switching-to-a-different-identity-provider-idp.md)**. Resetting the SSO connection signs out all users. They can sign in by email link until the new connection is live. For Entra ID, see **[Microsoft Entra ID SSO setup](../13-Enterprise-Admin/microsoft-entra-id-sso-setup.md)**.

- **Make sure email addresses match exactly.** Claude **[matches SSO logins to seats by email](../13-Enterprise-Admin/microsoft-entra-id-sso-scim-email-mismatch.md)**. A mismatch in the new IdP **[creates duplicate accounts](../15-Claude-AI-Features/switching-to-a-different-identity-provider-idp.md)**, and a SCIM email change **[removes the old user and creates a new one](../13-Enterprise-Admin/how-scim-sync-works-for-enterprise-organizations.md)**. Fix mismatches before anyone imports.

- **Check whether your Enterprise Admin Console organization shares the connection.** If it **[uses the existing SSO connection, SCIM directory, and verified domains](https://claude.com/docs/third-party/claude-desktop/admin-console)**, one IdP serves both. Before you reset SSO or close the older organization, ask your Anthropic account team how it affects the Enterprise Admin Console organization and the devices it manages.

We recommend this order:

1.  Connect the new IdP to your cloud provider first, and pilot sign-in there. On AWS, if IAM Identity Center already uses the old IdP, this step replaces that organization's one identity source. You can't pilot the two side by side in the same AWS organization.

2.  If the old IdP will stay in service long enough, leave the claude.ai SSO connection alone until the last wave has imported.

3.  If the old IdP retires sooner, make the switch between waves. Don't switch while a wave is importing. Compare the email attributes in both IdPs first.

4.  Keep claude.ai sign-in and member data export working until the final import is done.

## Settings for the overlap period

- **Sign-in screen:** Users can choose claude.ai or your provider configuration. **[`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/mdm#restrict-a-device-to-one-deployment-mode)** set to `3p` hides the claude.ai option (Claude Desktop 4.16336.0 or later). Set it in a device profile that also sets your connection. For earlier versions, also set `disableDeploymentModeChooser` to `true`. You can't set either key in the console. Don't set them on a device the console manages, because they **[make the app stop using the console](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile)**.

- **Organization lock:** **[`forceLoginOrgUUID`](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile)** limits standard sign-in on the device to your organization. It also accepts **[a list of organization IDs](../13-Enterprise-Admin/enterprise-configuration-for-claude-desktop.md)**. With the console, include your Enterprise Admin Console organization's ID as well as your Claude Enterprise organization's, and update devices to 2.37337.0 or later first. Otherwise, the console's settings don't apply.

- **Network allowlist:** **[Tenant Restrictions](../13-Enterprise-Admin/enforce-network-level-access-control-with-tenant-restrictions.md)** uses a header that lists allowed organization IDs. Make sure it includes every organization your users still sign in to.

- **Users in two organizations:** A console user who also belongs to another organization is **[asked whether to switch, and each switch restarts the app](https://claude.com/docs/third-party/claude-desktop/admin-console)**. Turn on **Require this organization in Claude Desktop** so users can't dismiss the prompt. If your Claude Enterprise organization blocks other accounts in Claude Desktop, first add the Enterprise Admin Console organization's ID to its Allowed organizations list.

- **Claude Code CLI:** List both providers in `allowedProviders` during the overlap period. **[`CLAUDE_CONFIG_DIR`](../02-Claude-Code-CLI/authentication.md)** gives each account its own configuration directory.
