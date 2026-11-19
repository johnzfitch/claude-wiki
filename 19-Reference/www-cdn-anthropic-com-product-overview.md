---
title: "Product overview"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/c95395f754f3ca24d46eb352f0c0a71266c36c13.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:35Z"
tags: ["news-research"]
---

Product overview                         4

How Anthropic’s Legal team uses Claude   9

Claude for legal adoption roadmap        11

Getting started                          15

Resources                                17


                                              2
Foreword
The legal profession is at an inflection point. The work is getting more demanding: matters are more
complex, clients expect faster turnaround, and hiring is harder than it used to be. At the same time, AI
has matured from a curiosity into a practical tool that can help with all three. Firms and legal departments
that adopt it thoughtfully now will be better positioned for what comes next.

A 2026 FTI Consulting / Relativity General Counsel Report found that 87% of general counsel now
report genAI use within their teams, compared with 44% the prior year. The longer-term trajectory is even
sharper: CLO gen AI use has climbed from 20% in 2023 to 87% in this year's report. Across drafting, research,
diligence, and matter management, the industry has historically been fast to adopt any technology that drives
productivity by accelerating repetitive workflows. Today, that's agentic AI: systems that act on the work, not
just answer questions about it. The same research found summarization (83%), contract clause identification
(63%), and transcription (53%) are the top gen AI use cases inside legal departments today.

At Anthropic, we are seeing this in action. Legal teams are using Claude for contract review and redlining,
legal research, M&A diligence, privacy impact assessments, matter management, regulatory monitoring,
and outside counsel oversight. Multiple Claude products can be used by legal teams and law firms: Claude
for chat and research, Claude Cowork for matter-level work across files and apps, and Claude for Microsoft
365 for the hours spent in Word, Excel, PowerPoint, and Outlook.

Legal work runs on a broad stack—contract lifecycle systems, research platforms, document management,
e-discovery, data rooms, and the firm-specific precedents and house style that sit on top. Claude connects
to all of it through three building blocks: MCP connectors bring matter data into Claude, practice-area
plugins bundle the workflows lawyers run most often, and an open-source ecosystem lets in-house teams
and firms extend Claude to match how they practice.

Beyond pure legal work, Claude is being used by businesses to manage the day-to-day knowledge work
that fills the rest of the workweek, such as triaging email, prepping for meetings, drafting status updates,
and other administrative work. Cowork is well suited to this kind of multi-app, multi-step overhead, so
the same tool that redlines an NDA in the morning can clear an inbox and prep tomorrow's deposition in
the afternoon.

This guide walks through each product, offers customer examples from across the legal industry, and shares
tips on how to roll out Claude inside your organization.

                                                                                                                 3
Chapter 1


Product overview   4
  Chapter 1


Product overview
Claude shows up to work for lawyers in a few forms: Claude chat, Claude Cowork,       Claude for Microsoft 365
Claude for Microsoft 365, Claude Platform, and Claude Managed Agents.
                                                                                      Legal teams can use Claude inside Microsoft 365 in two ways. Add-ins from
                                                                                      the Microsoft Marketplace put Claude inside Word, Outlook, Excel, and
Claude Chat                                                                           PowerPoint, so a lawyer can redline a contract with tracked changes and turn
                                                                                      the analysis into a memo without leaving the app. The Microsoft 365 connector
The Claude web and desktop app, at Claude.ai, is a chat interface for research
                                                                                      lets Claude search and analyze content in Outlook, Teams, SharePoint, and
and drafting. An associate might use it to summarize a deposition transcript or
                                                                                      OneDrive. Context carries across the suite, so a redline drafted in Word can be
pressure-test an argument before pulling it into a brief. Use Chat when the work
                                                                                      turned into a client update without rebuilding anything.
fits inside a single conversation: a question to the model, a research summary,
an inline draft. Each conversation is its own session, so Chat is suited to one-off
tasks rather than ongoing matters. It is often the first place a new user starts.     Claude Platform
                                                                                      The Claude Platform is Anthropic's API for organizations building their own
