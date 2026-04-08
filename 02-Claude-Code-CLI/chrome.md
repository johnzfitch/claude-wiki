---
source_url: "https://code.claude.com/docs/en/chrome.md"
category: "02-Claude-Code-CLI"
fetched_at: "2026-04-08"
---

# Use Claude Code with Chrome (beta)

Connect Claude Code to your Chrome browser to test web apps, debug with console logs, automate form filling, and extract data from web pages.

Claude Code integrates with the Claude in Chrome browser extension to give you browser automation capabilities from the CLI or the VS Code extension. Build your code, then test and debug in the browser without switching contexts.

Claude opens new tabs for browser tasks and shares your browser's login state, so it can access any site you're already signed into. Browser actions run in a visible Chrome window in real time.

> Chrome integration is in beta and currently works with Google Chrome and Microsoft Edge. WSL is not supported.

## Capabilities

- **Live debugging**: read console errors and DOM state, then fix the code
- **Design verification**: build a UI from a Figma mock, open it in browser to verify
- **Web app testing**: test form validation, check for visual regressions, verify user flows
- **Authenticated web apps**: interact with Google Docs, Gmail, Notion, or any app you're logged into
- **Data extraction**: pull structured information from web pages and save locally
- **Task automation**: automate repetitive browser tasks like data entry, form filling
- **Session recording**: record browser interactions as GIFs

## Prerequisites

- Google Chrome or Microsoft Edge
- Claude in Chrome extension v1.0.36+
- Claude Code v2.0.73+
- Direct Anthropic plan (Pro, Max, Team, or Enterprise)

> Not available through third-party providers (Bedrock, Vertex, Foundry).

## Get started

```bash
claude --chrome
```

Or enable from within a session with `/chrome`.

### Enable Chrome by default

Run `/chrome` and select "Enabled by default".

### Manage site permissions

Site-level permissions are inherited from the Chrome extension settings.

## Example workflows

### Test a local web application

```
I just updated the login form validation. Can you open localhost:3000,
try submitting the form with invalid data, and check if the error
messages appear correctly?
```

### Debug with console logs

```
Open the dashboard page and check the console for any errors when
the page loads.
```

### Automate form filling

```
I have a spreadsheet of customer contacts in contacts.csv. For each row,
go to the CRM at crm.example.com, click "Add Contact", and fill in the
name, email, and phone fields.
```

### Draft content in Google Docs

```
Draft a project update based on the recent commits and add it to my
Google Doc at docs.google.com/document/d/abc123
```

### Record a demo GIF

```
Record a GIF showing how to complete the checkout flow, from adding
an item to the cart through to the confirmation page.
```

## Troubleshooting

| Error                                | Cause                                            | Fix                                                             |
| ------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------- |
| "Browser extension is not connected" | Native messaging host cannot reach the extension | Restart Chrome and Claude Code, then run `/chrome` to reconnect |
| "Extension not detected"             | Chrome extension not installed or disabled        | Install or enable in `chrome://extensions`                      |
| "No tab available"                   | Claude tried to act before a tab was ready       | Ask Claude to create a new tab and retry                        |
| "Receiving end does not exist"       | Extension service worker went idle               | Run `/chrome` and select "Reconnect extension"                  |

## See Also

- [Computer use](/en/computer-use)
- [VS Code browser automation](/en/vs-code#automate-browser-tasks-with-chrome)
- [CLI reference](/en/cli-reference)
