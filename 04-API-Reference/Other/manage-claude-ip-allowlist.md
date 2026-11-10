---
title: "IP allowlisting - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/ip-allowlist"
category: "04-API-Reference/Other"
fetched_at: "2026-11-06T06:27:04Z"
tags: ["api", "enterprise"]
---

# IP allowlisting

Copy page



Secure your organization by limiting access to specific IP addresses that you trust.

Copy page



IP allowlisting protects your organization by only allowing [covered requests](#where-the-allowlist-applies) to come from specific IP ranges. This means that if an API key is leaked, it is much harder for an attacker to use the key. This can prevent data leaks and reduce the likelihood of being charged for abusive use.

An allowlist limits where a key works, but not for how long. You should also set a short [key expiration](manage-claude-authentication.md#key-expiration), or move to [Workload Identity Federation](manage-claude-workload-identity-federation.md) to stop using static keys. This is safer than allowlisting alone.



IP allowlisting is available in beta under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.

## How it works

An organization admin or owner sets up a list of IP ranges in settings. This list of ranges covers your entire organization. For each covered request, Anthropic compares the request’s public IP address with your list, and denies it if it is not allowed.

- **API requests** to [covered endpoints](#where-the-allowlist-applies) from an address outside the list are rejected. For example, the Messages API returns a 403 `permission_error` with the message `Your IP address isn't in this organization's allowed range.`
- **People** who connect from a disallowed address see a page titled **Your current network can’t access this organization**. Organization admins are also blocked, but you can optionally [give admins a way back in](#avoid-locking-yourself-out) to avoid lockout, in which case they can access only the allowlist settings.

## Claude Platform organizations

### Where the allowlist applies

- **The Claude Console:** UI access is restricted.
- **The following Claude API endpoints:** [Messages](../Endpoints/messages.md), [Message Batches](../Guides/build-with-claude-batch-processing.md), [Token Counting](../Guides/build-with-claude-token-counting.md), [Models](../Endpoints/models-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return., [Files](../Guides/build-with-claude-files.md), and [Skills](../Guides/build-with-claude-skills-guide.md), with an API key or a Workload Identity Federation token.
- **The following Claude Managed Agents endpoints:** [Agents](managed-agents-agent-setup.md), [Sessions](managed-agents-sessions.md), [Environments](managed-agents-environments.md), [Vaults](managed-agents-vaults.md), and [Memory stores](managed-agents-memory.md), with an API key or a Workload Identity Federation token.
- **The following organization APIs:** The [Admin API](manage-claude-admin-api.md) and the [Compliance API](manage-claude-compliance-api.md), with a [key that covers only this organization](manage-claude-admin-api-keys.md#which-key-do-you-need).

See also [Limitations](#limitations).

## Claude Enterprise organizations

A Claude Enterprise organization has its own IP allowlist, which only allows access to the [apps that it covers](#apps-that-the-allowlist-covers) from specific IP ranges. This means that if a user’s sign-in is stolen, it is much harder for an attacker to use it. This list covers your entire organization, owners included. Owners and primary owners can set it up. Before you [turn on the allowlist](#turn-on-the-allowlist), read [Avoid locking yourself out](#avoid-locking-yourself-out).

### Apps that the allowlist covers

Users outside the list lose access to your organization in:

- Claude in a browser, the desktop apps, and the mobile apps
- [Claude Code](../../01-Getting-Started/overview.md), when users sign in with their Claude account
- Claude in Chrome, the [Office add-ins](https://claude.com/docs/office-agents/overview), [Cowork](https://claude.com/docs/cowork/overview), and Remote Tools

This includes connectors and artifacts in these apps, except artifacts that a user shared outside the organization. For Claude Science, see [Identity and access in the Claude Science admin controls](https://claude.com/docs/claude-science/admin-controls#identity-and-access).

The allowlist also covers the [Admin API](manage-claude-admin-api.md) and the [Compliance API](manage-claude-compliance-api.md), with a [key that covers only this organization](manage-claude-admin-api-keys.md#which-key-do-you-need).

See also [Limitations](#limitations).

### What users can expect

On the web and in the desktop apps, blocked users see a page titled **Your current network can’t access this organization**. Owners are also blocked, but you can optionally [give owners a way back in](#avoid-locking-yourself-out) to avoid lockout, in which case they can access only the allowlist settings. In Claude Code, blocked users see a 403 API error with the message `Your IP address isn't in this organization's allowed range.`

- **Other accounts:** Blocked users can still sign in and use other organizations or a personal account.
- **Remote users:** Phones on mobile data, home Wi-Fi, and laptops off the VPN are blocked until they connect through a listed network.
- **Proxies:** Some features connect through `bridge.claudeusercontent.com`: Claude in Chrome, Cowork, Remote Tools, and [work across apps](https://claude.com/docs/office-agents/work-across-apps) in the Office add-ins. If your proxy sends that host out through a different address from `claude.ai` and `api.anthropic.com`, list that address too.

## Limitations

- **Claude Platform:** The allowlist covers requests to the [Claude Managed Agents](managed-agents-overview.md) endpoints, not the agents themselves. It doesn’t apply to any networking in the Claude Managed Agents runtime. The allowlist doesn’t apply to [Claude in Amazon Bedrock](../Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), [Claude Models on Google Cloud](../Guides/build-with-claude-claude-models-on-google-cloud-overview.md), or [Claude in Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md).
- **Claude Enterprise:** Claude Design, Claude in Slack, and Claude Academy aren’t covered. If Claude is working on a task in a chat when a user is blocked, the task can continue for up to 24 hours. The user can’t open or control that chat from outside the list.

## Turn on the allowlist

1.  1

    ### Turn on the toggle

    Go to your organization’s settings page:

    - **Claude Platform:** The [Identity and access](https://platform.claude.com/settings/identity) page in the Claude Console
    - **Claude Enterprise:** [claude.ai \> Organization settings \> Organization and access](https://claude.ai/admin-settings/organization#ip-allowlist)

    Turn on the **IP allowlist** toggle. Nothing changes until you save.

2.  2

    ### Add your ranges and save

    Click **Add entry** (Claude Console) or **Add IP range** (claude.ai), enter one or more addresses or ranges, separated by commas, and press Enter. List each network that your servers, CI, and users connect from, including the one you’re connecting from. Anthropic recommends making sure the **Allow admins to access this settings page from any IP address** (Claude Console) or **Allow owners to access this settings page from any IP address** (claude.ai) checkbox is selected to [avoid lockout](#avoid-locking-yourself-out). Then click **Save** and confirm.

3.  3

    ### Check your traffic

    Changes can take up to 15 minutes to apply. Watch your applications for 403 `permission_error` responses, including jobs that run only daily or weekly, and add any address that you missed. In a Claude Enterprise organization, ask users on each network to confirm that they can still open Claude. There, changes can take longer to reach connections that are already open, the Office add-ins, and Remote Tools.

### Entry format

- **Format:** You can allowlist IPv4 or IPv6 addresses. Each entry can be a single address (`203.0.113.5`) or a CIDR range (`203.0.113.0/24`, `2001:db8::/32`) no broader than `/8` for IPv4 or `/32` for IPv6. The list holds up to 1,000 entries.
- **Public addresses only:** List the addresses that your traffic leaves your network from, not private ranges such as `10.0.0.0/8`. If you add a shared proxy address, note that an attacker with a leaked key or a stolen sign-in could potentially use it through the proxy.

## Avoid locking yourself out

When you save, the settings page checks your current address against the list to make sure you aren’t about to lock yourself out. But it does not check your servers, your teammates, or the address you might connect from tomorrow.

- **Make sure to list every network first:** Include data centers, CI systems, offices, VPNs, proxies, and the workers of any [self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md), with their public IPv4 and IPv6 addresses. Note that home and mobile addresses can often change without notice.
- **Keep a way back in:** Anthropic recommends selecting the **Allow admins to access this settings page from any IP address** (Claude Console) or **Allow owners to access this settings page from any IP address** (claude.ai) checkbox. Then an admin (an owner in claude.ai) can fix the list from anywhere. The downside is that an attacker who compromises an admin’s or owner’s session could update the allowlist from a remote location. If you [set up the Compliance API](manage-claude-compliance-api-access.md) for your organization, its [Activity Feed](manage-claude-compliance-activity-feed.md) records changes to the allowlist, so you can audit them.

### If you are locked out

In a Claude Enterprise organization, admins can’t change the list, so “admin or owner” in these steps means an owner or primary owner.

1.  **Reconnect from a listed network:** Connect to your office network or VPN, and then click **Try again**. If there is no **Try again** button, reload the page.
2.  **Ask another admin or owner:** An admin or owner on a listed network can add your address.
3.  **Fix the list from where you are:** If you are an admin or owner and the checkbox under [Keep a way back in](#avoid-locking-yourself-out) is selected, open the Claude Console or Claude in a browser and click **Open IP allowlist**, or go to the [Identity and access](https://platform.claude.com/settings/identity) page ([Organization and access](https://claude.ai/admin-settings/organization#ip-allowlist) in claude.ai). Click **Add it** to add your current address, or turn off the allowlist, and then click **Save** and confirm. Access can take up to 15 minutes to return.
4.  **Contact Anthropic:** If no admin or owner can reach the page, ask [Anthropic support](https://support.claude.com) to turn off the allowlist.
