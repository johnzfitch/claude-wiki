---
category: "14-Connectors"
source_url: "https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide"
---


What It Is

The Microsoft 365 Connector is an Anthropic-hosted integration that enables Claude to securely access Microsoft 365 services (Outlook, SharePoint, OneDrive, Teams) through user-delegated permissions. Anthropic has completed Microsoft's publisher verification process, associating our verified Microsoft Partner Network account with this application to confirm our organizational identity.

 

The connector operates as a secure proxy, and your Microsoft 365 documents, emails, and files remain in your tenant. The connector only retrieves data on-demand during active queries and does not cache file content. Credentials are encrypted and managed by Anthropic's backend infrastructure. The MCP server itself does not store or manage these credentials. Microsoft's Azure SDK handles the On-Behalf-Of token exchange and caching on a per-user basis for accessing the Graph API.

 

Access Restriction
Access Can Be Fully Restricted

The connector provides multiple layers of access control to address your security requirements. For detailed information on administration of the Microsoft 365 Connector see Enabling and Using the Microsoft 365 Connector.

 

1. Organization-Level Gating

Access to the connector for Team and Enterprise plan users requires a two-step approval process. First, Owners must explicitly enable the Microsoft 365 connector in Claude Admin Settings by navigating to Admin Settings → Connectors → Browse connectors → Add "Microsoft 365". Until this approval is granted, users have no access.

 

Second, after the Owner enables the connector, a Microsoft Entra Global Administrator must complete individual authentication and grant consent on behalf of the whole organization before any team members can connect.

 

2. Microsoft Entra Admin Pre-Consent Requirement

Before users can access the connector, a Microsoft Entra Admin must complete a one-time setup, which will:

Add two service principals and Enterprise apps in Microsoft Entra ID (M365 MCP Client and M365 MCP Server). This establishes a service-level identity for the Microsoft 365 Connector apps in your tenant

Grant admin pre-consent for your Microsoft 365 tenant

Optionally restrict which Microsoft Entra ID users and groups are allowed to use the connector

Optionally restrict permissions the connector is allowed to use to selectively control which Microsoft 365 services are accessible

 

3. Granular Permission Revocation

You can selectively disable specific capabilities via Microsoft Entra Admin Center. For example:

To Restrict

 

Action

 

Effect

All access

 

Disable connector in Claude Admin Settings

 

Complete shutdown

SharePoint only

 

Revoke Sites.Read.All permission in Entra

 

Blocks SharePoint

Email access

 

Revoke Mail.Read permission in Entra

 

Blocks Outlook

Teams chat

 

Revoke Chat.Read permission in Entra

 

Blocks Teams

OneDrive files

 

Revoke Files.Read and/or Files.Read.All

 

Blocks reading files from OneDrive 

Changes take effect immediately for all users in your organization. Note that users can also choose to disable capabilities that they have permission to use during a chat or session by selectively toggling off the connector’s tools.

 

4. Microsoft Conditional Access Integration

The connector fully supports your existing Entra (Azure AD) policies:

Multi-factor authentication (MFA): Enforce MFA for connector access

Device compliance: Require managed/compliant devices

IP restrictions: Limit Microsoft authentication to corporate network or VPN

Group-based access: Restrict to specific security groups

5. User-Level Permissions

The Microsoft 365 Connector uses delegated permissions.

Users can only access Microsoft 365 data they already have permission for

SharePoint search requires Sites.Read.All permission. Site-specific permissioning (using *.Selected permissions) is not supported because the underlying search is tenant-wide.

Users cannot bypass SharePoint sharing settings or folder permissions

Users cannot access other users' private files or emails

Delegated permissions inherently respect Microsoft 365 data loss prevention (DLP) policies

6. Token Management

Refresh tokens expire after 90 days of inactivity by default, requiring re-authentication. This can be customized in Microsoft Entra ID using a token lifetime policy.

Access tokens typically expire within 60-90 minutes per Microsoft Entra ID defaults and are automatically refreshed

Admins or users can revoke access anytime via Microsoft Entra ID

The Microsoft 365 Connector never sees or stores passwords

 

Security Architecture Summary
Authentication Flow

OAuth 2.0 On-Behalf-Of (OBO): Industry-standard delegated authentication

PKCE protection: Public client uses Proof Key for Code Exchange to prevent authorization code interception

Two-stage token exchange: User authenticates to obtain access token for MCP server, then MCP server exchanges it for Graph API access using OBO flow with confidential client credentials. In this flow, not even the user or their Claude client has access to the OBO tokens. Only the MCP server can access and use tokens with access to the user’s data via the Microsoft Graph API.

No credential storage: Users never share Microsoft passwords with Anthropic

Encrypted token storage: Access and refresh tokens are encrypted while cached by the Claude backend

Data Flow

Documents and other content are retrieved only during active queries

Tool call results from the connector that are part of stored chats are retained

The user who requested the Claude chat can see the tool call results and Claude’s response incorporating the data

Other users shared on the chat can only see Claude’s response incorporating the result of the tool call

Each request creates a fresh data flow which is cleaned up after the response is returned

Multi-Tenant Isolation

Microsoft Entra tenants are cryptographically separated from each other using a common-scoped multi-tenant configuration

