---
title: "UST is bringing Claude to physical AI \\ Anthropic"
source_url: "https://www.anthropic.com/news/ust-claude"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:01Z"
tags: ["news-research"]
---

# UST is bringing Claude to physical AI

Jul 9, 2026

Before a factory commits to manufacturing millions of chips, engineers stress-test the design in the fab. Before a product ships, a fault on the assembly line has to be caught before it becomes a recall. When AI does this kind of work, it’s called physical AI: intelligence built into the equipment and engineering processes that produce the things people use.

We’re partnering with [UST](https://www.ust.com/), a technology and engineering services company that builds and runs the engineering environments its clients depend on to get chips, cars, and connected devices to market. UST is putting Claude to work inside those environments, and training 20,000 of its engineers, architects, and consultants on Claude worldwide.

### **How UST is putting Claude into the production processes behind physical products**

UST works alongside semiconductor, automotive, manufacturing, telecom, embedded, and IoT companies. It builds the systems those companies use to verify their designs, validate their chips, run their factories, and service their products once they’re out in the world.

These are long, multi-step processes where an early mistake gets more expensive with every step that follows. A design flaw caught during verification costs an engineer an afternoon; the same flaw caught after a factory has committed to manufacturing costs a production run.

UST is bringing Claude into this work. Claude Code reads the schematics and pinouts an engineer works from, then writes and runs the tests that check the design. It carries that task across many steps, holding the context of a design through hours-long tasks. UST is aiming to catch design flaws earlier, speed up chip validation, and bring hardware and software together in a single system.

The clearest example is a UST platform called iDEC, which its engineers use to validate hardware and silicon before it goes to production. Validation is the work of proving a chip actually behaves the way its designers intended, and it’s arduous: engineers write test scripts by hand, run them, read the results, and repeat the cycle many times over. UST reports that iDEC’s closed-loop pipeline,reads hardware designs, generates and runs regression tests, and compares live equipment data against its digital twin to flag issues early, already cuts validation cycle times by 50 to 70%, condensing standard four-day turnarounds into 48 hours.

UST is now integrating Claude into that pipeline as its reasoning layer. Claude Code reads chip pinouts and hardware schematics directly, then writes and runs regression tests—the checks that confirm a change to a design didn’t cause an unintended downstream effect—which engineers used to script by hand. Claude also compares the live data from real equipment against its digital twin—the software model of how that hardware is supposed to behave—and flags firmware regressions and signal-integrity faults. UST’s goal is to make its pipeline even faster, with less hand scripting and earlier fault detection, and no new tools for engineers to learn.

“Our alliance with Anthropic reflects UST’s unwavering commitment to helping clients navigate the AI landscape with confidence and achieve meaningful business outcomes. By combining the capabilities of Claude with UST’s engineering, industry knowledge, and delivery expertise, we are bringing to market industry-specific platforms and digital and engineering solutions that improve productivity, accelerate business outcomes, and help clients operationalize AI-led decisions in a safe and secure environment,” said Krishna Sudheendra, Chief Executive Officer, UST.

“UST helps the world’s banks, telecoms, and manufacturers put new technology to work. They’re proving Claude inside their own engineering first, and training 20,000 of their own people on it, before bringing it into the systems they build and run for clients,” said Paul Smith, Chief Commercial Officer, Anthropic.

### **How UST is putting Claude into healthcare, telecom, and banking systems**

UST is bringing Claude into three other platforms it operates for clients:

- **In healthcare**, insurers and providers use UST CarePath to run member services, care management, and claims. Claude connects CarePath directly to its underlying claims and care systems, and turns scattered health data into clear next steps for care teams. Every recommended action routes to a person for approval before it reaches a member, and it stays inside the data controls healthcare requires.
- **In telecom**, UST IntelliOps runs network operations. To keep networks up and running, teams work through the alerts that spot problems and outages, but this is a time-consuming process. Claude now helps operators spot service issues, predict failures in the radio access network (the towers and antennas that connect phones to the network), and shorten outages through response workflows, which a person still approves. For the teams watching the alerts, that means less time separating real problems from noise.
- **In banking**, most mid-sized institutions still run on core systems old enough that the ledger updates once a night rather than in real time. Banks often license these systems rather than own them, so every new product or integration means months of waiting for a vendor to make the change. UST FinX helps banks modernize progressively by solving immediate business and operational challenges while reducing the dependency on disruptive, high-risk transformation programs. FinX will use Claude to embed AI agents directly into bank workflows and processes, supporting both operations teams and customers through intelligent case handling, servicing automation, knowledge retrieval, workflow assistance, and decision support.

### **A partnership in AI adoption and training**

UST is committing to train 20,000 of its associates on Claude worldwide, including engineers, architects, consultants, industry specialists, and forward-deployed engineers, who sit alongside client teams. It’s also building specialized teams to deploy Claude. We’re supporting UST in this effort with enablement, technical guidance, and certification through the Claude Partner Network. This partnership also makes UST a Global Premier Partner in the Claude Partner Network.

### **Pairing reliability, safety, and governance**

The industries UST serves are extremely high-stakes. Human approval steps and audit controls are important forms of governance that make it possible for the systems to run in production. The reliability and safety we’ve prioritized in building Claude, paired with UST’s experience in governance and regulated delivery, enables this work to move out of a pilot and into the systems that run a business.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