Claude Cowork                                                                         applications on Claude. Legal engineering teams and legal tech companies use
                                                                                      it to embed Claude into contract lifecycle, e-discovery, matter management
Claude Cowork is a desktop application where Claude works across local files
                                                                                      systems, and other internal software.
and connected apps to complete multi-step matters. It can read and write local
documents, call connected services like iManage, NetDocuments, Box, and
Microsoft 365, and coordinate work across files and apps. Use Cowork when the         Claude Managed Agents
work spans multiple files, multiple apps, or multiple steps — reviewing every
contract in a data room, comparing third-party paper against the firm's playbook,     Claude Managed Agents allows teams to take any agent it builds on the Claude
or drafting a PIA from a folder of prior assessments. Cowork can run for minutes      Platform and have Anthropic run it as a hosted service, with the long-running
or hours on a single task, with the lawyer reviewing the output once it is done.      sessions, scoped permissions, and audit trail handled for them. For example, a
                                                                                      Contract Review agent might handle NDA triage across thousands of incoming
                                                                                      agreements.
   Claude Chat or Claude Cowork?
   The simplest distinction: Chat is for asking questions and working with
   Claude in the moment. Cowork is for delegating a project to Claude and
   reviewing the result. Most lawyers use both — Chat for quick questions
   through the day, and Cowork for the matter-level work that would
   otherwise eat an afternoon.
                                                                                                                                                                        5
Claude product matrix: when to use what


 Surface                    Best for                        Primary users                 Where it runs                  Example task


                            Conversational drafting,                                                                     "Summarize this
 Claude.ai                  research, and analysis in a     All legal staff               Browser, desktop, mobile       deposition transcript and
                            chat interface                                                                               flag inconsistencies."


                                                                                                                         "Review the data room
                            Cross-app matter work
                                                                                                                         contracts in Box, flag
 Claude Cowork              that touches files and          All legal staff               Claude desktop app
                                                                                                                         material issues, and produce
                            multiple tools
                                                                                                                         a diligence summary."


                            In-place drafting, redlining,                                 Word, Outlook, Excel,
                                                                                                                         "Redline this MSA against
                            and comparison across the                                     PowerPoint (add-ins); Teams,
 Claude for Microsoft 365                                   All legal staff                                              our playbook and produce
                            Microsoft 365 suite; context                                  SharePoint, OneDrive (via
                                                                                                                         a deviation summary."
                            carries across apps                                           M365 connector)


                            Building custom legal
                            applications; embedding                                       Anthropic API, Amazon          "Integrate Claude into our
                                                            Legal engineering, platform
 Claude Platform (API)      Claude into CLM,                                              Bedrock, Google Vertex AI,     CLM to triage incoming
                                                            teams, legal tech vendors
                            e-discovery, or matter                                        Microsoft Foundry              third-party paper"
                            management


                            Running custom legal agents                                                                  "Deploy our NDA triage
                            as hosted cloud services        Platform and legal                                           agent as a managed service
 Claude Managed Agents                                                                    Claude Platform
                            with Anthropic handling         engineering teams                                            with scoped permissions
                            the runtime                                                                                  and audit tracing."


                                                                                                                                                        6
Customizing Claude: connectors, skills, and plugins                                    The connectors most relevant to legal organizations include:


Claude becomes specific to a legal organization through three building                   Contract lifecycle & drafting:
blocks. Connectors give it access to the firm's matter data. Skills teach it how
to complete specific legal tasks in a repeatable way. Plugins bundle skills,
subagents, and connectors into installable packages for a specific practice area.
                                                                                         Document management:
MCP Connectors

MCP Connectors give Claude access to a specific data source over the Model
Context Protocol (MCP), an open standard that lets Claude query the provider's
system directly rather than working off an uploaded copy. This matters in legal          Legal research & case law:
work, where confidentiality and privilege must be preserved end to end.

Skills