Multi-tenant isolation is cryptographically enforced through digitally signed access tokens that bind each user to their organization’s tenant

 

Available Capabilities
Current Features (Read-Only Access)

The connector provides read-only access to:

Tool

 

Description

 

Required Permission

sharepoint_search

 

Search SharePoint documents and pages

 

Sites.Read.All

sharepoint_folder_search

 

Find SharePoint folders by name

 

Sites.Read.All

outlook_email_search

 

Search email with sender/date filters

 

Mail.Read

outlook_calendar_search

 

Search calendar events

 

Calendars.Read

find_meeting_availability

 

Find available meeting times

 

Calendars.Read

chat_message_search

 

Search Teams chat messages

 

Chat.Read

read_resource

 

Read files, emails, or chat by URI

 

Varies by resource type

 

Permissions List

Basic Permissions

User.Read - Sign in and read user profile (basic requirement)

Mail Permissions

Mail.Read - Read user mail (required for email tools/resources)

Mail.ReadBasic - Read user mail metadata (alternative for limited functionality)

Mail.Read.Shared - Read user and shared mail

MailboxFolder.Read - Read a user's mailbox folders

MailboxItem.Read - Read a user's mailbox items

Calendar Permissions

Calendars.Read - Read user calendars and events

Calendars.Read.Shared - Read calendars user can access, including shared

User Directory

User.ReadBasic.All - Read basic profiles of all users (for meeting availability)

Chat Permissions

Chat.Read - Read user chat messages

Chat.ReadBasic - Read user chat metadata (alternative for limited functionality)

ChatMember.Read - Read the members of chats

ChatMessage.Read - Read user chat messages (more specific than Chat.Read)

Channel Permissions

Channel.ReadBasic.All - Read the names and descriptions of channels

ChannelMessage.Read.All - Read channel messages

Meeting Permissions

OnlineMeetings.Read - Read online meetings

OnlineMeetingTranscript.Read.All - Read meeting transcripts

OnlineMeetingAiInsight.Read - Read all AI Insights for online meetings

OnlineMeetingArtifact.Read.All - Read user's online meeting artifacts

OnlineMeetingRecording.Read.All - Read all recordings of online meetings

Files Permissions

Files.Read - Read user files

Files.Read.All - Read all files user can access

Sites Permissions

Sites.Read.All - Read items in all site collections

Sites.Selected – Manages application access at the site collection level, providing access to a specific site collection

 

Current Limitations

No write capabilities: Cannot send emails, schedule meetings, create/modify documents, or post Teams messages

User-level access only: Access with service principal authentication is not supported

 

FAQs
Q: Can we test with a small pilot group before enterprise-wide rollout?

A: Yes. The recommended approach is to use app assignment to restrict who can use the connector:

Owner enables connector in Claude Admin Settings

Microsoft Entra Admin completes pre-consent setup

Use Microsoft Entra Enterprise App assignment to restrict access to specific users or groups (e.g., assign only "IT Security Test Group" to the app).

Expand groups progressively for gradual deployment

Q: How do we ensure no data leakage occurs between our organization and others in the multi-tenant environment?

A: Multi-tenant isolation ensures complete separation:

Server uses the common tenant configuration to accept tokens from any Microsoft Entra ID tenant

Each user's token contains their organization's tenant ID (tid claim) which is validated

Graph API tokens obtained through OBO are automatically scoped to the user and their tenant

Cross-tenant token access is prevented cryptographically by the design of Microsoft Graph’s OAuth 2.0 implementation.

Q: What happens if an employee tries to access company data from a personal Claude account?

A: The connector validates identity during authentication:

User must have access to the Team/Enterprise organization where the connector is enabled

Microsoft login validates user's Microsoft Entra ID credentials

Token validation confirms user's tenant ID

Graph API enforces tenant boundaries

Personal Claude accounts cannot access enterprise Microsoft 365 data without organization membership

Q: Do you have audit logging for compliance?

A: Yes, audit logging is available for your compliance needs. All Graph API calls made by the connector are logged in your organization's Microsoft 365 audit log, which you can access through the M365 Compliance Center. These logs show the timestamp, user, operation performed, and resource accessed, with retention periods matching your Microsoft 365 audit policy. Additionally, Anthropic logs authentication and tool execution events.

 

Q: Can we revoke access if we discover unauthorized usage?

A: There are multiple revocation methods:

User-level: Users disconnect via Claude Settings → Connectors

Admin-level: Disable connector in Claude Admin Settings (all users affected)

Permission-level: Revoke specific permissions in Microsoft Entra Admin Center

Tenant-level: Revoke all permissions in Microsoft Entra Admin Center

Q: What certifications does Anthropic have?

A: Anthropic has the following certifications:

SOC 2 Type II (annual audit)

ISO 27001 certified

GDPR compliant (DPA available)

Microsoft publisher-verified application

Additional resources

Claude Help Center: Enabling and Using the Microsoft 365 Connector

Overview of Microsoft Graph permissions: Delegated permissions

Related Articles
Getting started with custom connectors using remote MCP
Anthropic Connectors Directory FAQ
Using the Connectors Directory to extend Claude’s capabilities
Enabling and Using the Microsoft 365 Connector
Enforce network-level access control with Tenant Restrictions