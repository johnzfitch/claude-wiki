---
category: "13-Enterprise-Admin"
fetched_at: "2026-02-23T00:45:08Z"
source_url: "https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization"
title: "Find and join a Team or Enterprise organization | Claude Help Center"
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

[](#h_e83169e98f)

[](#h_4e3fb82c87)

[](#h_643400c16d)

[](#h_255b50bb3f)

[All Collections](/en/)

[Team and Enterprise Plans](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)

[Account and Member Management](https://support.claude.com/en/collections/9811449-account-and-member-management)

Find and join a Team or Enterprise organization

# Find and join a Team or Enterprise organization

Updated this week

Table of contents

[](#h_e83169e98f)

[](#h_4e3fb82c87)

[](#h_643400c16d)

[](#h_255b50bb3f)

Organization discovery allows you to find and join your company's existing Team or Enterprise plan organization when you start the sign-up flow with a work email address. Instead of creating a separate personal account, you can request to join—or be added automatically—depending on your organization's configuration.

**Note:** Organization discovery is only available for organizations that don't have **[single sign-on (SSO) enabled](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**. If your organization uses SSO, your existing provisioning settings remain in effect.

------------------------------------------------------------------------

## Admin setup

### Enable discoverability

Admins and above can manage organization discovery from **[Organization settings \> Identity and access](https://claude.ai/admin-settings/identity)**.

- **New organizations:**

  - **Team plans:** Discoverability is on by default. Admins see the option during plan onboarding with it pre-selected.

  - **Enterprise plans:** Discoverability is off by default. Admins will see the option disabled on the Identity and access page.

- **Existing organizations:** Discoverability is off by default. Admins can turn it on from settings at any time.

To enable discoverability:

1.  Log in as an Admin, Owner, Primary Owner.

2.  Navigate to **[Organization settings \> Identity and access](https://claude.ai/admin-settings/identity)**.

3.  Your organization’s domains are listed at the top of the page.

4.  Find the domain you want users to search for and click the toggle under **Discoverable**.

5.  Find **New member approval** under **Organization access** and choose either “Approve automatically” or “Approve one-by-one.”

### Configure allowed domains

Admins can specify which email domains are allowed to discover and join the organization by clicking “+ Add domain” under **Domains** on the Identity and access page. The organization owner’s domain will appear on the **Domains** list automatically, but admins can configure additional allowed domains by adding them here, verifying them, and toggling **Discoverable** on. Personal email domains (like Gmail) and .edu domains can't be added to the allowed list.

### Choose an approval mode

Admins select how join requests are handled:

**Instant approval:** Users are added to the organization’s lowest available seat tier automatically when they ask to join. Billing begins as soon as a user joins—if the organization has no available seats, billing auto-expands and a new seat is purchased immediately.

**Request + approve:** The admin reviews and approves each join request individually. Users aren't added to the organization until the admin approves. Billing begins when the request is approved—if no seats are available at that point, a new seat is purchased.

------------------------------------------------------------------------

## How to find and join an organization

When someone signs up for Claude with a work email address that matches a discoverable organization, they'll see the option to join during the signup flow. They can choose to join or continue with a personal account.

- If the organization uses **instant approval**, they're added right away.

- If the organization uses **request + approve**, a request is sent to the admin. The requester can choose to continue with a personal account (as long as "Restrict organization creation" is disabled) until the request is approved or denied.

If multiple organizations share the same email domain and are all discoverable, users will see all of them and can choose which one to join.

------------------------------------------------------------------------

## Join via invite link

Your admin may share an invite link that lets you join the organization directly, without going through the signup flow or waiting for an individual email invitation. For additional details, see **[Join an organization via invite link](https://support.claude.com/en/articles/13776697-join-an-organization-via-invite-link#h_af9f6b7825)**.

**Note:** If the invite link has been disabled or regenerated by your admin, it will no longer work. Ask your admin to share a new link.

------------------------------------------------------------------------

## SSO and organization discovery

Organization discovery is not available for organizations with single sign-on enabled. If your organization uses SSO, the feature doesn't apply—your existing provisioning settings (including any just-in-time provisioning) remain unchanged.

If you'd like to enable organization discovery, SSO must be turned off first.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)

Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

[](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)

Set up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)

Manage members on Team and Enterprise plans

[](https://support.claude.com/en/articles/13776697-join-an-organization-via-invite-link)

Join an organization via invite link

[](https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise)

Migrate your organization from Team to Enterprise

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