Skills are reusable, encoded workflows that teach Claude how to complete                 Deal rooms and transaction documents:
specific legal tasks in a repeatable way. They are valuable in legal work, where
consistency, oversight and accuracy are not optional.

Skills are best used for work that follows a standard format. An NDA review skill
                                                                                         E-discovery and review:
captures the firm's playbook and fallback positions, while a citation skill enforces
Bluebook or local format.

Anthropic has pre-built skills for PDF, Word, Excel, and PowerPoint creation.
Firms can also build their own skills. Simple skills are written in Markdown with
                                                                                         Legal AI assistants, skills, and expert network:
no code; more advanced ones can include executable scripts. Either way, skills
are uploaded in Claude.ai settings, Claude Code, or the API.


                                                                                         Productivity and collaboration:


                                                                                         Public Service:


                                                                                                                                                      7
Subagents                                                                               drafts DSAR responses with the right statutory timeline, and watches for drift
                                                                                        between what your policy promises and what your practice does.
Subagents are narrowly-scoped helper agents that Claude can delegate to
                                                                                      • Product Legal. The connective tissue between a Product Review Doc and a
mid-task. Where a skill tells Claude how to do something, a subagent is an
                                                                                        launch. Reviews launches against your framework, checks marketing claims
agent that runs in its own context window with its own system prompt and
                                                                                        for substantiation, triages "can we do this?" questions, and learns what actually
tool access, completes one bounded job (check a citation, extract a clause, audit
                                                                                        blocks a launch at your company.
defined terms) and reports back. They keep long matters from overloading a
single context window and let firms put tighter tool restrictions on the parts of a   • Regulatory Legal. Watches regulatory feeds, filters by your materiality
workflow that touch sensitive systems.                                                  threshold, diffs new rules against your policy library, tracks gaps and comment
                                                                                        deadlines, and drafts proposed policy updates for review.
Plugins can package subagents alongside skills and connectors so a practice area
                                                                                      • AI Governance Legal. Triages AI use cases against your governance tiers,
ships with the right helpers built in.
                                                                                        runs impact assessments, reviews vendor AI terms, and checks whether your
                                                                                        AI policy has kept pace with your practice. Ships with a policy-starter skill that
Plugins
                                                                                        drafts a firm AI policy from published model policies.
Plugins bundle skills, subagents, and connectors into a single installable package    • IP Legal. Trademark clearance, FTO triage, cease-and-desist drafting and
for a practice area.                                                                    response, DMCA takedowns, OSS compliance, IP clause review, invention
                                                                                        intake screening, and portfolio tracking. Loud guardrails on anything that
Anthropic-built plugins are open source, so firms can install them as shipped or
                                                                                        needs a specialist.
fork them to swap in their own playbooks and add approval workflows. Partner
plugins bring specialized data and provider-built skills into Claude.                 • Litigation Legal. Matter intake, portfolio tracking, legal holds, demand letters,
                                                                                        subpoena triage, chronologies, depo prep, privilege logs, claim charts, and brief
Lawyers have different areas of expertise and focus. These plugins expand               drafting. Adapts to in-house, firm associate, or solo practice.
beyond our initial legal plugin launched in early 2026, aligned to more specific
                                                                                      • Law Student. Socratic drilling that won't give you the answer, because
practice areas. Here is a list of plugins designed for legal professionals:
                                                                                        the point is learning. Case briefing, outlining, IRAC grading, bar prep with
• Commercial Legal. Reviews vendor agreements, NDAs, and SaaS                           jurisdiction distinctions.
  subscriptions against the playbook you taught it, with separate positions for
                                                                                      • Legal Clinic. Client intake, deadline tracking, case memos, and supervisor
  sales-side and purchasing-side work. Tracks renewals, routes escalations,
                                                                                        review queues. Supervisors set a pedagogy dial per practice area that controls
  and translates findings for business stakeholders.
                                                                                        how much the plugin does versus how much the student does. Built within
