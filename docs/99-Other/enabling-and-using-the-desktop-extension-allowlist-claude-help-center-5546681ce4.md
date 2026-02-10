---
category: "99-Other"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist"
title: "Enabling and using the desktop extension allowlist | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

Table of contents

[](#h_da8c500f7a)

[](#h_b62722df7c)

[](#h_280c37dd98)

[](#h_74028c1148)

[](#h_6198be6717)

[All Collections](/en/)

[Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop)

[Desktop Extensions](https://support.claude.com/en/collections/17879657-desktop-extensions)

Enabling and using the desktop extension allowlist

# Enabling and using the desktop extension allowlist

Updated this week

Table of contents

[](#h_da8c500f7a)

[](#h_b62722df7c)

[](#h_280c37dd98)

[](#h_74028c1148)

[](#h_6198be6717)

The desktop extension allowlist is available for Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

## How to enable the allowlist

**Important:** If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both `isDesktopExtensionDirectoryEnabled` and `isDesktopExtensionEnabled` are not set to "false" so the allowlist can populate the available registry. Refer to our [desktop enterprise configuration documentation](https://support.claude.com/en/articles/12622667-enterprise-configuration) for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that **users will be able to access all desktop extensions in the registry until you enable the allowlist.** To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

**To turn on the allowlist:**

1.  Open Claude Desktop

2.  Click your initials or name in the lower left corner

3.  Navigate to Admin settings \> Connectors

4.  Switch to the "Desktop" tab:

    [](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1770722100&signature=01c53a17557a7cbbb838344206d7df7a1a06da12769715a479e3ed8e089689ee&req=dScvF857mIBYW%2FMW1HO4zQ9pUkoN%2FXLa0ugSQm1MFW8qFTXgMo0lKPNkZ1St%0AdKo8%0A)

5.  Toggle **Allowlist** on:

    [](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1770722100&signature=6108f1dac20571e1ccf035e53c7f6c2b70a0863ea92a2b9906e0f69ccfb7137e&req=dScvF857mIRYUfMW1HO4zaj0C3EsS6UFTAorLxpdoc%2BTMp%2B7K7T7ItK%2BmZrD%0AUu2h%0A)

## What happens after enabling the allowlist?

Once the allowlist is enabled:

- Any existing desktop extension installations will be force-deleted from Claude Desktop clients.

- Users will no longer be able to install new desktop extensions that are not included within the allowlist.

- Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs.

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

**Important:** The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1770722100&signature=044ffa9062cf1a1e732859e66c7d5c019298b3c1aa6cc3703e612b77619ad45e&req=dScvF857m4hZWfMW1HO4zYUJpoOtCDDqCEDZ5AdBjIYNIQx3uYXNasC0yCsY%0AXP7VN%2BmIk8rfT2VMY20%3D%0A)

## Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1.  Navigate to Admin settings \> Connectors and select the “Desktop” tab.

2.  Click “Browse extensions” to view the list of available extensions.

3.  Select the extension you want to add.

4.  Click the “Add to your team” button.

5.  The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1770722100&signature=2ba82ad0d4e554650c713a7083dab5ea4c8c480506d253f5630c0f0469bac955&req=dScvF857nINaWfMW1HO4zTrxCqgu%2FVWUqXridZhfx1LXD8rHON2u%2F0DIBmkB%0AH9LAK0%2BaEX6ywb3xgFo%3D%0A)

## Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Admin settings \> Connectors \> Desktop.

**Note:** Ensure the name field in the manifest.json does not overlap with any existing MCPBs. All names for unique MCPBs / desktop extensions must be unique.

1.  Click “Add custom extension”

2.  This will open a filepicker; select the .mcpb file.

3.  The extension will appear under **Custom team extensions**.

4.  Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our [desktop extension developer documentation](https://github.com/anthropics/mcpb).

## Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)

Deploy Claude Desktop for macOS

[](https://support.claude.com/en/articles/12614803-using-the-10x-genomics-extension-in-claude)

Using the 10x Genomics Extension in Claude

[](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)

Deploying enterprise-grade MCP servers with desktop extensions

[](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb)

Building Desktop Extensions with MCPB

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
