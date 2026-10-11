---
title: "Migrate from standalone Claude Design to Claude | Claude Help Center"
source_url: "https://support.claude.com/en/articles/17440474"
category: "15-Claude-AI-Features"
fetched_at: "2026-10-10T06:28:24Z"
tags: ["claude-ai", "enterprise"]
---

# Migrate from standalone Claude Design to Claude


Claude Design now lives in Claude. The standalone Claude Design site (claude.ai/design) will close on December 14, 2026, and you can still access it until that date. This article explains what's changing and when, how to migrate your design systems today, and what happens to your projects.

Claude Design is available on Free, Pro, Max, Team, and Enterprise plans.

## What's changing and when

You can keep using the standalone version until it closes on December 14, 2026. After that, claude.ai/design will take you to Claude.

When you start a new design, design system or slide deck in Claude, it's created as an artifact.

## What happens to your work

When you migrate a design system, the original stays in the standalone version, unchanged, until it closes.

## What you need to do

- Migrate your design systems now.

- On Team and Enterprise plans, ask your organization's owner to set a default design system to get the most out of artifacts.

- You don't need to do anything with your projects yet.

- If you're a Team or Enterprise owner, check that artifacts and design systems are turned on. On Enterprise plans, design systems are off by default.

------------------------------------------------------------------------

## Migrate your design systems

### Before you start

- One migration brings over every design system in your organization, including other people's, so it only needs to be started once.

- Anyone who can use Claude Design can start it, not just your organization's owners.

- Each design system keeps its owner and the people it's shared with. If the owner has left your organization, the Primary Owner becomes its owner.

- Empty design systems aren't migrated, and neither are ones made from a built-in starter theme, even if you've edited them.

**Important:** Published design systems that aren't private will be shared with everyone in your organization and appear in their design system menu. On individual plans, nothing is shared.

### Start the migration

1.  Open the **Artifacts** page in Claude.

2.  Click "Migrate team design systems" in the "Claude Design lives here now" banner. If you've closed the banner, choose it from the **Claude Design** menu at the top right.


3.  Click "Migrate" to confirm. On individual plans, there's no confirmation step, and the migration starts right away.


4.  Wait for the migration to finish. If you close the window, it keeps running.

5.  Check the results. Under **Migrated**, the window lists each design system with its owner's name and an "Open" link. You'll see only the design systems you have access to, unless you're an owner of your organization.


### After you migrate

Your migrated design systems appear in the design system menu when you make designs and slide decks in Claude. To see them all, choose "View design systems" from the **Claude Design** menu on the **Artifacts** page. The list opens in **Settings**.


Owners can set your organization's default design system here. Open a design system's menu and choose "Set as default." Click a design system's name to open it.


A migrated design system keeps its files as they were, and you can't edit it yourself on its page yet. Its editors see a note at the top: "Migrated from the standalone version. Ask Claude to make changes."

Learn more about **[getting started with Claude Design](get-started-with-claude-design.md)**.

### If a design system can't be migrated

The window lists it under **Couldn't be migrated**, with its name, owner, and a short reason, such as "it's too large."


To reopen the results later, click the count in the banner on the **Artifacts** page, such as "6 of your 11 design systems couldn't be migrated."

Anyone who can edit the design system can fix problems with its own files or size. If you can't edit it, you won't be able to run the check, so ask its owner, who's named in the row.

**To fix a design system:**

1.  Click "Fix in Claude Design Standalone" in its row.

2.  Click "Check" on the "Check whether this design system can migrate to claude.ai" card.


3.  Fix the files the check lists, using the table below.


4.  Click "Check again" until it says "Nothing found in the way."

5.  Migrate again from the **Artifacts** page in Claude.

[TABLE]

If the whole design system is too large, the card says "It's too large. Make it smaller." instead of listing files. Remove files you don't need, then check again.

**Note:** The `uploads` folder often contains duplicate files, so it's an easy place to start trimming down a design system.

Some reasons need your organization's owner to fix them: "design systems are turned off for your team," "your team can't publish artifacts," or "its owner's role doesn't include design systems." The first two stop the migration, and any design systems it hadn't started are listed under **Not started**. Once they're fixed, migrate again.

Sometimes the check says "The problem is in the migration, not your files. There's nothing for you to fix." If this happens, try again later.

### Migrate again

To migrate new, changed, or fixed design systems, choose "Migrate again" from the **Claude Design** menu on the **Artifacts** page. To reopen your last results, choose "View details," just below it.


**When you migrate again:**

[TABLE]


To replace a migrated design system with a fresh copy, delete it in Claude, then migrate again. To keep any changes you've made to it, duplicate it first. Once nothing is left to migrate, the banner says "All of your design systems have migrated."

## What happens to your projects

Your projects stay in the standalone version and keep working until it closes. The **Artifacts** page in Claude also lists up to 60 of them, and they open in the standalone version. More details about moving your projects to Claude are coming soon.

## What isn't carried over

These stay in the standalone version and deleted after it closes, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**, in December 2026:

- Your chats with Claude

- Comments on your projects and design systems

Public links to projects in the standalone version will no longer work after it closes.

**Important:** Save anything you need from your chats and comments before the standalone version closes.

------------------------------------------------------------------------

## For Team and Enterprise owners

Claude Design in Claude depends on artifacts. If artifacts are off for your organization, people can't create designs in Claude or migrate anything, and they won't see the "Claude Design lives here now" banner.

To check your settings, navigate to **[Organization settings](https://claude.ai/admin-settings/artifacts)** [\> **Artifacts**](https://claude.ai/admin-settings/artifacts):

[TABLE]

On Enterprise plans with custom roles, each role also needs these permissions, which the role editor lists under **Artifacts**. This lets you turn on artifacts for just the people who use Claude Design. A design system can't be migrated if its owner's role doesn't include design systems.

While **Design systems** is off, owners who click "Migrate team design systems" see "Design systems are off for your organization" and an "Open Organization settings" button. Everyone else sees the button grayed out, with the reason "Ask your admin to turn on Design systems."

If your organization's default design system migrates, it becomes the default in Claude too, unless you've already set one there.

Organizations with zero data retention (ZDR) can't turn on artifacts, so they can't migrate. If that's your organization, download your projects before the standalone version closes. See **[Can I download all my projects?](#h_a676b76d76)**

------------------------------------------------------------------------

## Frequently asked questions

### What happens to my originals after the standalone version closes?

Your originals keep working in the standalone version until it closes on December 14, 2026. After that, they're deleted, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

### What if the owner of a design system or project has left my organization?

Your organization's Primary Owner becomes its owner.

### Can I download all my projects?

Not all at once. You can download them one at a time:

1.  Open the project in the standalone version.

2.  Click "Share," then choose "Project HTML." For a slide deck, it's under "More formats and apps."

3.  Keep "Project archive" selected and click "Export."


You get a `.zip` file with every file in the project. It's free and doesn't count toward your usage limits.

## Get help

If something didn't come over right, your original is still in the standalone version. Please let us know if your design system can't be migrated and there's no way for you to fix it. Learn more about **[how to get support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.