• Corporate Legal. M&A diligence at scale: extracts issues from a data room,            ABA Formal Op. 512.
  builds disclosure schedules, drafts board consents, tracks the closing checklist,
                                                                                      • Legal Builder Hub. Finds, reviews, installs, and updates community-built legal
  and runs tabular review across hundreds of agreements. Modular setup for
                                                                                        skills from registries like Lawvable, with a security review, license gate, and
  deals, board work, public company governance, and entity compliance.
                                                                                        freshness check on every install. The trust layer for the open legal skills ecosystem.
• Employment Legal. Jurisdiction-aware. Reviews hires and terminations,
  classifies workers, tracks leave deadlines, runs investigations, and drafts         Each role can run as a plugin in Cowork and the Microsoft 365 add-ins for
  policies with state supplements.                                                    desktop use with a human in the loop. Lawyers stay in the workflow, reviewing
                                                                                      and approving the agent's outputs before anything moves downstream.
• Privacy Legal. Reviews DPAs against your playbook, triages PIAs and DPIAs,
                                                                                                                                                                             8
Chapter 2


How Anthropic’s Legal
team uses Claude        9
  Chapter 2


How Anthropic’s Legal team uses Claude
Anthropic's own legal team has built four Claude-powered workflows into daily       to three days down to 24 hours after the tool went live. Lawyers still read every
practice. Each one targets work that follows a standard shape and gets reviewed     blog post; the self-review layer just clears the obvious issues so review time can
by a lawyer before anything moves downstream.                                       go to the calls that require judgment.


Marketing review                                                                    Outside business activity review

                                                                                    The Outside Business Activity Request Form expedites conflict-of-interest
                                                                                    review for Anthropic employees who want to consult or join a nonprofit board.
                                                                                    Employment lawyers were previously spending significant time on routine COI
                                                                                    form reviews; this workflow takes the routine cases off their plate.

                                                                                    Employees fill out a form with their department, manager, and a description of
                                                                                    the proposed activity. Claude analyzes the submission against the COI policy
                                                                                    framework and sends a recommendation to lawyers via Slack for approval.
                                                                                    Where reviewers used to follow up with employees over multiple rounds to
                                                                                    surface details, Claude reads the form, asks for more information if needed, and
                                                                                    proposes an outcome. The recommendation lands in the legal team’s queue with
                                                                                    the analysis already completed.


                                                                                    Privacy impact assessments
The Marketing Material Self-Review Tool lets go-to-market employees check
their own content before sending it to Legal for final review. Marketers paste      Writing PIAs from scratch was tedious, even when assessments followed similar

their draft into a Claude Project, and Claude analyzes it using a skill that        patterns. Anthropic’s legal team now uses MCP servers to connect Claude to

captures the legal team's historical guidance and review framework. The tool        a Google Drive folder of prior PIAs, paired with a Skill that captures the firm's

flags issues like publicity rights concerns, overstated claims, and statistical     format and the issues to look for in each new assessment.

accuracy problems, and labels each as low, medium, or high risk. It also suggests
                                                                                    A lawyer can ask Claude to read the prior assessments, apply the standard
fixes before the marketer submits a formal review ticket.
                                                                                    concerns from the Skill, and draft a new PIA from that context. The lawyer then

When content does get submitted for formal review, it is triaged to the right       reviews and finalizes the document. End-to-end, this new workflow reduces time

lawyer with the pre-flagged issues attached. Turnaround time dropped from two       spent on each PIA from roughly two hours to thirty minutes.


                                                                                                                                                                         10
Contract redlining


Comparing contract versions and recommending fallback language is time-
consuming work. Claude now compares document versions in Google Docs and
Microsoft 365, highlights the changes, and recommends language from the firm's
commercial playbook. The team configured Claude to work inside Google Docs
and comment with suggested edits in real time, so a reviewer can ask directly in
the document whether a piece of language meets the firm's standard, and get an
immediate answer.

The team also writes skills to streamline review of specific document types like
NDAs and third-party vendor agreements. This workflow has reduced redlining
from hours to minutes per agreement.


                                                                                   11
