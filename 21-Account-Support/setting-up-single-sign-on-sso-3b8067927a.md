---
category: "21-Account-Support"
source_url: "https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso"
---


Single sign-on is available for Team plans, Enterprise plans, and Console organizations.

This guide covers the steps to configure SSO for Team and Enterprise plans, and Claude Console organizations.

 

Step 1: Review prerequisites and important considerations

Before proceeding with SSO setup, complete the following:

 

Review the considerations guide: Read Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning to understand parent organizations, determine your setup path, and complete any prerequisite steps such as merging organizations.

 

Confirm you have the required role:

For Team or Enterprise plans: You must be an Owner or Primary Owner

For Claude Console: You must be an Admin

Confirm you have access to the following:

DNS settings for your company's email address domain

Your company's SSO Identity Provider (IdP) used to log in to third-party applications (e.g., Okta, Google Workspace, etc.)

Please contact your organization's IT Administrator if you do not have permissions to manage Claude or company DNS settings.

Note: WorkOS is Anthropic's provider for domain verification and SSO setup. More details can be found in Anthropic's Subprocessor List. You will be taken through a WorkOS setup flow when configuring SSO and provisioning features – find your Identity Provider in their Integration documentation.

 

Step 2: Verify your domain(s)

Domain verification proves that you own your company's domain. Once verified, you can configure SSO for accounts with your company's domain.

 

You can verify multiple domains for a single organization, but all domains must be managed through a single IdP. We don't support verifying domains from separate IdPs within the same organization.

Note: Verifying your domain by itself will not impact existing users' ability to access our products. End users’ access is only affected once SSO is set up and explicitly enforced.

Navigate to your “Identity and access” settings in Claude (claude.ai/admin-settings/identity) or Console (platform.claude.com/settings/identity) – note this page will only appear on Console if you've worked with Sales to enable SSO or completed a merge proposal.

In the Global SSO Configuration section, click “Add domain.”

Follow the instructions to add your TXT record.

If using a subdomain (e.g., subdomain.yourcompany.com), set your TXT record on that subdomain (e.g., _acme-challenge.subdomain.yourco. mpany.com).

Wait 10 minutes for your DNS change to propagate. Note: DNS changes can take 24-48 hours to propagate globally.

When you see the green "Verified" badge, you can close the instructions page.

If your domain shows as "Pending," use the "Refresh" button.

Note: Once your domain is verified, you'll see a Disable new organization creation toggle in the “Global SSO Configuration” section of the Identity and access page. Enable this if you want to prevent users from creating new Claude or Console organizations—including personal accounts—using your verified domains.

 

Step 3: Set up SSO with your Identity Provider

Navigate to your Identity and access settings in Claude (claude.ai/admin-settings/identity) or Console (platform.claude.com/settings/identity)

In the Global SSO Configuration section, click “Setup SSO” (or “Manage SSO”).

Follow the setup guide provided for your Identity Provider (see below for additional guides).

At the end of these steps, you’ll be prompted to Test Single Sign-on to confirm there are no errors and the configuration is successful.

Once complete, navigate back to the Identity and access settings page for further configuration options.

Important: SSO enforcement might result in users being unable to log in if they are not correctly assigned to the Anthropic app in the IdP. If you have more than one Claude/Console org connected to your “parent org,” you will want to consider creating a unique IdP Group for each - please see Advanced Group Mappings.

For IdP-specific setup instructions, see:

Okta SAML

Entra ID SAML (formerly Azure AD)

Google SAML

OneLogin SAML

JumpCloud SAML

Duo SAML

 

Step 4: Choose to enforce SSO

You can now choose to toggle on Enforce SSO for Console and/or Enforce SSO for Claude, on the Identity and access page, under SSO Configuration section.

 

 

When SSO is enforced, users must use the “Continue with SSO” option to access Claude/Console. When SSO is not enforced, they will have the option to choose “Continue with SSO” or “Continue with email.”

 

Please review What happens to existing users when SSO is enabled before deciding.

 

Step 5: Choose your provisioning approach

Once SSO is enabled, you need to decide how users will be added to your organization. This is controlled by the Provisioning mode setting in the Organization SSO Configuration section of your Identity and access settings.

 

Manual is the default. Users are added and removed directly in your Claude or Console settings. Please see Managing members on Team and Enterprise plans.

 

JIT (Just-in-Time) provisioning can be enabled to automatically provision users when they first log in. By default, users assigned to your Anthropic IdP app first login, they will receive the User role. This is the simplest automated option and requires no additional configuration beyond selecting it.

 

Advanced Group Mappings - when to configure additional provisioning features

For more control over provisioning, see Setting up JIT or SCIM provisioning. You'll want to review this guide if you need to:

Automatically assign roles or seat tiers based on IdP group membership.

Use SCIM directory sync for automatic provisioning and deprovisioning.

Manage access across multiple organizations (e.g., if you have both a Team/Enterprise organization and a Console organization linked to the same parent and need to control which users are provisioned to each).

Note: We don't currently support IdP-initiated login for Claude Console organizations that share SSO settings with a Team or Enterprise plan organization. Users will be redirected to claude.ai with IdP-initiated login. As a workaround, if possible in your IdP, create a bookmark called "Claude Console" that links to platform.claude.com/login?sso=true to redirect users to Console for SP-initiated login.

 

Updating your SSO certificate

When your Identity Provider's X.509 signing certificate expires or is rotated, you'll need to update it in Claude or Console to maintain SSO functionality.

Navigate to your Identity and access settings:

For Team and Enterprise plans: claude.ai/admin-settings/identity

For Claude Console: platform.claude.com/settings/identity

In the Global SSO Configuration section, click “Manage SSO.”

Select “Metadata Config.”

Click “Edit.”

Update your certificate information and save your changes.

Click "Test sign-in" on the same page to confirm everything is working.

 

Turning off SSO

You can toggle Enforce SSO on Claude.ai or Enforce SSO on Console off at any time. This will make SSO optional for all users.

 

To fully disconnect SSO, click “Manage SSO” then “Reset.” This will end all users’ sessions and require them to sign back in via email login link.

Related Articles
Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning
Getting Started with Claude for Education at Your University (for Owners/Admins)
Setting up JIT or SCIM provisioning
Enforce network-level access control with Tenant Restrictions
Switching to a different Identity Provider (IdP)