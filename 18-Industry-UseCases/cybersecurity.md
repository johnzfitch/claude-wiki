---
title: "Claude for Cybersecurity | Claude by Anthropic"
source_url: "https://www.claude.com/solutions/cybersecurity"
category: "18-Industry-UseCases"
fetched_at: "2026-09-26T06:41:23Z"
tags: ["case-studies", "security"]
---

# Defense at the pace threats now demand

Frontier AI models have surpassed all but the most skilled humans at finding and exploiting software vulnerabilities. Within months, we expect these capabilities will proliferate across AI models and become widely accessible to everyone, including attackers.

Defenders across industries, research, open source, and government must act to find and fix what’s exposed today, and build a durable advantage that drives vulnerabilities ever closer to zero in the future.

01

### State of cybersecurity

Insights on model capabilities today, including Claude Mythos.

Skip to

[Skip to](#state-of-cybersecurity)

Skip to

02

### Products and technology

Security-tuned models and tools you can deploy today.

Skip to

[Skip to](#products-and-technology)

Skip to

03

### Commitments

Open-source support, critical-systems defense, and policy advocacy.

Skip to

[Skip to](#commitments)

Skip to

04

### Resources

Cybersecurity resources, including research, guides, and field insights.

Skip to

[Skip to](#resources)

Skip to

The state of cybersecurity

## Where frontier capability stands today

Models can build working exploits, defeat security walls, or help defenders ship fixes at scale. The outcome depends on how they’re used.

Capability

Remediation

Active

## Model exploit capability

ExploitBench · V8 bugs

| Model          | T5  | T4  | T3  | T2  | T1  |
|----------------|-----|-----|-----|-----|-----|
| Mythos Preview | 41  | 38  | 35  | 22  | 18  |
| Opus 4.7       | 41  | 24  | 12  | 0   | 0   |
| Opus 4.6       | 41  | 23  | 9   | 0   | 0   |
| Sonnet 4.6     | 41  | 21  | 10  | 0   | 0   |
| Haiku 4.5      | 40  | 5   | 0   | 0   | 0   |
| GPT 5.5        | 41  | 29  | 13  | 2   | 1   |
| Kimi K2.6      | 40  | 16  | 0   | 0   | 0   |
| MiniMax M2.7   | 40  | 6   | 0   | 0   | 0   |

ExploitBench V8 bugs: environments where model reached tier or above

T1 = full control, hardest

### From finding flaws to full system control

A year ago, the most capable AI models could spot security flaws but couldn't reliably exploit them. Today, in the wrong hands, they can — and not just in simple software. Mythos Preview is the first model to consistently break through the sandbox protections modern browsers and operating systems rely on; other frontier models still stop at the wall. Defenses built on last year's assumptions are already behind.

Read Red Team research

[Read Red Team research](https://red.anthropic.com/2026/exploit-evals/)

Read Red Team research

Reading the chart

Capability trends downward as tasks get harder. T5 is "the model reaches vulnerable code." Only Mythos Preview passed T1: "the model fully controls the system."

### Tipping the scales to defenders

In March 2026, Mozilla shipped fixes for vulnerabilities found by Claude Opus 4.6, the model that found hundreds of bugs in open source software that survived decades of human review. With Mythos Preview, Mozilla shipped an additional 271 fixes in the April release, more than 20 times their monthly average. Says Bobby Holley, CTO of Firefox, “Defenders finally have a chance to win, decisively.”

Read Mozilla research

[Read Mozilla research](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

Read Mozilla research

Inside Mozilla's review process

The model expands what gets reviewed, and humans decide what gets patched.

Project Glasswing

### Our approach to dual-use with Claude Mythos models

Claude Mythos Preview, and now Claude Mythos 5, are models with significantly stronger cybersecurity capabilities, especially in exploit reasoning. As this capability carries the greatest potential for misuse in security, we are limiting initial access to a small number of partners through Project Glasswing. Claude Fable 5 is our Mythos-class model safe for general use through additional safeguards. [Read the latest](../19-Reference/claude-fable-5-mythos-5.md)

### Securing critical software

Glasswing partners maintain critical infrastructure or software the world depends on, where a successful attack would be catastrophic.

### Expanding through trusted access

We are working toward steadily expanding access to Claude Mythos 5 through a trusted access program, and will share more soon.

### Providing tools for defenders today

Claude Security, the open-source reference tools, and the practices emerging from Project Glasswing are available to all security teams.

Read our full approach

[Read our full approach](#)

Read our full approach

## How security teams put Claude to work for defense

Across enterprise security programs and inside Anthropic, teams use Claude to improve risk posture.

Learn more

[Learn more](../15-Claude-AI-Features/product-claude-security.md)

Learn more

Claude Security

Claude Code

Claude Developer Platform

Active

[Play video](#)

Play video

### Find and fix vulnerabilities with Claude Security

Claude Security reasons about your code like a security researcher: scanning for vulnerabilities, validating findings, and proposing targeted patches.

Start defending

[Start defending](../15-Claude-AI-Features/product-claude-security.md)

Start defending

Prompt

Can you tell me ...

● Scanning 247 files across app/, services/, routes/...

● Analyzing auth flows, input validation, file handling...

● Filtering by severity ≥ high...

● Found 4 findings in acme-corp/hookrelay  

CRITICAL

Shell command injection via webhook payload

app/services/notifiers/script_runner.py:21 · Command injection  

CRITICAL

JWT authentication bypass via "none" algorithm

app/auth/jwt_handler.py:28 · Auth bypass  

CRITICAL

Path traversal in export file download endpoint

app/routes/exports.py:39 · Path traversal  

HIGH

Server-side request forgery in destination URL validation

app/services/validator.py:36 · SSRF  

✓ 12 lower-severity findings filtered out  
  
  
### Ship secure code in your CI/CD workflow

Use the Code Review skill to set up automated PR reviews to catch logic errors, security vulnerabilities, and regressions across your full codebase.

Start reviewing

[Start reviewing](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Start reviewing

Prompt

Can you tell me ...

agent.py Python

    from claude_agent_sdk import Agent

    agent = Agent(
        model="claude-opus-4-8",
        system="Security co-pilot for Acme Defend.",
        mcp_servers=[
            {"name": "vuln_scanner", "cmd": "./mcp/scanner"},
            {"name": "asset_graph",  "cmd": "./mcp/assets"},
            {"name": "patch_engine", "cmd": "./mcp/patches"},
        ],
    )

    # Fan out to specialized subagents in parallel
    result = await agent.run(
        task=finding,
        subagents=["triage", "severity", "remediate"],
        parallel=True,
        sandbox=True,
    )

Response

Streaming…

### Deploy security agents with the Claude Developer Platform

Ship defender tools and custom security agents with sandboxed execution, credential isolation, and audit logging built in via the Agent SDK, MCP, and Claude API.

Start building

[Start building](https://www.claude.com/platform/api)

Start building

"Anthropic prioritized safety and security a lot more than other LLMs... As the largest cybersecurity company, that's a big deal for us."  
- Gunjan Patel, Director of Engineering

“Claude consistently performed best on complex, agentic workflows, especially multi-step investigations requiring policy adherence and sustained reasoning across multiple tools.”  
  
 - Anirudh Ravula, Head of AI

“The industry has always moved too slowly compared to attackers. AI is like giving defenders a jetpack when they've been limited to walking.”  
  
- Martin Holste, CTO of Cloud & AI

[Prev](#)

Prev


### Build threat context

Give scanning and response a map to work from. Claude derives a threat model from your codebase and past vulnerabilities, then enriches raw indicators with infrastructure links, attribution, and ATT&CK mapping, so analysts start with context.

Open source: Threat Intel Enrichment agent

[Open source: Threat Intel Enrichment agent](https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent)

Open source: Threat Intel Enrichment agent

Open source: Threat Model skill

[Open source: Threat Model skill](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/threat-model#threat-model)

Open source: Threat Model skill

### Vulnerability detection

Claude reads source code the way a researcher does, reasoning about reachability and exploitability, catching vulnerabilities that static tools often miss. A separate triage pass re-verifies every finding to help reduce false positives.

In Claude Security

[In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

In Claude Security

Open source: Vulnerability detection agent

[Open source: Vulnerability detection agent](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent)

Open source: Vulnerability detection agent

### Patching

Findings now arrive faster than teams can fix them. Claude traces each one to its root cause, locates sibling call sites with the same flaw, and writes a minimal diff with a regression test for your team to review.

In Claude Security

[In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

In Claude Security

Open source: Patching skill

[Open source: Patching skill](https://github.com/anthropics/defending-code-reference-harness/blob/main/.claude/skills/patch/SKILL.md#patch)

Open source: Patching skill

### Triage and verify findings

Hand Claude raw findings from any scanner and get back insights. Claude reads the surrounding code to confirm exploitability, deduplicates by root cause, and ranks by precondition and impact, so engineers can focus and work on real issues first.

In Claude Security

[In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

In Claude Security

Open source: Triage skill

[Open source: Triage skill](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/triage)

Open source: Triage skill

### Security review across the dev loop

Review code for security at every stage of development. Claude checks its own edits as it writes and fixes issues in the same session, then specialized agents re-examine pull requests against your codebase, posting verified findings inline without blocking your review gates.

‍Security guidance in Claude Code

[‍Security guidance in Claude Code](../02-Claude-Code-CLI/security-guidance.md)

‍Security guidance in Claude Code

Code Review in Claude Code

[Code Review in Claude Code](../02-Claude-Code-CLI/code-review.md)

Code Review in Claude Code

### Secure source code, end to end

As offensive capability accelerates, the find-and-fix loop has to close faster. Claude runs threat modeling, discovery, verification, triage, and patching as one continuous loop on your codebase, carrying context across every stage so each finding arrives at the fix with its full history.

Using LLMs to secure source code

[Using LLMs to secure source code](https://claude.com/blog/using-llms-to-secure-source-code)

Using LLMs to secure source code

Customer story

Cogent resolves security threats 97% faster with Claude

Read story

[Read story](cogent.md)

Read story

Claude Opus

500+

high-severity vulnerabilities found that survived decades of scrutiny and automated analysis

## Cyber defense powered by Claude, available through our partners

Frontier capabilities

### Leverage powerful models for defense

Claude reads code carefully, understands real risks, and sustains the long workflows that continuous defense requires. Verified practitioners can request [adjusted safeguards](../20-Models/real-time-cyber-safeguards-on-claude-opus-and-sonnet.md) for dual-use work.

Learn more

[Learn more](../20-Models/real-time-cyber-safeguards-on-claude-opus-and-sonnet.md)

Learn more

## Anthropic’s commitment to cyberdefense

Frontier AI capabilities are advancing faster than any single team can respond to, and developers, vendors, researchers, open-source maintainers, and public-sector defenders all have a role to play.

### Supporting open-source security

The internet runs on critical software maintained by people with limited resources. We extend access to capable models, fund the foundations behind them, and disclose vulnerabilities responsibly when Claude finds them.

Apply through Claude for Open Source

[Apply through Claude for Open Source](https://claude.com/contact-sales/claude-for-oss)

Apply through Claude for Open Source

Read our CVD policy

[Read our CVD policy](https://www.anthropic.com/coordinated-vulnerability-disclosure)

Read our CVD policy

See our work with the Linux Foundation

[See our work with the Linux Foundation](http://linuxfoundation.org/blog/project-glasswing-gives-maintainers-advanced-ai-to-secure-open-source)

See our work with the Linux Foundation

### Defending mission-critical systems

We partner with the organizations responsible for the world's most critical software and infrastructure — from Project Glasswing's work hardening systemically important code, to our research with Pacific Northwest National Laboratory (PNNL**)** on defending cyber-physical systems.

Read the latest on Project Glasswing

[Read the latest on Project Glasswing](../19-Reference/expanding-project-glasswing.md)

Read the latest on Project Glasswing

Read about Anthropic and PNNL

[Read about Anthropic and PNNL](../19-Reference/2026-critical-infrastructure-defense.md)

Read about Anthropic and PNNL

### Advocating for policy that backs defenders

Our Advanced AI Framework proposes policies for binding obligations on frontier labs, Anthropic included, and government authority to block dangerous deployments, alongside investment in open-source hardening and the safeguards that would let frontier cyber capability reach more defenders safely.

Read the Advanced AI Framework

[Read the Advanced AI Framework](https://www.anthropic.com/policy-on-the-ai-exponential/aaif)

Read the Advanced AI Framework

## Go deeper on cyberdefense

Everything you need to strengthen your defense posture, from research to implementation guides.

Research

Guides

In the field

Active

Title


Measuring LLMs’ impact on N-day exploits


June 8, 2026


Expanding Project Glasswing


June 2, 2026


Project Glasswing: An initial update


May 22, 2026


Measuring LLMs’ ability to develop exploits


May 22, 2026


Anthropic's coordinated vulnerabilty disclosure dashboard


May 22, 2026


Assessing Claude Mythos Preview’s cybersecurity capabilities


April 7, 2026


Reverse engineering Claude's CVE-2026-2796 exploit


March 6, 2026


LLM-discovered 0-days


February 5, 2026


AI models on realistic cyber ranges


January 16, 2026


Finding Bugs with Claude and Property-based Testing


January 14, 2026


Experimenting with AI to Defend Critical Infrastructure


January 8, 2026


Title

content type


Using LLMs to secure source code

content type

Blog


May 27, 2026


Zero Trust for AI Agents

content type


May 27, 2026


Secure the Advantage: A CISO's Guide to Agentic AI

content type

Blog


May 12, 2026


Vulnerability Detection Agent

content type

Cookbook


April 22, 2026


Preparing Your Security Program for AI-Accelerated Offense

content type

Blog


April 10, 2026


Threat Intelligence Enrichment Agent

content type

Cookbook


April 7, 2026


Title

content type


Claude Security: Putting Claude to Work for Defenders

content type

Webinar


May 28, 2026


How our partners are putting Opus to work for cybersecurity

content type

Blog


May 21, 2026


How Anthropic's cybersecurity team built a threat detection platform with Claude Code

content type

Blog


May 12, 2026


Long Running Agents: How Outtake built a Cyber investigator on Claude

content type

Webinar


April 28, 2026


Partnering with Mozilla to improve Firefox's security

content type

Blog


March 6, 2026


## Give defenders an edge with Claude


[Contact sales](https://www.claude.com/contact-sales)


Start building

[Start building](../04-API-Reference/Other/usage-limits.md)

Start building

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](../15-Claude-AI-Features/product-overview.md)
  Claude

- Claude Code

  [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
  Claude Code

- Claude Cowork

  [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
  Claude Cowork

- @Claude

  [@Claude](../14-Connectors/claude-for-slack.md)
  @Claude

- Claude Science

  [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
  Claude Science

- Claude Security

  [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
  Claude Security

- Download app

  [Download app](https://www.claude.com/download)
  Download app

- Pricing

  [Pricing](../17-Billing-Plans/pricing.md)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Capabilities

- Artifacts

  [Artifacts](https://www.claude.com/features/artifacts)
  Artifacts

- Design

  [Design](../15-Claude-AI-Features/product-design.md)
  Design

- Connectors

  [Connectors](https://www.claude.com/marketplace/connectors-plugins)
  Connectors

- Plugins

  [Plugins](https://www.claude.com/marketplace/plugins)
  Plugins

- Skills

  [Skills](https://www.claude.com/skills)
  Skills

Extensions

- Claude in Chrome

  [Claude in Chrome](https://www.claude.com/claude-in-chrome)
  Claude in Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)
  Claude for Microsoft 365

Models

- Mythos

  [Mythos](../15-Claude-AI-Features/claude-mythos.md)
  Mythos

- Fable

  [Fable](../15-Claude-AI-Features/claude-fable.md)
  Fable

- Opus

  [Opus](../15-Claude-AI-Features/claude-opus.md)
  Opus

- Sonnet

  [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
  Sonnet

- Haiku

  [Haiku](../15-Claude-AI-Features/claude-haiku.md)
  Haiku

Enterprise

- Overview

  [Overview](enterprise.md)
  Overview

- Claude Code for Enterprise

  [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
  Claude Code for Enterprise

Use cases

- AI agents

  [AI agents](agents.md)
  AI agents

- Code modernization

  [Code modernization](code-modernization.md)
  Code modernization

- Coding

  [Coding](coding.md)
  Coding

- Commerce

  [Commerce](commerce.md)
  Commerce

Departments

- Customer support

  [Customer support](customer-support.md)
  Customer support

- Cybersecurity

  [Cybersecurity](cybersecurity.md)
  Cybersecurity

- Legal

  [Legal](legal.md)
  Legal

- Sales

  [Sales](sales.md)
  Sales

Industries

- Financial services

  [Financial services](finance.md)
  Financial services

- Government

  [Government](government.md)
  Government

- Healthcare

  [Healthcare](healthcare.md)
  Healthcare

- Higher education

  [Higher education](education.md)
  Higher education

- K-12 teachers

  [K-12 teachers](teachers.md)
  K-12 teachers

- Life sciences

  [Life sciences](life-sciences.md)
  Life sciences

- Nonprofits

  [Nonprofits](nonprofits.md)
  Nonprofits

- Small business

  [Small business](small-business.md)
  Small business

Programs

- Startups

  [Startups](../15-Claude-AI-Features/programs-startups.md)
  Startups

- Scientists

  [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
  Scientists

Developers

- Developer docs

  [Developer docs](../02-Claude-Code-CLI/code-home.md)
  Developer docs

- Developer blog

  [Developer blog](https://claude.dev/)
  Developer blog

- Community

  [Community](https://www.claude.com/community)
  Community

- Console

  [Console](../04-API-Reference/Other/home.md)
  Console

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

Platform

- Overview

  [Overview](https://www.claude.com/platform/api)
  Overview

- Marketplace

  [Marketplace](https://www.claude.com/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
  Claude on AWS

- Google Cloud

  [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
  Microsoft Foundry

Resources

- Blog

  [Blog](https://www.claude.com/blog)
  Blog

- Claude partner network

  [Claude partner network](../04-API-Reference/Other/partners.md)
  Claude partner network

- Claude Academy

  [Claude Academy](https://academy.claude.com/)
  Claude Academy

- Customer stories

  [Customer stories](customers.md)
  Customer stories

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Powered by Claude

  [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
  Powered by Claude

- Service partners

  [Service partners](https://www.claude.com/marketplace/service-partners)
  Service partners

Help and security

- Availability

  [Availability](https://www.anthropic.com/supported-countries)
  Availability

- Check files

  [Check files](https://claude.com/check-files)
  Check files

- Regional compliance

  [Regional compliance](https://www.claude.com/regional-compliance)
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

  [Research](../19-Reference/anthropic-com-research.md)
  Research

- Anthropic news

  [Anthropic news](../19-Reference/news.md)
  Anthropic news

- Policy on the AI Exponential
