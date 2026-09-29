---
title: "App Attest for iOS and macOS apps - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/app-attest"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:30:39Z"
tags: ["api"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fapp-attest)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](../Guides/build-with-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](usage-limits.md)

[Admin](manage-claude-admin-api.md)Authentication

# App Attest for iOS and macOS apps

Copy page



Let genuine installations of your iOS or macOS app call the Claude API without shipping an API key or running a proxy, using Apple's App Attest service.

Copy page



App Attest authenticates iOS and macOS apps that call the Claude API directly from the device, with usage billed to your workspace. This page explains how App Attest works, how to register your app in the Claude Console, and how to revoke an app integration.

Apps use App Attest through the [Claude for Foundation Models](https://github.com/anthropics/ClaudeForFoundationModels) Swift package, which is in beta: it requires the OS 27 betas, and APIs might change during the beta. For the Swift configuration, see [Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md#app-attest-production).

## How App Attest works

Each installation of your app uses Apple's [App Attest](https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity) service to prove that it is a genuine, unmodified build of the app you registered. Anthropic then issues the device a short-lived access token that bills usage to your workspace. The app ships no API key, and there is no proxy for you to operate.

App Attest authentication is available only when your app calls the Claude API directly. It is not available through Amazon Bedrock, Google Cloud, or Microsoft Foundry.

The first time your app uses Claude on a device, the app requests a challenge from Anthropic, attests the device with Apple's `DCAppAttestService`, and exchanges the verified attestation for an access token. The Claude for Foundation Models package runs this flow automatically and requests new tokens as they expire; there is no attestation code for you to write.

Tokens are scoped to your workspace, expire after one hour, and authorize only [Messages API](../Endpoints/messages-create.md) calls. They carry no end-user identity: App Attest identifies your app, not the person using it, so handle any per-user logic in your app.

## Set up App Attest



App Attest requires a physical device. The Simulator, and hardware without a Secure Enclave, cannot perform App Attest. While developing in the Simulator, authenticate with an [API key](manage-claude-authentication.md#api-keys) instead.

To set up App Attest, you need your Apple Developer Team ID and the admin, owner, or primary owner role in your organization. Configure your Xcode project and register your app in the [Claude Console](usage-limits.md):

1.  In Xcode, add the **App Attest** capability to your app target under **Signing & Capabilities**.
2.  In your workspace's settings in the Claude Console, open **App integrations**.
3.  Click **Create app integration** and enter a name, your Apple Developer Team ID, and one or more bundle IDs (up to 32).
4.  Copy the client ID (`clid_...`) from the integration's **Overview** tab and pass it to your app's Claude configuration.

## Revoke an app integration

To stop a compromised or retired app, revoke its integration: in your workspace's settings in the Claude Console, open **App integrations**, select the integration, and click **Revoke**, then confirm. Revoking an integration revokes its outstanding tokens, and its registered devices can no longer request new ones. Revocation is permanent, so create a new app integration to restore access.

## Next steps



[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md#app-attest-production)

Configure App Attest in the Claude for Foundation Models Swift package



[Authentication](manage-claude-authentication.md)

Compare API keys, Workload Identity Federation, and App Attest
