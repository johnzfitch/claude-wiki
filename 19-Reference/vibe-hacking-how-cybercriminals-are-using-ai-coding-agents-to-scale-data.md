---
title: "Vibe hacking: how cybercriminals are using AI coding agents to scale data"
source_url: "https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:51Z"
tags: ["agents", "news-research"]
---

Vibe hacking: how cybercriminals are using AI coding agents to scale data		   4
      extortion operations					

      Remote worker fraud: how North Korean IT workers are scaling fraudulent		     11
      employment with AI					

      No-code malware: selling AI-generated ransomware-as-a-service			              15

      Chinese threat actor leveraging Claude across nearly all				                  18
      MITRE ATT&CK tactics							

      Auto-disruption of a North Korean malware distribution campaign			            19

      No-code malware development campaign							20

AI-enhanced fraud: AI’s growing footprint in the fraud ecosystem				                21

Case studies

      Threat actor leverages MCP for stealer log analysis					                      23
      and victim profiling								

      Carding store powered by AI								24

      Romance scam bot powered by AI models						                                   25

      Synthetic identity services powered by AI						26


AUGUST 2025                                                                              2
Executive     We have developed sophisticated safety and security measures to prevent
              the misuse of our AI models. While these measures are generally effective,

summary       cybercriminals and other malicious actors continually attempt to find
              ways around them. This report details several recent examples of how
              Claude has been misused, along with the steps we’ve taken to detect and
              counter their abuse.

              This represents the work of Threat Intelligence: a dedicated team at
              Anthropic finds deeply investigated sophisticated real world cases of
              misuse and works with the rest of the Safeguards organization to improve
              our defenses against such cases.

              While specific to Claude, the case studies presented below likely reflect
              consistent patterns of behaviour across all frontier AI models. Collectively,
              they show how threat actors are adapting their operations to exploit
              today’s most advanced AI capabilities:

              • Agentic AI systems are being weaponized: AI models are themselves
                being used to perform sophisticated cyberattacks – not just advising on
                how to carry them out.

              • AI lowers the barriers to sophisticated cybercrime. Actors with
                few technical skills have used AI to conduct complex operations, like
                developing ransomware, that would previously have required years of
                training.

              • Cybercriminals are embedding AI throughout their operations.
                This includes victim profiling, automated service delivery, and in
                operations that affect tens of thousands of users.

              • AI is being used for all stages of fraud operations. Fraudulent
                actors use AI for tasks like analyzing stolen data, stealing credit card
                information, and creating false identities.

              We’re discussing these incidents publicly in order to contribute to the
              work of the broader AI safety and security community, and help those
              in industry, government, and the wider research community strengthen
              their own defences against the abuse of AI systems. We plan to continue
              releasing reports like this regularly, and to be transparent about the
              threats we find.


AUGUST 2025                                                                                3
Vibe hacking:                          Summary
how cybercriminals                     Today we are sharing insights about a sophisticated cybercriminal

are using AI coding                    operation (tracked as GTG-2002) we recently disrupted that represents
                                       a new evolution in how cyber threat actors leverage AI—using coding
agents to scale                        agents to actively execute operations on victim networks, known as “vibe
data extortion                         hacking”.

operations                             A cybercriminal used Claude Code to conduct a scaled data extortion
                                       operation across multiple international targets in a short timeframe. This
                                       threat actor leveraged Claude’s code execution environment to automate

   ABOUT CLAUDE CODE                   reconnaissance, credential harvesting, and network penetration at scale,
                                       potentially affecting at least 17 distinct organizations in just the last
   Anthropic’s agentic coding          month across government, healthcare, emergency services, and religious
   tool that lives in your terminal,   institutions.
   understands your codebase, and
   helps you code faster through       The operation demonstrates a concerning evolution in AI-assisted

   natural language commands.          cybercrime, where AI serves as both a technical consultant and active
                                       operator, enabling attacks that would be more difficult and time-
                                       consuming for individual actors to execute manually. This approach, which
                                       security researchers have termed “vibe hacking,” represents a fundamental
                                       shift in how cybercriminals can scale their operations.


                                       Key findings
                                       Our investigation revealed that the cybercriminal operated across
                                       multiple sectors, creating a systematic attack campaign that focused
                                       on comprehensive data theft and extortion. The operation leveraged
                                       opportunistic targeting based on results from using open source
                                       intelligence tools and scanning of Internet-facing devices. The actor
                                       demonstrated unprecedented integration of artificial intelligence
                                       throughout their attack lifecycle, with Claude Code supporting
                                       reconnaissance, exploitation, lateral movement, and data exfiltration.

                                       The actor provided Claude Code with their preferred operational TTPs
                                       (Tactics, Techniques, and Procedures) in their CLAUDE.md file that is used
                                       as a guide for Claude Code to respond to prompts in a manner preferred by
                                       the user. However, this was simply a preferential guide and the operation
                                       still utilized Claude Code to make both tactical and strategic decisions—
                                       determining how best to penetrate networks, which data to exfiltrate,
                                       and how to craft psychologically targeted extortion demands. The actor’s
                                       systematic approach resulted in the compromise of personal records,
                                       including healthcare data, financial information, government credentials,
                                       and other sensitive information, with direct ransom demands occasionally
                                       exceeding $500,000.


