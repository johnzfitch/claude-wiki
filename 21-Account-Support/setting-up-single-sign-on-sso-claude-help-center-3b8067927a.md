---
category: "21-Account-Support"
fetched_at: "2026-02-17T01:30:57Z"
source_url: "https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso"
title: "Setting up single sign-on (SSO) | Claude Help Center"
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

[](#h_d591cc665a)

[](#h_5ee916332f)

[](#h_7b2015a8a5)

[](#h_37990b54c6)

[](#h_619ae744e5)

[](#h_1eaba95f25)

[](#h_dab8f2a6bc)

[All Collections](/en/)

[Identity Management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)

Setting up single sign-on (SSO)

# Setting up single sign-on (SSO)

Updated this week

Table of contents

[](#h_d591cc665a)

[](#h_5ee916332f)

[](#h_7b2015a8a5)

[](#h_37990b54c6)

[](#h_619ae744e5)

[](#h_1eaba95f25)

[](#h_dab8f2a6bc)

Single sign-on is available for Team plans, Enterprise plans, and Console organizations.

This guide covers the steps to configure SSO for Team and Enterprise plans, and Claude Console organizations.

## Step 1: Review prerequisites and important considerations

Before proceeding with SSO setup, complete the following:

**Review the considerations guide:** Read **[Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)** to understand parent organizations, determine your setup path, and complete any prerequisite steps such as merging organizations.

**Confirm you have the required role:**

- For Team or Enterprise plans: You must be an Owner or Primary Owner

- For Claude Console: You must be an Admin

**Confirm you have access to the following:**

- DNS settings for your company's email address domain

- Your company's SSO Identity Provider (IdP) used to log in to third-party applications (e.g., Okta, Google Workspace, etc.)

Please contact your organization's IT Administrator if you do not have permissions to manage Claude or company DNS settings.

**Note:** WorkOS is Anthropic's provider for domain verification and SSO setup. More details can be found in **[Anthropic's Subprocessor List](https://trust.anthropic.com/subprocessors)**. You will be taken through a WorkOS setup flow when configuring SSO and provisioning features – find your Identity Provider in their **[Integration documentation](https://workos.com/docs/integrations)**.

------------------------------------------------------------------------

## Step 2: Verify your domain(s)

Domain verification proves that you own your company's domain. Once verified, you can configure SSO for accounts with your company's domain.

You can verify multiple domains for a single organization, but all domains must be managed through a single IdP. We don't support verifying domains from separate IdPs within the same organization.

**Note:** Verifying your domain by itself will not impact existing users' ability to access our products. End users’ access is only affected once SSO is set up and explicitly enforced.

1.  Navigate to your “Identity and access” settings in Claude (**[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)**) or Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**) – note this page will only appear on Console if you've worked with Sales to enable SSO or completed a merge proposal.

2.  In the **Domains** section, click “Add or edit domains.”

3.  Enter the domain(s) you want to verify in the **Update organization email domains modal** and click the “+” button:

    [](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047041551/518afbae9c8011a6e3c98ffb651d/d2491145-362d-490b-bdcf-66a0a7656ddc?expires=1771293600&signature=f9ff165f115a0ef61b7fb3bfc0b42bbc68b660b4f73d05d7f6b0940cfa8e0f55&req=diAjEcl6nIRaWPMW1HO4zQCfASyeh47hs0%2B6T5c8FJ%2Bb23yDSiNANNn1ZiF6%0Acn81%0A)

4.  Click “Save” when you’re finished adding domains.

5.  The domain(s) you added will now appear in the **Domains** section; click “Verify” to the right of the domain(s) to begin the verification process.

6.  Enter your domain in the text box and click “Continue”:

    [](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047042630/0617a562cd28a7ff0e607d66a30b/6bd08e1d-2b65-40ab-bc79-a257153854c1?expires=1771293600&signature=555b7ed6e0fa2d7de20a94b69c02faf94298691f89f1fddd89848d2b5c86ded5&req=diAjEcl6n4dcWfMW1HO4zWHcuhyVntKsyoyXAW0OlXp2fymgqvSTDe0uopiw%0ApxR6%0A)

7.  This will generate a TXT record. Follow the instructions to add this TXT record to your domain provider.

    - If using a subdomain (e.g., subdomain.yourcompany.com), set your TXT record on that subdomain (e.g., \_acme-challenge.subdomain.yourco. mpany.com).

8.  Wait 10 minutes for your DNS change to propagate.

    - *Note: DNS changes can take 24-48 hours to propagate globally.*

9.  When you see the green "Verified" badge, you can close the instructions page.

10. If your domain shows as "Pending," use the "Refresh" button.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047044496/b8df54a0331784cc9ae8f00112aa/bf9609c1-dc93-4665-a066-4cae2fe4b002?expires=1771293600&signature=4c1077ed18fcf60adf39ab905d1ca2f3094a51c07ae50e570af0793c4ce1434a&req=diAjEcl6mYVWX%2FMW1HO4zVjmVigCZne%2FPM2D8ZcdgrhAFk2NfZa6xu6tsHhi%0AeFOcofdBdt064DWJkQA%3D%0A)

**Note:** Once your domain is verified, you'll see a **Restrict organization creation** toggle under **Security** on the Identity and access organization settings page. Enable this if you want to prevent users from creating new Claude or Console organizations—including personal accounts—using your verified domains.

------------------------------------------------------------------------

## Step 3: Set up SSO with your Identity Provider

1.  Navigate to your Identity and access settings in Claude (**[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)**) or Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identit)**)

2.  In the **Global access settings / Organization access** section, click “Setup SSO” (or “Manage”).

3.  Follow the setup guide provided for your Identity Provider (see below for additional guides).

4.  At the end of these steps, you’ll be prompted to Test Single Sign-on to confirm there are no errors and the configuration is successful.

5.  Once complete, navigate back to the Identity and access settings page for further configuration options.

**Important:** SSO enforcement might result in users being unable to log in if they are not correctly assigned to the Anthropic app in the IdP. If you have more than one Claude/Console org connected to your “parent org,” you will want to consider creating a unique IdP Group for each. For more information, see **[enable group mappings](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning#h_adee31eeba)**.

For IdP-specific setup instructions, see:

- **[Okta SAML](https://workos.com/docs/integrations/okta-saml)**

- **[Entra ID SAML (formerly Azure AD)](https://workos.com/docs/integrations/entra-id-saml)**

- **[Google SAML](https://workos.com/docs/integrations/google-saml)**

- **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)**

- **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)**

- **[Duo SAML](https://workos.com/docs/integrations/duo-saml/4-enter-duo-saml-settings-in-your-workos-dashboard)**

------------------------------------------------------------------------

## Step 4: Choose to require SSO

You can now choose to toggle on **Require SSO for Console** and/or **Require SSO for Claude,** on the Identity and access page, under **Global access settings / Organization access** section:

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047057631/e5832754120abfd5677be84e9fa7/c3fa3224-f8b5-4aa3-b42f-1974bbbd3193?expires=1771293600&signature=28fd9907825b52b133d8cd92eb17e151e790aacafcb15aa35cd0a7d1abc897b3&req=diAjEcl7modcWPMW1HO4zS%2FkDzm9jmsD7ziFrGT%2F4DCII3udpyT3uFYgVZD2%0AkwD9%2FpHmxpw5CgSrz8g%3D%0A)

When SSO is required, users must use the “Continue with SSO” option to access Claude/Console. When SSO is not required, they will have the option to choose “Continue with SSO” or “Continue with email.”

Before you decide, review **[What happens to existing users when SSO is enabled](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning#h_644f467167)**.

------------------------------------------------------------------------

## Step 5: Choose your provisioning approach

Once SSO is enabled, you need to decide how users will be added to your organization. This is controlled by the **Provisioning mode** setting in the **Global access settings / Organization access** section of your Identity and access settings.

**Manual** is the default. Users are added and removed directly in your Claude or Console settings. Please see **[Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

**JIT (Just-in-Time) provisioning** can be enabled to automatically provision users when they first log in. By default, users assigned to your Anthropic IdP app first login, they will receive the User role. This is the simplest automated option and requires no additional configuration beyond selecting it.

### Enable group mappings - when to configure additional provisioning features

For more control over provisioning, see **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**. You'll want to review this guide if you need to:

- Automatically assign roles or seat tiers based on IdP group membership.

- Use SCIM directory sync for automatic provisioning and deprovisioning.

- Manage access across multiple organizations (e.g., if you have both a Team/Enterprise organization and a Console organization linked to the same parent and need to control which users are provisioned to each).

**Note:** We don't currently support IdP-initiated login for Claude Console organizations that share SSO settings with a Team or Enterprise plan organization. Users will be redirected to claude.ai with IdP-initiated login. As a workaround, if possible in your IdP, create a bookmark called "Claude Console" that links to platform.claude.com/login?sso=true to redirect users to Console for SP-initiated login.

------------------------------------------------------------------------

## Updating your SSO certificate

When your Identity Provider's X.509 signing certificate expires or is rotated, you'll need to update it in Claude or Console to maintain SSO functionality.

1.  Navigate to your Identity and access settings:

    - For Team and Enterprise plans: **[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)**

    - For Claude Console: **[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**

2.  In the **Global access settings / Organization access** section, click “Manage SSO.”

3.  Select “Metadata Config.”

4.  Click “Edit.”

5.  Update your certificate information and save your changes.

6.  Click "Test sign-in" on the same page to confirm everything is working.

## 

------------------------------------------------------------------------

## Turning off SSO

You can toggle **Require SSO for Claude** or **Require SSO for Console** off at any time. This will make SSO optional for all users.

To fully disconnect SSO, click “Manage SSO” then “Reset.” This will end all users’ sessions and require them to sign back in via email login link.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)

Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13371040-logging-in-to-your-console-account)

Logging in to your Console account

[](https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp)

Switching to a different Identity Provider (IdP)

[](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization)

Find and join a Team or Enterprise organization

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
