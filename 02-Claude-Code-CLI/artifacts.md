---
title: "Share session output as artifacts - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/artifacts"
category: "02-Claude-Code-CLI"
fetched_at: "2026-11-17T06:24:29Z"
last_modified: "Tue, 17 Nov 2026 03:16:18 GMT"
tags: ["claude-code", "connectors", "mcp"]
---

## On this page

Back to top

- [When to use an artifact](#when-to-use-an-artifact)
  - [What an artifact is not](#what-an-artifact-is-not)
- [Create an artifact](#create-an-artifact)
  - [When Claude Code asks before publishing](#when-claude-code-asks-before-publishing)
- [Update an artifact](#update-an-artifact)
  - [Turn off one-step artifact updates](#turn-off-one-step-artifact-updates)
- [Find an artifact again](#find-an-artifact-again)
- [Share an artifact](#share-an-artifact)
  - [Link to a specific view](#link-to-a-specific-view)
  - [Let someone edit with you](#let-someone-edit-with-you)
- [Read an artifact shared with you](#read-an-artifact-shared-with-you)
- [Collect comments on an artifact](#collect-comments-on-an-artifact)
  - [Let Claude reply to comments on its own](#let-claude-reply-to-comments-on-its-own)
- [Pull live data with MCP connectors](#pull-live-data-with-mcp-connectors)
  - [How connector calls work for viewers](#how-connector-calls-work-for-viewers)
  - [The page shows no live data for a viewer](#the-page-shows-no-live-data-for-a-viewer)
- [Offer a file download](#offer-a-file-download)
- [What you can build](#what-you-can-build)
  - [Walk through a change](#walk-through-a-change)
  - [Compare alternatives](#compare-alternatives)
  - [Tune with interactive controls](#tune-with-interactive-controls)
  - [Bring the result back to your session](#bring-the-result-back-to-your-session)
  - [Track work in progress](#track-work-in-progress)
- [Improve the visual design](#improve-the-visual-design)
- [Start an artifact from a template](#start-from-a-slides-design-or-docs-template)
  - [Draft a design canvas](#draft-a-design-canvas)
  - [Write a document with Claude Docs](#write-a-document-with-claude-docs)
- [Page constraints](#page-constraints)
- [Availability](#availability)
- [Disable artifacts](#disable-artifacts)
- [Manage artifacts for your organization](#manage-artifacts-for-your-organization)
  - [Enable or disable artifacts](#enable-or-disable-artifacts)
  - [Control connector calls from artifacts](#control-connector-calls-from-artifacts)
  - [Control public sharing](#control-public-sharing)
  - [Set a retention policy](#set-a-retention-policy)
  - [Audit artifact activity with the Compliance API](#audit-artifact-activity-with-the-compliance-api)
  - [Allowlist the viewer domain](#allowlist-the-viewer-domain)
  - [List and delete artifacts with the Compliance API](#list-and-delete-artifacts-with-the-compliance-api)
- [Related resources](#related-resources)

Artifacts

# Share session output as artifacts

Copy pageCopy page

Artifacts turn Claude Code’s work into live, interactive pages on claude.ai that you can keep private, share with your organization, or publish to a public link.

Copy pageCopy page

Artifacts are available on Pro, Max, Ultra, Team, and Enterprise plans and require a session signed in with [`/login`](../01-Getting-Started/setup.md#authenticate). See [Availability](#availability) for the full set of requirements.

An [artifact](https://claude.com/features/artifacts) is a live, interactive web page that Claude Code publishes from your session to a private URL on claude.ai. You open it in a browser, and it updates in place as the session continues. Share it from the page header when you want someone else to see it too.

## [](#when-to-use-an-artifact)When to use an artifact

Use an artifact when terminal text is the wrong medium for what Claude produced: output that is easier to look at and interact with than to read line by line. Claude builds the page from anything your session can reach, including your codebase and data it pulls through your [connected tools](../06-MCP-Tools/General/mcp.md), so the page can show things that would take paragraphs to describe. For example, ask Claude to:

- Walk a reviewer through a pull request with annotated diffs
- Render a dashboard from data the session already pulled
- Lay out several design or implementation options side by side
- Keep an investigation timeline that fills in while a long task runs
- Send a teammate a link instead of pasting output into Slack
- Publish a status board that [pulls fresh data through MCP connectors](#pull-live-data-with-mcp-connectors) each time someone opens it

See [What you can build](#what-you-can-build) for prompts that match these, and [Pull live data with MCP connectors](#pull-live-data-with-mcp-connectors) for the connector-backed board’s prompt.

### [](#what-an-artifact-is-not)What an artifact is not

An artifact is a capture of work: one self-contained page with no backend, so it can’t serve multiple routes. For a hosted internal tool with a backend, deploy it on your own infrastructure instead. See [Page constraints](#page-constraints) for the full set of limits.

## [](#create-an-artifact)Create an artifact

Claude may publish an artifact on its own when the output suits a page, or you can ask for one directly. To ask, name the feature or describe the visual output you want in plain language. A good candidate is anything easier to see than to read as text, such as an annotated diff, a chart, or a set of options to compare. The prompts below are two examples; see [What you can build](#what-you-can-build) for more patterns.

```python
Make an artifact that walks through this PR with the diff annotated inline.
```

```python
Build a dashboard artifact of last week's deploy failures by service and keep it updated as you investigate.
```

Unless you name a location, Claude writes the page to an HTML or Markdown file in a temporary directory outside your project, then publishes it. The artifact stays private to you until you [share it](#share-an-artifact). After the first publish, Claude prints the URL, and your browser opens to the new page.

- **Reopen the page**: press `Ctrl+]` at any time to reopen the session’s most recent artifact
- **See this session’s artifacts**: a `⧉` pill below the prompt shows the artifact’s name, or a count when the session has several. In [fullscreen rendering](fullscreen.md), click it to open the [`/artifacts`](#find-an-artifact-again) list
- **Keep the browser from opening**: set `CLAUDE_CODE_ARTIFACT_AUTO_OPEN=0` in your environment
- **Remote Control**: if you sent the prompt through [Remote Control](remote-control.md) from claude.ai, Claude Desktop, or the Claude mobile app, no tab opens on the machine running the session. The browser opens there the next time Claude publishes the artifact from a prompt you type at the terminal

Claude picks the artifact’s title and a browser-tab icon that matches what the page is, such as a chart or a calendar. The title appears in your [gallery of artifacts](#share-an-artifact) on claude.ai and in shared links. Ask Claude for a specific title or tab icon if you want one. If Claude responds that it can’t publish, or writes a local HTML file without a link, artifacts aren’t enabled for your session. Check the [Availability](#availability) requirements. If the terminal shows `Artifacts need a claude.ai login`, see [that error’s entry](errors.md#artifacts-need-a-claude-ai-login) for how to sign in.

### [](#when-claude-code-asks-before-publishing)When Claude Code asks before publishing

A new artifact that Claude publishes in response to a prompt you type goes through without a permission prompt or classifier review. In these cases Claude Code asks you first, or in [auto mode](permission-modes.md#eliminate-prompts-with-auto-mode) has the classifier review the publish:

| When | What Claude Code does |
|:---|:---|
| The session is in [plan mode](permission-modes.md#analyze-before-you-edit-with-plan-mode) | Asks before the first publish of each artifact |
| The publish declares runtime capabilities for the page, such as [connector calls](#pull-live-data-with-mcp-connectors) or [file downloads](#offer-a-file-download) | Asks before that publish |
| You shared the artifact publicly | Asks once per conversation before changing it, and before each reply to a comment on it |
| Claude publishes in a turn that a [session-scoped scheduled task](scheduled-tasks.md) firing in your session started, rather than a prompt you typed | Asks before the first publish of each artifact |
| Claude can’t read the file without your approval | Asks before publishing it. An allow rule for the `Artifact` tool doesn’t skip this prompt |
| In [Manual](permission-modes.md) or `acceptEdits` mode, Claude makes a small change to an artifact’s file it can’t edit without your approval, such as a project file in Manual mode | Asks before publishing the change. You’re asked even if an allow rule covers the `Artifact` tool, because the edit to the file needs your approval |

To let Claude read a file outside your [working directories](permissions.md#working-directories) without your approval, add its folder as a working directory with [`--add-dir`](cli-reference.md#cli-flags) at launch or `/add-dir` during the session. Claude already reads files in those directories, and in the temporary directory it writes pages to, without asking. If a publish prompt includes a sentence such as `Also makes 1 edit to that file on disk.`, Claude is changing the artifact’s file and publishing it in one step. When you approve the prompt, Claude Code publishes the page, then writes the change to your file.

## [](#update-an-artifact)Update an artifact

Ask Claude to revise the page, or let a long-running task republish as it makes progress. Claude edits the underlying file and publishes again to the same URL.

```python
Add a per-region breakdown below the summary chart and republish.
```

Anyone with the page open sees the update in place. Each publish becomes a version, and from the **Share** control in the page header you can choose which version viewers see. To update an artifact from a different session, give Claude its URL, or attach it with [`/artifacts`](#find-an-artifact-again). Without either, a new session creates a new artifact instead of updating one.

```python
Update https://claude.ai/code/artifact/5fbea6f3-... with today's numbers.
```

### [](#turn-off-one-step-artifact-updates)Turn off one-step artifact updates

A one-step update is a small change Claude makes to an artifact’s file as part of a publish, instead of through an `Edit` or `Write` call. To turn one-step updates off, set [`CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS`](env-vars.md) to `0`. This example adds the variable to the `env` block in `~/.claude/settings.json`:

```python
{
  "env": {
    "CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS": "0"
  }
}
```

Then quit and relaunch Claude Code, because a running session doesn’t reread the variable.

## [](#find-an-artifact-again)Find an artifact again

Run `/artifacts` in Claude Code to list the artifacts you own and the ones shared with you. The current session’s artifacts come first, under **This session**. Select an artifact, then press one of these keys:

- **`Enter`**: opens it in your browser when it’s already attached to the current session, and attaches it when it isn’t
- **`o`**: opens it in your browser
- **`c`**: copies its link
- **`d`**: outside a [cloud session](claude-code-on-the-web.md), permanently deletes an artifact you own after you confirm. Its link stops working for everyone, including you

Claude Code reads the list from your claude.ai account, so `/artifacts` works in a new session and after `/clear`, when an artifact’s link has scrolled out of the terminal.

## [](#share-an-artifact)Share an artifact

A new artifact is visible only to you. To share it, open the artifact in your browser and use the **Share** control in the page header. The header also links to your gallery at [claude.ai/code/artifacts](https://claude.ai/code/artifacts), which lists every artifact you have created. Viewers in your organization can see who published the page: on an artifact shared within your organization, your name is in the title menu, and on a public artifact it’s in the page header for signed-in viewers in your organization. A viewer who opens a public link without signing in, or from outside your organization, sees the label `Content is user-generated and unverified.` instead of your name. Who you can share with depends on your plan:

- **Within your organization**: on Team and Enterprise plans, grant access to specific people in your organization, or to everyone in it. Viewers sign in to claude.ai as members of your organization to see the page.
- **People with access to a shared folder**: on Team and Enterprise plans, move the artifact to a folder that you own or are an editor of. Move it from the [Artifacts page](https://claude.ai/artifacts), which is available if you can use claude.ai chat. Everyone with access to the folder can then open it, and the folder’s owner and editors can change it.
- **Publicly**: share a link that anyone on the internet can open, with no claude.ai sign-in required. On Team and Enterprise plans, public sharing is off until an Owner [enables it for the organization](#control-public-sharing).

### [](#link-to-a-specific-view)Link to a specific view

If a page has several views, such as tabs or sections, you can link to one of them directly. Ask Claude for the links:

```python
Give me a link to each tab of the deploy failures dashboard.
```

Each link is the artifact’s link with an anchor on the end, such as `#overview`.

### [](#let-someone-edit-with-you)Let someone edit with you

People you share with are viewers by default: they see each version you publish but can’t change the page. On Team and Enterprise plans, you can also make someone an editor. In the share dialog, add a person and switch their role from **viewer** to **editor**. An editor publishes new versions the same way you [update the artifact from another session](#update-an-artifact): they give Claude the artifact’s URL, or attach it from [`/artifacts`](#find-an-artifact-again), and Claude pulls the current content and republishes with their changes. Everyone with the page open sees each update live. If an editor publishes while Claude holds an older copy of the page, Claude Code refuses a publish built on that copy. Claude then merges its changes onto the newer version and publishes again.

## [](#read-an-artifact-shared-with-you)Read an artifact shared with you

When someone shares an artifact with you, you can have Claude read it: give Claude its URL, or attach it from [`/artifacts`](#find-an-artifact-again). Claude reads a page someone else wrote the way it reads a web page with [WebFetch](tools-reference.md#webfetch-tool-behavior): it gets a summary of what it asked about rather than the raw page, and the summary reports instructions written into the page instead of relaying them. Claude Code also saves the page’s full source to a local file, which Claude can open when it needs the exact content, such as to republish the artifact as an [editor](#let-someone-edit-with-you). Claude Code asks for your approval before Claude reads the artifact in these cases, in addition to any prompt your permission mode or rules call for:

- **Cloud session without network access**: for a [cloud environment](cloud-environments.md#access-levels), that’s the **None** level. In [auto mode](permission-modes.md#eliminate-prompts-with-auto-mode), the classifier can approve instead; in a [Cowork](../15-Claude-AI-Features/product-cowork.md) session, the approval is yours alone.
- **Another organization’s public artifact**: Claude Code asks you first, even in auto mode. Where Claude Code can’t ask you, such as in `bypassPermissions` mode, Claude can’t read the artifact. Claude can read these artifacts only while [feature-flag fetching](env-vars.md#features-that-need-feature-flag-fetching) is on.
- **Unconfirmed owner or network setting**: when Claude Code can’t confirm who made the artifact, or can’t confirm a cloud session’s network setting, it asks, and your approval covers that one request. In [auto mode](permission-modes.md#eliminate-prompts-with-auto-mode), the classifier can approve or block the read instead of asking you.
- **Plan mode**: in [plan mode](permission-modes.md#analyze-before-you-edit-with-plan-mode), Claude Code asks before the Artifact tool reads an artifact someone else in your organization made.

When Claude reads the artifact with WebFetch, WebFetch’s own [prompting rules](tools-reference.md#webfetch-tool-behavior) still apply.

## [](#collect-comments-on-an-artifact)Collect comments on an artifact

When you share an artifact within your organization, the people you share it with can leave comments on the page, and you can have Claude read those comments and reply to them. You need Claude Code v2.1.221 or later. Claude reads the comments in two cases:

- **You ask Claude to read them**: give Claude the artifact’s URL and ask for the comments. Claude lists each thread and marks the comments someone who can edit the artifact sent to it.
- **Someone who can edit the artifact sends a comment to Claude**: in a thread on the page, they send a comment with **Send to Claude**, or mention `@claude` in one. Either way, they activate the thread.

Claude can reply to or resolve only an activated thread. Other threads stay open until a person resolves them on the page. Viewers see each reply attributed to Claude, via you. If you share an artifact publicly, people whose only access is the public link don’t see its comments and can’t add any. Existing comment threads stay on the artifact, and you and its editors can still read and reply to them. To ask for the comments yourself, give Claude the URL:

```python
Read the comments on https://claude.ai/code/artifact/5fbea6f3-... and make the changes the commenters ask for.
```

If Claude tells you it can’t read comments, confirm your version, your session, and your feature-flag setting:

- You’re running Claude Code v2.1.221 or later.
- You’re not in your first session since you installed Claude Code or upgraded from a version before v2.1.221. In that [first session after an install or upgrade](env-vars.md#first-session-after-an-install-or-upgrade), Claude might not be able to read comments yet; start a new session and ask again.
- You haven’t turned feature-flag fetching off.

### [](#let-claude-reply-to-comments-on-its-own)Let Claude reply to comments on its own

After your session publishes an artifact, Claude Code watches that artifact for comments. When someone who can edit the artifact sends a comment to Claude, it reaches your session right away, and Claude can read the thread and reply without you asking. You need Claude Code v2.1.228 or later. If you turned [feature-flag fetching](env-vars.md#features-that-need-feature-flag-fetching) off, Claude Code doesn’t watch for comments. Your [permission mode](permission-modes.md) decides what Claude does when a sent comment arrives:

- **Claude replies on its own**: if you’re in a permission mode that lets Claude post the reply without asking you, Claude reads the thread and replies. You see `Auto-replied to comment thread on Artifact: <name>`.
- **Claude waits for you**: outside plan mode, when posting the reply [would need your approval](#when-claude-code-asks-before-publishing), you see `Comments are waiting on Artifact: <name>`. Claude then asks you for approval to read the thread, and again to post the reply.
- **Claude pauses in plan mode**: you see `Comments are waiting on Artifact: <name>`, and Claude doesn’t reply until you leave plan mode and ask it to read and reply.

Claude also stops replying on its own to an artifact after it handles 60 sent comments or thread activations on that artifact within an hour. You see `Comments are waiting on Artifact: <name>` once, and Claude picks up again as that hour’s comments age out. Run `/tasks` to see the artifacts your session is watching. `/tasks` groups the watches Claude Code started on its own under the **System tasks** row. Press `Enter` on that row to list them. A watch you asked Claude to start appears under **Monitors**. You can stop Claude from replying on its own in any of these ways:

- **Press Ctrl+C once at an idle, empty prompt**: Claude pauses replying on every artifact your session is watching. Replies start again after you send your next message.
- **Stop the task in `/tasks`**: Claude stops replying on that artifact until you ask it to resume replies there. Publishing the artifact again doesn’t start replies again, and the stop still applies when you resume the session later.
- **Press `Ctrl+X Ctrl+K` twice within 3 seconds**: the chord that [stops every running background subagent](interactive-mode.md#general-controls) also stops Claude from replying on every artifact for the rest of the session. Asking Claude to resume replies doesn’t undo this stop.

A watch that Claude Code started on its own can end after the artifact goes several hours without activity. To start the watch again, publish the artifact again or ask Claude to watch it. If the service that delivers comments becomes unavailable or stops answering, Claude Code keeps trying to reconnect for a while, then stops watching each artifact your session was watching.

## [](#pull-live-data-with-mcp-connectors)Pull live data with MCP connectors

An artifact can call [MCP connectors](../06-MCP-Tools/General/mcp.md#use-mcp-servers-from-claude-ai) each time someone views it, so the page shows current data rather than a snapshot from the session that built it. Connector calls from artifacts are available on Pro, Max, Ultra, Team, and Enterprise plans and require Claude Code v2.1.209 or later. On earlier versions, Claude publishes the page with whatever data the session gathered while building it. To create a connector-backed page, name the connector and the data you want in your prompt:

```python
Build a dashboard artifact of our open pull requests that pulls the live list through my GitHub connector when the page loads.
```

Claude declares which connectors the page may call as part of publishing, and the page can’t call connectors outside that declaration. Only connectors from your claude.ai account qualify: Claude names them in the declaration, and when someone views the page, each call [runs through the viewing account’s own connection](#how-connector-calls-work-for-viewers) to that connector. Local MCP servers you configure in Claude Code, such as servers from `.mcp.json`, can supply data while Claude builds the page, but the published page can’t call them. The page fetches data when it loads and can refresh on an interval or when a viewer uses a refresh control on the page. Responses are cached in the viewer’s browser, so a reopened page renders from the cached responses immediately, then updates with fresh results.

### [](#how-connector-calls-work-for-viewers)How connector calls work for viewers

When a published page calls a connector, the call uses the account of the person viewing the page, not the account of the person who published it:

- **Each viewer uses their own connectors**: calls go through the viewing account’s connected tools, so two people opening the same dashboard can see different data depending on what their accounts can access. The page never sees anyone’s credentials; claude.ai makes the calls on the page’s behalf.
- **Viewers approve access first**: claude.ai asks each viewer for permission before the page’s first connector call. A viewer who declines, or who hasn’t connected a connector the page uses, still sees the page without its live sections.
- **Actions use the viewer’s account too**: a page can offer controls that invoke connector tools with side effects, such as posting a message or updating an issue. The action goes through the account of whoever selects the control.

When you plan to share a connector-backed page, ask Claude to include a fallback message in each live section that names the connector it needs. A viewer who’s missing the connection then sees what to connect instead of an empty section. You can [share a connector-backed page](#share-an-artifact) within your organization or publicly, as your plan and organization settings allow. Connector calls don’t run for a viewer who opens the public link without signing in to claude.ai, or from outside your organization. That viewer sees the page without its live sections.

### [](#the-page-shows-no-live-data-for-a-viewer)The page shows no live data for a viewer

When a connector-backed page renders but its live sections stay empty for a viewer in your organization, work through these causes:

- **The viewer hasn’t connected the connector**: connectors are per-account, so each viewer needs their own connection to every connector the page calls. They can add one at [claude.ai/customize/connectors](https://claude.ai/customize/connectors), then reload the page.
- **The viewer declined the permission ask**: a denial lasts for the rest of that page load. Reloading the page brings the permission ask back.
- **Connector calls are turned off for the organization**: an Owner controls the [**Enable artifact connectors** toggle](#control-connector-calls-from-artifacts) in admin settings.
- **The page calls tool names the connector doesn’t expose**: the affected sections stay empty for everyone, including you. This can happen when a page names the individual tools behind a gateway-style connector that exposes only a few tools of its own. Ask Claude to fix the tool names the page calls and publish it again. When Claude publishes the page and that connector’s tools are available in your session, Claude Code checks the tool names the page declares against them, warns Claude about names that don’t match, and refuses the publish when none do. Before v2.1.265, it published the page without checking them.

## [](#offer-a-file-download)Offer a file download

An artifact can offer viewers a file the page generates, such as a CSV export of a table or a PNG of a chart. The viewer saves it through a download control on the page, such as a button. File downloads are a runtime capability that claude.ai enables per account, so Claude checks whether your account has it before it builds the control. Viewers can’t save a file from an ordinary download link or a script on the page, because the artifact viewer on claude.ai blocks any download the page starts itself, including links to `data:` or `blob:` URLs. If a page has download buttons built that way, ask Claude to rebuild them with the downloads capability. To offer a file, ask for the control and the file format in your prompt:

```python
Add a button that downloads this table as a CSV file.
```

Claude declares the downloads capability as part of publishing, the same way it [declares connectors](#pull-live-data-with-mcp-connectors).

## [](#what-you-can-build)What you can build

An artifact is a single HTML page, so anything you can express in HTML, CSS, and inline JavaScript is in scope. The patterns below come up most often.

### [](#walk-through-a-change)Walk through a change

Ask for a page that renders a diff or a design change with annotations beside the relevant lines, so reviewers can read your reasoning next to the code instead of reconstructing it from a description.

```python
Make an artifact that walks through this PR. Render the diff with margin annotations and color-code findings by severity.
```

### [](#compare-alternatives)Compare alternatives

Ask for several variants on one page so you can evaluate them against each other. This works for layouts, copy, API shapes, or implementation plans.

```python
Make an artifact with four distinctly different layouts for the settings panel. Vary density and grouping, and lay them out as a grid with a one-line tradeoff under each.
```

### [](#tune-with-interactive-controls)Tune with interactive controls

Ask for sliders, toggles, or input fields bound to whatever you are adjusting, so you can explore values directly instead of describing them.

```python
Build an artifact with sliders for the easing curve, duration, and delay so I can try values on this transition. Show the animation live as I move them.
```

### [](#bring-the-result-back-to-your-session)Bring the result back to your session

An artifact can act as a lightweight editor for a decision you then send back to Claude. Ask for an export control that produces text you can paste into the terminal, so the result of interacting with the page flows back into the session instead of staying on the page.

```python
Make a triage board artifact with each open issue as a draggable card across Now, Next, Later, and Cut columns. Add a "Copy as prompt" button that gives me the final ordering to paste back here.
```

### [](#track-work-in-progress)Track work in progress

Ask Claude to keep an artifact current while a long task runs, so anyone with the link can follow along without reading the terminal.

```python
Turn this migration plan into a checklist artifact. Check items off as you complete them and add a note for anything you skip.
```

## [](#improve-the-visual-design)Improve the visual design

Claude applies a built-in design skill when it builds an artifact, so pages get a deliberate palette, typography, and layout without extra prompting. That skill also looks for an existing design system in your project before choosing its own. Design tokens are the named color, typography, and spacing values your design system reuses. To keep artifacts consistent with your product’s branding, record them where Claude can find them, such as the project’s [CLAUDE.md](memory.md) or a theme file in your repository:

```python
## Design system

- Colors: primary #1a4d8f, accent #f59e0b, surface #f8fafc
- Typography: Inter for body, JetBrains Mono for code
- Spacing: 8px scale, 6px border radius
```

Claude treats your design system as higher precedence than its own choices, and your prompt as higher precedence than both. The heading and format above are an example; any clear list of colors, fonts, and spacing works. For typography, Claude can load a typeface from Google Fonts, the one external font source an artifact page can load from. Claude inlines any other typeface as a `@font-face` data URI and gives every typeface a fallback stack, so the page still renders if a font doesn’t load. To use a specific typeface, name it in your prompt or your design system.

## [](#start-from-a-slides-design-or-docs-template)Start an artifact from a template

The [artifact templates](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them#h_11d5a9a5fa) on your claude.ai account also work from Claude Code. For example, use the [Claude Design](../15-Claude-AI-Features/get-started-with-claude-design.md) template for a visual design, or the [Claude Docs](../15-Claude-AI-Features/get-started-with-claude-docs.md) template for a document other people will read and edit. Your account can include others, such as Sheets, Whiteboards, or Data. To see which ones your session has, ask Claude to list the artifact templates available to you. To use a template from Claude Code, you need:

- A session where [artifacts are available](#availability)
- On Team and Enterprise plans, the template turned on for your organization. If it’s off, ask an Owner to [turn the template on](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans#h_6e06d8f1a8) under **Organization settings \> Artifacts** on claude.ai.
- On Enterprise plans with custom roles, a role that [includes the template](https://support.claude.com/en/articles/16994751-artifacts-admin-guide-for-team-and-enterprise-plans#h_d830917488)
- For the Docs and Sheets templates, the [Claude Docs connector](#write-a-document-with-claude-docs), which Claude uses to write the content of both. If you [turned the connector off](../06-MCP-Tools/General/mcp.md#disable-claude-ai-connectors), turn it back on first.
- Claude Code v2.1.265 or later, if you start the Design template with its [`/design` command](#draft-a-design-canvas)

To start from a template, name it or describe what you want, such as “write this plan up as a doc for the team” or “make a shared task spreadsheet”. Claude picks the matching template, fills it from your request and from what the session already has, and gives you the link. To get a file instead, name the format, such as `.csv`. To edit the artifact yourself, open the link, which goes to that template’s editor on claude.ai. You can also keep asking Claude for changes from your session. For export formats, see [View and export](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them#h_1403132eb8).

### [](#draft-a-design-canvas)Draft a design canvas

To mock up a UI, a screen flow, a landing page, or a poster rather than build a page, run `/design` with a brief. Claude drafts the design as artboards on one canvas and publishes the canvas as a Claude Design artifact. The brief names what you want drawn:

```python
/design a settings screen for a mobile banking app
```

Open the published artifact in a desktop browser to review the artboards. Select an element on an artboard and change it, and your edits save automatically. You can export each artboard as PNG or PDF.

### [](#write-a-document-with-claude-docs)Write a document with Claude Docs

Claude Docs reaches Claude Code as a claude.ai [connector](../06-MCP-Tools/General/mcp.md#use-mcp-servers-from-claude-ai) rather than a command. When it’s connected, `/mcp` lists it as `claude.ai Claude Docs`. A request for a document meant for other people then goes to Claude Docs instead of an artifact page: a spec, a proposal, or a write-up of the plan you worked through in the session. Claude gives you the doc’s link when it’s drafted. A document that belongs in the codebase, such as a README, stays a file. To get a file for something Claude would otherwise put in Claude Docs, name the format, such as `.docx` or a Markdown file in the repository. To turn off only the `claude.ai Claude Docs` connector, see [Disable claude.ai connectors](../06-MCP-Tools/General/mcp.md#disable-claude-ai-connectors). Keep the connector on if you use the Sheets template, which needs it too.

## [](#page-constraints)Page constraints

Each artifact is one self-contained page. Claude Code wraps the file you publish in an HTML document shell and serves it under a strict Content Security Policy (CSP), which shapes what the page can do.

| Constraint | Effect |
|:---|:---|
| External requests | The page can load typefaces from Google Fonts, and scripts from [five public CDN hosts](#allowlist-the-viewer-domain): cdnjs, unpkg, the Tailwind and jQuery CDNs, and selected paths on jsDelivr such as `/npm/`. The CSP blocks every external image and all other external scripts, stylesheets, and fonts, and lets `fetch`, XHR, and WebSocket calls reach only the page’s own origin and the Google Fonts hosts. Claude therefore loads any library the page needs from one of those CDNs, inlines all other CSS and JavaScript, and embeds images as data URIs. [Connector calls](#pull-live-data-with-mcp-connectors) go through claude.ai, which makes the network call itself. |
| No backend | An artifact is a static page. It can’t authenticate viewers itself. |
| Downloads | The page can’t start a download itself. To let viewers save a file the page generates, Claude declares the downloads capability. See [Offer a file download](#offer-a-file-download). |
| Source file types | The published file must be `.html`, `.htm`, or `.md`, and must decode as UTF-8, or as little-endian UTF-16 by its byte-order mark. Markdown files render as styled document pages with syntax-highlighted code. A file that doesn’t decode, or that contains the replacement character `U+FFFD`, is [refused with the line and column to fix](errors.md#the-source-file-is-not-valid-utf-8-text). |
| Source location | A file at a path that names a network host is refused without being read. See [Not published: that file is on a network share](errors.md#not-published-that-file-is-on-a-network-share) for which paths are refused and the mapped-drive exception on Windows. |
| Rendered size | The rendered page must be 16 MiB or smaller. Large embedded images are the usual cause when a publish fails for size. |

Generating an artifact uses output tokens like any other response, and a styled page is more token-intensive than the same content as terminal text. Inline CSS, JavaScript for interactive controls, and especially images embedded as data URIs are the main contributors. To reduce an artifact’s token cost:

- Prefer SVG, or HTML and CSS, for diagrams over embedded raster images
- Omit interactivity you do not need
- Have the page summarize large datasets rather than inline them in full

## [](#availability)Availability

Artifacts require every condition below. When one is not met, Claude writes a local HTML file or says it cannot publish instead.

| Requirement | Available when |
|:---|:---|
| Plan | Pro, Max, Ultra, Team, or Enterprise. On Pro, Max, and Ultra plans, artifacts are private to you until you share them, and no admin management applies. On Team and Enterprise plans, artifacts are on by default, and an Owner can [turn them off for the organization](#manage-artifacts-for-your-organization) in claude.ai admin settings. |
| Authentication | The session is backed by a claude.ai account: sign in with `/login` in the CLI or desktop app. Claude Tag sessions need no sign-in step. Sessions using an API key, [gateway token](../13-Enterprise-Admin/llm-gateway.md), or cloud-provider credential cannot publish. |
| Model provider | Anthropic API. Not available on [Amazon Bedrock](amazon-bedrock.md), [Google Cloud’s Agent Platform](google-vertex-ai.md), or [Microsoft Foundry](microsoft-foundry.md). |
| Organization policy | Customer-managed encryption keys (CMEK), HIPAA, and [Zero Data Retention](zero-data-retention.md) are not enabled for the organization. |
| Surface | Claude Code CLI, or the Claude desktop app version 1.13576.0 or later. [Claude Tag](https://claude.com/docs/claude-tag/overview) sessions can also publish artifacts when both Claude Tag and artifacts are enabled for the organization. Sessions served by [`claude remote-control`](remote-control.md) can publish artifacts when you started the session yourself. Requires Claude Code v2.1.281 or later. Off by default in the [Agent SDK](../05-Agent-SDK/agent-sdk-overview.md), the GitHub Action, and MCP-server contexts, when you run Claude Code with [`-p`](headless.md) from your own terminal or scripts, and when [`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`](env-vars.md) is set. |

Whether artifacts are allowed for your organization comes from your organization’s policy, which Claude Code loads from `api.anthropic.com`. When Claude Code can’t load the policy, artifacts are unavailable. When you ask for one, Claude says why. If a proxy, VPN, or web filter is involved, ask your IT admin to let `api.anthropic.com` through. Claude Code keeps retrying in the background, and artifacts become available once the policy loads and allows them.

## [](#disable-artifacts)Disable artifacts

To turn artifacts off for your own sessions regardless of your organization’s setting, use any of:

| Where | What to do |
|:---|:---|
| [`/config`](commands.md) | Turn the **Artifacts** row off, which writes [`"enableArtifact": false`](settings-reference.md#enableartifact) to your user settings |
| [Settings file](settings.md) | Set `"enableArtifact": false`. The deprecated `"disableArtifact": true` also turns artifacts off |
| [Environment variable](env-vars.md) | Set `CLAUDE_CODE_DISABLE_ARTIFACT=1` |
| [Permission rule](permissions.md) | Add `Artifact` to `permissions.deny` |

Once you turn artifacts off in a [`--settings`](cli-reference.md#cli-flags) file or with `CLAUDE_CODE_DISABLE_ARTIFACT`, or your administrator turns them off in [managed settings](../13-Enterprise-Admin/server-managed-settings.md), no settings file turns them back on. You can also set `"enableArtifact": false` in a project’s `.claude/settings.json` or `.claude/settings.local.json` to turn artifacts off for sessions in that project. An `"enableArtifact": true` in either file doesn’t turn them back on. Honoring the key in project and local settings requires Claude Code v2.1.242 or later. If you add a `WebFetch` deny or ask rule with no `domain:` part, it doesn’t turn artifacts off or block artifact reads. A [`WebFetch(domain:claude.ai)` rule in `deny` or `ask` does apply to artifact reads](permissions.md#allow-or-deny-every-fetch).

## [](#manage-artifacts-for-your-organization)Manage artifacts for your organization

Owners on Team and Enterprise plans control artifacts from [claude.ai admin settings](https://claude.ai/admin-settings/artifacts). Artifact content is stored on Anthropic-operated infrastructure and is visible only to authenticated members of the publishing organization and the people they share it with, unless the artifact is [shared publicly](#control-public-sharing).

### [](#enable-or-disable-artifacts)Enable or disable artifacts

To enable or disable artifacts for the whole organization, go to [**Organization settings \> Artifacts**](https://claude.ai/admin-settings/artifacts) and use the **Artifacts** toggle. On Enterprise plans with role-based access control, you can additionally scope artifacts to specific roles: go to [**Organization settings \> Roles**](https://claude.ai/admin-settings/roles), edit a role, and set the **Artifacts** permission.

### [](#control-connector-calls-from-artifacts)Control connector calls from artifacts

[Connector calls from artifacts](#pull-live-data-with-mcp-connectors) have their own toggle, separate from the **Artifacts** toggle that turns artifacts on or off. Go to [**Organization settings \> Capabilities**](https://claude.ai/admin-settings/capabilities) and use the **Enable artifact connectors** toggle. The same toggle governs connector calls from artifacts created in claude.ai conversations.

### [](#control-public-sharing)Control public sharing

Public sharing is off by default on Team and Enterprise plans. To let members publish artifacts to public links that anyone can view without signing in, go to [**Organization settings \> Artifacts**](https://claude.ai/admin-settings/artifacts) and turn on **External sharing** under the **Artifacts** toggle. Turning it back off blocks access through existing public links without changing each artifact’s audience; access resumes if you re-enable it.

### [](#set-a-retention-policy)Set a retention policy

To set how long artifacts are kept before automatic deletion, go to [**Organization settings \> Data and privacy**](https://claude.ai/admin-settings/data-privacy-controls). You can set separate retention periods for artifacts that are still private to their author and artifacts that have been shared.

### [](#audit-artifact-activity-with-the-compliance-api)Audit artifact activity with the Compliance API

On Enterprise plans, query the Compliance API’s [Activity Feed](../04-API-Reference/Other/manage-claude-compliance-activity-feed.md) to see who published, shared, or deleted an artifact. To find the activity types to filter by, expand `activity_types` in the [Activity Feed reference](../04-API-Reference/Admin/compliance-activities-list.md) and look for names that contain `artifact`.

### [](#allowlist-the-viewer-domain)Allowlist the viewer domain

The viewer on claude.ai loads each artifact from a sandboxed `*.claudeusercontent.com` origin. If your organization restricts outbound network access, add that domain to your allowlist alongside `claude.ai`. See [Network access requirements](../13-Enterprise-Admin/network-config.md#network-access-requirements) for the full list. An artifact that loads a typeface from [Google Fonts](#improve-the-visual-design) also requests `fonts.googleapis.com` and `fonts.gstatic.com`. Both hosts are optional. If you block them, artifacts render in fallback typefaces. Block with a fast rejection rather than a silent drop so the font request fails immediately instead of delaying the page’s first render. Artifacts can also load JavaScript libraries, such as React or a charting package, from `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `cdn.tailwindcss.com`, `code.jquery.com`, and `unpkg.com`, and from no other external host. If you block those hosts, the parts of an artifact that depend on a library don’t work, and unlike a blocked font, a blocked library has no fallback. Block with a fast rejection here too, so a blocked library request fails at once rather than hanging until it times out.

### [](#list-and-delete-artifacts-with-the-compliance-api)List and delete artifacts with the Compliance API

The [Compliance API](https://docs.claude.com/en/api/compliance) provides endpoints to list an organization’s artifacts, retrieve a specific version’s content, and delete an artifact:

| Method | Endpoint |
|:---|:---|
| `GET` | `/v1/compliance/apps/code/artifacts` |
| `GET` | `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` |
| `DELETE` | `/v1/compliance/apps/code/artifacts/{artifact_id}` |

For the request and response schemas, see the [Compliance API reference](../04-API-Reference/Admin/compliance-apps-code-artifacts.md).

## [](#related-resources)Related resources

- Browse [prompting patterns and workflows](prompt-library.md) that pair with artifacts
- Turn an artifact prompt you reuse into a [skill](../08-Plugins-Skills/skills.md) so you can invoke it as a command
- [Connect MCP servers](../06-MCP-Tools/General/mcp.md) so Claude can pull data into an artifact while it builds the page
