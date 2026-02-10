---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:59Z"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests"
title: "Create strong empirical evaluations - Claude API Docs"
---

Test & evaluate

# Create strong empirical evaluations

Copy page

Copy page

After defining your success criteria, the next step is designing evaluations to measure LLM performance against those criteria. This is a vital part of the prompt engineering cycle.

This guide focuses on how to develop your test cases.

## 

Building evals and test cases

### 

Eval design principles

1.  **Be task-specific**: Design evals that mirror your real-world task distribution. Don't forget to factor in edge cases!
    ### Example edge cases
2.  **Automate when possible**: Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).
3.  **Prioritize volume over quality**: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### 

Example evals

### Task fidelity (sentiment analysis) - exact match evaluation

### Consistency (FAQ bot) - cosine similarity evaluation

### Relevance and coherence (summarization) - ROUGE-L evaluation

### Tone and style (customer service) - LLM-based Likert scale

### Privacy preservation (medical chatbot) - LLM-based binary classification

### Context utilization (conversation assistant) - LLM-based ordinal scale

Writing hundreds of test cases can be hard to do by hand! Get Claude to help you generate more from a baseline set of example test cases.

If you don't know what eval methods might be useful to assess for your success criteria, you can also brainstorm with Claude!

------------------------------------------------------------------------

## 

Grading evals

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

1.  **Code-based grading**: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgements that require less rule-based rigidity.

    - Exact match: `output == golden_answer`
    - String match: `key_phrase in output`

2.  **Human grading**: Most flexible and high quality, but slow and expensive. Avoid if possible.

3.  **LLM-based grading**: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

### 

Tips for LLM-based grading

- **Have detailed, clear rubrics**: "The answer should always mention 'Acme Inc.' in the first sentence. If it does not, the answer is automatically graded as 'incorrect.'"

  A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.
- **Empirical or specific**: For example, instruct the LLM to output only 'correct' or 'incorrect', or to judge from a scale of 1-5. Purely qualitative evaluations are hard to assess quickly and at scale.
- **Encourage reasoning**: Ask the LLM to think first before deciding an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgement.

### Example: LLM-based grading

## 

Next steps

[](/docs/en/build-with-claude/prompt-engineering/overview)

Brainstorm evaluations

Learn how to craft prompts that maximize your eval scores.

[](https://platform.claude.com/cookbook/misc-building-evals)

Evals cookbook

More code examples of human-, code-, and LLM-graded evals.

Was this page helpful?

- 

- [Building evals and test cases](#building-evals-and-test-cases)

- [Eval design principles](#eval-design-principles)

- [Example evals](#example-evals)

- [Grading evals](#grading-evals)

- [Tips for LLM-based grading](#tips-for-llm-based-grading)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
