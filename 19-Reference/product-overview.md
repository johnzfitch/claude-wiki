---
title: "Product overview"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/34783bca828d7fa331f515ced26f1c9232151b2c.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:34Z"
tags: ["news-research"]
---

Product overview                             4

Building an AI-first financial enterprise:   9
real-world examples

Claude adoption roadmap                      11

Getting started                              15

Resources                                    17


                                                  2
Foreword
AI is rapidly transforming financial services. As executives face pressures on margins, talent, and regulation,
they are embracing AI technology for faster, better answers.

A 2026 NVIDIA survey found that 61% of financial services firms are using or assessing generative AI, with
89% reporting that AI has increased revenue while lowering costs. Across trading, underwriting, lending,
and advising, the industry has historically been fast to adopt any technology that offers an edge in research
and productivity. Today, that’s agentic AI: systems that act on the work, not just answer questions about it.
The NVIDIA survey found that 42% of firms are using or assessing agentic AI, with more than half of them
(56%) citing knowledge management and retrieval as their top overall use cases for AI agents.

At Anthropic, we are seeing this in action. Claude has changed how teams get answers and Claude Code has
transformed how engineers build software. Claude Cowork has brought that same execution power
to analysts and operators whose work revolves around documents and data.

Financial services organizations are using Claude for research, deal work, analysis, claims, model reviews,
reporting, and more. Most firms run more than one Claude product: Claude for chat and research, Claude
Cowork for project-level work across files and apps, Claude Code for quantitative and engineering teams,
Claude for Microsoft 365 for the hours spent in Excel, PowerPoint, and Word, and the Claude Platform and
Claude Managed Agents for building and deploying custom applications on Claude.

This guide walks through each product, offers customer examples from across the industry,
and tips on how to roll out Claude inside your firm.


                                                                                                                  3
Pillar 01: Chat                                  Pillar 02: Cowork                               Pillar 03: Code
Every knowledge worker                           Business operators and analysts                 Engineers and quants


The on-ramp. Conversational access for           Multi-step work done for you. Claude operates   The on-ramp. Conversational access for
drafting, research, analysis, and Q&A — in the   across the tools your people already use —      drafting, research, analysis, and Q&A — in the
browser and embedded in Microsoft 365.           inbox, files, CRM, internal systems — with      browser and embedded in Microsoft 365.
                                                 humans in the loop.
• Policy and memo drafting                                                                       • Legacy COBOL and Java migration
• Research synthesis                             • Deal room prep                                • Quant notebooks and models
• Email and client comms                         • KYC and onboarding                            • Test and review automation
                                                 • Portfolio and ops reviews


                                                                                                                                                  4
Chapter 1


Product overview   5
  Chapter 1


Product overview
Claude shows up to work in two forms: products your teams use directly such        Claude for Microsoft 365
as Claude Chat, Claude Cowork, Claude Code, and the Microsoft 365 add-
ins, as well as the Claude Platform, for firms building and running their own      Teams can use Claude within the Microsoft 365 suite in two ways. Add-ins from
applications and agents.                                                           the Microsoft Marketplace put Claude inside Outlook, Excel, PowerPoint, and
                                                                                   Word, so an analyst can update a financial model built in Excel, explain it with
                                                                                   cell-level citations, and turn it into a slide without leaving the app.
Claude Chat                                                                        The Microsoft 365 connector lets Claude search and analyze content in
                                                                                   Outlook, Teams, SharePoint, and OneDrive from chat, Cowork, or the add-ins.
The Claude web and desktop app, at Claude.ai, is a chat interface for research
                                                                                   Context carries across the suite, so a model built in Excel can be turned into a
and drafting. An analyst might use it, for example, to summarize an earnings
                                                                                   slide or a client email without the analyst rebuilding anything.
transcript or pressure-test a thesis before a memo goes to the committee. It is
often the first place a new user starts.
                                                                                   Claude Platform
Claude Cowork                                                                      The Claude Platform is Anthropic's API for firms building their own applications
                                                                                   on Claude. Quantitative teams, platform engineers, and internal tools teams
Claude Cowork is a desktop application where Claude works across local files
                                                                                   use it to embed Claude directly into trading platforms, risk systems, KYC and
and connected apps to complete multi-step projects.. It can read and write local
                                                                                   underwriting applications, and other production workflows.
documents, call connected services such as Google Drive, Gmail, Box, and Asana,
and coordinate multi-step work across files and apps. Examples of the kind of
project this is suited to include building a pitch book, reconciling a month-end   Claude Managed Agents
close, or preparing a board packet.
                                                                                   Claude Managed Agents is Anthropic’s suite of composable APIs for
                                                                                   building and deploying cloud-hosted agents on the Claude Platform. A firm
