---
category: "16-Mobile-Desktop"
source_url: "https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist"
---


The desktop extension allowlist is available for Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

 

How to enable the allowlist

Important: If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both isDesktopExtensionDirectoryEnabled and isDesktopExtensionEnabled are not set to "false" so the allowlist can populate the available registry. Refer to our desktop enterprise configuration documentation for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that users will be able to access all desktop extensions in the registry until you enable the allowlist. To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

 

To turn on the allowlist:

Open Claude Desktop

Click your initials or name in the lower left corner

Navigate to Admin settings > Connectors

Switch to the "Desktop" tab:

 

 

Toggle Allowlist on:

 

 

What happens after enabling the allowlist?

Once the allowlist is enabled:

Any existing desktop extension installations will be force-deleted from Claude Desktop clients.

Users will no longer be able to install new desktop extensions that are not included within the allowlist.

Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs. 

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

 

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

Important: The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:

 

 

Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

Navigate to Admin settings > Connectors and select the “Desktop” tab.

Click “Browse extensions” to view the list of available extensions.

Select the extension you want to add.

Click the “Add to your team” button.

The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

 

 

Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Admin settings > Connectors > Desktop.

Note: Ensure the name field in the manifest.json does not overlap with any existing MCPBs. All names for unique MCPBs / desktop extensions must be unique.

Click “Add custom extension”

This will open a filepicker; select the .mcpb file.

The extension will appear under Custom team extensions.

Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our desktop extension developer documentation.

 

Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

 

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.

Related Articles
Getting Started with Local MCP Servers on Claude Desktop
Deploy Claude Desktop for macOS
Using the 10x Genomics Extension in Claude
Deploying enterprise-grade MCP servers with desktop extensions
Building Desktop Extensions with MCPB