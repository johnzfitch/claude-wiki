---
category: "16-Mobile-Desktop"
source_url: "https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos"
---


Administrators on Team or Enterprise plans can deploy Claude Desktop automatically to manage installations and updates centrally. Claude Desktop installs to `/Applications` and updates automatically when new versions are released, unless disabled via enterprise policies.

 

Available formats:

- `.pkg` - Standard macOS installer package (recommended for enterprise)

- `.dmg` - Drag-and-drop installation

 

Download:

Universal (x64 or arm64) Claude PKG

The Universal build is compatible with both Intel and Apple Silicon machines and supports all Mac hardware.

 

Deploy via MDM

Upload the PKG to your MDM solution (Jamf, Kandji, Microsoft Intune) and deploy to target machines.

 

Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the Enterprise Configuration article.

 

Troubleshooting
Users cannot update Claude Desktop

Claude Desktop can be installed to either the user's Applications folder or the system Applications folder, which affects update permissions.:

`~/Applications` (user folder): Users can update without administrator privileges

`/Applications` (system folder): Users need administrator access and write permissions to `/Applications`, `Claude.app`, and all contained files

For shared machines, disable auto-updates via enterprise policies and manage updates centrally through your MDM solution.

Related Articles
Installing Claude Desktop
Getting Started with Local MCP Servers on Claude Desktop
Enterprise Configuration
Deploy Claude Desktop for Windows
Deploying enterprise-grade MCP servers with desktop extensions