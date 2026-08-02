---
title: "Detecting and countering misuse of AI: August 2025 \\ Anthropic"
source_url: "https://www.anthropic.com/news/detecting-countering-misuse-aug-2025"
category: "19-Reference"
fetched_at: "2026-08-02T05:43:08Z"
tags: ["claude-code"]
---

# Detecting and countering misuse of AI: August 2025

Aug 27, 2025

[Threat Intelligence Report: August 2025](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf)

We’ve [developed](https://www.anthropic.com/news/building-safeguards-for-claude) sophisticated safety and security measures to prevent the misuse of our AI models. But cybercriminals and other malicious actors are actively attempting to find ways around them. Today, we’re releasing a report that details how.

Our [Threat Intelligence report](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf) discusses several recent examples of Claude being misused, including a large-scale extortion operation using Claude Code, a fraudulent employment scheme from North Korea, and the sale of AI-generated ransomware by a cybercriminal with only basic coding skills. We also cover the steps we’ve taken to detect and counter these abuses.

We find that threat actors have adapted their operations to exploit AI’s most advanced capabilities. Specifically, our report shows:

- **Agentic AI has been weaponized.** AI models are now being used to *perform* sophisticated cyberattacks, not just advise on how to carry them out.
- **AI has lowered the barriers to sophisticated cybercrime.** Criminals with few technical skills are using AI to conduct complex operations, such as developing ransomware, that would previously have required years of training.
- **Cybercriminals and fraudsters have embedded AI throughout all stages of their operations**. This includes profiling victims, analyzing stolen data, stealing credit card information, and creating false identities allowing fraud operations to expand their reach to more potential targets.

Below, we summarize three case studies from our full report.

## **‘Vibe hacking’: how cybercriminals used Claude Code to scale a data extortion operation**

**The threat:** We recently disrupted a sophisticated cybercriminal that used Claude Code to commit large-scale theft and extortion of personal data. The actor targeted at least 17 distinct organizations, including in healthcare, the emergency services, and government and religious institutions. Rather than encrypt the stolen information with traditional ransomware, the actor threatened to expose the data publicly in order to attempt to extort victims into paying ransoms that sometimes exceeded \$500,000.

The actor used AI to what we believe is an unprecedented degree. Claude Code was used to automate reconnaissance, harvesting victims’ credentials, and penetrating networks. Claude was allowed to make both tactical and strategic decisions, such as deciding which data to exfiltrate, and how to craft psychologically targeted extortion demands. Claude analyzed the exfiltrated financial data to determine appropriate ransom amounts, and generated visually alarming ransom notes that were displayed on victim machines.

```
=== PROFIT PLAN FROM [ORGANIZATION] ===

💰 WHAT WE HAVE:
FINANCIAL DATA
[Lists organizational budget figures]
[Cash holdings and asset valuations]
[Investment and endowment details]

WAGES ([EMPHASIS ON SENSITIVE NATURE])
[Total compensation figures]
[Department-specific salaries]
[Threat to expose compensation details]

DONOR BASE ([FROM FINANCIAL SOFTWARE])
[Number of contributors]
[Historical giving patterns]
[Personal contact information]
[Estimated black market value]

🎯 MONETIZATION OPTIONS:

OPTION 1: DIRECT EXTORTION
[Cryptocurrency demand amount]
[Threaten salary disclosure]
[Threaten donor data sale]
[Threaten regulatory reporting]
[Success probability estimate]

OPTION 2: DATA COMMERCIALIZATION
[Donor information pricing]
[Financial document value]
[Contact database worth]
[Guaranteed revenue calculation]

OPTION 3: INDIVIDUAL TARGETING
[Focus on major contributors]
[Threaten donation disclosure]
[Per-target demand range]
[Total potential estimate]

OPTION 4: LAYERED APPROACH
[Primary organizational extortion]
[Fallback to data sales]
[Concurrent individual targeting]
[Maximum revenue projection]

📧 ANONYMOUS CONTACT METHODS:
[Encrypted email services listed]

⚡ TIME-SENSITIVE ELEMENTS:
[Access to financial software noted]
[Database size specified]
[Urgency due to potential detection]

🔥 RECOMMENDATION:
[Phased approach starting with organizational target]
[Timeline for payment]
[Escalation to alternative monetization]
[Cryptocurrency wallet prepared]
```

Copy

*Above: simulated ransom guidance created by our threat intelligence team for research and demonstration purposes.*

```
To: [COMPANY] Executive Team
Attention: [Listed executives by name]

We have gained complete compromise of your corporate infrastructure and extracted proprietary information.

FOLLOWING A PRELIMINARY ANALYSIS, WHAT WE HAVE:
FINANCIAL SYSTEMS
[Banking authentication details]
[Historical transaction records]
[Wire transfer capabilities]
[Multi-year financial documentation]

GOVERNMENT CONTRACTS ([EMPHASIZED AS CRITICAL])
[Specific defense contract numbers]
[Technical specifications for weapons systems]
[Export-controlled documentation]
[Manufacturing processes]
[Contract pricing and specifications]

PERSONNEL RECORDS
[Tax identification numbers for employees]
[Compensation databases]
[Residential information]
[Retirement account details]
[Tax filings]

INTELLECTUAL PROPERTY
[Hundreds of GB of technical data]
[Accounting system with full history]
[Quality control records with failure rates]
[Email archives spanning years]
[Regulatory inspection findings]

CONSEQUENCES OF NON-PAYMENT:
We are prepared to disclose all information to the following:
GOVERNMENT AGENCIES
[Export control agencies]
[Defense oversight bodies]
[Tax authorities]
[State regulatory agencies]
[Safety compliance organizations]

COMPETITORS AND PARTNERS:
[Key commercial customers]
[Industry competitors]
[Foreign manufacturers]

MEDIA:
[Regional newspapers]
[National media outlets]
[Industry publications]

LEGAL CONSEQUENCES:
[Export violation citations]
[Data breach statute violations]
[International privacy law breaches]
[Tax code violations]

DAMAGE ASSESSMENT:
[Defense contract cancellation]
[Regulatory penalties in millions]
[Civil litigation from employees]
[Industry reputation destruction]
[Business closure]

OUR DEMAND:
[Cryptocurrency demand in six figures]
[Framed as fraction of potential losses]

Upon payment:
[Data destruction commitment]
[No public disclosure]
[Deletion verification]
[Confidentiality maintained]
[Continued operations]
[Security assessment provided]

Upon non-payment:
[Timed escalation schedule]
[Regulatory notifications]
[Personal data exposure]
[Competitor distribution]
[Financial fraud execution]

IMPORANT:
[Comprehensive access claimed]
[Understanding of contract importance]
[License revocation consequences]
[Non-negotiable demand]

PROOF:
[File inventory provided]
[Sample file delivery offered]

DEADLINE: [Hours specified]

Do not test us. We came prepared.
```

Copy

*Above: A simulated custom ransom note. This is an illustrative example, created by our threat intelligence team for research and demonstration purposes after our analysis of extracted files from the real operation.*

**Implications:** This represents an evolution in AI-assisted cybercrime. Agentic AI tools are now being used to provide both technical advice and active operational support for attacks that would otherwise have required a team of operators. This makes defense and enforcement increasingly difficult, since these tools can adapt to defensive measures, like malware detection systems, in real time. We expect attacks like this to become more common as AI-assisted coding reduces the technical expertise required for cybercrime.

**Our response:** We banned the accounts in question as soon as we discovered this operation. We have also developed a tailored classifier (an automated screening tool), and introduced a new detection method to help us discover activity like this as quickly as possible in the future. To help prevent similar abuse elsewhere, we have also shared technical indicators about the attack with relevant authorities.

## **Remote worker fraud: how North Korean IT workers are scaling fraudulent employment with AI**

**The threat:** We discovered that North Korean operatives had been using Claude to fraudulently secure and maintain remote employment positions at US Fortune 500 technology companies. This involved using our models to create elaborate false identities with convincing professional backgrounds, complete technical and coding assessments during the application process, and deliver actual technical work once hired.

These employment schemes were designed to generate profit for the North Korean regime, in defiance of international sanctions. This is a long-running operation that began before the adoption of LLMs, and has been reported by [the FBI](https://www.ic3.gov/PSA/2025/PSA250723-4).

**Implications:** North Korean IT workers previously underwent years of specialized training prior to taking on remote technical work, which made the regime’s training capacity a major bottleneck. But AI has eliminated this constraint. Operators who cannot otherwise write basic code or communicate professionally in English are now able to pass technical interviews at reputable technology companies and then maintain their positions. This represents a fundamentally new phase for these employment scams.

**Our response:** when we discovered this activity we immediately banned the relevant accounts, and have since improved our tools for collecting, storing, and correlating the known indicators of this scam. We’ve also shared our findings with the relevant authorities, and we’ll continue to monitor for attempts to commit fraud using our services.

## **No-code malware: selling AI-generated ransomware-as-a-service**

**The threat:** A cybercriminal used Claude to develop, market, and distribute several variants of ransomware, each with advanced evasion capabilities, encryption, and anti-recovery mechanisms. The ransomware packages were sold on internet forums to other cybercriminals for \$400 to \$1200 USD.

**Implications:** This actor appears to have been dependent on AI to develop functional malware. Without Claude’s assistance, they could not implement or troubleshoot core malware components, like encryption algorithms, anti-analysis techniques, or Windows internals manipulation.

**Our response:** We have banned the account associated with this operation, and alerted our partners. We’ve also implemented new methods for detecting malware upload, modification, and generation, to more effectively prevent the exploitation of our platform in the future.

## **Next steps**

In each of the cases described above, the abuses we’ve uncovered have informed updates to our preventative safety measures. We have also shared details of our findings, including indicators of misuse, with third-party safety teams.

In the full report, we address a number of other malicious uses of our models, including an attempt to compromise Vietnamese telecommunications infrastructure, and the use of multiple AI agents to commit fraud. The growth of AI-enhanced fraud and cybercrime is particularly concerning to us, and we plan to prioritize further research in this area.

We’re committed to continually improving our methods for detecting and mitigating these harmful uses of our models. We hope this report helps those in industry, government, and the wider research community strengthen their own defenses against the abuse of AI systems.

## **Further reading**

For the full report with additional case studies, [see here.](https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf)


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](/news/investigating-incidents-cybersecurity-evals)

### Our position on open-weights models

[Read more](/news/position-open-weights-models)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](/news/cognizant-anthropic)

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](/learn)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
