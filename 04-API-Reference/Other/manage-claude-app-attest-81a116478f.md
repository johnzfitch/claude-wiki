---
title: "App Attest for iOS and macOS apps - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/app-attest"
category: "04-API-Reference/Other"
fetched_at: "2026-09-29T06:30:39Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [SDKs, CLI, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fapp-attest)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)

[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Authentication

# App Attest for iOS and macOS apps

Copy page



Let genuine installations of your iOS or macOS app call the Claude API without shipping an API key or running a proxy, using Apple's App Attest service.

Copy page



App Attest authenticates iOS and macOS apps that call the Claude API directly from the device, with usage billed to your workspace. This page explains how App Attest works, how to register your app in the Claude Console, and how to revoke an app integration.

Apps use App Attest through the [Claude for Foundation Models](https://github.com/anthropics/ClaudeForFoundationModels) Swift package, which is in beta: it requires the OS 27 betas, and APIs might change during the beta. For the Swift configuration, see [Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#app-attest-production).

## How App Attest works

Each installation of your app uses Apple's [App Attest](https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity) service to prove that it is a genuine, unmodified build of the app you registered. Anthropic then issues the device a short-lived access token that bills usage to your workspace. The app ships no API key, and there is no proxy for you to operate.

App Attest authentication is available only when your app calls the Claude API directly. It is not available through Amazon Bedrock, Google Cloud, or Microsoft Foundry.

The first time your app uses Claude on a device, the app requests a challenge from Anthropic, attests the device with Apple's `DCAppAttestService`, and exchanges the verified attestation for an access token. The Claude for Foundation Models package runs this flow automatically and requests new tokens as they expire; there is no attestation code for you to write.

Tokens are scoped to your workspace, expire after one hour, and authorize only [Messages API](/docs/en/api/messages/create) calls. They carry no end-user identity: App Attest identifies your app, not the person using it, so handle any per-user logic in your app.

## Set up App Attest



App Attest requires a physical device. The Simulator, and hardware without a Secure Enclave, cannot perform App Attest. While developing in the Simulator, authenticate with an [API key](/docs/en/manage-claude/authentication#api-keys) instead.

To set up App Attest, you need your Apple Developer Team ID and the admin, owner, or primary owner role in your organization. Configure your Xcode project and register your app in the [Claude Console](https://platform.claude.com/):

1.  In Xcode, add the **App Attest** capability to your app target under **Signing & Capabilities**.
2.  In your workspace's settings in the Claude Console, open **App integrations**.
3.  Click **Create app integration** and enter a name, your Apple Developer Team ID, and one or more bundle IDs (up to 32).
4.  Copy the client ID (`clid_...`) from the integration's **Overview** tab and pass it to your app's Claude configuration.

## Revoke an app integration

To stop a compromised or retired app, revoke its integration: in your workspace's settings in the Claude Console, open **App integrations**, select the integration, and click **Revoke**, then confirm. Revoking an integration revokes its outstanding tokens, and its registered devices can no longer request new ones. Revocation is permanent, so create a new app integration to restore access.

## Next steps



[Apple Foundation Models](/docs/en/cli-sdks-libraries/libraries/apple-foundation-models#app-attest-production)

Configure App Attest in the Claude for Foundation Models Swift package



[Authentication](/docs/en/manage-claude/authentication)

Compare API keys, Workload Identity Federation, and App Attest