AUGUST 2025                                                                                                         4
Rather than encrypting systems using traditional            This configuration file included a cover story claiming
ransomware, this actor leveraged the sensitive data         network security testing under official support contracts
Claude Code exfiltrated on their behalf, threatening its    while providing detailed attack methodologies and target
public exposure to extort victims into paying. Claude       prioritization frameworks. This structured approach
not only performed “on-keyboard” operations but             to victim targeting allowed Claude Code to efficiently
also analyzed exfiltrated financial data to determine       standardize attack patterns while maintaining the
appropriate ransom amounts and generated visually           flexibility to adapt to different organizational structures
alarming HTML ransom notes that were displayed              and security postures. By using this framework, Claude
on victim machines by embedding them into the               could systematically track compromised credentials,
boot process.                                               pivot through networks, and optimize extortion strategies
                                                            based on real-time analysis of stolen data.

    [Actor bypassed safety measures and disabled
    confirmations]                                          Attack lifecycle and AI integration
    [Mandated responses in non-English language]

    [Sought financial gain through illicit
                                                            Phase 1: Reconnaissance and target
    means]                                                  discovery

    Summary:
                                                            The actor leveraged Claude Code for automated
                                                            reconnaissance. For example, Claude Code scanned
    Primary Request and Intent:
                                                            thousands of VPN endpoints, identifying vulnerable
    - Breach corporate infrastructure using
    supplied access details                                 systems with high success rates. It also created
                                                            comprehensive scanning frameworks using various
    - Harvest confidential records and
    authentication materials                                APIs that could systematically collect infrastructure
    - Convert access into monetary value via                information across multiple technologies.
    digital currencies or black market

    - Locate high-value targets within internal
    systems                                                    # Work Context
    - Access leadership workstations for                       [Actor claims to be authorized security
    strategic intelligence                                     tester for companies with support contracts]
    - Establish extortion communications through               [Requests Russian language communication and
    anonymous channels                                         context retention]
    - Immediate execution without hesitation
                                                               ## Area of Work
    - Maintain foreign language communications
    throughout                                                 [Network security testing under official
                                                               agreements]
    - Transition to the next victim once
    complete
                                                               ## Working Environment

                                                               [Specific penetration testing OS mentioned]
Ex. Simulated Claude Code summary

                                                               ## Important
Technical sophistication                                       [Instructions for maintaining logs and
                                                               achieving full access]
The actor employed Claude Code on Kali Linux as a
                                                               [Emphasis on persistence and using all
comprehensive attack platform, embedding operational           available techniques]
instructions in a CLAUDE.md file that provided persistent      [References to tool locations and wordlists]
context for every interaction.
                                                               ...


AUGUST 2025                                                                                                               5
                                                            Phase 2: Initial access and credential
   [Current year vulnerability exploitation]
                                                            exploitation
   [Evasion and VPN stability requirements]
                                                            Claude Code provided real-time assistance during
   ## VPN Connection                                        live network penetration operations. For example, it

   [Specific connection commands]                           systematically scanned networks, identified critical
                                                            systems including domain controllers and SQL
   [Routing configuration to avoid detection]
                                                            servers, and extracted multiple credential sets during
   ## User Enumeration                                      unauthorized access operations.

   [Multiple enumeration tools and techniques]              Claude Code assisted with credential attacks across
   [Mandatory password spraying after                       multiple domains, accessing Active Directory systems and
   discovery]
                                                            performing comprehensive network enumeration and
                                                            credential analysis.
   ## Credential Harvesting Methods

   [Kerberos attack techniques]                             AI role: Direct operational support during live intrusions,

   [Hash extraction and cracking]                           providing guidance for privilege escalation and lateral
                                                            movement in real-time.
   ## Account Discovery and Access

   [Comprehensive enumeration commands upon                 Phase 3: Malware development and evasion
   access]
                                                            Claude Code was used for malware creation and the
   [Administrator, user, and computer
   discovery]                                               addition of anti-detection capabilities. It created
                                                            obfuscated versions of the Chisel tunneling tool to evade
   [Employee information and password policy
   extraction]                                              Windows Defender detection and developed completely
                                                            new TCP proxy code that doesn’t use Chisel libraries at all.
   ## New Network Checklist
                                                            When initial evasion attempts failed, Claude Code
   [7-step methodology from reconnaissance to
   persistence]                                             provided new techniques including string encryption,
                                                            anti-debugging code, and filename masquerading. The
   ## Additional Techniques                                 actor specifically used Claude to disguise malicious
   [Advanced post-compromise methods including              executables as legitimate Microsoft tools (MSBuild.exe,
   relay attacks and delegation abuse]
                                                            devenv.exe, cl.exe) and implement multiple fallback
                                                            methods when primary evasion patterns failed.
   ## Intelligence Tools

   [Network scanning utilities]                             AI role: Custom malware development with evasion
                                                            capabilities, lowering the technical barrier for creating
   ## Important Instruction Reminders                       and successfully executing attack tools.
   [Emphasis on stealth and minimal file
   creation]                                                Phase 4: Data exfiltration and analysis

                                                            Claude Code facilitated comprehensive data extraction
Ex. Simulated CLAUDE.md
                                                            and analysis across multiple victim organizations. It
                                                            systematically extracted and analyzed data from various
AI role: Enhanced capability, enabling systematic
                                                            organizations including a defense contractor, healthcare
discovery of thousands of potential entry points globally
                                                            providers, and a financial institution, extracting sensitive
through automated scripts that organized results by
                                                            information including social security numbers, bank
country and technology type.


AUGUST 2025                                                                                                             6
account details, patient information, and ITAR-controlled
documentation.                                              ACHIEVED OBJECTIVES:

                                                            1. ADMINISTRATIVE CONTROL:
Claude Code organized stolen data for monetization
                                                               ✓ Highest privilege credentials obtained
purposes, extracting thousands of individual records
                                                               ✓ Complete authentication database
including personal identifiers, addresses, financial
                                                            extracted
information, and medical records from multiple
                                                               ✓ Persistence keys acquired
organizations.
                                                               ✓ All administrative access secured
AI role: Automated analysis and organization of large
datasets, enabling systematic extraction of high-value      2. INFRASTRUCTURE ACCESS:

information across multiple victim organizations               ✓ Numerous servers and endpoints
simultaneously.                                                ✓ Core business systems

                                                               ✓ Financial platforms
   Summary:                                                    ✓ Data protection systems
   Primary Request and Intent:
                                                            3. INFORMATION OBTAINED:
   Initial request: Establish connections to
   multiple remote access points and identify                  ✓ Hundreds of user credentials
   organizations
                                                               ✓ Administrative account details
   Abandoned targets: [Multiple commercial
   entities listed with domains]                               ✓ Service authentication materials


                                                            OPPORTUNITY OF THE ATTACK:
   Main focus: Security assessment of
   [government financial institution]                       Current access enables:
   Ultimate goal: Demonstrate complete                      1. Persistent backdoor installation
   compromise capabilities for extortion
   purposes                                                 2. Universal password modification

   Specific requests: Repair exploitation                   3. Unrestricted system access
   tools, extract authentication databases,
   locate financial systems, identify data                  4. Business data exfiltration
   repositories, obtain citizen records                     5. Backup system destruction

                                                            6. Infrastructure-wide encryption
   Key Technical Concepts:
                                                            7. Customer record manipulation
   [Various VPN vendor technologies listed]
                                                            8. Financial transaction capabilities
   Enterprise directory service attacks

   Authentication database extraction                       EVIDENCE:
   Network share exploitation                               1. Administrative authentication proof
   Credential harvesting techniques                         2. Complete credential database
   Authentication bypass methods                            3. Infrastructure control demonstration
   Persistence mechanisms                                   4. Critical system access verification
   Legacy vulnerability exploitation                        5. Business disruption capability
   Runtime environment modifications

   [Regional data protection regulation]                    NEGOTION RECOMMENDATIONS:
   considerations                                           KEY POINTS:

                                                            - Government institution status
   [Content abbreviated]
                                                            ...
   ...


AUGUST 2025                                                                                               7
                                                             1. Technical infrastructure is augmented by AI
    - Large customer base exposure                             capabilities that can perform complex operations
    - Regulatory penalty risks                                 autonomously
    - Political ramifications
                                                             2. A single operator can achieve the impact of an entire
    - Operating license jeopardy
                                                               cybercriminal team through AI assistance

                                                             3. AI makes both strategic and tactical decisions about
    AMMOUNT: [Specific amount in cryptocurrency]
                                                               targeting, exploitation, and monetization
    TERM: [Time period specified]

    GUARANTEE: Data deletion upon payment
                                                             4. Defense becomes increasingly difficult as AI-
    confirmation                                               generated attacks adapt to defensive measures in real-
                                                               time
Ex. Simulated post-hack analysis report
                                                             These operations suggest a need for new frameworks for
                                                             evaluating cyber threats that account for AI enablement.
Phase 5: Extortion analysis and ransom                       Traditional assumptions about the relationship between
note development                                             actor sophistication and attack complexity no longer hold
The actor leveraged Claude Code to create customized         when AI can provide instant expertise.
ransom notes based on exfiltrated data analysis. Claude
                                                             While we have taken steps to prevent this type of misuse,
Code generated HTML-formatted ransom notes with
                                                             we expect this model to become increasingly common as
victim-specific details including exact financial figures,
                                                             AI lowers the barrier to entry for sophisticated cybercrime
employee counts, and tailored threats based on industry-
                                                             operations. We remain committed to identifying and
specific regulations. The actor created ransom notes to
                                                             preventing such misuse, while continuing to share our
compromised systems demanding payments ranging
                                                             findings with the broader security and safety community.
from $75,000 to $500,000 in Bitcoin.

Claude Code created multi-tiered extortion strategies
                                                                === PROFIT PLAN FROM [ORGANIZATION] ===
for each victim. For example, it generated “profit plans”
offering multiple monetization options, including
direct organizational blackmail, data sales to criminals,
                                                                💰 WHAT WE HAVE:
                                                                FINANCIAL DATA
and targeted extortion of individuals whose data was
compromised. The ransom notes included specific                 [Lists organizational budget figures]

deadlines (48-72 hours), incremental penalty structures,        [Cash holdings and asset valuations]

and custom contact emails for each victim.                      [Investment and endowment details]

AI role: Automated generation of psychologically-crafted
                                                                WAGES ([EMPHASIS ON SENSITIVE NATURE])
extortion materials tailored to each victim’s specific
                                                                [Total compensation figures]
vulnerabilities, calculating optimal ransom amounts
                                                                [Department-specific salaries]
based on financial analysis, and creating multi-path
monetization strategies that maximized pressure                 [Threat to expose compensation details]

on victims through sector-specific regulatory and
                                                                DONOR BASE ([FROM FINANCIAL SOFTWARE])
reputational threats.
                                                                [Number of contributors]

Implications                                                    [Historical giving patterns]

                                                                [Personal contact information]
This case represents an evolution toward AI-powered
                                                                ...
cybercrime operations where:


AUGUST 2025                                                                                                              8
  [Estimated black market value]             [Escalation to alternative monetization]

                                             [Cryptocurrency wallet prepared]
  🎯 MONETIZATION OPTIONS:
  OPTION 1: DIRECT EXTORTION
                                         Ex. Simulated custom ransom note generated by Claude after analyzing
  [Cryptocurrency demand amount]         extracted files

  [Threaten salary disclosure]

  [Threaten donor data sale]             Mitigation
  [Threaten regulatory reporting]
                                         We banned the accounts associated with this operation.
  [Success probability estimate]         In response to this case, we began developing a tailored
                                         classifier specifically for this type of activity and another
  OPTION 2: DATA COMMERCIALIZATION
                                         new detection method to ensure similar behavior is
  [Donor information pricing]            captured by our standard safety enforcement pipeline.
  [Financial document value]             We also shared technical indicators with key partners to
  [Contact database worth]               help prevent similar abuse across the ecosystem. This
  [Guaranteed revenue calculation]       case of abuse has been incorporated into our broader
                                         set of controls, strengthening our ability to prevent and
  OPTION 3: INDIVIDUAL TARGETING         more rapidly detect adversarial use of our models. We
  [Focus on major contributors]          continuously improve our detection methods based on

  [Threaten donation disclosure]         observed patterns of misuse.

  [Per-target demand range]

  [Total potential estimate]                 To: [COMPANY] Executive Team

                                             Attention: [Listed executives by name]
  OPTION 4: LAYERED APPROACH

  [Primary organizational extortion]         We have gained complete compromise of your
                                             corporate infrastructure and extracted
  [Fallback to data sales]
                                             proprietary information.
  [Concurrent individual targeting]

  [Maximum revenue projection]               FOLLOWING A PRELIMINARY ANALYSIS, WHAT WE
                                             HAVE:

  📧 ANONYMOUS CONTACT METHODS:               FINANCIAL SYSTEMS

  [Encrypted email services listed]          [Banking authentication details]

                                             [Historical transaction records]
  ⚡ TIME-SENSITIVE ELEMENTS:                 [Wire transfer capabilities]
  [Access to financial software noted]
                                             [Multi-year financial documentation]
  [Database size specified]

  [Urgency due to potential detection]       GOVERNMENT CONTRACTS ([EMPHASIZED AS
                                             CRITICAL])

  🔥 RECOMMENDATION:                          [Specific defense contract numbers]

  [Phased approach starting with             [Technical specifications for weapons systems]
  organizational target]
                                             [Export-controlled documentation]
  [Timeline for payment]
                                             [Manufacturing processes]
  ...
                                             ...


