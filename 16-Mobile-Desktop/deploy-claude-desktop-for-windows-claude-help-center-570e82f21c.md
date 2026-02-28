---
category: "16-Mobile-Desktop"
fetched_at: "2026-02-28T11:22:18Z"
source_url: "https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows"
title: "Deploy Claude Desktop for Windows | Claude Help Center"
---

# Deploy Claude Desktop for Windows

Updated today


Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer an installer and an MSIX package for Windows deployments, enabling secure, scalable distribution.

## Available installation formats

- **Installer (recommended):** Downloads and installs Claude Desktop. On compatible systems, installs as an MSIX package with full features including Cowork. Requires administrator credentials, which are requested automatically during setup. If admin access is not available, installs Claude with all features except Cowork.

- **MSIX package:** For enterprise deployment via Microsoft Intune, SCCM, Group Policy, or PowerShell. Use this if you are managing installations centrally rather than having users install individually.

## Installation requirements

- The recommended installer requires Windows 10 version 2004 or later (build 19041+). Windows S Mode must be disabled.

- For full feature support including Cowork, administrator privileges are required. Users will see a Windows UAC prompt during installation. Users without admin access can still install Claude but Cowork will not be available.

- For silent deployment without user interaction, use the MSIX package directly with your enterprise management tool.

## Cowork requirements

Claude Desktop for Windows requires the **[Virtual Machine Platform](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)** to use Cowork. You can automate installation of this feature via most endpoint management solutions, but you may also run the following command to install it manually:

    Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart

## Download

- **[Claude Desktop Installer](https://downloads.claude.ai/releases/win32/ClaudeSetup.exe)**

- **[Claude MSIX (x64)](https://claude.ai/api/desktop/win32/x64/msix/latest/redirect)**

- **[ARM64 Claude MSIX Installer](https://claude.ai/api/desktop/win32/arm64/msix/latest/redirect)**

## Installation commands

For manual installation on individual machines, use the following PowerShell commands:

### Install for single user

    ```powershell
    Add-AppxPackage -Path "Claude.msix"
    ```

For more details, see Microsoft's **[Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps)** documentation.

### Install for all users (provisions machine-wide)

    ```powershell
    Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"
    ```

For more details, see Microsoft's **[Add-AppxProvisionedPackage](https://learn.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2022-ps)** documentation.

## Deploy via MDM

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

- **[Microsoft Intune](https://docs.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-intune)**

- **[Microsoft Endpoint Configuration Manager (SCCM)](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-mem-adminconsole)**

- **[Group Policy Software Installation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)**

- **[Deployment Image Servicing and Management (DISM.exe)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism?view=windows-10)**

- **[PowerShell Scripts](https://learn.microsoft.com/en-us/windows/msix/desktop/powershell-msix-cmdlets)**

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see **[Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)**.

## Troubleshooting

### MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

------------------------------------------------------------------------

Related Articles


Installing Claude Desktop


Getting Started with Local MCP Servers on Claude Desktop


Deploy Claude Desktop for macOS


Deploying enterprise-grade MCP servers with desktop extensions


Claude in Chrome admin controls
