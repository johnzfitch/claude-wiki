---
category: "16-Mobile-Desktop"
fetched_at: "2026-02-08T20:52:00Z"
source_url: "https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows"
title: "Deploy Claude Desktop for Windows | Claude Help Center"
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

[](#h_4d6c8a8150)

[](#h_e9da199af9)

[](#h_de227a9e4a)

[](#h_36f2edfa0f)

[](#h_6561194980)

[](#h_aaf5adfb6a)

[All Collections](/en/)

[Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop)

[General](https://support.claude.com/en/collections/17879568-general)

Deploy Claude Desktop for Windows

# Deploy Claude Desktop for Windows

Updated yesterday

Table of contents

[](#h_4d6c8a8150)

[](#h_e9da199af9)

[](#h_de227a9e4a)

[](#h_36f2edfa0f)

[](#h_6561194980)

[](#h_aaf5adfb6a)

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer an MSIX package for Windows deployments, enabling secure, scalable distribution.

## Available Formats

\- \`.msix\` - Compatible with Microsoft Intune and Microsoft Store

\- \`.exe\` - Standard installer. Installs to \`%LOCALAPPDATA%\Programs\Claude\\. Updates automatically when new versions are released, unless disabled via enterprise policies.

## Download:

- [X64 Claude MSIX Installer](https://claude.ai/api/desktop/win32/x64/msix/latest/redirect)

- [ARM64 Claude MSIX Installer](https://claude.ai/api/desktop/win32/arm64/msix/latest/redirect)

## Installation commands:

For manual installation on individual machines, use the following PowerShell commands:

**Install for single user:**

    ```powershell
    Add-AppxPackage -Path "Claude.msix"
    ```

See Microsoft's [Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps) documentation for more details.

**Install for all users (provisions machine-wide):**

    ```powershell
    Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"
    ```

See Microsoft's [Add-AppxProvisionedPackage](https://learn.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2022-ps) documentation for more details.

## Deploy via MDM

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

- [Microsoft Intune](https://docs.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-intune)

- [Microsoft Endpoint Configuration Manager (SCCM)](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-mem-adminconsole)

- [Group Policy Software Installation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)

- [Deployment Image Servicing and Management (DISM.exe)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism?view=windows-10)

- [PowerShell Scripts](https://learn.microsoft.com/en-us/windows/msix/desktop/powershell-msix-cmdlets)

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the [Enterprise Configuration article](https://support.claude.com/en/articles/12622667-enterprise-configuration).

## Troubleshooting

### MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10065433-installing-claude-desktop)

Installing Claude Desktop

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)

Deploy Claude Desktop for macOS

[](https://support.claude.com/en/articles/12622667-enterprise-configuration)

Enterprise Configuration

[](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)

Deploying enterprise-grade MCP servers with desktop extensions

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