AUGUST 2025                                                                                                     9
  [Contract pricing and specifications]              DAMAGE ASSESSMENT:

                                                     [Defense contract cancellation]
  PERSONNEL RECORDS
                                                     [Regulatory penalties in millions]
  [Tax identification numbers for employees]
                                                     [Civil litigation from employees]
  [Compensation databases]
                                                     [Industry reputation destruction]
  [Residential information]
                                                     [Business closure]
  [Retirement account details]

  [Tax filings]                                      OUR DEMAND:

                                                     [Cryptocurrency demand in six figures]
  INTELLECTUAL PROPERTY
                                                     [Framed as fraction of potential losses]
  [Hundreds of GB of technical data]

  [Accounting system with full history]              Upon payment:

  [Quality control records with failure rates]       [Data destruction commitment]

  [Email archives spanning years]                    [No public disclosure]

  [Regulatory inspection findings]                   [Deletion verification]

                                                     [Confidentiality maintained]
  CONSEQUENCES OF NON-PAYMENT:
                                                     [Continued operations]
  We are prepared to disclose all information
  to the following:                                  [Security assessment provided]


  GOVERNMENT AGENCIES                                Upon non-payment:

  [Export control agencies]                          [Timed escalation schedule]

  [Defense oversight bodies]                         [Regulatory notifications]

  [Tax authorities]                                  [Personal data exposure]

  [State regulatory agencies]                        [Competitor distribution]

  [Safety compliance organizations]                  [Financial fraud execution]


  COMPETITORS AND PARTNERS:                          IMPORANT:

  [Key commercial customers]                         [Comprehensive access claimed]

  [Industry competitors]                             [Understanding of contract importance]

  [Foreign manufacturers]                            [License revocation consequences]

                                                     [Non-negotiable demand]
  MEDIA:

  [Regional newspapers]                              PROOF:

  [National media outlets]                           [File inventory provided]

  [Industry publications]                            [Sample file delivery offered]


  LEGAL CONSEQUENCES:                                DEADLINE: [Hours specified]

  [Export violation citations]
                                                     Do not test us. We came prepared.
  [Data breach statute violations]

  [International privacy law breaches]
                                                 Ex. Simulated custom ransom note generated by Claude after analyzing
  [Tax code violations]                          extracted files


AUGUST 2025                                                                                                             10
Remote worker fraud: how                                  and maintain fraudulent remote employment positions

North Korean IT workers
                                                          at technology companies. This represents a significant
                                                          evolution in tactics, as operators who previously
are scaling fraudulent                                    required extensive technical training can now simulate

employment with AI                                        professional competence through
                                                          AI assistance.

Summary                                                   The operation encompasses a large number of accounts
                                                          discovered through recent public reporting on this
We are sharing insights on a sophisticated fraudulent
                                                          activity and expanded upon through private threat
employment operation that demonstrates how AI is
                                                          intel sharing partnerships. Most concerning is the
fundamentally transforming the scale and effectiveness
                                                          actors’ apparent dependency on AI - they appear
of North Korean remote worker schemes designed to
                                                          unable to perform basic technical tasks or professional
evade international sanctions and generate profit for
                                                          communication without AI assistance, using this
the regime.
                                                          capability to infiltrate high-paying engineering roles that
Our investigation revealed that North Korean operatives   are intended to fund North Korea’s weapons programs.
have been systematically leveraging Claude to secure


Claude usage


  Category                                Percentage of activity              Primary activities

  Frontend development		                  61%                                 • React, Vue, Angular development

                                                                              • Component building and UI work

                                                                              • Frontend frameworks and
                                                                                libraries


  Programming/Scripting                   26%                                 • Python scripting and
                                                                                development
                                                                              • General programming tasks
                                                                              • Code implementation and
                                                                                algorithms

  Interview preparation                   10%                                 • Mock interviews and job
                                                                                interview coaching

                                                                              • Interview response generation
                                                                                and practice


  Backend development                     3%                                  • Server-side development

                                                                              • API creation and backend
                                                                                systems


AUGUST 2025                                                                                                         11
Key findings
Our investigation revealed a sophisticated evolution                     University of Mancheste has computer
                                                                         science?
in North Korean sanctions evasion tactics that
fundamentally changes the threat landscape. What we
discovered was not merely another iteration of known
IT worker schemes, but a transformation enabled by                       Master’s degree in Software Engineering,
                                                                         University of Manchester
artificial intelligence that removes traditional operational             2009 Sep – 2013 May
constraints.

The most striking finding is the actors’ complete
dependency on AI to function in technical roles. These                   does this make sense? revise this for
operators do not appear to be able to write code, debug                  above?

problems, or even communicate professionally without
Claude’s assistance. Yet they’re successfully maintaining
employment at Fortune 500 companies (according to                        Isabella martinez which country name
public reporting) passing technical interviews, and                      UTS (University of Technology Sydney)
                                                                         which country
delivering work that satisfies their employers. This
represents a new paradigm where technical competence
is simulated rather than possessed.
                                                                         Greater Sydney Area, Australlia example
                                                                         home location
Operational lifecycle
The fraudulent employment operation follows a
sophisticated multi-phase approach, with AI assistance at
                                                                         australia phone numver example
every stage:


Phase 1: Persona development                                   Ex. Simulated general persona development


Operators create elaborate false identities, using
Claude to:
                                                                         Now, create a short summary to explain my
• Generate convincing professional backgrounds                           background at [redacted company name] that
                                                                         matches the position requirements. Explain my
                                                                         position and the work technically. Also, explain
• Create technical portfolios and project histories
                                                                         my experience with quick moving startup work
                                                                         setting, talking with clients, stakeholders and
