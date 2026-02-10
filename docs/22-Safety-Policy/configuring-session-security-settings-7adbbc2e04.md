---
category: "22-Safety-Policy"
source_url: "https://support.claude.com/en/articles/13163631-configuring-session-security-settings"
---


This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

 

Enabling session length settings
For Enterprise Admins

Log in to your Enterprise organization as an Admin or above.

Navigate to Admin settings > Identity and access.

Locate the Session security section.

Click “Enable” next to Shortened session length, then select a duration from the dropdown: 7 days, 14 days, or 28 days.

Confirm your selection by clicking “Enable.”

 

For Console Admins

Log in to your Console account as an Admin.

Navigate to Settings > Identity and access.

Locate the Session security section.

Click “Enable” next to Shortened session length, then select a duration from the dropdown: 1 day, 3 days, or 7 days.

Confirm your selection by clicking “Enable.”

 

What happens after enabling shortened session length?

Existing sessions older than the selected duration will expire immediately.

Other active sessions will expire no later than the selected duration.

Users whose sessions expire will be directed to sign in again.

 

Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

Sessions older than the new duration will expire immediately.

Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

 

 

Disabling session length settings

To disable session duration, select "Disable" next to Shortened session length. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

 

Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.

Related Articles
What is the Pro plan?
Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning
Setting up Single Sign-on (SSO)
Setting up JIT or SCIM provisioning
Managing members on Team and Enterprise plans