Claude Code                                                                        builds an agent on the platform and Anthropic runs it as a cloud service,
                                                                                   with the production scaffolding Managed Agents provides (long running
Claude Code is a command-line interface for technical teams: quantitative
                                                                                   sessions, scoped permissions, managed credential vaults, and full execution
researchers, data engineers, and platform teams building internal tools. Finance
                                                                                   tracing built in). Financial services firms use Managed Agents to run agents
firms use Claude Code to write and audit quantitative code, including trading
                                                                                   programmatically, for example, a Valuation Reviewer agent handling month-end
logic and data pipelines under version control.
                                                                                   reconciliation across a multi-hour close.


                                                                                                                                                                      6
Claude product matrix: when to use what

 Surface                    Best for                        Primary users                Where it runs                 Example task


                            Conversational drafting,
                                                                                                                       "Summarize this report and
 Claude Chat                research, and analysis in a     Anyone                       Browser, desktop, mobile
                                                                                                                       draft a response."
                            chat interface


                            Agentic coding inside a
                                                                                                                       "Refactor this module and
 Claude Code                repo — building, refactoring,   Developers                   Terminal, IDE
                                                                                                                       run the tests."
                            testing


                                                                                                                       "Read the five vendor PDFs
                            Cross-app knowledge             Knowledge workers                                          in my Downloads folder,
 Claude Cowork              work that touches files and     (analysts, PMs, operators,   Claude desktop app            compare them on price and
                            multiple tools                  researchers)                                               SLAs, and put the result in a
                                                                                                                       spreadsheet."


                            In-place drafting, modeling,                                 Outlook, Excel, PowerPoint,
                                                            Knowledge workers                                          "Update this DCF with the
                            and editing across the                                       Word (add-ins); Teams,
 Claude for Microsoft 365                                   (analysts, PMs, operators,                                 new guidance and turn it
                            Microsoft 365 suite; context                                 SharePoint, OneDrive (via
                                                            researchers)                                               into a three-slide deck."
                            carries across apps                                          M365 connector)


                                                                                                                       “Add Claude to our
                            Building custom applications
                                                            Developers, quantitative     Anthropic API, Amazon         advisor platform to draft
                            on Claude; embedding
 Claude Platform (API)                                      teams, platform and          Bedrock, Google Vertex AI,    personalized portfolio
                            Claude into internal systems
                                                            engineering teams            Microsoft Foundry             commentary at scale,
                            and production workflows
                                                                                                                       with a human in the loop.”

                                                                                                                       “Deploy our Valuation
                            Running custom agents as
                                                                                                                       Reviewer agent as a
                            hosted cloud services with      Platform and engineering     Claude Platform (hosted by
 Claude Managed Agents                                                                                                 managed service with
                            Anthropic handling the          teams                        Anthropic)
                                                                                                                       scoped permissions and
                            runtime
                                                                                                                       audit tracing.”


                                                                                                                                                       7
Customizing Claude: connectors, skills, and plugins                                   MCP connectors relevant to financial services firms:


Claude becomes specific to a financial services firm through three building
blocks: connectors that give it access to the firm's data, skills that teach it how     Credit and risk data:
to complete specific tasks in a repeatable way, and plugins that bundle skills,
subagents, and connectors into installable packages for a specific job.


MCP Connectors                                                                          Market and company data:

MCP Connectors give Claude access to a specific data source over the
Model Context Protocol (MCP), an open standard that lets Claude query the
provider’s system directly rather than working off an uploaded copy.
This is important for firms with strict data-residency or entitlement
requirements.

Skills                                                                                  Industry research and expert networks:

Skills are reusable, encoded workflows—instructions, templates, and optionally
scripts—that teach Claude how to complete specific tasks in a repeatable
way. They are especially valuable in heavily regulated industries like financial
services and insurance, where consistency matters.                                      News and real-time feeds:

Skills are best used for work that follows a standard format. For example, a credit
memo skill captures the firm's template, required disclosures, and formatting,
and a KYC skill captures the onboarding checks the compliance team runs on
every new client.                                                                       Diligence and data rooms:

Anthropic has pre-built skills for PDF, Word, Excel, and PowerPoint creation.
Firms can also build their own skills. Simple skills are written in Markdown with
no code; more advanced ones can include executable scripts. Either way, skills
                                                                                        Productivity and collaboration:
are then uploaded in Claude.ai settings (via the customize tab in both web and
desktop), Claude Code, or the API.


                                                                                                                                             8
Pre-built finance agent reference architectures                                     Examples include:


Anthropic has shipped ten pre-built agent reference architectures for financial
                                                                                      Research and client coverage                Finance and operations
services work that packages up the skills, tools, and data connections a specific
workflow needs into a template. Firms can then customize those templates to
                                                                                     • Pitch builder creates target lists, runs   • General ledger reconciler reconciles
their modeling standards, data sources, and review steps.
                                                                                        comparables, and drafts pitchbooks          general ledger accounts and runs net
                                                                                        for client meetings;                        asset value calculations against the
                                                                                                                                    books of record;
                                                                                     • Meeting preparer assembles client
                                                                                        and counterparty briefs ahead of calls;   • KYC screener assembles entity
                                                                                                                                    files, reviews source documents, and
                                                                                     • Earnings reviewer reads transcripts
                                                                                                                                    packages escalations for compliance
                                                                                        and filings, updates models, and flags
                                                                                                                                    review;
                                                                                        thesis-relevant changes;
                                                                                                                                  • Month-end closer runs the close
                                                                                     • Model builder builds and maintains
                                                                                                                                    checklist, prepares journal entries,
                                                                                        financial models from filings, data
                                                                                                                                    and produces close reports;
                                                                                        feeds, and analyst inputs.
                                                                                                                                  • Statement auditor reviews financial
                                                                                     • Market researcher: tracks sector and
                                                                                                                                    statements for consistency,
                                                                                        issuer developments, synthesizes
                                                                                                                                    completeness, and audit-readiness;
                                                                                        news, filings, and broker research, and
                                                                                        flags items for credit and risk review.   • Valuation reviewer checks valuations
                                                                                                                                    against comparables, methodology,
                                                                                                                                    and the firm's review standards;


                                                                                    Each role can run as a plugin in Cowork and the Microsoft 365 add-ins for
                                                                                    desktop use with a human in the loop, or via Claude Managed Agents in the
                                                                                    Claude Platform. Either way, analysts stay in the loop, reviewing, iterating on,
                                                                                    and approving the agent's outputs before anything moves downstream.


                                                                                                                                                                           9
Chapter 2


Building an AI-first financial
enterprise: real-world examples   10
  Chapter 2


Building an AI-first financial enterprise:
real-world examples
Claude is changing how financial services teams work, from investment                Commonwealth Bank of Australia is building its AI transformation on Claude,
banking to wealth management to insurance. The firms adopting AI across their        with early focus on fraud prevention and customer service enhancement.
workloads, whether front-office or back-office, are reporting meaningful shifts in   Read the announcement.
how analyst and specialist hours are spent, and in how efficiently work gets done.

AIG is using Claude inside underwriting to compress review timelines by more            "Our strategic partnership with Anthropic is foundational to our success
than 5x in early rollouts and raise data accuracy from 75% to over 90%.                 and our strategy to become a global leader in AI innovation in banking.
Read the announcement.                                                                  Claude's advanced capabilities, combined with Anthropic's commitment
                                                                                        to safety, are central to our purpose of harnessing AI responsibly, as we
                                                                                        drive for transformation in critical areas like fraud prevention & customer
   "Our partnership with Anthropic will fundamentally transform how we                  service enhancement."
   approach underwriting at scale... This collaboration is about propelling             — Rodrigo Castillo, Chief Technology Officer,
   growth and providing our underwriters the tools to make better decisions             Commonwealth Bank of Australia
   at an accelerated pace, ultimately driving our ability to serve more clients
   with greater insight."
   — Peter Zaffino, CEO, AIG
                                                                                     Moody's is building an MCP application that brings its credit analysis and
                                                                                     compliance agents directly into Claude’s environment. Powered by Moody’s
                                                                                     connected intelligence of 600M+ entities, 2 billion ownership links, and cross-
IG Group, a global online trading and financial services firm, has streamlined       domain risk data, these agents have already cut credit memo prep time from 40
internal processes across teams, with the analytics function alone saving 70 hours   hours to 2 minutes. Read the press release.
a week on AI-assisted analytics and query handling. Read the customer story.


                                                                                        "As AI becomes the interface for decisions, trust becomes the standard.
   "We achieved full ROI within the first three months, through productivity            Moody’s decision-grade connected intelligence is key to unlocking AI for
   improvements, speed-to-market gains, and agency cost reductions. In some             high‑stakes credit and compliance decision‑making."
   use cases, productivity increased by 100%, beyond my wildest expectations."          — Rob Fauber, President & Chief Executive Officer, Moody’s
   — Olga Pirog, Global Head of Data and AI Transformation, IG Group


                                                                                                                                                                       11
