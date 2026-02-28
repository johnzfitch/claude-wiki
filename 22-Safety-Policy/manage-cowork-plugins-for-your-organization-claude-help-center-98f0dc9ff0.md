---
category: "22-Safety-Policy"
fetched_at: "2026-02-28T11:22:14Z"
source_url: "https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization"
title: "Manage Cowork plugins for your organization | Claude Help Center"
---

4.  Manage Cowork plugins for your organization

# Manage Cowork plugins for your organization


Plugin marketplaces allow Team and Enterprise plan owners to distribute curated plugins to everyone in their organization through Cowork. You create a marketplace, add plugins to it, and control exactly which plugins your team members can see and use.

Owners and Primary Owners of Team and Enterprise plans can manage organization plugins on Claude Desktop.

**Requirements:** Cowork and Skills must both be enabled for your organization before you can use plugin marketplaces.

------------------------------------------------------------------------

## Set up a plugin marketplace

1.  Open Claude Desktop and go to **Organization settings \> Plugins.**

2.  Click “Add plugins” and select “Upload to a new marketplace” as the source.

3.  Give your marketplace a name.

4.  Either drag your files in, or click the upload prompt and select your file.

    1.  **Note:** The file must be a valid .zip under 50 MB.

5.  Repeat for each plugin you want to add.

6.  Click “Upload” to add your plugins to a new marketplace.

If you upload a plugin with the same name as an existing one, it overwrites the previous version automatically — no need to delete the old one first.

------------------------------------------------------------------------

## Control plugin distribution

Once your marketplace has plugins, you control how they're distributed using installation preferences. For each plugin, you can set one of three options:

[TABLE]

## Set preferences

1.  In **Organization settings \> Plugins**, navigate to your marketplace.

2.  Select the installation preference for each plugin.

3.  Changes take effect on each member's next session or plugin refresh.

## What members experience

Members browse available plugins through the **Browse plugins** modal in Cowork. Auto-installed plugins appear in their installed list automatically. Available plugins show up in the catalog for self-service installation.

Members can't edit organization-managed plugins, which prevents conflicting changes to shared tooling.

------------------------------------------------------------------------

## Update and remove plugins

To update a plugin, upload a new ZIP file with the same plugin name. The new version overwrites the existing one automatically. Plugin names are the unique identifier—legal will always replace legal.

To remove a plugin, delete it from your marketplace in **Organization settings \> Plugins**.

------------------------------------------------------------------------

## Limits

[TABLE]

## 

------------------------------------------------------------------------

## Naming rules

Plugin names must use **lowercase words separated by hyphens** (for example, deployment-tools, not Deployment Tools). The following marketplace names are reserved and can't be used:

- `Claude-code-marketplace`

- `Claude-code-plugins`

- `Claude-plugins-official`

- `Anthropic-marketplace`

- `Anthropic-plugins`

- `Agent-skills`

- `life-sciences`

Names that impersonate official Anthropic marketplaces are also blocked.

------------------------------------------------------------------------

## Troubleshooting

### Upload rejected

Common causes: the file exceeds 50 MB, it isn't a valid ZIP file, or the marketplace has reached the 100-plugin limit. Check the file size and format, and remove unused plugins if you're at capacity.

### Plugin not appearing for members

Check the plugin's installation preference in your marketplace settings. If it's set to **Not available**, members won't see it. Also confirm that Cowork and Skills are both enabled for your organization.

### Updated plugin not reflecting for members

Changes take effect on each member's next session or plugin refresh. If the update still isn't showing, confirm the upload succeeded by checking the plugin version in your marketplace.

------------------------------------------------------------------------

Related Articles


How to use the single-cell-rna-qc skill with Claude


Get started with Cowork


Cowork for Team and Enterprise plans


Use plugins in Cowork


Install financial services plugins for Cowork