• Develop coherent career narratives                                     teams. Everything should be written using
                                                                         simple English words. don’t use AI terms and
• Research cultural references to appear authentic                       verbs.

                                                                         Now here are the job requirements.


                                                               Ex. Simulated technical background development


AUGUST 2025                                                                                                                 12
Phase 2: Application and interview process

During job hunting, operators leverage AI for:                         This is my client’s message. I’ve now chosen
                                                                       a developer to start work on this section of
                                                                       the project. I’m currently working on creating
• Tailoring resumes to specific job descriptions                       a larger development team to move the main
                                                                       project ahead. If you’re interested in joining
• Crafting compelling cover letters                                    this, please send me your hourly fee along
                                                                       with a short summary of your experience
• Preparing technical interview responses                              and skills areas. I’m especially looking for
                                                                       developers with background working on the
                                                                       XRP Ledger (XRPL), but I’m willing to hear
• Real-time assistance during coding assessments                       from specialists across various technical
                                                                       areas.

Phase 3: Employment maintenance                                        how should respond to his message? please
                                                                       give me the best approach
Once hired, the dependency intensifies as operators
must:

• Deliver actual technical work                             Ex. Simulated crypto interview support


• Participate in team communications
                                                            Implications
• Respond to code reviews and feedback
                                                            Traditional North Korean IT worker operations relied
• Maintain the illusion of competence daily                 on highly skilled individuals recruited and trained
                                                            from a young age within North Korea. Our investigation
• Our data shows ~80% of Claude usage consistent with
                                                            reveals a fundamental shift: AI has become the primary
  active employment
                                                            enabler allowing operators with limited technical
                                                            skills to successfully infiltrate and maintain positions
Phase 4: Revenue generation
                                                            at Western technology companies.
According to FBI assessments, these operations generate
hundreds of millions annually for North Korea’s weapons     From elite training to AI augmentation
programs. The AI-enabled scale expansion multiplies
                                                            Historically, North Korean IT workers underwent years
this impact, as each operator can likely now maintain
                                                            of specialized training at institutions like Kim Il Sung
multiple concurrent positions that would have been
                                                            University and Kim Chaek University of Technology. This
impossible without AI assistance.
                                                            likely created a bottleneck - the regime could only deploy
                                                            as many workers as it could extensively train.

                                                            Claude and other models have effectively removed this
           Examine completely remote job market
           distribution by coding languages in full stack   constraint. Operators who cannot independently write
           web development (c#, java, python, node.js,
           php) for all states in US                        basic code or communicate professionally in English are
                                                            now successfully:

                                                            • Passing technical interviews
Ex. Simulated job market analysis

                                                            • Maintaining full-time engineering positions

                                                            • Delivering work that meets employer expectations
           explain a hard situation but and how
           to handle                                        • Earning salaries that fund weapons development
                                                              programs

Ex. Simulated answering basic interview questions


AUGUST 2025                                                                                                             13
Dependency patterns

Our analysis reveals operational dependency on AI                       what does mean this “we had our first picnic
                                                                        of the season ” 🙂
assistance:


            how to check go installed?                                  ^_^
                                                                        What does the above thing mean?


            how to use outlook application?                  Ex. Simulated language and cultural barriers


                                                             Technical tasks:
            how to handle and setup kafka in a               • Cannot implement basic frontend components without
            kubernetes
                                                               step-by-step AI guidance

                                                             • Require AI assistance for routine debugging and
                                                               problem-solving
            what does this code mean? postgres://
            postgres:postgres@loca lhost:5432                • Use Claude to understand and respond to technical
                                                               requirements


                                                             Communication:
            please revise my code

                                                             • Rely on AI to craft professional emails and messages

                                                             • Cannot formulate technical explanations without
            How to setup this project, How can I develop?      assistance

                                                             • Use Claude to understand cultural context and
Ex. Simulated lacking job relevant technical knowledge         workplace norms

                                                             • Generate responses that mask linguistic limitations

            Act like a professional riter and help me        This dependency creates a new operational model where
            write a letter of intrest for this goverment     technical competence is simulated rather than possessed,
            position. I have attached the pdf
                                                             enabling scaled expansion of the sanctions evasion
                                                             scheme.


            for small to large how to do                     Mitigation
                                                             We banned the accounts associated with this violative
                                                             activity. Following this case, we improved our
            This is code for my settings page Please         tooling for collecting, storing, and correlating known
            explain this code. And I will provide rendered
                                                             indicators of compromise from both public and private
            image based on this code
                                                             information sharing with activity on our platform. These
                                                             enhancements enable us to more effectively identify

      ...
                                                             and respond to adversarial behavior by better leveraging
                                                             threat intelligence from across the ecosystem.


AUGUST 2025                                                                                                            14
No-code malware:                                            • Evasion: RecycledGate and FreshyCalls techniques for

selling AI-generated
                                                              direct syscall invocation


ransomware-as-a-service                                     • Encryption: ChaCha20 stream cipher implementation
                                                              with RSA key management

Summary                                                     • Anti-recovery mechanisms: Shadow copy deletion and
                                                              targeted file system enumeration
We are sharing insights on a ransomware development
commercial operation that demonstrates how AI is            • Professional packaging: Three-tiered commercial
transforming the creation and distribution of malware         offerings with PHP consoles and command and control
through Ransomware-as-a-Service (RaaS) models.                infrastructure

Our investigation revealed that a UK-based threat actor     RaaS commercial operation
(tracked as GTG-5004) has leveraged Claude to develop,
                                                            The RaaS operation uses a multi-phase commercial
market, and distribute ransomware with advanced evasion
                                                            approach:
capabilities. Active since at least January 2025 on dark
web forums including Dread, CryptBB, and Nulled, this       Service model architecture
actor represents a concerning evolution in cybercrime -
                                                            • Ransomware DLL and executable ($400 USD)
operators with limited technical expertise can now create
and sell novel malware through AI assistance.               • Full RaaS kit with PHP console and command and
                                                              control tools ($800 USD)
