---
title: "Manufacturing | Claude by Anthropic"
source_url: "https://www.claude.com/solutions/manufacturing"
category: "18-Industry-UseCases"
fetched_at: "2026-11-18T06:29:39Z"
tags: ["case-studies"]
---

# Built for people who build things

Claude helps your teams price new jobs, write up quality issues, and diagnose machine breakdowns from your facility’s records. It works through the steps, and your experts make the call.

[Get the plugin (opens in new tab)](https://claude.ai/customize/plugins/id/45112ff2-6233-4954-b8ec-c448ef2d1e59%40anthropic-plugin-directory)[Contact sales](https://www.claude.com/contact-sales)

## Designed to work on day one

### Works with your systems

Start from the ERP records, drawings, and procedures you have today. Claude meets your team where the work already happens. Vendors’ systems remain the system of record.

[Explore connectors](https://www.claude.com/marketplace/connectors-plugins)

### Skills adapt to your procedures

Skills are a starting point. Your team adapts them to its own forms and procedures, picks one process to measure first, and builds new skills for work only your facility does.

[Get the plugin (opens in new tab)](https://claude.ai/customize/plugins/id/45112ff2-6233-4954-b8ec-c448ef2d1e59%40anthropic-plugin-directory)

### Drafts come with context

See where figures came from: drafts can link to the drawing, requirement, or record behind them. Claude can flag what a template might miss, like a failure that has happened before.

[See use cases](#use-cases)

### Approvals stay with your team

Quality, estimating, and production teams can review drafts. On Team and Enterprise plans, owners can require approval before a connector changes anything, or block changes.

[Visit the Trust Center (opens in new tab)](https://trust.anthropic.com/)

Introducing Claude for Manufacturing

Draft quotes, reports, and supplier requests that start in your systems and are built to end with your review.

[Read the announcement](https://www.claude.com/resources/articles/claude-for-manufacturing)

## How manufacturing teams use Claude

Inspection to CAPA

RFQ to quote

Morning report

Machine down

Trade study

Prompt

Draft the 8D for the INSP-1105 bore nonconformance.

Connectors

- [Infor](https://www.claude.com/marketplace/connectors/infor)
- [Microsoft 365](https://www.claude.com/marketplace/connectors/microsoft-365)

8D: DRAFT customer version

*Controlled 8D template: not on file; standard eight-discipline structure used.*

##### D1: Team (proposed roles; owner edits)

- Lead: quality engineering, unassigned
- Finder: inspection
- Production supervisor, unassigned
- Boring-operation operator, unassigned
- Metrology / calibration owner, unassigned
- Reviewer: quality review

##### D2: Problem description

- **Requirement:** DWG-PN-305 Rev B, Sheet 1, detail A, zone C3: bore Ø12.000–12.025 mm.
- Found 2026-11-05 09:10 EST, INSP-1105, by inspection: 4 of 8 sequentially sampled pieces from LOT-1105 (WO-305) above 12.025 mm (pieces 4, 5, 6, 8; max 12.034 mm, 0.009 mm over).
- **Gauge:** the inspection gauge; calibration unverified, so measurement validity is unconfirmed.
- **Scope:** whole lot suspect. Reported lot quantity: 200, unreconciled; wider suspect scope unknown. This does not establish that all pieces are defective.
- **Prior nonconformance on the same part and characteristic:** 2 Oct 2026. Whether its CAPA held is unknown.

##### D3: Interim containment (plan confirmed; execution unverified)

- Reported done (supervisor, 09:25, unverified): operation stopped; red hold tag on lot rack; all 200 reported onsite, none shipped.
- **Open, owners unassigned:** shipment-record check covering installed-at-customer, at-customer and in-transit (immediate); verify segregation, count lot, ERP hold (immediate); confirm none in finished goods (same day).
- **Held:** 100% inspection, until the inspection gauge is verified. Not authorized: disposition, release, restart, inspection execution.

##### D4: Root cause

**Status:** ROOT CAUSE NOT VALIDATED. Ranked candidates below; the leading candidate is weakly ahead and not confirmed.

###### Occurrence, candidate 1 (leading, weak): setup offset error after insert change

- **Chain:** insert changed 08:40 → offset adjusted → offset left bore cutting oversize → parts ran oversize until 09:10 sample.
- **Link 1** insert changed. For: process note C, 08:40. Against: none.
- **Link 2** offset adjusted. For: note C says adjusted. Against: no offset log; value unknown. WEAK POINT: no record of the value set.
- **Link 3** bore cut oversize. For: 4 of 8 over (A); an operator-reported suspicion of a setting error (unvalidated). Against: pieces 1–3 and 7 in limits; readings rise across 1–5 rather than step; which pieces were cut after 08:40 is unknown; gauge unverified.
- **Confirm:** CNC offset history shows a changed bore offset at 08:40 AND retained post-08:40 pieces are oversize on a verified gauge.
- **Rule out:** retained pieces re-measure within limits on a verified gauge, or pieces cut before 08:40 are equally oversize.

###### Occurrence, candidate 2 (unresolved, cannot be excluded): gauge reads high

- **Chain:** the inspection gauge out of calibration or mis-set → readings biased high → in-limit bores reported oversize.
- **Link 1** gauge out of cal. For: certificate unavailable (A). Against: unavailable is not lapsed.
- **Link 2** readings biased high. For: none. WEAK POINT. Note: a uniform +0.009 mm bias would put all 8 readings within limits (lowest becomes 12.002 mm), so the data cannot exclude it. Against: no evidence of bias.
- **Confirm:** the inspection gauge reads a certified master outside its accuracy.
- **Rule out:** the inspection gauge reads a certified master within its accuracy.

###### Occurrence, candidate 3 (weakest): progressive drift

- **Chain:** thermal growth or edge build-up after restart → bore grows across the run → later pieces oversize.
- **Link 1** drift mechanism. For: none. WEAK POINT. Against: new insert at 08:40 argues against wear; no sensor or thermal data.
- **Link 2** bore grows across run. For: readings rise across pieces 1–5. Against: rise does not continue (pieces 6–8: 12.029, 12.021, 12.030); six-points-increasing run rule not met (longest run 5).
- **Confirm:** further sequential pieces on a verified gauge keep growing.
- **Rule out:** a verified-gauge sequence shows a stable offset.

###### Cheapest discriminating test

Check the inspection gauge against a certified master, then re-measure retained pieces 1–8 on a verified instrument. Separates Candidate 2 from Candidates 1 and 3, and every other conclusion depends on it.

###### Escape / detection, candidate, not validated

Why it was not caught before 09:10: first-piece check after insert change is required by the work instruction per note C, but no first-piece approval exists for 08:40. Whether it was skipped, done and not recorded, or not applicable is unknown; the instruction's document-control record was not supplied.

###### Systemic, candidate, not validated

The prior nonconformance on this part and characteristic (2 Oct 2026) was closed after offset correction and retraining; its corrective action's effectiveness check has no results. Effectiveness unknown, not proven failed. Whether today's cause matches October's is not established.

##### D5: Permanent corrective actions

**Status:** PROPOSED, NOT CHOSEN. No owners, no dates. Contingent on the D4 test results.

###### P1: breaks Candidate 1, link 2 (offset value unrecorded/unverified)

After any insert change, record the offset value set and require a measured first piece on a verified gauge before the run continues.

###### P2: breaks Candidate 2, link 1 (gauge out of calibration)

**If confirmed:** quarantine the inspection gauge, recalibrate, and assess every inspection it performed since its last valid calibration.

###### Moved to D3 (containment, not corrective)

100% inspection of the lot; ERP hold; shipment check.

###### Improvement, not corrective action

Review whether 8-piece sequential sampling is adequate for this characteristic.

##### D6: Implement and verify

**Placeholder.** Action implemented, implemented by and date, verification method and result, and verified by and date, all to be completed.

##### D7: Prevent recurrence

**Status:** PROPOSED, NOT APPROVED. The items below are QUESTIONS TO INVESTIGATE, not established facts. Missing evidence in the supplied extracts does not show how the prior CAPA was run.

###### Known (from supplied quality-history extract)

The prior nonconformance on this part (2 Oct 2026) was closed after offset correction and operator retraining. Its corrective action record lists retraining completed 4 Oct and an effectiveness field reading 'check next 3 lots'. No lot results, independent verification or closure evidence were supplied. Effectiveness is unknown, not proven failed.

###### Questions to investigate

- **Q1. Effectiveness check.** Did its corrective action's effectiveness check have an owner, a due date and a data source, and was it run? Records not supplied.
- **Q2. Closure sequence.** When was the prior nonconformance closed relative to the effectiveness check, and what closure criteria applied? Records not supplied.
- **Q3. Scope of the prior action.** Was retraining the only action under the prior corrective action, or were setup or first-piece controls also changed? The extract lists retraining; it may not be complete.
- **Q4. Calibration visibility.** Was the inspection gauge's calibration status visible and checked at the point of use? Only the certificate's unavailability is known.

###### Candidate system changes (conditional on the answers; none selected)

- **If Q1 or Q2 shows a gap:** require effectiveness evidence before CAPA closure.
- **If Q3 shows training-only control:** add a recorded first-piece release after insert or offset changes.
- **If Q4 shows a gap:** record gauge calibration status with each inspection result.

##### D8: Close and recognize

**Placeholder.** Closure approval, date, effectiveness evidence reference and team recognition, all to be completed.

##### Redaction diff

**Gate 2: redaction diff approved by Quality Reviewer, 2026-11-05 10:07 EST.** Seven rows of personnel names and internal identifiers removed. Does not approve the 8D conclusions, corrective actions or release. Draft; unsent; no customer identified.

### Turn a failed inspection into a draft 8D

Share an inspection finding and Claude writes the NCR against its requirement, checks past NCRs for the same failure, ranks likely causes with evidence for each, and drafts the 8D. Your quality engineer reviews and signs.

### Build a quote that shows its math

Forward an RFQ. Claude fills in your intake form, lists what’s missing from the drawing, and prices the job from cost history and similar past jobs. Your estimator reviews the draft quote before it goes out.

### Open the morning report with last night’s numbers

Set the schedule once. Claude joins overnight production, downtime, and scrap exports into one report with output against plan and ranked OEE losses. Your supervisors start the day with it in hand.

### Rank likely causes when a machine goes down

Share recent sensor exports, maintenance history, photos, and your OEM manual. Claude ranks likely causes with evidence for a technician to check and decide on.

### Compare design variants on one slide

Set your target parameters. Claude generates variants in Autodesk Fusion from your engineer’s model, scores them side by side, and drafts the comparison for design review. Your design engineer checks it and shares it.

## Claude works with your tools

Claude connects to ERP, CAD, and document systems.

[Explore connectors](https://www.claude.com/marketplace/connectors-plugins)

- 

  > “Manufacturers need answers grounded in how their business really runs, and then the ability to act on them. Infor brings the industry depth and governed controls, allowing customers to access that industry-specific context in Claude or in Infor, wherever they choose to work. When AI begins managing your workflows, the system underneath matters more, not less.”

  Kevin Samuelson, CEO of Infor

## Access starts and ends with your admins

Anthropic was founded to build AI that’s reliable and safe. In your facility, that means your admins set what Claude can reach and your team can review work before it goes out.

[Visit the Trust Center (opens in new tab)](https://trust.anthropic.com/)

### Choose what Claude can see

Your team chooses which systems to connect, and connectors generally follow each person’s permissions in those systems.

[Browse connectors](https://www.claude.com/marketplace/connectors-plugins)

### Review every draft before it goes out

Claude drafts documents, like quotes and reports, for your manufacturing team to review and approve. It doesn’t operate equipment.

### Set who can use it

On Enterprise plans, admins can make the plugin available to one group or to everyone. Connectors are managed separately.

[Explore Claude Enterprise](enterprise.md)

## More products and tools for manufacturing

### Infor in Claude plugin

Extend Infor to Claude. Ask questions, approve suggestions, and let Infor complete tasks like creating a purchase order or shifting production lines after unplanned downtime—without switching applications.

[Get the plugin (opens in new tab)](https://claude.ai/directory/infor)

### Claude for Microsoft 365

Bring Claude to Word, Excel, PowerPoint, and Outlook, where your procedures, reports, and exports live.

[Learn more](https://www.claude.com/claude-for-microsoft-365)

### Claude Code

For engineering teams that write software and tests alongside the hardware they design.

[Learn more](../15-Claude-AI-Features/product-claude-code.md)

### Claude Developer Platform

For teams building their own applications on Claude models, direct or through AWS, Google Cloud, and Microsoft Foundry.

[Learn more](https://www.claude.com/platform/api)

Webinar

On November 17, join a one-hour technical session on what works in facilities today, how to start, and a first look at the Model Hardware Standard.

[Register now](https://www.claude.com/resources/webinars/claude-for-manufacturing-put-your-plants-know-how-to-work)

Research preview

## Introducing the Model Hardware Standard

A shared specification for AI agents to safely operate physical devices, now in a limited research preview with research labs and advanced manufacturers. It’s separate from the Claude for Manufacturing plugin, which drafts documents and doesn’t operate equipment.

[Read the announcement (opens in new tab)](../19-Reference/model-hardware-standard-research-preview.md)

## Manufacturing resources


The Model Hardware Standard, a research preview

Blog


UST: writing and running the tests that check a hardware design

Customer story


How to customize plugins in Claude

Tutorial

## FAQs

### What is Claude for Manufacturing?

Claude for Manufacturing is Claude tailored to your facility. It’s AI for manufacturing teams, delivered as a plugin with [ready-made skills](https://claude.com/skills) for quoting, quality, operations, supply chain, and design. It connects to Oracle NetSuite, Microsoft 365, Autodesk Fusion, and Infor.

### What types of tasks can Claude for Manufacturing help me with?

With the [Claude for Manufacturing plugin](https://claude.com/marketplace/plugins), Claude drafts quotes, NCRs, 8Ds, and production reports from your facility’s records, and your team reviews each one.

### Does Claude replace our manufacturing quoting software?

No. Claude works from your ERP’s cost history, routings, and past jobs to draft a quote for your estimator to review. If you also run manufacturing estimating software, it stays in place, and Claude can work from the exports your team pulls from it.

### Where does Claude fit in a smart manufacturing plan?

Most smart manufacturing programs begin with sensors, new systems, and a data platform. Claude begins with the documents and exports your facility has today, so there’s no data project to finish first. Start with one process you measure, such as quoting or quality, and expand from there.

### Does Claude operate equipment in our facility?

No. Claude drafts documents for your team to review. It doesn’t run production control, operate equipment, or write to your systems of record. The [Model Hardware Standard (opens in new tab)](../19-Reference/model-hardware-standard-research-preview.md), a separate research preview, covers how AI could work with equipment in the future.

### Which plans include the plugin, and how do we install it?

The plugin is available on [paid plans](../17-Billing-Plans/pricing.md), including Enterprise bought through [AWS Marketplace](../04-API-Reference/Other/partners-claude-on-aws.md). Admins install it from the [plugin directory](https://claude.com/marketplace/plugins). After that, anyone with access can say “set us up,” and Claude asks which systems you run, tests the connectors, and lists anything still missing.

### We’re a process manufacturer. Is this for us?

Partly, today. The plugin fits best where each job gets its own quote, drawing, and routing, and where quality issues are written up as NCRs and 8Ds. Process manufacturers in food, CPG, chemicals, and steel can use the morning production report, breakdown diagnosis, and supplier skills right away. Skills are also adaptable, so your team can change the quoting and quality skills to match your batch records and procedures.

How can I help?

We just received this RFQ. Can you help me fill out our intake form and tell me what’s missing from the drawing?


Ask Claude (opens in new tab)

How can I help?

Has this failure come up in past NCRs, and did the fix work?


Ask Claude (opens in new tab)

How can I help?

Hey Claude, summarize this supplier’s quality issues from the last year


Ask Claude (opens in new tab)

1 of 3

How can I help?

We just received this RFQ. Can you help me fill out our intake form and tell me what’s missing from the drawing?


Ask Claude (opens in new tab)

How can I help?

Has this failure come up in past NCRs, and did the fix work?


Ask Claude (opens in new tab)

How can I help?

Hey Claude, summarize this supplier’s quality issues from the last year


Ask Claude (opens in new tab)

## One process is enough to start

[Get the plugin (opens in new tab)](https://claude.ai/customize/plugins/id/45112ff2-6233-4954-b8ec-c448ef2d1e59%40anthropic-plugin-directory)[Contact sales](https://www.claude.com/contact-sales)
