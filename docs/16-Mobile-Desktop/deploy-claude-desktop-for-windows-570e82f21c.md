---
category: "16-Mobile-Desktop"
source_url: "https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows"
---


Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer an MSIX package for Windows deployments, enabling secure, scalable distribution.

 

Available Formats

- `.msix` - Compatible with Microsoft Intune and Microsoft Store 

- `.exe` - Standard installer. Installs to `%LOCALAPPDATA%\Programs\Claude\`. Updates automatically when new versions are released, unless disabled via enterprise policies.

 

Download:

X64 Claude MSIX Installer

ARM64 Claude MSIX Installer

Installation commands:

For manual installation on individual machines, use the following PowerShell commands:

 

Install for single user:

```powershell
Add-AppxPackage -Path "Claude.msix"
```

See Microsoft's Add-AppxPackage documentation for more details.

 

Install for all users (provisions machine-wide):

```powershell
Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"
```

See Microsoft's Add-AppxProvisionedPackage documentation for more details.

 

Deploy via MDM 

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

Microsoft Intune

Microsoft Endpoint Configuration Manager (SCCM)

Group Policy Software Installation

Deployment Image Servicing and Management (DISM.exe)

PowerShell Scripts

Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the Enterprise Configuration article.

 

Troubleshooting
MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

Related Articles
Installing Claude Desktop
Getting Started with Local MCP Servers on Claude Desktop
Deploy Claude Desktop for macOS
Enterprise Configuration
Deploying enterprise-grade MCP servers with desktop extensions