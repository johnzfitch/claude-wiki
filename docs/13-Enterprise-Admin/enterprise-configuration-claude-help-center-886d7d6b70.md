---
category: "13-Enterprise-Admin"
fetched_at: "2026-02-10T10:49:30Z"
source_url: "https://support.claude.com/en/articles/12622667-enterprise-configuration"
title: "Enterprise Configuration | Claude Help Center"
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

[](#h_33652e6230)

[](#h_21d03dc3bb)

[](#h_003283c7cb)

[All Collections](/en/)

[Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop)

[General](https://support.claude.com/en/collections/17879568-general)

Enterprise Configuration

# Enterprise Configuration

Updated this week

Table of contents

[](#h_33652e6230)

[](#h_21d03dc3bb)

[](#h_003283c7cb)

Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

**Note:** Enterprise policy controls at the user-machine level will override the in-app **[allowlist](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)**. If you want to use the allowlist, ensure `isDesktopExtensionEnabled` and `isDesktopExtensionDirectoryEnabled` are not set to "false" so the allowlist can populate the available registry.

------------------------------------------------------------------------

## macOS Enterprise Configuration

Deploy configuration settings through your MDM solution using configuration profiles. Claude Desktop reads preferences from the domain \`com.anthropic.claudefordesktop\`. Use your MDM tool (Jamf Pro, Kandji, Microsoft Intune) to deploy configuration profiles to target machines or user groups. Configuration profiles allow you to manage Claude Desktop settings centrally without user intervention.

**Configuration profile tools:**

- Built-in MDM profile editors (Jamf Pro, Kandji, Intune)

- **[ProfileCreator](https://github.com/profileCreator/ProfileCreator/)** - Profile management

- **[iMazing Profile Editor](https://imazing.com/profile-editor)** - Configuration profiles

------------------------------------------------------------------------

## Windows Enterprise Configuration

Deploy configuration settings through your enterprise management solution using **[Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)** or Intune policies. Settings can be configured at machine-wide (HKLM) or per-user (HKCU) level. Machine-level settings take priority over user-level settings when both are configured.

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

------------------------------------------------------------------------

## Enterprise Policy Options

[TABLE]

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

Getting Started with Local MCP Servers on Claude Desktop

[](https://support.claude.com/en/articles/12489464-using-enterprise-search)

Using Enterprise Search

[](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)

Deploy Claude Desktop for macOS

[](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)

Deploy Claude Desktop for Windows

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
