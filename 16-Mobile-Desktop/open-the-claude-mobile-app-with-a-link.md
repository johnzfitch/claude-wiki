---
title: "Open the Claude mobile app with a link | Claude Help Center"
source_url: "https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link"
category: "16-Mobile-Desktop"
fetched_at: "2026-09-29T06:30:53Z"
tags: ["desktop", "mobile"]
---

# Open the Claude mobile app with a link

May 6, 2026


The Claude mobile apps for iOS and Android respond to the `claude://` URL scheme. Third-party apps, shortcuts, and web pages can use these links to open the Code tab, jump to an existing session, or prefill the new-session composer. All parameter values must be URL-encoded.

These links require Claude Code access on your account. If you don't have access to Claude Code, the links won't work.

## Open the Code tab

`claude://code`

Opens the Code tab on the session list.

## Open an existing Code session

`claude://code/{session-id}`

Opens an existing Claude Code session by ID. If the ID is unknown, you'll land on the session list.

## Open a new Code session

`claude://code/new`

With optional parameters: `claude://code/new?q=Fix%20the%20failing%20test&repo=anthropics%2Fclaude-code&branch=main`

Opens the new-session composer, optionally prefilled. All parameters are optional.

[TABLE]

The **[desktop-only folder and file parameters](open-claude-desktop-with-a-link.md)** are ignored on mobile.

## Universal links

The same Code routes are also reachable via **[https://claude.ai/code/](https://claude.ai/code/)...** universal links. If the app is installed, the operating system opens it; otherwise the link opens in the browser.

[TABLE]
