---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T00:43:41Z"
last_modified: "Fri, 27 Feb 2026 22:56:48 GMT"
source_url: "https://claude.com/resources/tutorials/using-the-icd-10-connector-in-claude"
title: "Using the ICD-10 Connector in Claude | Claude"
---
- [](https://www.anthropic.com/claude/opus)
    Opus
  - [](https://www.anthropic.com/claude/sonnet)
    Sonnet
  - [](https://www.anthropic.com/claude/haiku)
    Haiku

- Platform

  - [](/platform/api)
    Overview
  - [](https://docs.claude.com/)
    Developer docs
  - [](http://claude.com/pricing#api)
    Pricing

  - [](https://platform.claude.com/)
    Console login

- Solutions

  Use cases

  - [](/solutions/agents)
    AI agents
  - [](/solutions/claude-code-security)
    Claude Code Security
  - [](/solutions/coding)
    Coding

  Industries

  - [](/solutions/customer-support)
    Customer support
  - [](/solutions/education)
    Education
  - [](/solutions/financial-services)
    Financial services
  - [](/solutions/government)
    Government
  - [](/solutions/healthcare)
    Healthcare
  - [](/solutions/life-sciences)
    Life sciences
  - [](/solutions/nonprofits)
    Nonprofits

- Pricing

  - [](/pricing)
    Overview
  - [](/pricing#api)
    API

  Pricing

  - [](/pricing/max)
    Max plan
  - [](/pricing/team)
    Team plan
  - [](/pricing/enterprise)
    Enterprise plan

- Resources

  Insights

  - [](/blog)
    Blog
  - [](/customers)
    Customer stories
  - [](https://www.anthropic.com/events)
    Events
  - [](https://www.anthropic.com/news)
    Anthropic news

  Learn

  - [](https://www.anthropic.com/learn)
    Anthropic Academy
  - [](/resources/courses)
    Courses
  - [](/resources/tutorials)
    Tutorials
  - [](/resources/use-cases)
    Use cases

  Tools

  - [](/connectors)
    Connectors
  - [](/plugins)
    Plugins

- [](https://claude.ai/login)
  Login

&nbsp;

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

[](#)

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- Meet Claude

  Products

  - [](/product/overview)
    Claude
  - [](/product/claude-code)
    Claude Code
  - [](/product/cowork)
    Cowork

  Features

  - [](/chrome)
    Claude in Chrome
  - [](/claude-in-slack)
    Claude in Slack
  - [](/claude-in-excel)
    Claude in Excel
  - [](/claude-in-powerpoint)
    Claude in PowerPoint
  - [](/skills)
    Skills

  Models

  - [](https://www.anthropic.com/claude/opus)
    Opus
  - [](https://www.anthropic.com/claude/sonnet)
    Sonnet
  - [](https://www.anthropic.com/claude/haiku)
    Haiku

- Platform

  - [](/platform/api)
    Overview
  - [](https://docs.claude.com/)
    Developer docs
  - [](http://claude.com/pricing#api)
    Pricing

  - [](https://platform.claude.com/)
    Console login

- Solutions

  Use cases

  - [](/solutions/agents)
    AI agents
  - [](/solutions/claude-code-security)
    Claude Code Security
  - [](/solutions/coding)
    Coding

  Industries

  - [](/solutions/customer-support)
    Customer support
  - [](/solutions/education)
    Education
  - [](/solutions/financial-services)
    Financial services
  - [](/solutions/government)
    Government
  - [](/solutions/healthcare)
    Healthcare
  - [](/solutions/life-sciences)
    Life sciences
  - [](/solutions/nonprofits)
    Nonprofits

- Pricing

  - [](/pricing)
    Overview
  - [](/pricing#api)
    API

  Pricing

  - [](/pricing/max)
    Max plan
  - [](/pricing/team)
    Team plan
  - [](/pricing/enterprise)
    Enterprise plan

- Resources

  Insights

  - [](/blog)
    Blog
  - [](/customers)
    Customer stories
  - [](https://www.anthropic.com/events)
    Events
  - [](https://www.anthropic.com/news)
    Anthropic news

  Learn

  - [](https://www.anthropic.com/learn)
    Anthropic Academy
  - [](/resources/courses)
    Courses
  - [](/resources/tutorials)
    Tutorials
  - [](/resources/use-cases)
    Use cases

  Tools

  - [](/connectors)
    Connectors
  - [](/plugins)
    Plugins

- [](https://claude.ai/login)
  Login

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

1.  Tutorials

    [](/resources/tutorials)
    Tutorials

    /

2.  
    Using the ICD-10 Connector in Claude

Explore here

- [](#)

  Ask questions about this page
- [](#)

  Copy as markdown

# Using the ICD-10 Connector in Claude

- 

  Category

  Healthcare

- 

  Product

- 

  Reading time

  Watch time

  5

  min

  min

- 

  Share

  [Copy link](#)
  https://claude.com/resources/tutorials/using-the-icd-10-connector-in-claude

The ICD-10 connector gives Claude access to ICD-10-CM diagnosis codes and ICD-10-PCS procedure codes (2026 edition), enabling healthcare organizations to search, validate, and explore medical coding hierarchies required for HIPAA-compliant billing and clinical documentation. This article explains how to set up and use the ICD-10 integration with Claude to streamline medical coding and billing compliance workflows.

The ICD-10 integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

This integration provides access to the 2026 International Classification of Diseases, 10th Revision code sets used in the United States healthcare system. ICD-10 is based on the World Health Organization (WHO) classification system, with ICD-10-CM (Clinical Modification) authorized by WHO and developed by the CDC's National Center for Health Statistics (NCHS) for diagnosis coding, and ICD-10-PCS (Procedure Coding System) developed by CMS for inpatient procedure coding. Both code sets are HIPAA-mandated standards that became effective October 1, 2015, and are updated annually. The FY 2026 release includes over 550 diagnosis code changes (487 additions, 28 deletions, 38 revisions) and became effective October 1, 2025, for patient encounters and discharges through September 30, 2026.

This connector provides nine primary tool calls that access ICD-10-CM and ICD-10-PCS codes.

- **search_diagnosis_by_description** enables users to find diagnosis codes by disease name or medical terminology (e.g., "diabetes", "myocardial infarction", "breast cancer"), using case-insensitive text matching across code descriptions with automatic filtering for HIPAA-valid codes (excludes category headers that cannot be billed).
- **search_diagnosis_by_code** finds diagnosis codes by exact code match or prefix search (e.g., "E11" returns all Type 2 diabetes codes), useful for exploring code families and related conditions.
- **search_procedure_by_description** searches ICD-10-PCS procedure codes by anatomical terms and root operations (e.g., "appendix", "resection", "percutaneous endoscopic" for laparoscopic procedures), noting that PCS uses standardized terminology rather than common procedure names.
- **search_procedure_by_code** finds procedure codes by exact match or prefix (e.g., "0DT" returns gastrointestinal resection procedures), enabling systematic exploration of procedure code families.
- **lookup_code** retrieves complete details for a specific code when the exact code is known (e.g., "E11.65", "0DTJ4ZZ"), returning short and long descriptions plus HIPAA transaction validity status.
- **validate_code** checks whether a code exists in the database and confirms its validity for HIPAA-covered transactions, distinguishing between billable codes and category headers.
- **get_hierarchy** retrieves the full code family tree under a category prefix (e.g., "E11" returns all 117 Type 2 diabetes codes), showing parent-child relationships and complication progressions.
- **get_by_category** navigates diagnosis codes by chapter (single letter like "E" for Endocrine diseases) or 3-character category (e.g., "E11" for Type 2 Diabetes).
- **get_by_body_system** retrieves ICD-10-PCS procedure codes for specific anatomical systems using the first character body system code (e.g., "0" for Central Nervous System, "D" for Gastrointestinal).

On the provider side, the connector accesses a locally stored database of the 2026 ICD-10-CM and ICD-10-PCS code sets published by CMS and CDC/NCHS. The database includes code structure (chapter, category, subcategory), short and long descriptions, and HIPAA transaction validity flags. ICD-10-CM codes are 3-7 alphanumeric characters documenting diagnoses; ICD-10-PCS codes are exactly 7 alphanumeric characters documenting inpatient procedures. Category header codes (shorter codes like "E11" or "E11.3") serve as organizational groupings and are NOT valid for billing—only fully specified codes with maximum detail are HIPAA-compliant.

‍

## **Who should use the ICD-10 integration**

- **Medical Coders & Health Information Management Professionals:** Search and validate diagnosis and procedure codes for accurate medical record documentation, ensure code specificity meets billing requirements, verify HIPAA transaction validity, and explore code hierarchies to select the most appropriate codes.
- **Revenue Cycle Management Teams & Billing Specialists:** Validate code accuracy before claim submission to reduce denials, verify codes are valid for the current fiscal year (FY 2026), identify codes requiring additional documentation specificity, and ensure compliance with payer coding requirements.
- **Clinical Documentation Improvement (CDI) Specialists:** Query physicians for more specific documentation when codes lack required detail, identify incomplete or non-specific codes that may result in claim denials, ensure documentation supports the most accurate and specific ICD-10 codes, and track code hierarchy relationships for comorbidity and complication coding.
- **Healthcare IT & EHR Integration Teams:** Build and maintain code validation logic in electronic health record systems, implement automated code suggestion features based on clinical documentation, create coding reference tools integrated into clinical workflows, and ensure coding databases are updated with annual ICD-10 revisions.
- **Medical Auditors & Compliance Officers:** Audit coded medical records for accuracy and specificity, identify patterns of coding errors or undercoding, verify compliance with CMS coding guidelines and HIPAA standards, and conduct retrospective reviews of diagnosis and procedure coding quality.
- **Healthcare Data Analysts & Population Health Teams:** Analyze disease prevalence and treatment patterns using standardized ICD-10 codes, track diagnosis trends across patient populations, conduct outcomes research using procedure codes, and support quality reporting and value-based care initiatives with accurate coded data.

‍

## **Setting up the ICD-10 integration**

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Admin settings \> Connectors
2.  Click "Browse connectors"
3.  Click “**ICD-10**”
4.  Click “Add to your team”

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors
2.  Find “**ICD-10**”
3.  Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/healthcare`
2.  Command:` /plugin install /plugin install icd10-codes@healthcare`
3.  Restart Claude Code
4.  Verify that the server is connected with /mcp

Technical details of the ICD-10 integration can be found in the [ICD-10 MCP Server Documentation](https://docs.mcp.deepsense.ai/guides/icd10_codes.html).

‍

## **Example use cases**

**Medical Coding & Documentation Accuracy**

- Scenario: Coders and CDI specialists ensuring accurate, specific code selection for billing and documentation
- Sample Prompts:\
  - *"Find all ICD-10 codes for Type 2 diabetes with complications. Show me the complete hierarchy"*
  - *"Validate code E11.65 for HIPAA billing. Is this code specific enough or is it a category header?"*
  - *"Search for diagnosis codes related to hypertension with chronic kidney disease"*
  - *"What ICD-10-PCS codes exist for laparoscopic appendectomy? Search procedures for 'appendix' and 'percutaneous endoscopic'"*

**Billing Compliance & Claims Processing**

- Scenario: Revenue cycle teams validating codes before claim submission to prevent denials
- Sample Prompts:\
  - *"Is E11.9 valid for HIPAA transactions? What's the full description?"*
  - *"Search for all myocardial infarction diagnosis codes that are valid for billing"*
  - *"Find procedure codes for coronary artery bypass graft by searching code prefix '021'"*
  - *"Validate this procedure code 0DTJ4ZZ - is it valid for inpatient hospital billing?"*

**Clinical Documentation Improvement & Audit**

- Scenario: CDI specialists and auditors reviewing documentation specificity and code appropriateness
- Sample Prompts:\
  - *"Show me the hierarchy of breast cancer diagnosis codes to identify if we're using the most specific code"*
  - *"Search for diabetes codes with retinopathy complications - which codes distinguish between severity levels?"*
  - *"What ICD-10 codes exist in the category E08 for diabetes due to underlying condition?"*
  - *"Find all gastrointestinal resection procedures by body system. Are we coding to the appropriate specificity level?"*

## Related tutorials

[How to use the Prior Auth Review sample skill with Claude](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)

How to use the Prior Auth Review sample skill with Claude

How to use the Prior Auth Review sample skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)

Tutorial

[Using the Function Connector in Claude](/resources/tutorials/using-the-function-connector-in-claude)

Using the Function Connector in Claude

Using the Function Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-function-connector-in-claude)

Tutorial

[Using the HealthEx Connector in Claude](/resources/tutorials/using-the-healthex-connector-in-claude)

Using the HealthEx Connector in Claude

Using the HealthEx Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-healthex-connector-in-claude)

Tutorial

[How to use the FHIR Developer agent skill with Claude Code](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)

How to use the FHIR Developer agent skill with Claude Code

How to use the FHIR Developer agent skill with Claude Code

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)

Tutorial

[Homepage](https://claude.com)

Homepage

[Next](#)

Next

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)

Button Text

Learn

[Button Text](#)

Button Text

Code

[Button Text](#)

Button Text

Write

- Help me develop a unique voice for an audience

  [](#)

  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style

  [](#)

  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas

  [](#)

  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply

  [](#)

  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas

  [](#)

  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview

  [](#)

  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept

  [](#)

  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips

  [](#)

  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me

  [](#)

  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies

  [](#)

  This is another test

- Write grant proposals

  [](#)

  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts

  [](#)

  this is a test

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

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

- Cowork

  [Cowork](/product/cowork)
  Cowork

- Max plan

  [Max plan](/pricing/max)
  Max plan

- Team plan

  [Team plan](/pricing/team)
  Team plan

- Enterprise plan

  [Enterprise plan](/pricing/enterprise)
  Enterprise plan

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)
  Log in

Features

- Claude in Chrome

  [Claude in Chrome](/chrome)
  Claude in Chrome

- Claude in Slack

  [Claude in Slack](/claude-in-slack)
  Claude in Slack

- Claude in Excel

  [Claude in Excel](/claude-in-excel)
  Claude in Excel

- Claude in PowerPoint

  [Claude in PowerPoint](/claude-in-powerpoint)
  Claude in PowerPoint

- Skills

  [Skills](/skills)
  Skills

Models

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Solutions

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Claude Code Security

  [Claude Code Security](/solutions/claude-code-security)
  Claude Code Security

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Education

  [Education](/solutions/education)
  Education

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

Claude Developer Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://docs.claude.com/)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Amazon Bedrock

  [Amazon Bedrock](/partners/amazon-bedrock)
  Amazon Bedrock

- Google Cloud’s Vertex AI

  [Google Cloud’s Vertex AI](/partners/google-cloud-vertex-ai)
  Google Cloud’s Vertex AI

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Console login

  [Console login](https://platform.claude.com/)
  Console login

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Connectors

  [Connectors](/connectors)
  Connectors

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](/plugins)
  Plugins

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/partners/services)
  Service partners

- Startups program

  [Startups program](/programs/startups)
  Startups program

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
  Use cases

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Responsible Scaling Policy

  [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
  Responsible Scaling Policy

- Security and compliance

  [Security and compliance](https://trust.anthropic.com/)
  Security and compliance

- Transparency

  [Transparency](https://anthropic.com/transparency)
  Transparency

Help and security

- Availability

  [Availability](https://www.anthropic.com/supported-countries)
  Availability

- Status

  [Status](https://status.anthropic.com/)
  Status

- Support center

  [Support center](https://support.claude.com/en/)
  Support center

Terms and policies

Privacy choices

### Cookie settings

We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy [here](https://www.anthropic.com/legal/cookies).

Customize cookie settings

Reject all cookies

Accept all cookies

###### Necessary

Enables security and basic functionality.

Required

###### Analytics

Enables tracking of site performance.

Off

###### Marketing

Enables ads personalization and tracking.

Off

Save preferences

Privacy policy

[Privacy policy](https://www.anthropic.com/legal/privacy)

Privacy policy

Responsible disclosure policy

[Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)

Responsible disclosure policy

Terms of service: Commercial

[Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)

Terms of service: Commercial

Terms of service: Consumer

[Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)

Terms of service: Consumer

Usage policy

[Usage policy](https://www.anthropic.com/legal/aup)

Usage policy

[x.com](https://x.com/claudeai)

x.com

[LinkedIn](https://www.linkedin.com/showcase/claude/)

LinkedIn

[YouTube](https://www.youtube.com/@anthropic-ai)

YouTube

[Instagram](https://www.instagram.com/claudeai)

Instagram

English (US)

[English (US)](/resources/tutorials/using-the-icd-10-connector-in-claude)

[日本語 (Japan)](/ja-jp)

[Deutsch (Germany)](/de-de)

[Français (France)](/fr-fr)

[한국어 (South Korea)](/ko-kr)
