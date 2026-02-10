---
category: "99-Other"
source_url: "https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions"
---


The Claude Console uses a role-based access system with five distinct roles: User, Claude Code User, Developer, Billing, and Admin. Each role has specific permissions and capabilities designed to help teams manage their API access securely.

 

Role Types and Permissions
User

Can only use Workbench

Cannot view API keys, usage logs, or billing details. 

Claude Code User

Can use Workbench and Claude Code

Can access Claude Code workspace in your org

Developer

Can use Workbench and Claude Code

Can manage API keys

Can view usage and cost data

Billing

Can use Workbench

Can manage billing details

Can view usage and cost data

Cannot access Claude Code workspace in your org

Admin

Can perform all actions available to User, Developer, and Billing roles

Can manage users and their role assignments

Workspace-Level Permissions

Organization Admins automatically receive Workspace Admin permissions in all Workspaces.

Organization Billing role holders can view cost, usage, and limit values across all Workspaces.

Organization-level roles serve as a baseline, while Workspace roles can grant additional permissions.

For example, a User at the organization level can be granted Admin permissions within specific Workspaces

Important Notes

Removing an Admin or Billing role does not automatically update the billing email in our payment processor.

To modify the primary billing email address or add additional billing contact emails, please contact our Support Team.

Related Articles
How do I pay for my Claude API usage?
Cost and Usage Reporting in the Claude Console
Creating and managing Workspaces in the Claude Console
Claude Code usage analytics
Inviting members to the Claude Console