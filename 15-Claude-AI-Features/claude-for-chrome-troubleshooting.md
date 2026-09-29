---
title: "Claude in Chrome troubleshooting | Claude Help Center"
source_url: "https://support.claude.com/en/articles/12902405-claude-for-chrome-troubleshooting"
category: "15-Claude-AI-Features"
fetched_at: "2026-09-29T06:31:55Z"
tags: ["claude-ai", "claude-code", "desktop"]
---

# Claude in Chrome troubleshooting

August 12, 2026


This article helps you resolve common issues with Claude in Chrome and explains how to provide feedback.

Claude in Chrome is available for all paid plans (Pro, Max, Team, and Enterprise). It's generally available in Claude Cowork and Claude Code, and in beta in the Chrome browser. On Max and Team plans, the side panel runs as a Claude Cowork session, and this is rolling out to Pro plans in the coming weeks. On Enterprise plans, the side panel runs as a Cowork session once your admin has enabled Cowork in the cloud; until then, it uses the classic experience.

## The side panel looks different than it used to

On Max and Team plans, on Pro plans as the rollout reaches you, and on Enterprise plans where an admin has enabled it, the side panel now runs as a Claude Cowork session, so it uses the same interface as Cowork on the web and desktop. Your conversations are saved to your history and can be reopened on your other devices. The Cowork side panel also defaults to "Automatically approve" mode, so Claude works continuously and pauses only when an action needs your approval.

If you'd rather use the previous side panel, click the three dots in the upper right corner and select "Switch back to classic." For details, see **[Get started with Claude in Chrome](getting-started-with-claude-for-chrome.md)**.

## I don't see the Cowork side panel

- If you're on an Enterprise plan, the Cowork side panel requires your admin to enable Cowork in the cloud and Claude in Chrome for your organization. Contact your admin, or see **[Claude in Chrome admin controls](../13-Enterprise-Admin/claude-for-chrome-admin-controls.md)**.

- If you're on a Pro plan, the Cowork side panel may not have reached your account yet. The rollout is in progress.

## Claude can't see the webpage

- Refresh the page and ensure the extension is enabled.

- Check that you've granted permission for the current site.

- Some sites with heavy JavaScript may require a moment to fully load.

## Actions aren't working correctly

- Ensure you're using the latest version of Chrome.

- **[Disable other extensions](https://support.google.com/chrome_webstore/answer/2664769?hl=en)** that might interfere with webpage interaction.

- Try refreshing the page and starting the task again.

## Extension won't install or sign in

- Verify you have an active paid plan subscription (Pro, Max, Team, or Enterprise).

- If you're on a Team or Enterprise plan, confirm with your admin that the extension is enabled for your organization.

- Clear your browser cache and cookies for claude.ai (see **[Delete cookies from a site](https://support.google.com/chrome/answer/95647?sjid=5857968454187791521-NC#zippy=%2Cdelete-cookies-from-a-site)**).

- Try signing out and back into your Claude account.

## Performance issues

- Close unnecessary tabs to free up browser resources.

- Consider breaking complex tasks into smaller steps.

## Claude can't access a website

- Check that you've granted permission for the site (see **[Claude in Chrome permissions guide](claude-for-chrome-permissions-guide.md)**).

- The site may be in Claude's default blocked categories (financial services, banking, investment platforms, cryptocurrency exchanges, adult content, pirated content).

- If you're on a Team or Enterprise plan, your admin may have restricted access to this site. Contact your admin for more information.

## The extension won’t connect to Claude Desktop or Claude Code

- Start by restarting or updating the Chrome extension if it isn’t connecting to Claude Code or Claude Desktop.

- If the Claude in Chrome toggle isn’t active in your desktop app Connector settings, restart or update Claude Desktop.

- Restart or update Claude Code if the extension won’t connect to it.

------------------------------------------------------------------------

## Usage limits

Usage limits apply across different interfaces, so using Claude in Chrome will count against the same plan limits that apply to Claude or Claude Code. Browser interactions are more compute-intensive than regular chats with Claude, so you can expect the extension to use more of your limit. With the long-running workflow capabilities, tasks can continue for extended periods, which may use more of your usage allocation. The Cowork side panel defaults to "Automatically approve" mode, which runs extra safety checks on each action and uses more of your usage limit than the other modes.

------------------------------------------------------------------------

## Give feedback

Your feedback directly shapes how we improve Claude's browser capabilities and safety measures.

### How to report issues

- **Thumbs up/down** on Claude's responses in the side panel.

- **Report suspected prompt injection** if Claude behaves unexpectedly.

  - **Email [\[email protected\]](https://support.claude.com/cdn-cgi/l/email-protection#275254425554464142535e674649534f5548574e440944484a)** to report any safety issues or unexpected behaviors.

- **[Contact Support](../21-Account-Support/how-can-i-contact-support.md)** for technical issues or account problems.

### What we're learning

- Which websites work best with Claude

- Common failure modes and how to prevent them

- Most valuable use cases for browser use

- Effective safety measures that don't disrupt workflow

- Types of attempted malicious attacks

**Note:** Features and functionality may change as we develop this feature based on user feedback and safety considerations.
