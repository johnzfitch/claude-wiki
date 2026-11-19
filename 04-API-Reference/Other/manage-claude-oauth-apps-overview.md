---
title: "Claude Platform OAuth - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/oauth-apps/overview"
category: "04-API-Reference/Other"
fetched_at: "2026-11-18T06:27:32Z"
tags: ["api", "oauth"]
---

# Claude Platform OAuth

Copy page



Let your customers pay for the Claude usage in your product from their own Claude organization.

Copy page





Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.

Claude Platform OAuth lets your users bill their Claude organization for usage within your app.

## What you can build

### Let customers pay for their own Claude usage

When your product calls Claude, the usage can be billed to your customers’ own Claude organization. Your users click a **Link your Claude organization** button, sign in to Claude, and approve your app. For Linked billing, the user must have the Admin or Billing role in their Claude organization.

After that:

- You choose on each Claude API request whether the customer pays or you pay.
- If a request you mark for the customer can’t be billed to them, the Claude API rejects it rather than billing you.
- The customer can unlink your app at any time.
- You may bill a customer only for the requests they direct you to make, never for your own usage.

You support your customers: Anthropic provides the approval page and the Claude Console page where they set a spend cap or unlink your app, and all other questions about your app come to you.

Linked billing works for customers whose Claude organization pays Anthropic directly for its API usage. It doesn’t work for organizations billed through a cloud marketplace. See [Linked billing](manage-claude-oauth-apps-organization-billing-connections.md).

## How it works

Linked billing follows a short round trip. The person leaves your product for Claude’s approval page once, approves your app there, and comes back:

The approval page shows your app’s name and what your app is asking for, so the person knows what they’re approving.



If you’ve worked with OAuth before: Claude Platform OAuth uses the OAuth 2.0 authorization code flow with PKCE, with Anthropic as the authorization server.

## One-time OAuth app setup

Linked billing starts with these one-time setup steps in the Claude Console. The [Linked billing](manage-claude-oauth-apps-organization-billing-connections.md#setup-process) guide walks you through them.

1.  **Create the app.** A member of your Claude organization with the Admin role creates an OAuth app in the Claude Console and copies its client ID. The app holds the name that people see on the approval page, and the address in your product that they return to.
2.  **Set up client authentication.** Instead of a client secret, your back end proves that a request comes from your app with a short-lived token from your own identity provider, such as AWS, Google Cloud, Microsoft Entra ID, or Kubernetes. You select the identity provider, and which of its tokens to accept, on the app’s **Client authentication** tab.
3.  **Set up your back end’s identity.** Create a service account and a second federation rule with [Workload Identity Federation](manage-claude-workload-identity-federation.md), and select the service account as the app’s operator service account.

## Next steps

The Linked billing guide walks you through setup and your first linked customer.

[Linked billing](manage-claude-oauth-apps-organization-billing-connections.md)

Let your customers pay for the Claude usage in your product from their own Claude organization



[OAuth reference](manage-claude-oauth-apps-oauth-reference.md)

Endpoints, parameters, token responses, lifetimes, and errors
