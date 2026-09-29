---
title: "Activating AI Safety Level 3 protections \\ Anthropic"
source_url: "https://www.anthropic.com/news/activating-asl3-protections"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:36Z"
tags: ["news-research", "security"]
---

# Activating AI Safety Level 3 protections

May 22, 2025

*We have activated the AI Safety Level 3 (ASL-3) Deployment and Security Standards described in Anthropic’s Responsible Scaling Policy (RSP) in conjunction with launching Claude Opus 4. The ASL-3 Security Standard involves increased internal security measures that make it harder to steal model weights, while the corresponding Deployment Standard covers a narrowly targeted set of deployment measures designed to limit the risk of Claude being misused specifically for the development or acquisition of chemical, biological, radiological, and nuclear (CBRN) weapons. These measures should not lead Claude to refuse queries except on a very narrow set of topics.*

*We are deploying Claude Opus 4 with our ASL-3 measures as a precautionary and provisional action. To be clear, we have not yet determined whether Claude Opus 4 has definitively passed the Capabilities Threshold that requires ASL-3 protections. Rather, due to continued improvements in CBRN-related knowledge and capabilities, we have determined that clearly ruling out ASL-3 risks is not possible for Claude Opus 4 in the way it was for every previous model, and more detailed study is required to conclusively assess the model’s level of risk. (We have ruled out that Claude Opus 4 needs the ASL-4 Standard, as required by our RSP, and, similarly, we have ruled out that Claude Sonnet 4 needs the ASL-3 Standard.)*

*Dangerous capability evaluations of AI models are inherently [challenging](strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team.md), and as models approach our thresholds of concern, it takes longer to determine their status. Proactively enabling a higher standard of safety and security simplifies model releases while allowing us to learn from experience by iteratively improving our defenses and reducing their impact on users.*