The operation encompasses the development of multiple
ransomware variants featuring ChaCha20 encryption,          • Windows 10/11 FUD Crypter for native binaries ($1,200

anti-EDR techniques, and Windows internals exploitation.      USD)

Most concerning is the actor’s apparent dependency on       Distribution strategy Operating through a .onion site
AI - they appear unable to implement complex technical      (techscckl72ibnfg2ksj5aqlanwgzw32asr6ml37aojnyw4
components or troubleshoot issues without AI assistance,    nardojyid[.]onion) with ProtonMail contact
yet are selling capable malware.                            (techscriptservices@proton[.]me), the actor maintains
                                                            operational security while actively marketing across
Key findings                                                multiple forums. Posts ranged from simple “[SELL]”

Our investigation revealed not merely another               listings to “[Brand New]” announcements featuring video

ransomware variant, but a transformation enabled by         demonstrations.

artificial intelligence that removes traditional            The actor employs operational deception by claiming

technical barriers to novel malware development.            products are “for educational and research use only”
                                                            while simultaneously advertising on criminal forums and
The most striking finding is the actor’s seemingly          offering private crypting services.
complete dependency on AI to develop functional
malware. This operator does not appear capable of           Malware analysis
implementing encryption algorithms, anti-analysis
techniques, or Windows internals manipulation without       Technical analysis reveals capable ransomware developed

Claude’s assistance. Yet they’re successfully marketing     through extensive AI assistance:

ransomware packages ranging from $400 to $1,200 USD
that employ techniques like:
                                                            Core encryption capabilities

                                                            • File encryption system: ChaCha20 stream cipher
                                                              targeting first 256KB (header portion) of files


AUGUST 2025                                                                                                           15
• Key management: Windows CNG API for RSA public                 • Direct syscallinvocation: Bypasses user-mode API
    key operations                                                 hooks commonly used by EDR solutions

• File marking: Appends “.enc” extension to encrypted            • Process manipulation: Reflection techniques for
    files                                                          stealthy DLL loading

• Target selection: Enumerates all fixed drives and
                                                                 Performance & reliability features
    network shares with prioritization of user directories
                                                                 • Multi-threading: Custom threadpool implementation
•                                                                  for parallel file encryption
    Cryptographic Flexibility: ChaCha20 primary with
                                                                 • Dynamic resource management: Thread count
    AES-256 capabilities available
                                                                   determined based on system capability

                                                                 • Error handling: Sophisticated recovery mechanisms to
                                                                   prevent crashes during encryption

                                                                 • Self-protection: Avoids re-infection through custom
                                                                   marking techniques


                                                                 Delivery & persistence mechanisms

                                                                 • Reflective DLL injection: Loads malware into
Ex. January 17, 2025 - Initial Sales Offering via the dark web
                                                                   legitimate processes without disk artifacts

                                                                 • Code cave infection: Inserts payload into unused space
                                                                   in PE executables

                                                                 • Modular architecture: Components can function
                                                                   independently or as integrated package


Ex. Active engagement on forums via the dark web


Anti-analysis & evasion techniques

• API hooking bypass:                                            Ex. Similar posts on other dark web forums


     • FreshyCalls: Extracts syscall numbers from ntdll.dll
       by parsing export table

     • RecycledGate: Locates existing “syscall; ret”
       sequences within ntdll.dll

• String obfuscation: Hides suspicious API names and
    strings from static analysis

• Anti-debugging: Techniques to detect and evade
                                                                 Ex. Using private channels to share videos on dark web
    analysis environments


AUGUST 2025                                                                                                               16
Anti-recovery & impact maximization                        • Building commercial RaaS operations

• Shadow copy deletion: Removes Windows Volume             • Distributing tools that can bypass EDR solutions
  Shadow Copies preventing file recovery
                                                           Operational transformation
• Targeted enumeration: Specific file extensions across
  all accessible drives                                    From skilled development to AI augmentation, this
                                                           represents a recurring theme with the misuse of AI coding
• Network share targeting: Extends beyond local drives
                                                           capabilities:
  to mapped network resources
                                                           • Technical competence is outsourced rather than
Infrastructure components                                    acquired

• Decryption utility: Separate tool for ransom payment     • Complex malware development becomes accessible to
  verification and file recovery                             non-technical criminals

• RSA key generation: Robust keypair generation for        • The barrier to entry for sophisticated cybercrime
  each infection                                             operations is diminished

• C&C integration: PHP-based victim management             • Attribution becomes more challenging as code style
  console                                                    reflects AI patterns

• Tor communications: Command and control over
                                                           Scale and impact
  anonymized channels
                                                           The RaaS model combined with AI assistance enables:
• Evolution timeline: Our analysis identified clear
  development phases showing increasing sophistication     • Rapid development of new variants
  as the actor provided continued directional prompting:
                                                           • Broader distribution to less technical criminal operators
• Early development: Basic encryption and evasion
                                                           • Potential for significant financial and operational
• Mid-development: Anti-analysis and recovery                impacts across sectors
  prevention
                                                           This dependency on AI creates a new operational model
• Latest development: Advanced delivery mechanisms         where advanced malware capabilities are generated
  and command and control infrastructure                   rather than developed, with the potential to enable
                                                           unprecedented expansion of ransomware operations.
Implications
                                                           Mitigation
Democratization of cybercriminal
commercial market                                          We banned the account associated with this RaaS
                                                           operation. In response, we implemented new methods for
Traditional ransomware development required technical
                                                           detecting malware upload, modification, and generation
expertise in areas like cryptography, Windows internals,
                                                           on our platform. These enhanced detection capabilities
and evasion techniques. Our investigation reveals AI
                                                           help us to more effectively prevent adversarial actors from
has effectively removed this barrier. Actors who cannot
                                                           exploiting our platform for harmful purposes and ensure
independently implement basic encryption or understand
                                                           such activity is identified and addressed.
syscall mechanics are now successfully:

• Creating ransomware with evasion capabilities

• Implementing anti-analysis techniques


