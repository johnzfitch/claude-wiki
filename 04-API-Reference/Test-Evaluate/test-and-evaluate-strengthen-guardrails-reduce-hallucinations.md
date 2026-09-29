---
title: "Reduce hallucinations - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-09-26T06:39:50Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Ftest-and-evaluate%2Fstrengthen-guardrails%2Freduce-hallucinations)





SearchCtrlK

Use cases

[Overview](../About/about-claude-use-case-guides-overview.md)[Ticket routing](../About/about-claude-use-case-guides-ticket-routing.md)[Customer support agent](../About/about-claude-use-case-guides-customer-support-chat.md)[Content moderation](../About/about-claude-use-case-guides-content-moderation.md)[Legal summarization](../About/about-claude-use-case-guides-legal-summarization.md)[Commerce agent](../About/about-claude-use-case-guides-commerce-agents.md)

Prompt engineering

[Overview](../../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md)[Prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)[Prompting Claude Fable 5.1](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md)[Prompting Claude Fable 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md)[Prompting Claude Opus 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)[Prompting Claude Opus 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md)[Prompting Claude Opus 4.8](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-4-8.md)[Prompting Claude Sonnet 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md)

Test and evaluate

[Define success and build evaluations](test-and-evaluate-develop-tests.md)[Reducing latency](test-and-evaluate-strengthen-guardrails-reduce-latency.md)

Strengthen guardrails

[Reduce hallucinations](test-and-evaluate-strengthen-guardrails-reduce-hallucinations.md)[Increase output consistency](test-and-evaluate-strengthen-guardrails-increase-consistency.md)[Mitigate jailbreaks](test-and-evaluate-strengthen-guardrails-mitigate-jailbreaks.md)[Reduce prompt leak](test-and-evaluate-strengthen-guardrails-reduce-prompt-leak.md)

Reference

[Glossary](../About/about-claude-glossary.md)[Additional resources](../About/about-claude-additional-resources.md)

[Console](../Other/usage-limits.md)

[Best practices](../About/about-claude-use-case-guides-overview.md)Strengthen guardrails

# Reduce hallucinations

Copy page



Minimize hallucinations in Claude's outputs by allowing uncertainty, grounding responses in direct quotes, and verifying claims with citations.

Copy page



Even the most advanced language models, like Claude, can sometimes generate text that is factually incorrect or inconsistent with the given context. This phenomenon, known as "hallucination," can undermine the reliability of your AI-driven solutions. This guide will explore techniques to minimize hallucinations and ensure Claude's outputs are accurate and trustworthy.

## Basic hallucination minimization strategies

- **Allow Claude to say "I don't know":** Explicitly give Claude permission to admit uncertainty. This simple technique can drastically reduce false information.

### Example: Analyzing a merger & acquisition report

User



``` block
As our M&A advisor, analyze this report on the potential acquisition of AcmeCo by ExampleCorp.

<report>
{{REPORT}}
</report>

Focus on financial projections, integration risks, and regulatory hurdles. If you're unsure about any aspect or if the report lacks necessary information, say "I don't have enough information to confidently assess this."
```

- **Use direct quotes for factual grounding:** For tasks involving long documents (\>20k tokens), ask Claude to extract word-for-word quotes first before performing its task. This grounds its responses in the actual text, reducing hallucinations.

### Example: Auditing a data privacy policy

User



``` block
As our Data Protection Officer, review this updated privacy policy for GDPR and CCPA compliance.
<policy>
{{POLICY}}
</policy>

1. Extract exact quotes from the policy that are most relevant to GDPR and CCPA compliance. If you can't find relevant quotes, state "No relevant quotes found."

2. Use the quotes to analyze the compliance of these policy sections, referencing the quotes by number. Only base your analysis on the extracted quotes.
```

- **Verify with citations**: Make Claude's response auditable by having it cite quotes and sources for each of its claims. You can also have Claude verify each claim by finding a supporting quote after it generates a response. If it can't find a quote, it must retract the claim.

### Example: Drafting a press release on a product launch

User



``` block
Draft a press release for our new cybersecurity product, AcmeSecurity Pro, using only information from these product briefs and market reports.
<documents>
{{DOCUMENTS}}
</documents>

After drafting, review each claim in your press release. For each claim, find a direct quote from the documents that supports it. If you can't find a supporting quote for a claim, remove that claim from the press release and mark where it was removed with empty [] brackets.
```

------------------------------------------------------------------------

## Advanced techniques

- **Chain-of-thought verification**: Ask Claude to explain its reasoning step-by-step before giving a final answer. This can reveal faulty logic or assumptions.

- **Best-of-N verification**: Run Claude through the same prompt multiple times and compare the outputs. Inconsistencies across outputs could indicate hallucinations.

- **Iterative refinement**: Use Claude's outputs as inputs for follow-up prompts, asking it to verify or expand on previous statements. This can catch and correct inconsistencies.

- **External knowledge restriction**: Explicitly instruct Claude to only use information from provided documents and not its general knowledge.



Remember, while these techniques significantly reduce hallucinations, they don't eliminate them entirely. Always validate critical information, especially for high-stakes decisions.
