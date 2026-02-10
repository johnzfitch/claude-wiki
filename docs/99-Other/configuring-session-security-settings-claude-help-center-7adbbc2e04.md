---
category: "99-Other"
fetched_at: "2026-02-10T10:49:35Z"
source_url: "https://support.claude.com/en/articles/13163631-configuring-session-security-settings"
title: "Configuring session security settings | Claude Help Center"
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

[](#h_108d682077)

[](#h_925fe69d9c)

[](#h_30fe52d2bc)

[](#h_243029ac31)

[All Collections](/en/)

[Claude](https://support.claude.com/en/collections/4078531-claude)

[Account Management](https://support.claude.com/en/collections/9811145-account-management)

Configuring session security settings

# Configuring session security settings

Updated this week

Table of contents

[](#h_108d682077)

[](#h_925fe69d9c)

[](#h_30fe52d2bc)

[](#h_243029ac31)

This feature is available to Admins and Owners of Enterprise plans and Console Admins.

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

## Enabling session length settings

### For Enterprise Admins

1.  Log in to your Enterprise organization as an Admin or above.

2.  Navigate to [Admin settings \> Identity and access](https://claude.ai/admin-settings/identity).

3.  Locate the **Session security** section.

4.  Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 7 days, 14 days, or 28 days.

5.  Confirm your selection by clicking “Enable.”

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1770722100&signature=1a951d3e4cd4ddacf53e0f641245e5dc77b8d9b76ec7b9b1dec33c7c69de4d62&req=dSgvHs14lIVcX%2FMW1HO4zQNx5OIgQVhRg%2F6XaftFnjxXpYvXZsMhAv%2FWPZOZ%0ARmUsOMSicgwgwK0Zn2c%3D%0A)

### For Console Admins

1.  Log in to your Console account as an Admin.

2.  Navigate to [Settings \> Identity and access](http://platform.claude.com/settings/identity).

3.  Locate the **Session security** section.

4.  Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.

5.  Confirm your selection by clicking “Enable.”

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1770722100&signature=d3b4be788feaf3866b94d32e365a2dcbb4ffdc6765ae57b77ed4a8283ab4f501&req=dSgvHs14lIVcXPMW1HO4zWzx17kxJX0gXZ5D7eVpMtdKRJ6QqH7dpSyCMBkS%0ApWYIRKy3faEcdqPqajg%3D%0A)

### What happens after enabling shortened session length?

- Existing sessions older than the selected duration will expire immediately.

- Other active sessions will expire no later than the selected duration.

- Users whose sessions expire will be directed to sign in again.

## Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

- Sessions older than the new duration will expire immediately.

- Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1770722100&signature=3a631de975c0332b1fac74f6be4b34475420744ad9744344df1ee943070d0516&req=dSgvHs14lIVcXvMW1HO4zZ7mVcic5TuiA00cbyPOLDVsKNRooHqF7EuEE3ns%0AXSXpxU7muWkRhES7t88%3D%0A)

## Disabling session length settings

To disable session duration, select "Disable" next to **Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

## Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)

What is the Pro plan?

[](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)

Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

[](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)

Setting up single sign-on (SSO)

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)

Managing members on Team and Enterprise plans

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