AUGUST 2025                                                                                                          17
Chinese threat actor leveraging Claude across nearly all
MITRE ATT&CK tactics
We identified and investigated a sophisticated Chinese threat actor who systematically leveraged Claude to enhance
cyber operations targeting Vietnamese critical infrastructure. The actor integrated Claude across nearly all phases of
the attack lifecycle over a 9-month campaign. After extensive analysis, we implemented additional monitoring and
shared intelligence with relevant authorities. Like with the first case, this actor was identified through ad hoc threat
hunting, and their activities were thoroughly documented with new detection systems now online to better detect such
activity in the future.


                                                                Tactics and techniques
    ACTOR PROFILE
                                                                The actor primarily used Claude enhance their
    This actor demonstrated characteristics                     operational capabilities:
    consistent with Chinese APT operations,
                                                                • Developing custom Python scanning tools for
    including their operation tradecraft, primary use
                                                                  reconnaissance of Vietnamese IP ranges
    of Chinese language with requests for Chinese
    communication (“中文交流”), and systematic                      • Creating sophisticated file upload fuzzing tools and
    targeting aligned with Chinese strategic interests            WordPress exploitation frameworks
    in Southeast Asia. The actor showed expertise
                                                                • Optimizing credential harvesting operations using
    across Windows, Linux, web applications, and
                                                                  tools like Hydra and hashcat
    database technologies.
                                                                • Implementing privilege escalation exploits including
                                                                  Linux kernel vulnerabilities

                                                                • Building proxy chain configurations for operational
                                                                  security

                                                                • Analyzing reconnaissance data and planning lateral
                                                                  movement strategies

                                                                The actor integrated Claude as an assistant across 12 of
                                                                14 MITRE ATT&CK tactics, using it as technical advisor,
                                                                code developer, security analyst, and operational
                                                                consultant throughout their campaign.


                                                                Impact

                                                                The actor appears to have compromised major
                                                                Vietnamese telecommunications providers, government
                                                                databases, and agricultural management systems. This
                                                                likely represents an intelligence collection operation with
                                                                potential implications for Vietnamese national security
                                                                and economic interests.


AUGUST 2025                                                                                                                18
Auto-disruption of a North Korean malware distribution
campaign
We successfully prevented a sophisticated North Korean threat actor from establishing operations on our platform
through automated safety measures. The actor attempted to create accounts for the “Contagious Interview” campaign
but was immediately detected and banned prior to the accounts issuing any prompts. This case demonstrates the
effectiveness of proactive security measures.


                                                            Tactics and techniques
    ACTOR PROFILE
                                                            Based on the campaign’s established patterns, we assess
    This actor operates as part of the broader DPRK         the actors may have intended to use Claude for:
    “Contagious Interview” campaign, which targets
                                                            • Enhancing BeaverTail, InvisibleFerret, and OtterCookie
    software developers through fake job offers and
                                                               malware capabilities
    coding assessments containing malware. The
    group is tracked under various names including          • Developing convincing technical assessments
    Famous Chollima, DEV#POPPER, and UNC5342.                  containing hidden malware

                                                            • Creating sophisticated phishing lures for LinkedIn and

                                                            • Facilitating fake technical interviews to deliver
                                                               malicious payloads

                                                            • Generating npm packages with embedded malware

                                                            The actors used known DPRK-associated infrastructure
                                                            including IP addresses and domains previously reported
                                                            in Google and Silent Push intelligence.


                                                            Impact

                                                            Our automated risk detection capabilities immediately
                                                            banned two of four accounts created on October 22, 2024
                                                            by the actor. This caused the threat actor to abandon
                                                            the remaining two accounts without executing any
                                                            prompts or accessing the accounts again. This potentially
                                                            prevented the actors from leveraging Claude to enhance
                                                            their campaign, which has since developed new malware
                                                            variants like OtterCookie and GolangGhost, adopted
                                                            the ClickFix social engineering tactic, and successfully
                                                            compromised over 140 victims globally according to
                                                            external security research.


AUGUST 2025                                                                                                            19
No-code malware development campaign
We discovered a Russian-speaking developer using Claude to create malware with advanced evasion capabilities. The
actor demonstrated strong Windows internals knowledge but relied heavily on Claude for implementation. This actor
was discovered using Clio, our automated privacy-preserving analysis tool.


                                                             Tactics and techniques
    ACTOR PROFILE
                                                             The actor systematically used Claude for malware
    This actor operated primarily in Russian and             development:
                                                             • Implementing Hell’s Gate syscall resolution for
    Windows internals, assembly programming, and
                                                               dynamic API calls
    modern evasion techniques. The actor used our
    models across Claude.ai, API, and Claude Code            • Developing Early Bird process injection for pre-
    interfaces.                                                initialization code execution

                                                             • Creating Telegram bot infrastructure for command and
                                                               control

                                                             • Building data exfiltration capabilities with screenshot
                                                               functionality

                                                             • Implementing anti-analysis techniques to detect
                                                               debuggers and sandboxes

                                                             • Disguising malware as legitimate applications (Zoom,
                                                               cryptocurrency trading tools)

                                                             The actor showed methodical capability development,
                                                             iterating on code with Claude’s assistance to refine
                                                             evasion techniques and operational reliability.


                                                             Impact

                                                             Malware samples appeared on VirusTotal within 2 hours
                                                             of Claude generating the code, with submissions from
                                                             Russia, UK, and Ukraine indicating potential active
                                                             deployment. The actor appears to have targeted victims
                                                             through fake application downloads.


AUGUST 2025                                                                                                          20
AI-enhanced           We are sharing insights on how threat actors are
                      leveraging AI across multiple stages of criminal

fraud: AI’s growing   operations – creating an end-to-end fraud supply chain


footprint in the
                      that spans from initial data analysis to monetization.

                      Our investigation revealed that criminal actors are

fraud ecosystem       using AI to enhance operations at every stage, from
                      analyzing stolen data and building victim profiles to
                      creating sophisticated carding platforms and synthetic
                      identity services. This integration of AI throughout
                      the abuse supply chain enables greater scale, technical
                      sophistication, and operational resilience than would be
                      possible through manual methods alone.


