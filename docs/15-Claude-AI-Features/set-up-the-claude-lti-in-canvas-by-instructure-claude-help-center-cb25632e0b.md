---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-08T20:51:44Z"
source_url: "https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure"
title: "Set up the Claude LTI in Canvas by Instructure | Claude Help Center"
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

[](#h_62540b0a37)

[](#h_6bf481f89d)

[](#h_13754a113a)

[](#h_f3b6c5a53c)

[All Collections](/en/)

[Claude for Education](https://support.claude.com/en/collections/12630177-claude-for-education)

Set up the Claude LTI in Canvas by Instructure

# Set up the Claude LTI in Canvas by Instructure

Updated yesterday

Table of contents

[](#h_62540b0a37)

[](#h_6bf481f89d)

[](#h_13754a113a)

[](#h_f3b6c5a53c)

This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

## Creating Claude LTI Developer Key in Canvas

1.  In Canvas, sign in as an administrator and navigate to **Admin -\> Developer Keys**.

2.  Click "+ Developer Key" then "+ LTI Key."

3.  Enter the following:

    1.  **Key Name:** Claude LTI

    2.  **Description:** Enter a short description for the Canva LTI 1.3 app

    3.  **Redirect URIs:** [https://claude.ai/lti/launch](https://claude.ai/lti/launch)

    4.  **Title:** Claude LTI

    5.  **Target Link URI:** [https://claude.ai/lti/launch](https://claude.ai/lti/launch)

    6.  **OpenID Connect Initiation Url:** [https://claude.ai/api/lti/login](https://claude.ai/api/lti/login)

    7.  **JWK method:** [https://claude.ai/api/lti/keys](https://claude.ai/api/lti/keys)

4.  Under **Additional Settings**, toggle Privacy Level to **Public**.

5.  Under **Placements**, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options.

6.  Click "Save."

7.  Toggle the state to **On**.

## Installing Claude LTI as an App

1.  In Canvas, go to Admin -\> Settings -\> Apps.

2.  Click "View App Configurations" then select "+ App."

3.  Select **Configuration Type** “By Client ID.”

4.  Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas).

5.  Click "Install" and refresh the course page.

[](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1770585300&signature=ca91e78530c3fa39aeabfc4b4001696eebfa3b9a1a4001df359ececef76f7eb5&req=dSYmF818n4VcWfMW1HO4zTEDZesbk%2FaCEv2ojHLMylaymsgTeZeQE76uWCuJ%0Aw3v7PQ1grgauH4TRC84%3D%0A)

## Turn on the Claude LTI Integration in Claude for Education admin settings

1.  In Claude for Education, sign in as an administrator.

2.  Navigate to [Admin settings \> Connectors](https://claude.ai/admin-settings/connectors).

3.  Find **Canvas** and click "Enable."

4.  In the settings modal that pops up, input the required information to enable the integration

    1.  **Canvas Domain**

    2.  **Client ID** (found in Canvas Admin -\> Developer Keys)

    3.  **Deployment ID** (found in Canvas Admin -\> Settings -\> Apps -\> View App Configurations -\> Claude LTI Settings Button -\> Deployment ID)

5.  Click "Save Changes." The integration should now show as enabled.

## Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/10168395-setting-up-claude-integrations)

Setting up Claude integrations

[](https://support.claude.com/en/articles/11139094-getting-started-with-claude-for-education-at-your-university-for-owners-admins)

Getting Started with Claude for Education at Your University (for Owners/Admins)

[](https://support.claude.com/en/articles/11139144-faqs-on-using-claude-for-education-at-your-university)

FAQs on Using Claude for Education at Your University

[](https://support.claude.com/en/articles/11649438-prototype-ai-powered-apps-with-claude-artifacts)

Prototype AI-Powered Apps with Claude artifacts

[](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)

Enforce network-level access control with Tenant Restrictions

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
