---
title: "Claude Enterprise Plan | Claude by Anthropic"
source_url: "https://www.claude.com/solutions/enterprise"
category: "18-Industry-UseCases"
fetched_at: "2026-09-19T06:30:30Z"
tags: ["enterprise"]
---

# Claude enterprise solutions

The frontier, on every desk

Put Claude to work across your organization. Help everyone think deeper, do more, and build securely.

Get Enterprise plan

[Get Enterprise plan](http://claude.ai/create/enterprise)

Get Enterprise plan

Build on Claude Platform

[Build on Claude Platform](/platform/api)

Build on Claude Platform

## Trusted by the world’s leading organizations


“Slack’s close collaboration with Anthropic has helped our Engineering and Product teams accelerate prototyping and model testing.”

97minutes per week saved by the average user through summarization and recap features

Industry:Software

Company size:Large

Product:Claude Platform

Location:North America

“With this partnership, Allianz is taking a decisive step to address critical AI challenges in insurance. Anthropic's focus on safety and transparency complements our strong dedication to customer excellence and stakeholder trust.”

90%week-over-week growth company-wide deployment, with rapid global adoption

Industry:Insurance

Company size:Large

Product:Claude Platform

Location:EMEA

“Through using Claude, we’ve saved millions, which we have reinvested in *upskilling* our customer support agents. We’ve empowered our agents to focus on those more complex issues that really require human care.”

87%reduction in customer support time

30%more accurate teams making sharper calls

Industry:Transportation

Company size:Large

Product:Claude Platform

Location:North America

“As AI becomes the interface for decisions, trust becomes the standard. Moody’s decision-grade connected intelligence is key to unlocking AI for high‑stakes credit and compliance decision‑making.”

1200%credit memo prep time cut from 40 hours to 2 minutes with Claude-built agents

Industry:Financial services

Company size:Large

Product:Claude Platform

Location:North America

“We saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.”

30+concurrent agent tasks from a single task board

97%reduction in prototyping time

Industry:Software

Company size:Large

Product:Claude Managed Agents

Location:North America

“In a highly regulated industry, we can't just throw our data and information into a large language model and hope for the best. Our conversations with Anthropic really guided in the ways we can securely use Claude for planning, for strategic tasks, for code generation.”

1000xclinical study documentation down from 10 weeks to 10 minutes

Industry:Life sciences

Company size:Large

Product:Claude Code

Location:Europe

## Built for enterprise

### Built on the best models

Claude leads on reasoning, coding, and analysis benchmarks. The same frontier models power every surface, from business apps to developer tools.

### No model training by default

Your prompts, data, and results are not used to train our models by default. Review our data practices at the Trust Center.

### Flexible by design

Pick the products and platform that are right for your teams, whether you’re collaborating with Claude at work or building your own products and offerings.

### Made to pass security review

The security, compliance, and admin controls your organization needs.

Learn more

[Learn more](https://trust.anthropic.com/)

Learn more

\*Data retention controls and OTEL monitoring are currently available on Claude Enterprise only.

Single sign-on (SSO/SAML) and domain capture

SOC 2, ISO 27001, GDPR, and CCPA compliance

Usage analytics and reporting

SCIM provisioning

Spend controls

Data retention controls\*

Compliance API

HIPAA-ready offering

Audit logs and OpenTelemetry monitoring\*

Role-based access control (RBAC)

## Bring Claude to your enterprise two ways

Deploy Claude to your workforce or build it into your products.

### Claude Enterprise

Give every employee secure access to Chat, Claude Cowork, Claude Code, and your company's connectors. Get the admin controls, management, and visibility your IT and security teams need.

See plans

[See plans](#pricing)

See plans

### Claude Platform

Access the Claude API to power new experiences, ship production-grade agents, and integrate Claude into the workflows and applications you're building.

Explore the platform

[Explore the platform](/platform/api)

Explore the platform

Results with Claude Code

90%

less time spent on complex code migrations

## Secure products for employees, everywhere your teams work

Claude Code

Claude Cowork

Claude Chat

Claude Security

Active

[Play video](#)

Play video

### Code faster across your enterprise stack

Build, debug, and ship using natural language from your terminal, IDE, Slack, or the web. Claude Code works wherever your team does.

Learn more

[Learn more](/product/claude-code/enterprise)

Learn more

[Play video](#)

Play video

### Delegate tasks to Claude with Cowork

Connect your files and tools, then hand off research, documents, and repetitive work. Get polished deliverables back while you focus on the work that needs your judgment.

Learn more

[Learn more](/product/cowork)

Learn more

[Play video](#)

Play video

### Chat: A thinking partner for everyday work

Chat with Claude to develop ideas, draft content, tighten reports, work through hard problems, and more.

Learn more

[Learn more](/product/overview)

Learn more

[Play video](#)

Play video

### Find and fix vulnerabilities with Claude Security

Claude helps security teams and developers by reviewing code for security issues, drafts patches, and explains the risk in language your whole team can act on.

Learn more

[Learn more](/product/claude-security)

Learn more

Tailor Claude to your business

Connect to Gmail, Google Drive, Slack and more to give Claude context from across your stack. Use Claude directly inside Microsoft 365 or with Google Chrome.

Learn more

[Learn more](/connectors)

Learn more

## Real work, across every function

Engineering

Marketing

Sales

Product Management

Human Resources

Security

Active

Prompt

Audit our use of the deprecated legacy-auth library across the monorepo. Generate a migration plan to move all 47 services to auth-v2, prioritized by risk and ordered by dependencies.

✻ Migration plan: legacy-auth → auth-v2


Audited 47 services, 312 call sites, 8 distinct usage patterns.


Recommended order


Phase 1 — Low risk (weeks 1–2, 12 services)  
Internal admin tools with no external dependencies. Safe to validate the auth-v2 codemod and surface unknown patterns.

Phase 2 — Leaf services (weeks 3–5, 18 services)  
No downstream consumers in the dependency graph. Failures stay contained; single staged rollout per service.

Phase 3 — Core services (weeks 6–9, 17 services)  
Auth-critical paths with downstream impact. Requires feature flags, shadow traffic comparison, and per-team rollback plans.


Risk callouts


payments-api — blocker  
Uses undocumented legacy-auth.signWithRotation() not present in auth-v2. Needs design discussion before migration.

mobile-bff — needs review  
Integration tests pinned to legacy-auth response format. Token envelope changed (token.claims → token.payload); 23 fixtures to update.

identity-gateway — coordinated cutover  
Sits in front of 31 of 47 services. Recommend cutover at the Phase 2 → 3 boundary with a 48-hour dual-write window.


Suggested next steps


1\. Open an RFC for the signWithRotation equivalent in auth-v2.  
2. Run the codemod against Phase 1 services, one PR per service.  
3. Add a CI check that fails on new legacy-auth imports in week 2.  
4. Schedule identity-gateway cutover with platform for week 5.


### Engineering

- Convert project requirements into technical specifications
- Design system architecture and component interactions
- Troubleshoot errors and runtime issues
- Identify code optimizations and performance improvements

Claude Code for Enterprise

[Claude Code for Enterprise](/product/claude-code/enterprise)

Claude Code for Enterprise

Prompt

Build a Q1 channel performance review. Pull spend and conversions from HubSpot and paid social metrics from our LinkedIn dashboards. Show ROAS by channel over the last six months and flag the channels where performance is declining.

Attachments

HubSpot_Q1_export

24 kb

CSV


8 kb

CSV

Q1 channel performance review

ROAS by channel — last 6 months

Email Organic Direct Paid social

↓ Paid social ROAS dropped 38% after Feb iOS update

↑ Email overperforming after segmentation refresh in March

→ Organic steady at 3.4x, direct holding around 2.9x

### Marketing

- Interpret market trends and consumer behavior patterns
- Brainstorm multi-platform content items
- Develop marketing campaign strategies
- Create post campaign performance reports

Prompt

I have a renewal call with Acme Corp's VP of Operations on Thursday. Pull the account picture from HubSpot, open work in Asana, and any mentions in \#acme-account on Slack. Produce a brief covering relationship status, open risks, expansion signals, and three talking points for the call. Send to me in Slack.

Connectors

Hubspot


Slack


Asana


Search

Camilla Lee

Messages

Jot something down

*Acme Corp – Thursday renewal prep*

📇 *Account:* Sarah Chen, VP Ops · Renewal Jun 30 · ARR \$148k · 240 seats (Team)

🤝 *Relationship:* Healthy, Y2 renewal · CSM Jordan Park · NPS 8 in April · Mar 18 QBR went well

⚠️ *Risks:* P1 SSO ticket open since Apr 29 (eng ETA slipped 2x) · Finance asked for ROI one-pager (Asana ACME-184, Wed) · Lattice ran discovery w/ ops leads last week

📈 *Expansion:* Adoption +42% MoM · Legal, Procurement, RevOps onboarded · Enterprise tier discussed in March · automation seat add-on ~\$22k upside

🎯 *Three talking points*

1.  Open with the SSO ticket — bring new ETA + offer a credit if it slips again
2.  Frame +42% adoption and 3 new departments as Enterprise-level value
3.  Pre-empt Lattice with the Procurement cycle-time win, then tee up the automation add-on

Sent using @Claude

### Sales

- Analyze sales calls to craft tailored account plans
- Develop objection handling strategies
- Build compelling and tailored pitches
- Interpret sales metrics and KPIs

Prompt

Score the candidate features for our Q3 roadmap. Pull usage data from Amplitude, recent product feedback from \#product-feedback in Slack, and engineering effort estimates from Linear. Score each feature on reach, impact, and effort. Rank them and flag the top three to discuss in roadmap planning Thursday.

Connectors

Amplitude


Slack


Linear


X

Q3 Prioritization.xlsx

### Product Management

- Define product vision and objectives
- Analyze user feedback and usage data
- Create product specifications and requirements documents
- Interpret product usage metrics and KPIs

Prompt

Build a 30-60-90 day onboarding plan for our new Senior Product Designer starting Monday. Pull from the role's job description, the design team's Notion handbook, recent Figma files the team has shipped. Include who they should meet in week one, what to read, what to ship by day 30, and goals for days 60 and 90.

Connectors

Figma


Notion


#### Onboarding plan: Maya Chen, Senior Product Designer

*Start date: Monday, May 18  
Manager: Priya Shah*


**Week 1 — Get oriented**

###### **People to meet (15 min each)**

- Priya Shah (managetr) — already on calendar, Monday 10am
- Jordan Lee (design lead, peer) — book Tuesday
- Sam Patel (PM partner for the checkout team)
- Two engineers from the checkout team: Ana Torres, Ben Wu

###### **Read first**

- Design system docs (Notion: /Design/System)
- Last quarter's research readouts (Notion: /Research/Q1)
- Checkout team's most recent Figma file (Onboarding-redesign-v2)

###### **Days 1–30 — Land**

- Ship one small UI fix end-to-end to learn the workflow
- Attend three user research sessions
- Present a teardown of one competitor's checkout in week 4 design crit

###### **Days 31–60 — Contribute**

- Own one in-flight project (likely the cart abandonment redesign)
- First design review on owned work by day 60

###### **Days 61–90 — Lead**

- Drive the next quarter's roadmap discussion for the checkout team
- Goal: ship one feature you scoped end-to-end

### Human Resources

- Summarize candidate feedback into hiring recommendations
- Create performance review templates and calibration summaries
- Develop learning and development programs
- Interpret headcount and workforce planning metrics

Prompt

Scan our webhook service for security vulnerabilities

● Scanning 247 files across app/, services/, routes/...

● Analyzing auth flows, input validation, file handling...

● Filtering by severity ≥ high...

● Found 4 findings in acme-corp/hookrelay


CRITICAL Shell command injection via webhook payload

app/services/notifiers/script_runner.py:21 · Command injection

  
CRITICAL JWT authentication bypass via "none" algorithm

app/auth/jwt_handler.py:28 · Auth bypass

  
CRITICAL Path traversal in export file download endpoint

app/routes/exports.py:39 · Path traversal

  
HIGH Server-side request forgery in destination URL validation

app/services/validator.py:36 · SSRF


✓ 12 lower-severity findings filtered out

### Security

- Triage alerts and prioritize real threats
- Investigate incidents and trace attack paths
- Correlate signals across logs and tools
- Draft incident reports and post-mortems
- Build detection rules and tune existing ones


## Get the Enterprise plan

Explore features

[Explore features](/pricing#team-enterprise-features)

Explore features

### Enterprise

Get started today. Includes Enterprise security and compliance, chat, Claude Code, Cowork, connectors, SSO, SCIM, audit logs, and more.

\$20

Per seat / month, billed annually.  
Usage is billed as you go at API rates, based on what your team uses. Annual commitment required. Minimum 20 seats.

Get the Enterprise plan

[Get the Enterprise plan](http://claude.ai/create/enterprise)

Get the Enterprise plan

Chat with buying specialist

[Chat with buying specialist](https://claude.ai/buying-specialist)

Chat with buying specialist

[Usage limits](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices) apply. Prices shown don’t include applicable tax. Price and plans are subject to change at Anthropic's discretion.

[Usage limits](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices) apply. Price and plans are subject to change at Anthropic's discretion.

## Build on the Claude Platform

Give developers access to the API to build AI-enabled products, services, and agents.

View documentation

[View documentation](https://platform.claude.com/docs)

View documentation

### Primitives

Building blocks to integrate Claude, including the Messages API and tools, with full control over every layer.

Learn more

[Learn more](https://platform.claude.com/docs)

Learn more

### Harnesses and infrastructure

Everything you need to ship production-grade agents, including Claude Managed Agents.

Learn more

[Learn more](https://claude.com/blog/claude-managed-agents)

Learn more

### Operating system

Controls to deploy and manage agents across your organization, including authorization, governance, and observability.

Learn more

[Learn more](https://platform.claude.com/)

Learn more

Customer story

Canva empowers employees across teams with Claude

Read story

[Read story](https://claude.com/customers/canva)

Read story

Customer story

GitLab enhances productivity with Claude

Read story

[Read story](https://claude.com/customers/gitlab-enterprise)

Read story

[Prev](#)

Prev


Code modernization

Modernize legacy code without starting over. Claude Code handles large-scale refactoring while keeping your existing business logic intact.

Learn more

[Learn more](https://claude.com/solutions/code-modernization)

Learn more

### Build on your own

Launch your own generative AI-enabled products with:

- Access to all Claude models
- Usage-based tiers
- Automatically increasing rate limits
- Pay-as-you-go pricing
- Self-serve deployment on workbench
- [Prompting guides and developer docs](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)

Start building

[Start building](/platform/api)

Start building

### Get extra support

Need custom rate limits or hands-on help? Contact our sales team for:

- Anthropic-supported onboarding
- Custom rate limits
- Billing via monthly invoices
- Prompting support
- Deployment support


[Contact sales](/contact-sales)


## FAQ

Security and compliance

Products and capabilities

Getting started

Active

### Security and compliance

### Does Anthropic train on our data?

No. Your inputs and outputs are not used to train our models by default. Review our data practices at the [Trust Center](https://trust.anthropic.com/).

### What security and compliance controls does Claude Enterprise include?

Enterprise is built for organizations with real compliance obligations:

- **Identity and access** — SSO and domain capture, SCIM and JIT provisioning, and role-based access control. Admins define groups, roles, and capabilities to govern exactly which people can use which products and connectors.
- **Visibility and logging** — audit logs, a Compliance API for programmatic access to activity logs, chats, files, and projects, OpenTelemetry, and an Analytics API for aggregated adoption and engagement data. Both feed the DLP, SIEM, and monitoring tools your security team already runs.
- **Data controls** — custom data retention, customer-managed encryption keys, and US-only inference.
- **Network controls** — IP allowlisting and network-level access control, which prevents access to personal or non-corporate Claude instances from enterprise networks.
- **Connector governance** — admins approve which connectors are available org-wide and set per-tool permissions. Connectors respect the permissions users already have in the underlying systems.

### Do you support HIPAA? Can we get a BAA?

Yes, for both the Claude Platform and Claude Enterprise. Claude Platform: Healthcare customers can sign a BAA with no Zero Data Retention requirement. The HIPAA-ready feature set in the Messages API includes prompt caching, web search, and structured outputs, with coverage expanding over time. Claude Enterprise: HIPAA-ready configuration is available with a BAA from Anthropic. Once enabled, your organization can process Protected Health Information (PHI) through Claude in accordance with HIPAA.

[Prev](#)

Prev


### Products and capabilities

### What is the Claude Enterprise plan?

Claude Enterprise is Anthropic's complete offering for organizations deploying Claude at scale. One seat gives every employee the full suite: Chat for everyday thinking work, Claude Code for engineering, Claude Cowork for delegating multi-step knowledge work, Claude Design for turning a prompt into polished visuals, and Claude in the tools your teams already use including Microsoft 365, Chrome, and Slack.

Underneath all of it sits one identity, one policy, and one set of admin controls. Connectors bring in your organization's data, skills encode how your teams actually work, and enterprise-grade security, governance, and analytics give IT and security teams the visibility they need. Please reference [pricing](https://claude.com/pricing#team-&-enterprise) for a full feature breakdown.

### What’s included in the Enterprise plan?

The Claude Enterprise plan supports deep, cross-functional workflows and provides one seat for every surface:

**One seat, every surface**

- **Chat** — a thinking partner for everyday work, on web, desktop, and mobile
- **Claude Code** — agentic coding in the terminal, IDE, Slack, and on the web
- **Claude Cowork** — delegate your tasks such as research, analysis, and documents; get finished deliverables back
- **Claude Design** — go from prompt to polished visuals, prototypes, and slides
- **Claude for Microsoft 365** — Work with Claude in Excel, PowerPoint, Word, and Outlook
- **Claude in Chrome** — Claude navigates, clicks, and fills out forms across your tabs

**Context from your organization**

- Pre-built connectors, plus custom connectors via MCP for internal systems
- Skills that capture your templates, standards, and workflows so every team runs them the same way
- Memory across conversations, so Claude carries context forward

**Security, governance, and administration**

- Single sign-on (SSO), domain capture, SCIM and JIT provisioning
- Role-based access control for fine-grained user, feature, and spend management
- Audit logs, Compliance API, and Analytics API
- Custom data retention, customer-managed encryption keys, IP allowlisting, network-level access control

### What's the difference between Chat, Claude Code, and Claude Cowork?

Chat is meant for research, brainstorming, writing, and analysis. Claude Code is for software development from your terminal, desktop app, or the web. Claude Cowork is for delegating complex tasks that run in the background. All three are included in every Enterprise plan and entitlements are managed with role-based access controls from organization settings.

### Can we connect Claude to the tools we already use?

Yes. Connectors bring context from Google Drive, Gmail, Slack, Microsoft 365 and many more into Claude. You can also use Claude directly inside Excel, PowerPoint, Outlook, Slack, and Chrome. See the [Enterprise administrator guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) for setup.

### What is Claude for Work?

Claude for Work was the earlier name for our business plans — what are now the Team and Enterprise plans. The name has been retired, but the plans still exist: Team for collaboration across smaller organizations, and Enterprise for organizations operating at scale that need advanced security, compliance, and administrative controls.

[Prev](#)

Prev


### Getting started

### Can we buy Claude through AWS Marketplace, Google Cloud, or Azure?

Claude Enterprise is available directly from Anthropic and through AWS Marketplace, where it can draw down from your existing AWS commit. Claude Platform (the API) is also available on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Azure.

### Do you support invoice billing on Claude Enterprise?

Yes. Sales-assisted Claude Enterprise plans include invoice billing. Self-serve Enterprise plans accept credit card or ACH bank transfer.

### How can I integrate Claude into my own products or services?

If you're a developer building user-facing experiences or new products with Claude, the Claude Platform is the right starting point. It gives you direct access to our models, the Claude Agent SDK, and the building blocks for production agents.

‍[Explore the developer docs](https://docs.claude.com/en/home) to get started, or [contact our Sales team](https://claude.com/contact-sales) to talk through platform plans and volume commitments.

### Where do I get an API key for Claude Platform and how does billing work?

Create an API key in the [Claude Console](http://platform.claude.com/settings/keys). For production workloads, you can use [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) to exchange your cloud provider's identity for short-lived tokens instead of managing static keys. Self-serve accounts are prepaid: add a payment method, purchase credits, and optionally enable auto-reload. Credits cover API usage, the Workbench, and Claude Code (when authenticated with an API key). Enterprise customers can use monthly invoicing instead, [contact sales](https://claude.com/contact-sales) to set this up.

[Prev](#)

Prev


## Enterprise resources

Everything you need to integrate AI thoughtfully into your organization.

[Claude Enterprise administrator guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide)

Claude Enterprise administrator guide

Claude Enterprise administrator guide

Tutorial

[Tutorial](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide)

Tutorial

[Claude Academy](https://academy.claude.com/)

Claude Academy

Claude Academy

Resource

[Resource](https://academy.claude.com/)

Resource

[Zero trust AI agents](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a0521e14a6fed28fe4a3b3b_Claude-eBook-Zero-Trust-for-AI-Agents-05132026.pdf)

Zero trust AI agents

Zero trust AI agents

Guide

[Guide](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a0521e14a6fed28fe4a3b3b_Claude-eBook-Zero-Trust-for-AI-Agents-05132026.pdf)

Guide

[Deploying Claude across your organization](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/69f24d3e09b921b92403774e_Claude-Deploying-Claude-Across-Your-Organization-04292026.pdf)

Deploying Claude across your organization

Deploying Claude across your organization

Guide

[Guide](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/69f24d3e09b921b92403774e_Claude-Deploying-Claude-Across-Your-Organization-04292026.pdf)

Guide

[The Enterprise AI transformation guide](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a05227a9465cf77dba4c51a_The%20Enterprise%20AI%20Transformation%20Guide%20101425%20(1).pdf)

The Enterprise AI transformation guide

The Enterprise AI transformation guide

Guide

[Guide](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a05227a9465cf77dba4c51a_The%20Enterprise%20AI%20Transformation%20Guide%20101425%20(1).pdf)

Guide

[The 2026 state of AI agents report](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a0522b7ebbb33addef0d238_2026%20State%20of%20AI%20Agents%20Report%20(1).pdf)

The 2026 state of AI agents report

The 2026 state of AI agents report

‍Report

[‍Report](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a0522b7ebbb33addef0d238_2026%20State%20of%20AI%20Agents%20Report%20(1).pdf)

‍Report

## Ready to bring Claude to your organization?

Get Enterprise plan

[Get Enterprise plan](http://claude.ai/create/enterprise)

Get Enterprise plan

Build on Claude Platform

[Build on Claude Platform](/platform/api)

Build on Claude Platform

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Capabilities

- Artifacts

  [Artifacts](/features/artifacts)
  Artifacts

- Design

  [Design](/product/design)
  Design

- Connectors

  [Connectors](/connectors)
  Connectors

- Plugins

  [Plugins](/plugins)
  Plugins

- Skills

  [Skills](/skills)
  Skills

Extensions

- Claude in Chrome

  [Claude in Chrome](/claude-in-chrome)
  Claude in Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Enterprise

- Overview

  [Overview](/solutions/enterprise)
  Overview

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

Use cases

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Commerce

  [Commerce](/solutions/commerce)
  Commerce

Departments

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Legal

  [Legal](/solutions/legal)
  Legal

- Sales

  [Sales](/solutions/sales)
  Sales

Industries

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Programs

- Startups

  [Startups](/programs/startups)
  Startups

- Scientists

  [Scientists](/programs/team-plan-for-scientists)
  Scientists

Developers

- Developer docs

  [Developer docs](https://code.claude.com/docs/en/overview)
  Developer docs

- Community

  [Community](/community)
  Community

- Console

  [Console](https://platform.claude.com/docs/en/home)
  Console

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

Platform

- Overview

  [Overview](/platform/api)
  Overview

- Ecosystem

  [Ecosystem](/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Claude Academy

  [Claude Academy](https://academy.claude.com/)
  Claude Academy

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](#)
  Service partners

Help and security

- Availability

  [Availability](https://www.anthropic.com/supported-countries)
  Availability

- Check files

  [Check files](https://claude.com/check-files)
  Check files

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Report abuse

  [Report abuse](https://claude.com/form/anthropic-content-reporting)
  Report abuse

- Security and compliance

  [Security and compliance](https://trust.anthropic.com/)
  Security and compliance

- Status

  [Status](https://status.anthropic.com/)
  Status

- Support center

  [Support center](https://support.claude.com/en/)
  Support center

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Research

  [Research](https://www.anthropic.com/research)
  Research

- Anthropic news

  [Anthropic news](https://www.anthropic.com/news)
  Anthropic news

- Policy on the AI Exponential
