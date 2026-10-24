---
title: "Cyber Verification Program | Claude Help Center"
source_url: "https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet"
category: "21-Account-Support"
fetched_at: "2026-10-23T06:29:07Z"
tags: ["account", "cli", "security"]
---

# Cyber Verification Program

Updated today


**Updated October 2026.** The CVP previously covered Claude Opus and Sonnet with a single level of access. We are now offering three access tiers for Claude Opus 5.5, our most capable cyber model yet, Claude Sonnet 5.5, Claude Mythos 5.1, and new models moving forward.

For more details, register for our upcoming **[webinar on the Cyber Verification Program](https://claude.com/resources/webinars/inside-the-cyber-verification-program)** on October 14th at 9am PT.

## Overview

The Cyber Verification Program (CVP) makes advanced cyber capabilities and reduced blocking classifiers available to qualifying security professionals. Each tier includes access to our most capable models, including Claude Opus 5.5, Claude Sonnet 5.5, Claude Mythos 5.1, and new models moving forward.

Our generally available models can still be used by all users for secure code review, threat modeling, patching known issues, finding vulnerabilities in your own source code, and triaging security alerts. However, other cyber security work like malware analysis or exploit validation may be interrupted by our safety classifiers. If you are a cybersecurity professional, and your work is being blocked, apply for the Cyber Verification Program using the instructions below in the “How to Apply” section.

## Access tiers


## How to apply

Apply through the **[Verification Portal](https://portal.anthropic.com/programs)**. We aim to send an email notification with our review decision or request for more information within seven business days. Fill out a single application, and we will place you at the highest tier based on the information we receive.

Apply once per organization. Individual users within organizations should not apply separately as organization admins can designate seats for the program. Independent researchers, maintainers, and bug bounty hunters apply as individuals. Please note that only Defense access is available for individual applicants at this time.

What you'll need:

- Details of your organization and the person applying, for verification. See **[identity verification on Claude](identity-verification-on-claude.md)**

- A description of your security work

- An attestation to the security controls applicable to your desired tier

[TABLE]

## Once you're approved

- The **[Usage Policy](https://www.anthropic.com/legal/aup)** still applies in full.

- You may leverage CVP enabled models for internal use such as running the model over your own code. See the **Building client-facing products** section for more information.

- We may review, narrow, or withdraw a grant.

## Building client-facing products

Your CVP access covers security work on your organization's own code, products, and infrastructure. Using your CVP access to deliver work to your customers, for example by running the model against a customer's code or systems or by letting customers use something you've built on the model, requires approval. Please submit a separate application for **each service or product you offer**.

**Managed services: applications are open.** In a managed service, your own staff use the model to do security work for a customer, on code and systems the customer owns or operates. The customer receives only finished deliverables, such as a findings report or patched code. Your customers never prompt the model, interact with it, or see its raw output.

**Products: not open yet.** In a product, your customers use something you built on the model, such as a scanner or a code-review tool, even if they can only trigger or configure it. Products are categorized as follows:

- **Constrained products:** Customers use something built on the model but cannot direct it or see its raw output

- **Unconstrained products:** Any other customer-facing product, such as one where customers can give the model their own instructions or see its responses as written.

While we are not yet reviewing applications for products, you can express interest by selecting “Constrained product” or “Unconstrained product,” then select “Express interest.” We'll contact you when we're accepting product applications, and you'll need to submit a full application then.

### How to apply for a managed service

You must be an admin of an organization approved for the Cyber Verification Program.

1.  Sign in to the **[Verification Portal](https://portal.anthropic.com/programs/cyber-productization)**, open “Programs,” then choose “Cyber productization.”

2.  Select “Register an offering,” then choose “Managed service.”

3.  Name the service and describe how it runs, who operates the model, and what your customers receive. Then confirm the six security commitments and give a security contact and the name and title of the company officer who signs off.

4.  Accept the Anthropic Cyber Defender Partner Addendum, then select “Submit” for review.

5.  To apply for another managed service, go back to the Cyber productization page and repeat steps 2 to 4.

### How to express interest in a constrained or unconstrained product

You must be an admin of an organization approved for the Cyber Verification Program.

1.  Sign in to the **[Verification Portal](https://portal.anthropic.com/programs/cyber-productization)**, open “Programs,” then choose “Cyber productization.”

2.  Select “Register an offering,” then choose “Constrained” or “Unconstrained” product.

3.  Describe the product in one line.

4.  Add a name and email.

5.  Select “Express Interest."

Check your answers before you submit: you can't edit or withdraw an application after you send it. You can follow each application's status on the **Cyber productization** page. Don't serve customers through a service until it's approved. Until then, you can keep using your CVP access for work on your own code, products, and infrastructure.

## Security controls and requirements

Each access level has its own security requirements. The security requirements for each tier are outlined in detail in the **[CVP Security Requirements Help Center article](cyber-verification-program-security-requirements-claude-help-center.md)**. For existing CVP customers, your current access and corresponding security requirements are not impacted and stay under your current terms.

**Defense Access will have until *December 15, 2026* to adopt phishing-resistant multi-factor authentication and to stop using API keys.** Until then, multi-factor authentication of some kind is required, and API keys will expire every seven days. We recommend migrating now to using **[Workload Identity Federation](../04-API-Reference/Other/manage-claude-workload-identity-federation.md)**.

## Provisioning access using your Grants

After your application has been approved, the steps to provision access to your Grants vary depending on how you access Claude.

[TABLE]

## Existing members

If your organization was previously enrolled in Project Glasswing or CVP, you don't need to apply again to join the updated CVP program. Your existing access to the models you use today via Project Glasswing or CVP will keep working under your existing terms, and you'll be transitioned to the relevant new program tier for Claude Opus 5.5, Claude Sonnet 5.5, and Claude Mythos 5.1.

The Cyber Verification Program requires data retention, which enables us to monitor for harmful cyber misuse in the program and detect bad actors. Once Enterprise Frontier Safeguards (EFS) is available, eligible organizations will be able to store data in cloud infrastructure they control. To register interest in EFS, fill out **[this form](https://claude.com/form/enterprise-frontier-safeguards)**.

In the meantime, organizations with a data retention exemption for Claude Fable or Claude Mythos models can also use CVP with zero data retention (ZDR) on all supported models. Until EFS is available, if your organization has access to Claude Fable or Claude Mythos with ZDR, you can also use CVP with ZDR.

## If you’re not approved for a tier

The Cyber Verification Program is designed to get advanced cyber capabilities to defenders as widely as we responsibly can. Access depends on a number of factors, including the work an organization does, our ability to verify who it is, and the security controls it has in place.

### Why might an organization not have access?

Eligibility reflects a range of factors, including one or more of the following:

1.  **The nature of the work.** The program is built for defense. Organizations whose main business falls outside that scope may not be eligible.

2.  **Verification.** We need to be able to confirm who an organization is and what it does.

3.  **The environment an organization operates in.** We consider the legal and regulatory environment, the risk that advanced capabilities could be diverted, and the risk that access could be compelled.

4.  **Who the work is ultimately for.** The risk that capabilities are passed on or repurposed is higher where an organization primarily serves military, intelligence, or law enforcement customers. We take a more cautious approach in those cases.

5.  **The tier applied for.** Requirements rise with the level of access. For Specialized Access, every organization is reviewed in depth in collaboration with the US government. Existing members of Project Glasswing will transition to this tier and don't require reapproval for current models. We continue to work with the US government to expand the number of eligible organizations, both in the US and internationally.

## Frequently asked questions

### Can I apply as an individual?

Yes, for Defense Access, on a paid plan. Red Team Access and Specialized Access tiers are for organizations only.

### My organization has a grant, but I'm still blocked

Check that your admin has provisioned you access to the relevant CVP grant(s). If using a Claude Console account, ensure you're in the correct Workspace and that the activity falls inside your tier.

### Why is CVP on Amazon Bedrock only available to customers with Enterprise Frontier Safeguards?

Amazon Bedrock does not yet support human review of automated safety flags, which CVP requires by default. As a result, on Bedrock, CVP is only available to organizations that have a data retention exemption for Fable 5.1; those customers can also use CVP with ZDR and will be eligible to use CVP with Enterprise Frontier Safeguards once available. We're working to expand CVP to all customers on Bedrock.

### I’m approved, why can’t I access Mythos on my preferred Cloud provider?

Access to Mythos on third-party cloud providers will trail approval by approximately five business days.

### How do usage limits for Mythos 5.1 work?

On Pro and Max plans, Mythos 5.1 follows the same usage rules as Fable 5.1.

- For Pro plans, Mythos 5.1 is available only with usage credits. It doesn’t draw on your plan’s included usage, so you’ll need usage credits turned on to use it.

- For Max plans, Mythos 5.1 and Fable share a single allowance of up to 50% of your weekly usage limit, not a separate allowance for each model. This usage also counts toward your plan's regular usage limits. Once the shared allowance is used up, you can keep using Mythos 5.1 or Fable with usage credits (if you have them turned on), or switch to another model.
