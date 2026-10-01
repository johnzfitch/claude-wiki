---
title: "Prompting Claude's long context window \\ Anthropic"
source_url: "https://www.anthropic.com/news/prompting-long-context"
category: "19-Reference"
fetched_at: "2026-09-10T06:45:56Z"
tags: ["evaluation", "news-research", "prompting", "testing"]
---

# Prompt engineering for Claude's long context window

Sep 23, 2023

  
Claude’s [100,000 token long context window](100k-context-windows.md) enables the model to operate over hundreds of pages of technical documentation, or even an [entire book](https://twitter.com/AnthropicAI/status/1656700156518060033). As we continue to scale the Claude API, we’re seeing increased demand for prompting guidance on how to maximize Claude’s potential. Today, we’re pleased to share a quantitative case study on two techniques that can improve Claude’s recall over long contexts:  

1.  Extracting reference quotes relevant to the question before answering
2.  Supplementing the prompt with examples of correctly answered questions about other sections of the document

Let’s get into the details.  

## Testing long context recall: Multiple choice Q&A

Our goal with this experiment is to evaluate techniques to maximize Claude’s chance of correctly recalling a specific piece of information from a long document.  

As the underlying data source for our testing, we used a daily-issue, publicly available [government document](https://www.govinfo.gov/content/pkg/FR-2023-07-13/xml/FR-2023-07-13.xml) that contains the meeting transcripts and activities of many different departments. We chose a document from July 13, which is after Claude’s training data cutoff. This minimizes the chance that Claude already knows the information in the document.  
  
In order to generate a dataset of question and answer (Q&A) pairs, we used an approach we call “randomized collage”. We split the document into sections and used Claude to generate five multiple choice questions for each section, each with three wrong answers and one right answer. We then reassembled randomized sets of these sections into long documents so that we could pass them to Claude and test its recall of their contents.

## Prompting Claude to generate multiple choice questions

Getting Claude to write your evaluations (evals) for you is a powerful tool and one that we as a prompt engineering team use often. However, it takes careful prompting to get Claude to write questions in the sweet spot of difficulty. Here are some challenges we worked through along the way to designing an effective test suite:

- Claude may propose questions that it can answer off the top of its head without reference to any document, like “What does the Department of Transportation do?”
- Claude may include questions that it struggles to answer correctly, even in short context situations. For example, because Claude sees the world in terms of tokens, not words, a question like “How many words are in the passage?” tends to give Claude trouble.
- Claude may leave unintentional clues in its answers that make the correct answer easy to guess. Notably, we noticed its default was to make the right answer very detailed in comparison to the wrong answers.
- Claude may reference “this document” or “this passage” without specifying what passage it means. This is problematic because when we stitch together multiple documents to form the long context, Claude has no way to know which document the question is asking about.
- There’s also the risk of going too far and making the questions so explicit that they contain the answer. For example, “What is the publication date of the Department of the Interior’s July 2, 2023 notice about additional in-season actions for fisheries?” would be an ineffective question.

To help navigate these pitfalls, we used a prompt template that includes two sample meeting chunks along with hand-written questions to act as few-shot question writing examples, as well as some writing guidelines to get Claude to specify details about the passage. The template and all other prompts used in this experiment are available [here](https://www-cdn.anthropic.com/d1198e53f52c64b6f647fa49fc3399c7eafb2b78/Prompt_Eng_pdf.pdf).

## Evaluation

For this evaluation, we primarily focused on our smaller Claude Instant model (version 1.2) as opposed to our Claude 2 model. This is for a couple of reasons. First, Claude 2 is already very good at recalling information after reading very long documents. Claude Instant needs more help, which makes it easy to see when changes to prompting improve performance. Additionally, Claude Instant is so fast that you can reproduce these evals yourself with the notebook we share.  
  
When provided with only the exact passage Claude used to write the question, Claude Instant was able to answer its own generated question about 90% of the time. We discarded the 10% of questions it answered incorrectly – since Claude was getting them wrong even in a short-context situation, they’re too difficult to be useful for testing long context.[1](#f1)  
  
We also tested Claude’s recall when given a random section not containing the question’s source material. Theoretically, with three wrong answers, Claude should be able to guess the right answer only 25% of the time. In practice, it guessed right 34% of the time; above chance, but not too much so. Claude is likely sometimes intuiting the right answer based on its general knowledge, or based on subtle cues in the answer.  
  
In order to build long documents from shorter chunks, we artificially generated a new long context for each question by stitching together a random assortment of passages until we reached the desired number of tokens. We tested Claude on stitched-together documents containing roughly 75,000 and 90,000 tokens.  
  
This patchwork context formation is why Claude referencing ambiguous phrases like “this document” or “this passage” in its question was causing problems. A question like “What is the publication date of this notice?” ceases to be answerable when there are a dozen different notices in the context to which “this notice” could refer. This is why our question generation prompt includes language telling Claude to be explicit about the passage to which the question refers – for example, “What is the publication date of the notice about additional in-season actions for fisheries?"  
  
After generating the long documents (collages), we tested Claude’s recall using four different prompting strategies:

1.  **Base** – just ask Claude to answer
2.  **Nongov examples** - Give Claude two fixed examples of correctly answered general knowledge multiple choice questions that are unrelated to the government document[2](#f2)
3.  **Two examples** - Give Claude two examples of correctly answered multiple choice questions, dynamically chosen at random from the set of Claude-generated questions about other chunks in the context
4.  **Five examples** - Same strategy as \#3, but with five examples

For each of the four strategies above, we also tested them with and without the use of a \<scratchpad\>, in which we instruct Claude to pull relevant quotes. Furthermore, we tested each of these strategies with the passage containing the answer positioned either at the beginning, the end, or in the middle of the input. Finally, to get a sense of the effect of context length on the results, we tested with both 70K and 95K token documents.  
  
We used Claude Instant 1.2 for the above test. We also show results for Claude 2 on the baseline strategy and the strategy that performed best for Claude Instant 1.2.

## Results

  
Some notes on the experiment:

- While performance on the beginning and middle of the doc are substantially improved by the use of a scratchpad and examples, performance on the end can be degraded. This could be because the addition of the examples in the prompt increases the distance between the very end of the document (where the relevant information is) and when Claude needs to answer it. This is likely of only minor concern as only a small fraction of the data in the source document is at the very end. However, it does emphasize the importance of putting the instructions [at the end of the prompt](https://docs.anthropic.com/claude/docs/advanced-text-analysis#document-qa-with-citations), as we want Claude’s recall of them to be as high as possible.
- Claude 2’s improvement from 0.939 to 0.961 with prompting might seem small in absolute terms, but it reflects a 36% reduction in errors.

Some takeaways you can use for writing your long-context Q&A prompts:

- Use many examples and the scratchpad for best performance on both context lengths.
- Pulling relevant quotes into the scratchpad is helpful in all head-to-head comparisons. It comes at a small cost to latency, but improves accuracy. In Claude Instant’s case, the latency is already so low that this shouldn’t be a concern.
- Contextual examples help on both 70K and 95K, and more examples is better.
- Generic examples on general/external knowledge do not seem to help performance.

For Claude Instant, there seems to be a monotonic inverse relationship between performance and the distance of the relevant passage to the question and the end of the prompt, while Claude 2 performance on 95K sees a small dip in the middle.[3](#f3)

## Introducing the new Anthropic Cookbook

Fully reproducible code for this experiment is live in the new [Anthropic Cookbook](https://platform.claude.com/cookbook). This growing set of resources also contains two other recipes at the moment:

- A [Search and Retrieval demo](https://platform.claude.com/cookbook/third-party-wikipedia-wikipedia-search-cookbook) showcasing a tool use flow for searching Wikipedia.
- Guidance on implementing [mock-PDF uploading functionality](https://platform.claude.com/cookbook/misc-pdf-upload-summarization) via the Anthropic API.

We’re looking forward to expanding the Anthropic Cookbook and our other prompt engineering resources in the future, and we hope they inspire you to dream big about what you can build with Claude. If you haven’t received access to the Claude API yet, please [register your interest](https://www.anthropic.com/api).

## Footnotes

[1](#b1)A common theme in the questions Claude gets wrong is counting, e.g. “What is the estimated number of responses per respondent that the notice states for each form in the Common Forms Package for Guaranteed Loan Forms?” and “How many proposed finished products are listed in the notification for production activity at the Getinge Group Logistics Americas LLC facility?” Notably, on some of these questions, Claude’s pre-specified “correct” answer (from when it generated the QA pairs) is not in reality correct. This is a source of noise in this experiment.

[2](#b2)The questions are: 1. Who was the first president of the United States? A. Thomas Jefferson, B. George Washington, C. Abraham Lincoln, D. John Adams, 2. What is the boiling temperature of water, in degrees Fahrenheit? A. 200, B. 100, C. 287, D. 212.

[3](#b3)A [recent paper](https://arxiv.org/abs/2307.03172) found a U-shaped relationship between performance and location in the context for a similar task. A possible explanation for the differing results is that the examples in the paper have avg. length 15K tokens (Appendix F), compared to 70K/95K here.


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
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

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