*This post and the accompanying [report](http://anthropic.com/activating-asl3-report) discuss the new measures and the rationale behind them.*

## Background

Increasingly capable AI models warrant increasingly strong deployment and security protections. This principle is core to Anthropic’s [Responsible Scaling Policy](https://www-cdn.anthropic.com/872c653b2d0501d6ab44cf87f43e1dc4853e4d37.pdf) (RSP).¹

- **Deployment measures** target specific categories of misuse; in particular, our RSP focuses on reducing the risk that models could be misused for attacks with the most dangerous categories of weapons–CBRN.
- **Security** **controls** aim to prevent the theft of model weights–the essence of the AI’s intelligence and capability.

Anthropic’s RSP includes *Capability Thresholds* for models: if models reach those thresholds (or if we have not yet determined that they are sufficiently far below them), we are required to implement a higher level of *AI Safety Level Standards*. Until now, all our models have been deployed under the baseline protections of the AI Safety Level 2 (ASL-2) Standard. ASL-2 deployment measures include training models to refuse dangerous CBRN-related requests. ASL-2 security measures include defenses against opportunistic attempts to steal the weights. The ASL-3 Standard requires a higher level of defense against both deployment and security threats, suitable against sophisticated non-state attackers.

## Rationale

We have not yet determined whether Claude Opus 4 capabilities actually require the protections of the ASL-3 Standard. So why did we implement those protections now? We anticipated that we might do this when we launched our last model, Claude Sonnet 3.7. In that case, we determined that the model did not require the protections of the ASL-3 Standard. But we [acknowledged](visible-extended-thinking.md) the very real possibility that given the pace of progress, near future models might warrant these enhanced measures.² And indeed, in the lead up to releasing Claude Opus 4, we proactively decided to launch it under the ASL-3 Standard. This approach allowed us to focus on developing, testing, and refining these protections before we needed them.

This approach is also consistent with the RSP, which allows us to err on the side of caution and deploy a model under a higher standard than we are sure is needed. In this case, that meant proactively carrying out the ASL-3 Security and Deployment Standards (and ruling out the need for even more advanced protections). We will continue to evaluate Claude Opus 4’s CBRN capabilities. If we conclude that Claude Opus 4 has not surpassed the relevant Capability Threshold, then we may remove or adjust the ASL-3 protections.

## Deployment Measures

The new ASL-3 deployment measures are narrowly focused on preventing the model from assisting with CBRN-weapons related tasks of concern,³ and specifically from assisting with extended, *end-to-end* CBRN workflows in a way that is additive to what is already possible without large language models. This includes limiting *universal jailbreaks*—systematic attacks that allow attackers to circumvent our guardrails and consistently extract long chains of workflow-enhancing CBRN-related information. Consistent with our underlying threat models, ASL-3 deployment measures do not aim to address issues unrelated to CBRN, to defend against non-universal jailbreaks, or to prevent the extraction of commonly available single pieces of information, such as the answer to, “What is the chemical formula for sarin?” (although they may incidentally prevent this). Given the evolving threat landscape, we expect that new jailbreaks will be discovered and that we will need to rapidly iterate and improve our systems over time.

We have developed a three-part approach: making the system more difficult to jailbreak, detecting jailbreaks when they do occur, and iteratively improving our defenses.

- **Making the system more difficult to jailbreak.** We have implemented [Constitutional Classifiers](research-constitutional-classifiers.md)—a system where real-time classifier guards, trained on synthetic data representing harmful and harmless CBRN-related prompts and completions, monitor model inputs and outputs and intervene to block a narrow class of harmful CBRN information. Our pre-production testing suggests we can substantially reduce jailbreaking success while adding only moderate compute overhead (additional processing costs beyond what is required for model inference) to normal operations.
- **Detecting jailbreaks when they occur.** We have also instituted a wider monitoring system including a [bug bounty program](testing-our-safety-defenses-with-a-new-bug-bounty-program.md) focused on stress-testing our Constitutional Classifiers, offline classification systems, and threat intelligence partnerships to quickly identify and respond to potential universal jailbreaks that would enable CBRN misuse.
- **Iteratively improving our defenses.** We believe we can rapidly remediate jailbreaks using methods including [generating synthetic jailbreaks](https://arxiv.org/abs/2411.07494) that resemble those we discovered and using those data to train a new classifier.

All these measures will require ongoing refinement, both to improve their effectiveness and because they may still occasionally affect legitimate queries (that is, they may produce false positives).⁴ Nevertheless, they represent a substantial advance in defending against catastrophic misuse of AI capabilities.⁵

## Security

Our targeted security controls are focused on protecting model weights—the critical numerical parameters that, if compromised, could allow users to access our models without deployment protections. Our approach involves more than 100 different security controls that combine preventive controls with detection mechanisms, primarily targeting threats from sophisticated non-state actors⁶ from initial entry points through lateral movement to final extraction. Many of these controls, such as two-party authorization for model weight access, enhanced change management protocols, and endpoint software controls through binary allowlisting, are examples of following the best practices established by other security-conscious organizations.

One control in particular, however, is more unique to the goal of protecting model weights: we have implemented preliminary egress bandwidth controls. Egress bandwidth controls restrict the flow of data out of secure computing environments where AI model weights reside. The combined weights of a model are substantial in size. By limiting the rate of outbound network traffic, these controls can leverage model weight size to create a security advantage. When potential exfiltration of model weights is detected through unusual bandwidth usage, security systems can block the suspicious traffic. Over time, we expect to get to the point where rate limits are low enough that exfiltrating model weights before being detected is very difficult—even if an attacker has otherwise significantly compromised our systems. Implementing egress bandwidth controls has been a forcing function to understand and govern the way in which data is flowing outside of our internal systems, which has yielded benefits for our detection and response capabilities.

As with the deployment protections, we are continuing to work on improving the coverage and maturity of our security controls, always taking into account the evolving threat landscape. In particular, we will continue improving our egress controls, mitigations against more sophisticated insider threats, and our overall security posture.

## Conclusions

As we have emphasized above, the question of which deployment and security measures to apply to frontier AI models is far from solved. We will continue to introspect, iterate, and improve. The practical experience of operating under the ASL-3 Standards will help us uncover new and perhaps unexpected issues and opportunities.

We will continually work with others in the AI industry, users of Claude, and partners in government and civil society to improve our methods of guarding these models. We hope that our detailed report will be of use to others in the AI industry attempting to implement similar protections and help us all prepare for the promise and challenge of even more capable AI.

Read the full [report](https://www.anthropic.com/activating-asl3-report).

#### Footnotes

¹The RSP is only one component of our [approach](our-approach-to-understanding-and-addressing-ai-harms.md) to mitigating potential risks.

²In particular, we had some evidence of improved CBRN-related capabilities. Experiments showed that access to Claude Sonnet 3.7 helped participants do somewhat better on tasks related to CBRN weapon acquisition than those with standard internet access (although all participants’ plans still had critical failures). Model performance on evaluations like the [Virology Capabilities Test](https://arxiv.org/abs/2504.16137) had been steadily increasing over time.

³Initially they are focused exclusively on biological weapons as we believe these account for the vast majority of the risk, although we are evaluating a potential expansion in scope to some other CBRN threats.

⁴ We have also established access control systems so that users with dual-use science and technology applications may be vetted to receive targeted exemptions from some classifier actions.

⁵For more information on our assessment of the effectiveness and sufficiency of these measures, see the [ASL-3 Deployment Safeguards Report](http://anthropic.com/asl3-deployment-safeguards).

⁶Nation-state threats (other than those using non-novel attack chains) and sophisticated insider risk are out of the scope of the ASL-3 Standard.  

  
## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](investigating-incidents-cybersecurity-evals.md)

### Our position on open-weights models

[Read more](position-open-weights-models.md)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](cognizant-anthropic.md)

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
- [Claude for Chrome](https://claude.com/chrome)
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
- [Courses](https://www.anthropic.com/learn)
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
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
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