Chapter 3


Claude adoption roadmap   12
  Chapter 3


Claude adoption roadmap
Most successful Claude rollouts follow this sequence: the team lays the foundation   that might be creating the first draft of a research note, a pitch book section, or a
for a pilot program, runs a pilot, and scales out to the rest of the organization.   credit memo. In back-office, that could be a KYC file review, a regulatory filing, or
Anthropic’s recommended adoption playbook maps out these three phases.               a claims summary. Avoid piloting Claude on novel or high-stakes work.


Phase 1: Lay the foundation                                                          Pro-tip: Have your champions leverage pre-configured plugins so they get value
                                                                                     in the first session. The cold-start problem is real: if someone opens Claude
Before launching a Claude pilot program, the responsible team needs to put all       Cowork and doesn't know what to do, they’ll close it. But if they open it, type /
access and connectors in place. For most firms, this means standing up Claude on     morning-briefing, and get something useful in ninety seconds, they return.
the first-party API, Amazon Bedrock, Google Vertex AI, or Microsoft Foundry—
whichever keeps Claude inside the firm’s existing cloud perimeter. Enterprise        Phase 2: Pilot
controls for SSO, SCIM, audit logs, and custom data retention need to be
configured at this stage. Scope governance in parallel: model risk management,       At this stage, champions are running real workflows with real data and

SEC/FINRA alignment, and data-privacy (GDPR/CCPA) review should run                  measuring the pilot’s success against criteria you have defined upfront. Time

alongside access setup.                                                              saved is a common metric used here, tracking the team’s cycle time on the pilot
                                                                                     job before and after Claude. Another one is how often a user keeps Claude’s
The connector set usually starts with the Microsoft 365 connector for Outlook,       draft without a meaningful rewrite. Together, these two criteria help you assess
Teams, SharePoint, and OneDrive access, plus one or two market data research         whether the pilot is working.
or document providers that the pilot team uses. Those could be FactSet, S&P
Capital IQ, Morningstar, Moody’s, Chronograph, Egnyte, etc. Firms can install        Another strong signal that a pilot is working is when champions start to build

these a la carte as MCP connectors, or access them inside one of Anthropic’s         their own skills. For example, a credit analyst takes the memo workflow she's

finance plugins (note: they still need to be set up individually).                   been running by hand and turns it into a skill with the firm's template, credit
                                                                                     policy, and approval flow embedded, and that is now a skill the rest of the org can
Next, choose the teams that will be using the pilot and let them surface use cases   begin using immediately.
that matter to their function rather than prescribing from above. Choose two or
three champion teams rather than one. A single team gives you one data point,        In most pilots, Claude's product surfaces come online in a specific order. Skills

while two or three teams will tell you whether, for example, the time savings and    and plugins come first because they're low-risk and high-reuse. The Microsoft

quality gains are repeatable or came from one team’s motivation and skill. Pick      365 add-ins come next, extending what a pilot team has built into Excel,

teams with a motivated lead who's already experimenting with AI, as they are         PowerPoint, Word, and Outlook,where the bulk of front- and back-office work

likely to surface the real use cases faster.                                         actually happens. Claude Cowork tends to come in at the back end of the pilot,
                                                                                     when the team's ready to move from single-document work to project-level work
Pick work that's document-heavy and standard-shape. For front-office work,           that spans files and apps.
                                                                                                                                                                             13
Pro-tip: Schedule weekly check-ins with your pilot teams; they surface edge              The table below summarizes the actions you would take at each stage and what
cases fast and you want to hear about them while they're fresh and in time to            you can expect to see as you go through rollout.
course-correct before a wider rollout.
                                                                                           Phase               Actions                         Phase
Phase 3: Scale

At this stage, plugins and skills that worked during the pilot are being rolled out to                         Security review. Identify 2–3
                                                                                                                                               Champions reporting back
more teams across the organization through admin-managed plugin marketplaces.                                  champion teams. Install pre-
                                                                                          Foundation                                           use cases. First "this saved
New hires benefit as well, as they start on day one with already encoded                                       built plugins. Connect 1–2
                                                                                                                                               me an hour" moments.
                                                                                                               core systems.
workflows. Onboarding is faster and the whole team can work more efficiently.

Over time, skills begin compounding across teams. A skill built for one team
                                                                                                               Champions run real
