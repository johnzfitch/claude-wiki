---
category: "13-Enterprise-Admin"
source_url: "https://support.claude.com/en/articles/12622667-enterprise-configuration"
title: "Set machine-wide settings (recommended)"
---


Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

Note: Enterprise policy controls at the user-machine level will override the in-app allowlist. If you want to use the allowlist, ensure isDesktopExtensionEnabled and isDesktopExtensionDirectoryEnabled are not set to "false" so the allowlist can populate the available registry.

 

macOS Enterprise Configuration

Deploy configuration settings through your MDM solution using configuration profiles. Claude Desktop reads preferences from the domain `com.anthropic.claudefordesktop`. Use your MDM tool (Jamf Pro, Kandji, Microsoft Intune) to deploy configuration profiles to target machines or user groups. Configuration profiles allow you to manage Claude Desktop settings centrally without user intervention.

 

Configuration profile tools:

Built-in MDM profile editors (Jamf Pro, Kandji, Intune)

ProfileCreator - Profile management

iMazing Profile Editor - Configuration profiles

 

 

Windows Enterprise Configuration

Deploy configuration settings through your enterprise management solution using Group Policy or Intune policies. Settings can be configured at machine-wide (HKLM) or per-user (HKCU) level. Machine-level settings take priority over user-level settings when both are configured.

```powershell
# Set machine-wide settings (recommended)
New-Item -Path "HKLM:\SOFTWARE\Policies\Claude" -Force
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "disableAutoUpdates" -Value 0 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "autoUpdaterEnforcementHours" -Value 72 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionDirectoryEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isLocalDevMcpEnabled" -Value 1 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isClaudeCodeForDesktopEnabled" -Value 1 -Type DWord
```

 

 

Enterprise Policy Options

Key

 

Type

 

Default

 

Description

disableAutoUpdates

 

Boolean

 

false

 

Disable automatic updates 

autoUpdaterEnforcementHours

 

Integer (1-72)

 

72

 

Hours before forcefully restarting Claude to apply a prepared update

isClaudeCodeForDesktopEnabled

 

Boolean

 

true

 

Enable Claude code access in desktop

isDesktopExtensionEnabled

 

Boolean

 

true

 

Enable/disable extensions

isDesktopExtensionDirectoryEnabled

 

Boolean

 

true

 

Enable extension directory access

isLocalDevMcpEnabled

 

Boolean

 

true

 

Enable local MCP servers 

secureVmFeaturesEnabled

 

Boolean

 

true

 

Enable Cowork access in desktop

Related Articles
Getting Started with Local MCP Servers on Claude Desktop
Using Enterprise Search
Enabling and using the desktop extension allowlist
Deploy Claude Desktop for macOS
Deploy Claude Desktop for Windows