Chapter 3


Claude for legal
adoption roadmap   12
  Chapter 3


Claude for legal adoption roadmap
Most successful Claude rollouts in legal organizations follow this sequence: the      Pro-tip: Have your champions leverage pre-configured plugins so they get value
team lays the foundation for a pilot program, runs a pilot with a focused practice    in the first session. If a lawyer opens Claude Cowork and does not know what to
group, and scales out to the rest of the legal department or firm. Anthropic's        do or what the desired outcome is, they’re unlikely to open it again. If they open
recommended Claude Cowork adoption playbook maps out these three phases.              it, type /nda-triage, and get a clean redline in ninety seconds, they’re more likely
                                                                                      to return.
Phase 1: Lay the foundation
                                                                                      Phase 2: Pilot
Before launching a Claude pilot program, the responsible team needs to put
access and connectors in place. For most legal organizations, this means standing     At this stage, champions are running real workflows with real matter data
up Claude on the first-party API, Amazon Bedrock, Google Vertex AI, or Microsoft      and measuring the pilot's success against pre-defined criteria. Time saved is a
Foundry — whichever keeps Claude inside the firm's existing cloud perimeter.          common metric, specifically tracking the team's cycle time on the pilot job before
Enterprise controls for SSO, SCIM, audit logs, and custom data retention need         and after Claude. Another is how often a lawyer keeps Claude's draft without
to be configured at this stage. Scope governance in parallel: legal hold, privilege   a meaningful rewrite. Together, these two criteria help you assess whether the
protection, and data-privacy review should run alongside access setup.                pilot is working.

The connector set usually starts with the Microsoft 365 connector for Outlook,        Another strong signal that a pilot is working is when champions start to build their
Teams, SharePoint, and OneDrive access, plus one or two systems the pilot team        own skills. A privacy counsel takes the DPIA workflow she has been running by
relies on most. Common starting points are iManage or NetDocuments for matter         hand and turns it into a skill with the firm's template and approval flow embedded.
files, Thomson Reuters for research, and Ironclad or DocuSign for contracts.          That is now a skill the rest of the legal team can begin using immediately.
Firms can install these a la carte as MCP connectors, or access them inside one of
Anthropic's legal plugins.                                                            In most pilots, Claude's product surfaces come online in a specific order. Skills
                                                                                      and plugins come first because they are low-risk and high-reuse. The Microsoft
Next, use Claude to analyze your legal ticket requests to solve the cold start        365 add-ins come next, extending what a pilot team has built into Word, Excel,
problem. Point Claude at your inbox, your ticket queues, and other work to figure     PowerPoint, and Outlook. Claude Cowork tends to come in at the back end of
out what Claude might be able to assist your department with.                         the pilot, when the team is ready to move from single-document work to matter-
                                                                                      level work that spans files and apps.
Pick work that is document-heavy and standard-shape. For an in-house team,
that might be NDA triage or PIA drafting. For a law firm, that could be diligence     Pro-tip: Schedule weekly check-ins with your pilot teams. They surface edge
document review or first-draft research memos. Avoid piloting Claude on novel or      cases fast, like citation hallucination or jurisdiction-specific variations, and you
high-stakes matters without strong human review.                                      want to hear about them while they are fresh.


                                                                                                                                                                             13
Phase 3: Scale                                                                     The table below summarizes the actions you would take at each stage and what
                                                                                   you can expect to see as you go through rollout.
At this stage, plugins and skills that worked during the pilot are being rolled
out to more teams across the legal department or firm through admin-managed          Phase               Actions                          Phase
plugin marketplaces. New hires benefit as well, as they start on day one with
already-encoded workflows. Onboarding is faster and the whole team can work
more efficiently.                                                                                        Security and privilege review.
                                                                                                         Identify 2–3 champion teams.
                                                                                                                                          Champions reporting back
Over time, skills begin compounding across teams. A skill built for one practice                         Install pre-built plugins.
                                                                                    Foundation                                            use cases. First "this saved
