---
title: "Reduce prompt leak - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-08-02T05:40:55Z"
tags: ["api", "prompting"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/about-claude/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

API reference




Console








Search


Use cases

[Overview](/docs/en/about-claude/use-case-guides/overview)[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)

Prompt engineering

[Overview](/docs/en/build-with-claude/prompt-engineering/overview)[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)[Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Test and evaluate

[Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests)[Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Strengthen guardrails

[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)[Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

Reference

[Glossary](/docs/en/about-claude/glossary)

[](/login)




Best practices

Reduce prompt leak

Best practices/Strengthen guardrails

# Reduce prompt leak




Reduce the risk of prompt leaks by separating context from user queries, filtering Claude's outputs, and auditing prompts, without degrading task performance.




Prompt leaks can expose sensitive information that you expect to be "hidden" in your prompt. While no method is foolproof, the strategies below can significantly reduce the risk.




Before you try to reduce prompt leak

Consider using leak-resistant prompt engineering strategies only when **absolutely necessary**. Attempts to leak-proof your prompt can add complexity that may degrade performance in other parts of the task due to increasing the complexity of the LLM’s overall task.

If you decide to implement leak-resistant techniques, be sure to test your prompts thoroughly to ensure that the added complexity does not negatively impact the model’s performance or the quality of its outputs.



Try monitoring techniques first, like output screening and post-processing, to try to catch instances of prompt leak.

------------------------------------------------------------------------




Strategies to reduce prompt leak

- **Separate context from queries:** You can try using system prompts to isolate key information and context from user queries. You can emphasize key instructions in the `User` turn, then reemphasize those instructions by prefilling the `Assistant` turn. (Note: prefilling is not supported on Claude 4.6 and later models and [Claude Mythos Preview](https://anthropic.com/glasswing).)

### Example: Safeguarding proprietary analytics

- **Use post-processing**: Filter Claude's outputs for keywords that might indicate a leak. Techniques include using regular expressions, keyword filtering, or other text processing methods.
  

  You can also use a prompted LLM to filter outputs for more nuanced leaks.
- **Avoid unnecessary proprietary details**: If Claude doesn't need it to perform the task, don't include it. Extra content distracts Claude from focusing on "no leak" instructions.
- **Regular audits**: Periodically review your prompts and Claude's outputs for potential leaks.

Remember, the goal is not just to prevent leaks but to maintain Claude's performance. Overly complex leak-prevention can degrade results. Balance is key.
