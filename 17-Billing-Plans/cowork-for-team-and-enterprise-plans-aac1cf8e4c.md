---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans"
---


This article explains important limitations and considerations for Team and Enterprise organizations using Cowork during the research preview period.

Cowork is available as a research preview for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS.

 

Download for macOS

 

Admin controls

Cowork will be on by default when the research preview launches, but organization owners can manually disable it.

 

How to enable or disable Cowork:

Log in to your Team or Enterprise organization as an Owner or Primary Owner.

Navigate to Admin settings > Capabilities.

Locate the Cowork toggle.

Toggle off to disable Cowork for all users in your organization.

Note: This is an organization-wide setting. Granular controls by user or role are not available during the research preview.

Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

 

When Cowork is enabled, users can:

Access pre-installed knowledge work plugins (e.g., sales, legal, data analysis, finance, productivity)

Install additional plugins from Anthropic's public repository

Customize existing plugins or create new ones locally on their machines

Note: During the research preview, plugins are saved locally to each user's machine and cannot be centrally provisioned or managed by admins. Admin-provided plugins and org-wide plugin management are planned for a future release.

 

Compliance and monitoring limitations

Cowork currently lacks several enterprise monitoring and compliance capabilities. These limitations are important to understand before enabling Cowork for your organization.

 

No audit logging or data exports

Cowork activity is not captured in:

Audit Logs

Compliance API

Data Exports

Security teams will have no visibility into Cowork usage through standard enterprise monitoring tools. If your organization requires audit trails for compliance purposes, do not enable Cowork for regulated workloads.

 

Local conversation storage

Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard data retention policies and cannot be centrally managed or exported by admins.

 

No role-based access controls

Cowork access cannot be selectively limited by user, role, or team within your organization. The admin toggle is organization-wide only—either all users have access or none do.

 

If you need to selectively enable Cowork for specific users or teams, contact your account representative.

 

 

Security considerations
Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. While we've implemented safety measures including model training and content classifiers, the risk of prompt injection attacks is non-zero.

Users should:

Avoid granting access to files with sensitive information

Monitor Claude for suspicious actions

Limit browser and web access to trusted sources

Report suspicious behavior immediately

See Using Cowork Safely for detailed guidance.

 

Network access

Cowork respects your organization's current network egress permissions. Review your network access settings in Admin settings > Capabilities before enabling Cowork.

Related Articles
Installing Claude Desktop
Managing user feedback settings on Team and Enterprise plans
Managing members on Team and Enterprise plans
Getting started with Cowork
Using Cowork safely