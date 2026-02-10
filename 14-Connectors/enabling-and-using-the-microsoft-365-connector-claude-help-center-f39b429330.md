---
category: "14-Connectors"
fetched_at: "2026-02-10T10:49:29Z"
source_url: "https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector"
title: "Enabling and Using the Microsoft 365 Connector | Claude Help Center"
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

[](#h_4910776452)

[](#h_e7bfeb1c26)

[](#h_13ee12e144)

[](#h_5ce7ca9327)

[](#h_abfadb1d54)

[](#h_ce57889e77)

[](#h_ba673d1dff)

[](#h_a794575e3a)

[](#h_eae00eba07)

[](#h_2b65cd4fd6)

[](#h_a9852878ce)

[](#h_cbf8774a69)

[](#h_0db4b319d6)

[All Collections](/en/)

[Connectors](https://support.claude.com/en/collections/15399129-connectors)

[Pre-Built Connectors](https://support.claude.com/en/collections/17879307-pre-built-connectors)

Enabling and Using the Microsoft 365 Connector

# Enabling and Using the Microsoft 365 Connector

Updated this week

Table of contents

[](#h_4910776452)

[](#h_e7bfeb1c26)

[](#h_13ee12e144)

[](#h_5ce7ca9327)

[](#h_abfadb1d54)

[](#h_ce57889e77)

[](#h_ba673d1dff)

[](#h_a794575e3a)

[](#h_eae00eba07)

[](#h_2b65cd4fd6)

[](#h_a9852878ce)

[](#h_cbf8774a69)

[](#h_0db4b319d6)

The Microsoft 365 connector is available for users on Team and Enterprise plans.

This article explains how to connect Claude to Microsoft 365 using our pre-built MCP connector, allowing Claude to search, analyze, and access information across SharePoint, OneDrive, Outlook, and Teams.

With Microsoft 365 connected, Claude can:

- **Search and analyze documents** across SharePoint sites and OneDrive libraries

- **Access email threads** and analyze communications from Outlook

- **Review meeting information** from Teams Calendar

- **Pull insights** from Teams Chat discussions

## Enabling the Microsoft 365 connector

Enabling the Microsoft 365 connector for your organization requires two separate setup phases with specific steps that must be completed by a Microsoft Entra ID Global Administrator, and a Claude Team or Enterprise plan Owner.

**Prerequisites for enablement:**

- A Claude user with an Owner or Primary Owner role on a Team or Enterprise organization

- Someone with Global Administrator access to your organization's Microsoft Entra tenant

- Users must have Microsoft 365 accounts to connect to the connector and start using it with Claude.

### Phase 1: Initial Microsoft Entra Global Administrator Setup

A Microsoft Entra Global Administrator must complete a one-time setup process before Claude Team and Enterprise plan users can connect to the Microsoft 365 connector.

**Automatic Setup through Auth Consent Flow (Recommended)**

This process triggers an auth consent flow when connecting to the Microsoft 365 connector for the first time as a Global Administrator.

**Steps:**

**1) Enable in Claude Admin Settings**

As an organization Owner and Microsoft Entra Global Administrator:

1.  Sign in to Claude.

2.  Navigate to [Admin Settings \> Connectors](https://claude.ai/admin-settings/connectors).

3.  Click the “Browse connectors” button at the bottom of the page.

4.  Find "Microsoft 365" and click "Add to your team."

“Microsoft 365” will now appear in the list of Connectors at [Settings \> Connectors](https://claude.ai/settings/connectors).

**2) Enable in individual Claude Settings**

After completing the previous step on behalf of the Claude organization, the Microsoft Entra Global Administrator needs to connect to Microsoft 365 in their individual Claude user settings:

1.  Navigate to [Settings \> Connectors](https://claude.ai/settings/connectors).

2.  Find "Microsoft 365" in the list and click "Connect."

3.  Authenticate with your Microsoft 365 credentials.

4.  You can then review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

    - You must complete this step before any team members can connect to Microsoft 365 individually.

5.  (Optional) **To restrict which users in your Microsoft Entra tenant can use the connector**, navigate to the M365 MCP Server for Claude enterprise application in the Entra admin center ([https://entra.microsoft.com](https://entra.microsoft.com)), go to Properties and set “Assignment required?” to Yes, then add the specific users or groups under the Users and groups section—only those assigned will be able to authenticate and use the connector. Repeat this same process for the M365 MCP Client for Claude enterprise application to ensure both components are restricted to the same set of authorized users.​​​​​​​​​​​​​​​​

6.  (Optional) **To selectively restrict which permissions scopes users in your tenant can use** see the below “Permission categories” and “Selectively revoking permissions” sections.

**Manual Setup in Microsoft Entra ID**

Alternatively, you can add the connector apps and grant admin pre-consent on behalf of the whole tenant in Microsoft Entra ID. This process manually achieves what is done above in the Automatic Setup through Auth Consent Flow section above. You can use this method if your Microsoft Entra Global Administrator is not a member of the Claude Team or Enterprise organization or to troubleshoot the app install and permissions setup in Microsoft Entra ID.

This process adds two service principals to Graph Explorer; each principal establishes a service-level identity for one of the two M365 MCP for Claude app registrations in your tenant, allowing them to access and interact with your organization's data and resources via the Microsoft Graph API.

**Steps:**

**1) Add the service principals**

Using [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer), add both required service principals:

M365 MCP Client for Claude

POST [https://graph.microsoft.com/v1.0/servicePrincipals](https://graph.microsoft.com/v1.0/servicePrincipals)

{"appId":"08ad6f98-a4f8-4635-bb8d-f1a3044760f0"}

M365 MCP Server for Claude

POST [https://graph.microsoft.com/v1.0/servicePrincipals](https://graph.microsoft.com/v1.0/servicePrincipals)

{"appId":"07c030f6-5743-41b7-ba00-0a6e85f37c17"}

**2) Grant admin pre-consent**

Construct and visit the following URLs in your browser, replacing {your-tenant-id} with your organization's tenant ID:

M365 MCP Client for Claude

[https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0](https://login.microsoftonline.com/%7Byour-tenant-id%7D/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0)

M365 MCP Server for Claude

[https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17](https://login.microsoftonline.com/%7Byour-tenant-id%7D/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17)

When you visit each URL, you'll be prompted to consent to the delegated user permissions required by the integration on behalf of your organization.

**3) Enable in Claude Admin Settings**

After the Microsoft Entra Admin completes the admin consent process, an organization Owner needs to:

1.  Sign in to Claude.

2.  Navigate to [Admin Settings \> Connectors](https://claude.ai/admin-settings/connectors).

3.  Click the “Browse connectors” button at the bottom of the page.

4.  Find "Microsoft 365" and click "Add to your team."

“Microsoft 365” will now appear in the list of Connectors at [Settings \> Connectors](https://claude.ai/settings/connectors).

**4) Enable in individual Claude Settings**

After completing the previous step on behalf of the organization, the Microsoft Entra Admin needs to connect to Microsoft 365 in their individual Claude user settings:

1.  Navigate to [Settings \> Connectors](https://claude.ai/settings/connectors).

2.  Find "Microsoft 365" in the list and click "Connect."

3.  Authenticate with your Microsoft 365 credentials.

4.  You can then review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

    - You must complete this step before any team members can connect to Microsoft 365 individually.

5.  (Optional) **To restrict which users in your Microsoft Entra tenant can use the connector**, navigate to the M365 MCP Server for Claude enterprise application in the Entra admin center ([https://entra.microsoft.com](https://entra.microsoft.com)), go to Properties and set “Assignment required?” to Yes, then add the specific users or groups under the Users and groups section—only those assigned will be able to authenticate and use the connector. Repeat this same process for the M365 MCP Client for Claude enterprise application to ensure both components are restricted to the same set of authorized users.​​​​​​​​​​​​​​​​

6.  (Optional) **To selectively restrict which permissions scopes users in your tenant can use** see the below “Permission categories” and “Selectively revoking permissions” sections.

**5) Test the connector**

After you connect successfully, start a new chat with Claude and try making a simple request (e.g., “List all of my SharePoint docs”). If Claude can access the requested data using the Microsoft 365 connection, this confirms the connector is working. All Claude organization members can start authenticating with and using the Microsoft 365 connector.

### Phase 2: Enablement steps for Team and Enterprise users

Once enabled by an Owner, members can choose to connect Claude to Microsoft 365 in their settings.

**Steps:**

1.  Navigate to [Settings \> Connectors](https://claude.ai/settings/connectors).

2.  Find "Microsoft 365" in the list and click "Connect."

3.  Authenticate with your Microsoft 365 credentials to start using the Microsoft 365 connector with Claude.

**Note:** Once you've added the Microsoft connector to your Claude account, you can authenticate with the tool and use it on Claude for iOS or Android.

------------------------------------------------------------------------

## How to use the Microsoft 365 connector

Ask Claude a question that requires accessing your Microsoft 365 data. Claude will automatically detect which tools it needs and retrieve the relevant information.

### Example queries

- "Find the Q4 strategic planning document in SharePoint."

- "Summarize email conversations about the product launch."

- "What discussions happened in the Teams channel about the marketing campaign?"

- "Review meeting notes from last week's leadership sync."

Claude will provide a response based on information retrieved from your Microsoft 365 environment, including relevant context and citations when applicable.

## SharePoint and OneDrive document access

- Search documents across SharePoint sites and libraries to locate project specifications, strategic plans, and other business documents.

- Access files stored in your OneDrive and have Claude analyze content without manually uploading.

- Consolidate information from distributed file locations and analyze trends across multiple documents.

## Outlook email analysis

- Search email threads and conversations to track project status, client feedback, and team alignment.

- Access message content and metadata, filtering by date, sender, subject, and other criteria.

- Analyze communication patterns and find specific information from past correspondences.

## Outlook Calendar meeting analysis and summarization

- Review meeting summaries, attendee information, and content to prepare for upcoming meetings or understand discussions you missed.

- Analyze scheduling patterns and track project decisions.

## Teams chat capabilities

- Access Teams chat messages and channel discussions where you're a participant.

- Review team collaboration patterns and find decisions made across conversations.\
  ​

------------------------------------------------------------------------

## Which permissions does the Microsoft 365 Connector require?

When you connect the Microsoft 365 integration, you'll be asked to grant several permissions that allow Claude to access your Microsoft 365 data on your behalf.

**Important to understand:**

- All permissions are **delegated permissions**, which means Claude acts on behalf of the user’s Microsoft 365 account and can only access data they already have permission to view in Microsoft 365.

- Claude can only access Microsoft 365 data for the account you've connected.

- Claude cannot access anything beyond your existing permissions.

- These permissions enable read-only access—Claude cannot modify, delete, or create content in your Microsoft 365 tenant.

## Permission categories

During authentication, the Microsoft 365 connector requests the following permissions:

**Basic access**

- **User.Read**: Sign in and read your user profile

- **openid: Sign in with your organizational account**

- **offline_access: Maintain access to data you have given it access to**

- **email: View your email address**

- **profile: View your basic profile information**

**Email (Outlook)**

- **Mail.Read**: Read your email messages

- **Mail.ReadBasic**: Read email metadata (sender, subject, date)

- **Mail.Read.Shared**: Read emails in mailboxes you have access to

- **MailboxFolder.Read**: Read your mailbox folder structure

- **MailboxItem.Read**: Read items in your mailbox

**Calendar**

- **Calendars.Read**: Read your calendar events

- **Calendars.Read.Shared**: Read calendars shared with you

**Teams Chat**

- **Chat.Read**: Read your Teams chat messages

- **Chat.ReadBasic**: Read Teams chat metadata

- **ChatMember.Read**: Read information about chat participants

- **ChatMessage.Read**: Read your Teams chat messages

**Teams Channels**

- **Channel.ReadBasic.All**: Read channel names and descriptions

- **ChannelMessage.Read.All**: Read channel messages

**Meetings**

- **OnlineMeetings.Read**: Read your online meetings

- **OnlineMeetingTranscript.Read.All**: Read meeting transcripts

- **OnlineMeetingAiInsight.Read**: Read AI-generated meeting insights

- **OnlineMeetingArtifact.Read.All**: Read meeting recordings and artifacts

- **OnlineMeetingRecording.Read.All**: Read meeting recordings

**Files (OneDrive and SharePoint)**

- **Files.Read**: Read your files

- **Files.Read.All**: Read all files you can access

- **Sites.Read.All**: Read items in SharePoint sites

**User Directory**

- **User.ReadBasic.All**: Read basic profile information for all users in your organization (used for finding meeting availability)

## Why are these permissions needed?

These permissions allow Claude to do the following when prompted:

- Search your emails, documents, and calendar to answer your questions.

- Access meeting information and Teams discussions.

- Find and analyze content across your Microsoft 365 environment.

- Provide accurate, contextual responses based on your work data.

Additionally, the Microsoft 365 Connector searches SharePoint across the entire tenant using the permissions of the user. Site-specific search restriction is unsupported.

You can revoke these permissions as a user at any time by disconnecting the connector in your Claude settings, or as an organization by removing the connector in your Claude Admin settings.

## Selectively revoking permissions

To limit which types of resources the connector is able to access, you can selectively revoke permissions from the default set of authorized scopes the connector uses to access the Microsoft Graph API.

1.  As a Microsoft Entra Admin, go to: entra.admin.com

2.  Select “Enterprise Applications.”

3.  Next to the search box, remove the application type filter.

4.  Search for and click "M365 MCP Server for Claude."

5.  Go to Permissions.

6.  Under the Admin consent tab and in the Microsoft Graph list of permissions, select the permission you would like to revoke and click the breadcrumbs button (“...”).

7.  Select “Revoke permission,” and confirm with the “Yes, revoke” button.

8.  Claude will now be unable to access resources via that API. Attempts to access a resource with a revoked permission will show a "Failed to call tool \<name of tool\>".

9.  As a convenience, users can also individually toggle off which tools the connector will use in the Microsoft 365 connector settings to prevent Claude from trying to access a tool for which the permission is revoked.

To restore a revoked permission, follow the steps to grant admin pre-consent described in [Phase 1: Initial Microsoft Admin Setup](#h_f93cbae211). This will revert the permissions to the default state.

## Privacy and security

- **Permission inheritance:** Claude mirrors your existing Microsoft 365 permissions.

- **On-demand access:** Claude only accesses your data when you explicitly ask questions requiring it.

- **Revocable access:** You can disconnect the integration at any time through [Settings \> Connectors](https://claude.ai/settings/integrations).

Read more here: [Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide).\
​

------------------------------------------------------------------------

## Troubleshooting

### Authentication is failing. What should I check?

1.  **Verify your credentials:** Ensure you're using the correct Microsoft 365 account.

2.  **Check subscription status:** Confirm your Microsoft 365 license is active.

3.  **Review organizational policies:** Your IT team may need to approve third-party app access.

4.  **Try a different browser:** Some browsers may block authentication popups.

5.  **Disable browser extensions:** Ad blockers or privacy extensions may interfere.

6.  **Clear cookies and cache:** Try a fresh browser session.

### Claude says it can't find documents I know exist

Check the following:

1.  **Permissions:** Verify you have access to the document in Microsoft 365 directly.

2.  **Location:** Ensure the document is in SharePoint or OneDrive, not local storage.

3.  **Indexing delay:** Recently uploaded documents may take time to become searchable.

4.  **Specific location:** Try specifying the exact SharePoint site or library name.

5.  **File name:** Try searching by exact file name or unique keywords from the document.

### Search results are incomplete or irrelevant

Tips to improve your search queries:

- Be more specific about what you're looking for.

- Specify locations (site names, date ranges, document types).

- Use exact phrases for better matching.

- Try breaking up complex queries into simpler, more focused questions.

- Verify spelling of names, projects, or terms.\
  ​

------------------------------------------------------------------------

## FAQ

### Can Claude modify my Microsoft 365 data?

No. The current Microsoft 365 integration provides **read-only access**. Claude can search and analyze your data but cannot:

- Create, edit, or delete documents

- Send emails or calendar invites

- Modify SharePoint sites or OneDrive files

- Change Teams settings or permissions

### Can I use the Microsoft 365 Connector with Enterprise Search?

Yes, the Microsoft 365 Connector works well with [Enterprise Search](https://support.claude.com/en/articles/%5Bnew-id%5D-using-enterprise-search). When enabled:

1.  Enterprise Search can query Microsoft 365 alongside other connected tools.

2.  You get unified search across Slack, Google Workspace, Microsoft 365, and more.

3.  Enterprise Search's optimized prompts help Claude search more effectively.

### Can Claude search archived emails?

Yes, Claude can search all emails you have access to in Outlook, including archived messages, as long as they're accessible through your account.

### Does Claude search shared drives and team sites?

Yes, Claude can search any SharePoint sites and shared drives you have permission to access. This includes:

- Team sites

- Communication sites

- SharePoint document libraries

- Shared OneDrive folders

### Can Claude access private Teams channels?

Claude can only access Teams content that you have permission to view in Microsoft 365. If you're a member of a private channel, Claude can search for that content. If you're not a member, Claude cannot access it.

### How do I ask Claude to search specific locations?

Be specific in your queries:

- **For specific SharePoint sites:** "Search the Engineering team site in SharePoint for architecture documents."

- **For specific date ranges:** "Find emails from the last week about the Q4 budget."

- **For specific senders or topics:** "Show me Teams discussions with Sarah about the product roadmap."

- **For specific file types:** "Find PowerPoint presentations in SharePoint about sales strategy."

### Can Claude summarize long email threads?

Yes. One of Claude's strengths is analyzing and summarizing complex communications. Try: "Summarize the email thread about the vendor selection process." Claude will read the thread and provide a concise summary with key points and decisions.

### What happens if a Microsoft 365 user tries to connect before a MicrosoftEntra Global Admininstrator grants tenant-wide permission?

If a user without Microsoft Entra Global Administrator permissions attempts to connect their Microsoft 365 account, they will receive an error message indicating that an Administrator must grant app permissions before they can use the connector. The connection attempt will fail until a Microsoft Entra Global Administrator approves the necessary permissions as detailed above in Phase 1.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp)

Getting started with custom connectors using remote MCP

[](https://support.claude.com/en/articles/11724452-using-the-connectors-directory-to-extend-claude-s-capabilities)

Using the Connectors Directory to extend Claude’s capabilities

[](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)

When to use desktop and web connectors

[](https://support.claude.com/en/articles/12614810-using-the-benchling-connector-in-claude)

Using the Benchling Connector in Claude

[](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)

Microsoft 365 Connector: Security Guide

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
