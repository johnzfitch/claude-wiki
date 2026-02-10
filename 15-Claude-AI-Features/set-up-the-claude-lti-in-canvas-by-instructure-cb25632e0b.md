---
category: "15-Claude-AI-Features"
source_url: "https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure"
---


This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

 

Creating Claude LTI Developer Key in Canvas

In Canvas, sign in as an administrator and navigate to Admin -> Developer Keys.

Click "+ Developer Key" then "+ LTI Key."

Enter the following:

Key Name: Claude LTI

Description: Enter a short description for the Canva LTI 1.3 app

Redirect URIs: https://claude.ai/lti/launch

Title: Claude LTI

Target Link URI: https://claude.ai/lti/launch

OpenID Connect Initiation Url: https://claude.ai/api/lti/login

JWK method: https://claude.ai/api/lti/keys

Under Additional Settings, toggle Privacy Level to Public.

Under Placements, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options.

Click "Save."

Toggle the state to On.

 

Installing Claude LTI as an App

In Canvas, go to Admin -> Settings -> Apps.

Click "View App Configurations" then select "+ App."

Select Configuration Type “By Client ID.”

Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas).

Click "Install" and refresh the course page.

 

Turn on the Claude LTI Integration in Claude for Education admin settings

In Claude for Education, sign in as an administrator.

Navigate to Admin settings > Connectors.

Find Canvas and click "Enable."

In the settings modal that pops up, input the required information to enable the integration

Canvas Domain

Client ID (found in Canvas Admin -> Developer Keys)

Deployment ID (found in Canvas Admin -> Settings -> Apps -> View App Configurations -> Claude LTI Settings Button -> Deployment ID)

Click "Save Changes." The integration should now show as enabled.

Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).

Related Articles
Setting Up Claude Integrations
Getting Started with Claude for Education at Your University (for Owners/Admins)
FAQs on Using Claude for Education at Your University
Prototype AI-Powered Apps with Claude artifacts
Enforce network-level access control with Tenant Restrictions