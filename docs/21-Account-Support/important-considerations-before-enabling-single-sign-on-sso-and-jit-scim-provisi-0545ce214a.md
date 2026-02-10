---
category: "21-Account-Support"
fetched_at: "2026-02-10T10:49:16Z"
source_url: "https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning"
title: "Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning | Claude Help Center"
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

[](#h_a192e0c123)

[](#h_3bad8701c8)

[](#h_deb791918e)

[](#h_ea414d72b0)

[](#h_167139e633)

[](#h_3cfd4f318c)

[](#h_0a4a90ab59)

[](#h_44db9cb1d7)

[](#h_afdb12b7aa)

[All Collections](/en/)

[Identity Management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)

Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

# Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

Updated today

Table of contents

[](#h_a192e0c123)

[](#h_3bad8701c8)

[](#h_deb791918e)

[](#h_ea414d72b0)

[](#h_167139e633)

[](#h_3cfd4f318c)

[](#h_0a4a90ab59)

[](#h_44db9cb1d7)

[](#h_afdb12b7aa)

Before setting up SSO for your Claude or Claude Console organization, review this guide to understand key concepts, plan your approach, and complete any prerequisite steps.

## Understanding parent organizations

Our single sign-on feature uses the concept of a "parent organization"—an entity that stores SSO settings that can be shared across multiple Claude or Console organizations. Your plan type determines whether or not you have a parent organization by default:

[TABLE]

### Key things to know

- **Domain verification is required before you can configure SSO.** Domains are verified at the parent organization level—once verified, other parent organizations cannot claim the same domain.

- **Multiple organizations can be linked to the same parent organization** to share domain verification and SSO configuration. This is useful if you have both Claude (Team/Enterprise plans) and Console organizations.

- **Each parent organization can only be linked to one Identity Provider.** This means that every organization linked to a single parent organization must be managed through the same IdP.

- **Advanced Group Mappings** allow you to control which users are provisioned to which organizations under your parent, and with which roles. See **[Configure groups and assign users in your IdP](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning#h_0178209cfa)** for details.

### What this means for you

You will need to check the parent organization dynamic depending on your plan:

- **If you have a Team or Enterprise plan:** You can proceed directly to the **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** guide. Your parent organization is already in place (or will be created when you enable SSO for Team plans).

- **If you have a Claude Console organization and an existing Team or Enterprise plan:** Your Console organization may already be linked to your Team or Enterprise parent organization. Check if you can access **[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)** – if so, this indicates that the org is linked to the parent organization and SSO is already configured. If not, an Owner on your Team or Enterprise plan can initiate a merge to link your Console organization (see **[Merging organizations](#h_3bad8701c8)** below) to their parent organization and the existing SSO configuration.

- **If you have a Claude Console organization without a Team or Enterprise plan:** **[Contact our Sales team](https://claude.com/contact-sales)** to request a parent organization for your Console account. Once we create your parent organization, you will see the Identity settings page in Claude Console and can proceed with SSO setup.

------------------------------------------------------------------------

## Merging organizations

Team or Enterprise organizations can invite other orgs to join an existing parent organization and share SSO configuration.

**Important:** The **Merge Organizations** option is only available on Claude (claude.ai). Console organizations cannot initiate a merge—they must be invited by a Team or Enterprise organization.

### Requirements for merging

- The Team or Enterprise organization initiating the proposal must have verified domains in their parent organization.

- All members in the organization being invited must have email addresses matching those verified domains.

- An Admin (Console) or Owner (Claude) for the invited organization needs to approve the merge.

### To initiate a merge proposal

1.  Navigate to **[Admin settings \> Identity and access](https://claude.ai/admin-settings/identity)**.

2.  Click "Invite" under **Merge Organizations**.

3.  Select the organization you want to invite and click "Next."

4.  Review the member count and click "Invite."

5.  The merge proposal will be sent to the invited organization's Admins/Owners, with the email subject “*Parent Organization Update: New Member Organization Proposed*,” and must be approved within 14 days.

**Note:** If the person initiating the merge is also an Admin/Owner in the invited organization, only one approval is required.

Once a Console organization is merged, it will gain access to the **[Identity and access page](http://platform.claude.com/settings/identity)**, in the Admin settings, to configure SSO and provisioning settings.

------------------------------------------------------------------------

## Understanding global versus organization SSO configuration

When you access the Identity and access page, you may see two configuration sections:

- **Global access settings:** Settings in this section apply to all Claude and Console organizations that have joined the parent organization. This is where you configure domain verification, the primary SSO connection, and policies that apply across multiple joined Claude or Console organizations.

- **Organization access:** Settings in this section apply only to the specific organization you're currently viewing. This allows you to enable organization-specific features like group mappings.

------------------------------------------------------------------------

## Restricting new organization creation

Once your organization's domains are verified, owners will see a **Restrict organization creation** toggle under **Security** on the Identity and access admin settings page. Toggle this on to prevent users from creating new Claude or Console organizations—including personal accounts—using any of your verified domains.

------------------------------------------------------------------------

## Provisioning options

Once SSO is configured, you can choose how users are provisioned to your organization.

[TABLE]

**\*Note:** Only Enterprise plan organizations can enable SCIM provisioning; if a Console organization is merged with a Team plan’s parent org, it will not have access to SCIM provisioning.

For detailed information on how each provisioning method works, see **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**.

------------------------------------------------------------------------

## What happens to existing users when SSO is enabled

After enabling SSO for your organization, there are two distinct scenarios to consider for users who have individual accounts associated with your verified company domain:

### Users with existing free/Pro/Team/Max accounts who ARE added to your SSO application

These users will maintain access to their existing free/Pro/Team/Max accounts. They will have the ability to toggle between the Team or Enterprise plan account and their previous accounts by clicking the profile icon with their initials in the bottom left corner.

### Users with existing free/Pro/Team/Max accounts who are NOT added to your SSO application

- **If "Require SSO for Claude" is NOT enabled:** These users can still access their existing accounts using the "Continue with email" option.

- **If "Require SSO for Claude" IS enabled:** These users will be unable to access their existing free/Pro/Team/Max accounts. Please note that these accounts are not deleted, but will be inaccessible as users are unable to log in via SSO.

------------------------------------------------------------------------

## How to view existing Claude / Console accounts associated with your verified domain

To view or download information about your verified domains and their usage across Claude organizations:

1.  Navigate to the Identity and access section in Claude (**[claude.ai/admin-settings/identity](http://claude.ai/admin-settings/identity)**) or Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**).

2.  Click “Domain memberships” in the **Domains** section.

3.  Review the information or download details in CSV or JSON format.

------------------------------------------------------------------------

## Recommended steps before implementing SSO

### Communicate clearly with your team

- Notify all employees about the upcoming migration to SSO.

- Provide a clear timeline for when the change will occur.

- Advise employees who won't be added to the SSO application to save or **[export their conversation history](https://support.claude.com/en/articles/9450526-how-can-i-export-my-claude-data)** if SSO will be enforced.

### Plan for a smooth transition

- Schedule the SSO implementation during a time that minimizes disruption.

- Ensure your IT team is prepared to support employees with the transition.

- Have a clear process in place for granting access to authorized users.

- If possible, implement both SSO and provisioning features at the same time.

Taking time to test, communicate, and plan before enabling domain capture and SSO will help ensure a successful transition and positive experience for your organization.

------------------------------------------------------------------------

## Next steps

Once you've reviewed these considerations and completed any necessary prerequisite steps (such as merging organizations), proceed to **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** for detailed implementation instructions.

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)

Setting up single sign-on (SSO)

[](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)

Setting up JIT or SCIM provisioning

[](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)

Managing members on Team and Enterprise plans

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