can be adapted for another when their work shares workflows or structure. For                                                                  Measurable time savings.
                                                                                                               workflows. Weekly check-
example, a fraud review workflow and an AML check workflow share most of                                                                       Champions building and
                                                                                          Pilot                ins. Measure against defined
their structure. Adding a second team usually goes faster than the first, and the                                                              scheduling custom skills. Pull
                                                                                                               criteria. Demo wins to
firm's skill library grows.                                                                                                                    from other teams.
                                                                                                               adjacent teams.

Pro-tip: Provision plugins at the admin level rather than letting individuals
                                                                                                               Admin-provisioned plugin        Skills shared across
install them ad hoc. Admin-provisioned plugins give you consistency across
                                                                                                               marketplace. Encode pilot       teams. New hires ramping
teams, security controls from the first user, and a single place to push updates          Scale                learnings as org-wide skills.   on encoded workflows.
when you improve a workflow.                                                                                   Onboard the next wave of        Declining support tickets for
                                                                                                               users.                          "how do I do this."


                                                                                                                                                                                14
Industry use cases
The work financial services teams tend to bring to Claude first is output-heavy (spreadsheets, presentations, documents), follows a standard shape, and gets reviewed
by a senior person before it ships. For example, Claude takes on the drafting so reviewers can focus on the work that requires judgment. The sections below show what
that looks like across four financial services sectors. They are illustrative, rather than exhaustive.

If your team is doing interesting and impactful work with Claude that we haven’t mentioned here, reach out at sales@anthropic.com.


   Investment banking and private equity                                                       Wealth and asset management
   Teams spend most of their time on documents that need to get built fast                     Portfolio managers and client-facing teams need to turn positions,
   and are reviewed by senior bankers. Claude speeds up the drafting, saving                   performance, and research into material a client can read. Claude handles
   analysts hours and reducing deal cycle times with:                                          the document production so the PM can spend time on judgment calls and
                                                                                               can enable higher AUM per advisor, reduced reporting time, and lower
   • Pitch book drafting                                                                       recon error rates with:
   • Comps tables and valuations support
   • CIM / teaser creation                                                                     • Portfolio reporting and investment committee memos
   • LBO model build and analysis                                                              • LBO model build and review
                                                                                               • Performance decks
                                                                                               • Month-end close and reconciliation support


   Retail and commercial banking
   Teams spend the majority of their time on documents that follow standard
   formats. Claude can reduce turnaround times for underwriting and                            Insurance
   improve coverage ratios with:                                                               Insurance work sits across a mix of structured data and unstructured
                                                                                               documents, much of it in regulated filings. Claude can improve accuracy
   • Branch P&L reporting                                                                      across the books, from filing accuracy to effective tax rates and recon error
   • Branch policy and procedue lookup for frontline staff                                     rates with:
   • Deal origination pitches
                                                                                               • Actuarial workbook review
                                                                                               • Regulatory filing slides prep
                                                                                               • Scenario and liability modeling


                                                                                                                                                                               15
Chapter 4


Getting started   16
  Chapter 4


Getting started
The Claude ecosystem for financial services spans connectors, plugins, partner
MCP apps, and ten pre-built agent roles for front- and back-office work. All of it
runs on the enterprise controls regulated firms require, including SSO, SCIM,
audit logs, custom data retention, and ISO/IEC 42001:2023 certification.

To explore how Claude fits your firm, visit Claude for Financial Services or
contact your Anthropic account team at sales@anthropic.com.


                                                                                     17
Resources   18
Resources
• Claude for financial services: a high-level overview of how Claude helps
  financial institutions improve how they serve markets and manage risk.

• Finance tutorials on Claude.com: step-by-step guides covering financial
  analysis workflows, using PitchBook and FactSet for research, installing the
  financial services plugins, Excel-based modeling, and more.

• Claude skills catalog: Anthropic's public catalog of community-contributed
  skills, useful for finding pre-built skills before authoring your own.

• Open-source financial services plugins repository: The GitHub repo where
  Anthropic publishes the finance plugins covered in this guide.

• Case study: Newfront modernizes insurance experiences with Claude: A
  modern insurance brokerage uses Claude to automate tedious insurance tasks
  and provide instant support to its 20% market share of US unicorn startups.

• Case study: Hebbia helps knowledge workers save thousands of hours with
  Claude: Built on Claude, this AI platform for knowledge work serves over a
  third of the top 50 asset managers and Tier 1 investment banks and law firms.


                                                                                  19
claude.ai