area can be adapted for another when their work shares structure. A commercial                           Connect 1–2 core systems
                                                                                                                                          me an hour" moments.
contract review workflow and an employment contract review workflow share                                (iManage/NetDocuments,
                                                                                                         Thomson Reuters/Ironclad).
most of their structure. Adding a second practice group usually goes faster than
the first, and the firm's skill library grows.

Pro-tip: Align as a team on an intentional governance framework to enable
                                                                                                         Champions run real
scaling with confidence and velocity. Have an understanding of how skills                                                                 Measurable time savings.
                                                                                                         workflows. Weekly check-ins.
are quality-controlled, tested before being rolled out, and maintained after                                                              Champions building and
                                                                                    Pilot                Measure against defined
deployment to be kept up-to-date and functional.                                                                                          sharing custom skills. Pull
                                                                                                         criteria. Demo wins to
                                                                                                                                          from other teams.
                                                                                                         adjacent practice groups.


                                                                                                         Admin-provisioned plugin         Skills shared across practice
                                                                                                         marketplace. Encode pilot        areas. New hires ramping
                                                                                    Scale                learnings as firm-wide skills.   on encoded workflows.
                                                                                                         Onboard the next wave            Declining support tickets for
                                                                                                         of users.                        "how do I do this."


                                                                                                                                                                          14
Practice and segment use cases
The work legal teams tend to bring to Claude first is document-heavy and follows a standard shape, with human review before it ships. Still, Claude takes on the drafting
so reviewers can focus on the work that requires judgment, like client counseling and final contract review. The sections below show what that looks like across in-house
teams and different legal practices. They are illustrative rather than exhaustive, and legal use cases continue to expand as model intelligence and tool use evolves.


   In-house legal departments                                                                Litigation and disputes
   In-house teams spend most of their time on documents that need to ship                    Litigation practices process huge volumes of unstructured material on tight
   fast and are reviewed before going to the business or to outside counsel.                 timelines. Claude can shorten review cycles and improve consistency with:
   Claude speeds up the drafting, giving counsel more time for the work that
   requires judgment, with:                                                                  • Discovery document review and privilege coding
                                                                                             • Deposition preparation and witness summaries
   • Contract review and redlining against playbook                                          • Brief drafting and citation checking
   • NDA triage and counterparty paper review                                                • Pleadings analysis and motion drafting
   • Privacy impact assessments and data subject requests                                    • Expert report review
   • Outside counsel billing review and matter management
   • Marketing copy and product feature review
   • Board materials preparation and corporate governance tasks
   • Regulatory monitoring and compliance updates                                            Compliance and regulatory
                                                                                             Compliance and regulatory teams sit across structured filings and
                                                                                             unstructured guidance, much of it in regulated jurisdictions. Claude can
                                                                                             improve accuracy and timeliness across the program with:
   Transactional review
   Transactional practices spend the majority of their time on documents                     • Regulatory filing preparation and review
   that follow standard formats and partner-led review. Claude can compress                  • Audit response and gap analysis
   diligence cycles and improve coverage with:                                               • Policy drafting and jurisdictional comparison
                                                                                             • AI governance and vendor review
   • M&A diligence document review and summary memos                                         • KYC/AML screening and escalation
   • Pitch book preparation and competitive analysis
   • Comparable transaction analysis
   • CIM and offering document drafting
   • Closing checklist tracking


                                                                                                                                                                            15
Frequently asked questions for CIOs and IT leaders                                   sessions require server-side storage to function—so ZDR does not apply
                                                                                     there. Enterprise plans for those surfaces support custom retention windows
To help you get up and running, here are some common questions related to            configurable down to 30 days, and Anthropic does not train on customer data on
Claude and Claude Cowork that legal teams might need to address for their CIOs.      any surface.

