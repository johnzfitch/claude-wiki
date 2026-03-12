---
category: "22-Safety-Policy"
fetched_at: "2026-03-12T08:19:36Z"
source_url: "https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization"
title: "Manage Cowork plugins for your organization | Claude Help Center"
---

4.  Manage Cowork plugins for your organization

# Manage Cowork plugins for your organization


Plugin marketplaces allow Team and Enterprise plan owners to distribute curated plugins to everyone in their organization through Cowork. You create a marketplace, add plugins to it, and control exactly which plugins your team members can see and use.

Owners and Primary Owners of Team and Enterprise plans can manage organization plugins on Claude Desktop.

**Requirements:** Cowork and Skills must both be enabled for your organization before you can use plugin marketplaces.

There are two ways to add plugins to a marketplace:

- **Manual upload**—Upload individual plugin ZIP files through the admin UI. Best for quick iteration, one-off tools, or teams that don't use GitHub for plugin development.

- **GitHub syncing**—Connect a private GitHub repository and Cowork automatically syncs plugins from it. Best when multiple developers collaborate on plugins or you want version-controlled updates.

You can use both approaches in parallel—for example, a GitHub-synced marketplace for your core plugins and a separate manual marketplace for ad-hoc tools.

------------------------------------------------------------------------

## Set up a manual marketplace

1.  Open Claude Desktop and go to **Organization settings \> Plugins**.

2.  Click “Add plugins” and select “Upload a file” as the source.

3.  If this is your first time setting up a marketplace, “Upload to a new marketplace” will be auto-selected.

    1.  You’ll be able to choose “Add to an existing marketplace” when uploading plugins moving forward.

4.  Enter a name for your marketplace.

5.  Either drag your files in, or click the upload prompt and select your file.

    1.  **Note:** The file must be a valid .zip under 50 MB.

6.  Repeat for each plugin you want to add.

7.  Click “Upload” to add your plugins to a new marketplace.

If you upload a plugin with the same name as an existing one, it overwrites the previous version automatically—no need to delete the old one first.

------------------------------------------------------------------------

## Set up a GitHub-synced marketplace

GitHub syncing lets you manage plugins as code in a repository. When you push changes, you can trigger a sync to update your marketplace.

### Prepare your repository

Your repository must be **private or internal**—public repos aren't allowed for organization marketplaces. Repos hosted on custom GitHub Enterprise Server instances aren't supported. Your repo must be hosted on github.com.

For details on plugin structure and formatting, see the **[plugin reference documentation](https://code.claude.com/docs/en/plugins-reference)**.

Additional resources:

- **[Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)**

- **[Create plugins](https://code.claude.com/docs/en/plugins)**

- **[Creating a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)**

### Connect the repository

1.  Make sure both Cowork and Skills are enabled for your organization.

2.  Go to **Organization settings \> Plugins**.

3.  Click "Add plugin" and select "GitHub" as the source.

4.  Enter the repository in `owner/repo` format (for example, `acme-corp/claude-plugins`).

Your personal GitHub token is verified to confirm you have access, then Cowork uses its GitHub App installation token for sync operations.

**Can't see your repo?** Make sure the Cowork GitHub App is installed in that repository.

### How syncing works

An initial sync runs automatically when you connect a repository. After that, you can trigger syncs manually by clicking “Check for updates” on your marketplace in **Organization settings \> Plugins**.

During a sync, Cowork compares the latest commit in your repo against the last-synced commit. If nothing has changed, the sync is skipped. If there are changes, Cowork reads the manifest, validates each plugin, and replaces all plugins in the marketplace with the current state of the repo. Syncs can take up to 30 minutes depending on the number of plugins.

**Important:** If a sync fails, plugins may be temporarily removed for your team members. If this happens, check the failure message, fix the issue in your repo, push the update, and trigger the sync again. Once the sync succeeds, verify that your installation preferences are still set correctly — they may have been reset during the failure.

------------------------------------------------------------------------

## Control plugin distribution

Once your marketplace has plugins, you control how they're distributed using installation preferences. For each plugin, you can set one of three options:

[TABLE]

### Set preferences

1.  In **Organization settings \> Plugins**, navigate to your marketplace.

2.  Select the installation preference for each plugin.

3.  Changes take effect on each member's next session or plugin refresh.

### What members experience

Members browse available plugins through the **Browse plugins** modal in Cowork. Auto-installed plugins appear in their installed list automatically. Available plugins show up in the catalog for self-service installation.

Members can't edit organization-managed plugins, which prevents conflicting changes to shared tooling.

------------------------------------------------------------------------

## Update and remove plugins

### Manual marketplaces

To update a plugin, upload a new ZIP file with the same plugin name. The new version overwrites the existing one automatically. Plugin names are the unique identifier — `legal` will always replace `legal`.

To remove a plugin, delete it from your marketplace in **Organization settings \> Plugins**.

### GitHub-synced marketplaces

Push your changes to the connected repository, then go to **Organization settings \> Plugins**, find your marketplace, and click "Check for updates" to trigger a sync. Each sync replaces all plugins with the current state of the repo.

To remove a plugin, delete it from the repository and trigger a sync.

------------------------------------------------------------------------

## Limits

[TABLE]

## 

------------------------------------------------------------------------

## Naming rules

Plugin names must use **lowercase words separated by hyphens** (for example, `deployment-tools`, not `Deployment Tools`). The following marketplace names are reserved and can't be used:

- `claude-code-marketplace`

- `claude-code-plugins`

- `claude-plugins-official`

- `anthropic-marketplace`

- `anthropic-plugins`

- `agent-skills`

- `life-sciences`

Names that impersonate official Anthropic marketplaces are also blocked.

------------------------------------------------------------------------

## Choose between manual upload and GitHub sync

[TABLE]

------------------------------------------------------------------------

## Troubleshooting

### Upload rejected

Common causes: the file exceeds 50 MB, it isn't a valid ZIP file, or the marketplace has reached the 100-plugin limit. Check the file size and format, and remove unused plugins if you're at capacity.

### Plugin not appearing for members

Check the plugin's installation preference in your marketplace settings. If it's set to **Not available**, members won't see it. Also confirm that Cowork and Skills are both enabled for your organization.

### Updated plugin not reflecting for members

Changes take effect on each member's next session or plugin refresh. If the update still isn't showing, confirm the upload succeeded by checking the plugin version in your marketplace.

### GitHub sync fails with a content error

One or more plugins in your repo is likely formatted incorrectly. Fix the formatting issue, push the update to GitHub, and trigger the sync again. For plugin structure requirements, see the **[plugin reference documentation](https://code.claude.com/docs/en/plugins-reference)**.

### Plugins disappeared after a failed sync

A failed GitHub sync can temporarily remove plugins from your marketplace. Fix the underlying issue, re-sync successfully, then verify that installation preferences are set correctly—they may have been reset.

### Can't see a GitHub repo when connecting

Make sure the Cowork GitHub App is installed in that repository. Your personal GitHub token is checked first to confirm access, but the sync itself uses the GitHub App installation token.

------------------------------------------------------------------------

Related Articles


Using the GitHub Integration


Use Cowork safely


Use Cowork on Team and Enterprise plans


Use plugins in Cowork


Install financial services plugins for Cowork