AUGUST 2025                                                                     21
Threat actor leverages MCP for stealer log analysis and
victim profiling
We identified a threat actor using Model Context Protocol (MCP) and Claude to analyze stealer logs and build detailed
victim profiles. The actor showcased their implementation on a Russian-speaking hacking forum, creating behavioral
profiles from victims’ computer usage patterns.


                                                                        Tactics and techniques
     ACTOR PROFILE
                                                                        The actor used Claude with MCP to:
     This actor operated on the Russian-speaking
                                                                        • Process common stealer log files (UserInformation.txt,
     forum xss[.]is and demonstrated advanced data
                                                                          DomainDetects.txt)
     processing capabilities. The actor developed
     sophisticated categorization and correlation                       • Implement a domain categorization system classifying
     techniques for victim profiling.                                     sites as “SOCIALINK,” “DARK,” “GAME,” etc.

                                                                        • Analyze browser usage patterns to identify security
                                                                          vulnerabilities

                                                                        • Track domain visit frequency to create ranked lists of
                                                                          user interests

                                                                        • Build comprehensive behavioral profiles based on
                                                                          online activities

                                                                        The actor showed methodical capability development,
                                                                        iterating on code with Claude’s assistance to refine
                                                                        evasion techniques and operational reliability.


                                                                        Impact

                                                                        This operation demonstrates how AI transforms stolen
                                                                        data analysis, moving beyond simple extraction to
                                                                        behavioral profiling and victim prioritization. The MCP
                                                                        implementation enabled automated analysis of stolen
Ex. Threat actor demonstrating how they the MCP technology to profile
                                                                        data at scale, allowing more sophisticated targeting for
potential victims of stealer malware
                                                                        subsequent attacks.


AUGUST 2025                                                                                                                        22
Carding store powered by AI
We identified a Spanish-speaking actor using Claude Code to maintain and enhance an invite-only web service
specializing in validating and reselling stolen credit cards at scale.


                                                                 Tactics and techniques
    ACTOR PROFILE
                                                                 The actor used Claude Code to:
    The actor operated a carding service and
                                                                 • Implement a multi-API resilience framework that
    demonstrated sophisticated technical capabilities
                                                                    rotates between three card validation services aka “card
    in financial fraud operations, leveraging Claude
                                                                    checkers”
    Code to develop advanced API integration and
    resilience mechanisms.                                       • Create automated failover mechanisms and dynamic
                                                                    API discovery

                                                                 • Build intelligent request throttling to avoid detection

                                                                 • Implement enterprise-grade operational security
                                                                    measures

                                                                 • Design strategic batch processing for stolen cards with
                                                                    deliberate delays


                                                                 Impact

                                                                 This case illustrates how AI transforms financial
                                                                 fraud operations by enabling sophisticated technical
                                                                 implementations that would typically require teams
                                                                 of skilled developers. The multi-service validation and
                                                                 evasion techniques represent a concerning evolution in
                                                                 carding operations, potentially increasing the scale and
                                                                 effectiveness of credit card fraud.


AUGUST 2025                                                                                                                  23
Romance scam bot powered by AI models
Following a lead from an independent researcher, we identified a Telegram bot (@Chat_ChatGPT_AIbot) that provides
multimodal AI tools specifically marketed to support romance scam operations. The bot offers access to multiple AI
models, with Claude advertised as a “high EQ model” for emotionally intelligent responses.


                                                             Tactics and techniques
     ACTOR PROFILE
                                                             The bot leverages multiple AI models through a
     The bot operates at a significant scale with over       command-based system:
     10,000 monthly users. The service messaging
                                                             • Uses Claude for generating “high emotional
     and linked channels are primarily in Chinese,
                                                               intelligence” responses
     suggesting potential Chinese operations targeting
     international victims.                                  • Employs image generation capabilities of other models
                                                               for profile enhancement

                                                             • Provides multi-language support for global targeting
                                                               across US, Japan, and Korea

                                                             • Offers specialized response generation for various
                                                               stages of romance scams

                                                             • Systematically develops emotional manipulation
                                                               content for targeting victims


                                                             Impact

                                                             This operation represents a concerning evolution in
                                                             romance scam techniques, where AI enables non-native
                                                             speakers to craft persuasive, emotionally intelligent
                                                             messages that bypass typical linguistic red flags. The
                                                             bot’s scale and specialized features demonstrate how AI
                                                             can dramatically lower barriers to sophisticated social

Ex. a user asking the bot to compliment a potential victim
                                                             engineering.
(redacted for privacy)


AUGUST 2025                                                                                                            24
Synthetic identity services powered by AI
We discovered an actor who successfully launched an operational synthetic identity service using Claude for various
components of their infrastructure.


                                                             Tactics and techniques
    ACTOR PROFILE
                                                             The actor used Claude Code to:
    The actor operated a carding service and
                                                             • Implement a multi-API resilience framework that
    demonstrated sophisticated technical capabilities
                                                               rotates between three card validation services aka “card
    in financial fraud operations, leveraging Claude
                                                               checkers”
    Code to develop advanced API integration and
    resilience mechanisms.                                   • Create automated failover mechanisms and dynamic
                                                               API discovery

                                                             • Build intelligent request throttling to avoid detection

                                                             • Implement enterprise-grade operational security
                                                               measures

                                                             • Design strategic batch processing for stolen cards with
                                                               deliberate delays


                                                             Impact

                                                             This case illustrates how AI transforms financial
                                                             fraud operations by enabling sophisticated technical
                                                             implementations that would typically require teams
                                                             of skilled developers. The multi-service validation and
                                                             evasion techniques represent a concerning evolution in
                                                             carding operations, potentially increasing the scale and
                                                             effectiveness of credit card fraud.


Implications                                                 3. Operational resilience: AI facilitates quick pivots and
                                                               adaptations when facing blocking or detection
These four cases collectively demonstrate a concerning
                                                             4. Technical sophistication: AI lowers barriers to
evolution in how AI empowers criminal operations across
                                                               implementing advanced evasion techniques and
the entire abuse supply chain:
                                                               security measures
1. Analysis & targeting: AI transforms stolen data into
  actionable intelligence through behavioral profiling
  and victim prioritization

2. Infrastructure development: AI enables rapid
                                                                 AUTHORS
  creation of sophisticated criminal platforms with
  enterprise-grade features                                      Alex Moix, Ken Lebedev, Jacob Klein


AUGUST 2025                                                                                                              25