Note: The questions below cover Claude.ai (web and desktop chat) and Claude          What identity and access controls do you support? Enterprise plans include
Cowork (desktop application). Custom applications built on the Claude Platform       SSO via SAML, SCIM for user provisioning, role-based access controls, and
have additional configuration options handled directly with the account team.        admin-managed plugin marketplaces for both surfaces.

Where are Claude.ai and Claude Cowork hosted? Both are SaaS products                 What certifications do you hold? Anthropic is ISO/IEC 42001:2023 certified
hosted by Anthropic. Firms that need workloads to run inside their own cloud         for responsible AI management and SOC 2 Type II audited. Additional
perimeter typically build custom applications on the Claude Platform via             documentation is available at trust.anthropic.com.
Amazon Bedrock, Google Vertex AI, or Microsoft Foundry, rather than using
Claude.ai or Cowork directly.                                                        How does Claude Cowork integrate with our document management
                                                                                     system? Cowork connects to iManage, NetDocuments, Box, and more document
What does Claude Cowork install on user endpoints? Cowork is a signed                management systems through MCP connectors. The connectors authenticate as
desktop application available for macOS and Windows. It runs as a standard           the end user and respect entitlements at the matter and folder level, so Cowork
user-space application, requires no kernel-level components, and updates             only sees what the user already has access to.
through standard auto-update channels. IT can deploy and manage it through
MDM and standard endpoint management tools.                                          How is attorney-client privilege protected? Privilege protection rests on access
                                                                                     control and data handling. Connectors in Cowork honor the access controls
How does Claude Cowork access local files? Cowork only reads files in folders        already configured in your DMS or matter management system. Anthropic does
the user explicitly grants access to from inside the application. Access is scoped   not train on customer data, and Enterprise plans support custom retention. Firms
per user, the same way modern desktop applications handle file permissions on        working with privileged content typically pair this with firm-defined policies on
macOS and Windows. There is no background indexing of the user's drive.              which matters and document types can be processed.

Is our data used to train Claude's models? No. Anthropic does not train on           How do we set firm-wide policies and guardrails? Plugins, skills, and
inputs or outputs from Enterprise Plan accounts using Claude.ai or Cowork.           connectors can be provisioned through admin-managed marketplaces in both
                                                                                     Claude.ai and Claude Cowork rather than installed per user. This gives IT a
What retention controls are available? Enterprise plans support custom               single place to control which workflows are available and which approval steps
data retention, including zero-retention configurations, for both Claude.ai          are required before output moves downstream.
conversations and Cowork sessions.
                                                                                     Who are the subprocessors? A current list of Anthropic subprocessors is
Do you support Zero Data Retention (ZDR)? ZDR is available on the Claude             published at trust.anthropic.com and updated as the list changes.
Platform (API) and Claude Code for approved customers. Claude.ai and Claude
Cowork are stateful products—conversation history, Projects, and Cowork              Learn more in our Claude Cowork Enterprise Admin Guide.


                                                                                                                                                                         16
Chapter 4


Getting started   17
  Chapter 4


Getting started
The Claude ecosystem for legal spans connectors, plugins, partner MCP
apps, and pre-built agent roles for in-house, law firm, and compliance work.
All of it runs on the enterprise controls regulated organizations require,
including SSO, SCIM, audit logs, custom data retention, and ISO/IEC
42001:2023 certification.

To explore how Claude fits your firm or legal department, visit our legal
solutions page or contact your Anthropic account team at sales@anthropic.com.


                                                                                18
Resources   19
Resources
• Legal tutorials on Claude.com: step-by-step guides covering contract review,
  NDA triage, legal research workflows, installing the legal plugins, and more.

• Claude skills catalog: Anthropic's public catalog of community-contributed
  skills, useful for finding pre-built legal skills before authoring your own.

• Open-source legal plugins repository: The GitHub repo where Anthropic
  publishes the legal plugins covered in this guide.

• Blog article: How Anthropic uses Claude for legal work: A look at how our
  own legal team uses Claude in daily practice across PIAs, marketing review,
  and contract redlining.


                                                                                  20
claude.ai
