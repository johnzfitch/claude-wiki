---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:04Z"
source_url: "https://platform.claude.com/docs/en/about-claude/model-deprecations"
title: "Model deprecations - Claude API Docs"
---

Models & pricing

# Model deprecations

Copy page

Copy page

As we launch safer and more capable models, we regularly retire older models. Applications relying on Anthropic models may need occasional updates to keep working. Impacted customers will always be notified by email and in our documentation.

This page lists all API deprecations, along with recommended replacements.

## 

Overview

Anthropic uses the following terms to describe the lifecycle of our models:

- **Active**: The model is fully supported and recommended for use.
- **Legacy**: The model will no longer receive updates and may be deprecated in the future.
- **Deprecated**: The model is no longer available for new customers but continues to be available for existing users until retirement. We assign a retirement date at this point.
- **Retired**: The model is no longer available for use. Requests to retired models will fail.

Please note that deprecated models are likely to be less reliable than active models. We urge you to move workloads to active models to maintain the highest level of support and reliability.

## 

Migrating to replacements

Once a model is deprecated, please migrate all usage to a suitable replacement before the retirement date. Requests to models past the retirement date will fail.

To help measure the performance of replacement models on your tasks, we recommend thorough testing of your applications with the new models well before the retirement date.

For specific instructions on migrating to the latest Claude models, see the [Migration guide](/docs/en/about-claude/models/migration-guide).

## 

Notifications

Anthropic notifies customers with active deployments for models with upcoming retirements. We provide at least 60 days notice before model retirement for publicly released models.

## 

Auditing model usage

To help identify usage of deprecated models, customers can access an audit of their API usage. Follow these steps:

1.  Go to the [Usage](/settings/usage) page in Console
2.  Click the "Export" button
3.  Review the downloaded CSV to see usage broken down by API key and model

This audit will help you locate any instances where your application is still using deprecated models, allowing you to prioritize updates to newer models before the retirement date.

## 

Best practices

1.  Regularly check our documentation for updates on model deprecations.
2.  Test your applications with newer models well before the retirement date of your current model.
3.  Update your code to use the recommended replacement model as soon as possible.
4.  Contact our support team if you need assistance with migration or have any questions.

## 

Deprecation downsides and mitigations

We currently deprecate and retire models to ensure capacity for new model releases. We recognize that this comes with downsides:

- Users who value specific models must migrate to new versions
- Researchers lose access to models for ongoing and comparative studies
- Model retirement introduces safety- and model welfare-related risks

At some point, we hope to make past models publicly available again. In the meantime, we've committed to long-term preservation of model weights and other measures to help mitigate these impacts. For more details, see [Commitments on Model Deprecation and Preservation](https://www.anthropic.com/research/deprecation-commitments).

## 

Model status

All publicly released models are listed below with their status:

| API Model Name | Current State | Deprecated | Tentative Retirement Date |
|----|----|----|----|
| `claude-opus-4-6` | Active | N/A | Not sooner than February 5, 2027 |
| `claude-opus-4-5-20251101` | Active | N/A | Not sooner than November 24, 2026 |
| `claude-opus-4-1-20250805` | Active | N/A | Not sooner than August 5, 2026 |
| `claude-opus-4-20250514` | Active | N/A | Not sooner than May 14, 2026 |
| `claude-sonnet-4-5-20250929` | Active | N/A | Not sooner than September 29, 2026 |
| `claude-sonnet-4-20250514` | Active | N/A | Not sooner than May 14, 2026 |
| `claude-3-7-sonnet-20250219` | Deprecated | October 28, 2025 | February 19, 2026 |
| `claude-haiku-4-5-20251001` | Active | N/A | Not sooner than October 15, 2026 |
| `claude-3-5-haiku-20241022` | Deprecated | December 19, 2025 | February 19, 2026 |
| `claude-3-haiku-20240307` | Active | N/A | Not sooner than March 7, 2025 |

## 

Deprecation history

All deprecations are listed below, with the most recent announcements at the top.

### 

2025-12-19: Claude Haiku 3.5 model

On December 19, 2025, we notified developers using Claude Haiku 3.5 model of its upcoming retirement on the Claude API.

| Retirement Date   | Deprecated Model            | Recommended Replacement     |
|-------------------|-----------------------------|-----------------------------|
| February 19, 2026 | `claude-3-5-haiku-20241022` | `claude-haiku-4-5-20251001` |

### 

2025-10-28: Claude Sonnet 3.7 model

On October 28, 2025, we notified developers using Claude Sonnet 3.7 model of its upcoming retirement on the Claude API.

| Retirement Date   | Deprecated Model             | Recommended Replacement |
|-------------------|------------------------------|-------------------------|
| February 19, 2026 | `claude-3-7-sonnet-20250219` | `claude-opus-4-6`       |

### 

2025-08-13: Claude Sonnet 3.5 models

These models were retired October 28, 2025.

On August 13, 2025, we notified developers using Claude Sonnet 3.5 models of their upcoming retirement.

| Retirement Date  | Deprecated Model             | Recommended Replacement |
|------------------|------------------------------|-------------------------|
| October 28, 2025 | `claude-3-5-sonnet-20240620` | `claude-opus-4-6`       |
| October 28, 2025 | `claude-3-5-sonnet-20241022` | `claude-opus-4-6`       |

### 

2025-06-30: Claude Opus 3 model

This model was retired January 5, 2026.

On June 30, 2025, we notified developers using Claude Opus 3 model of its upcoming retirement.

| Retirement Date | Deprecated Model         | Recommended Replacement |
|-----------------|--------------------------|-------------------------|
| January 5, 2026 | `claude-3-opus-20240229` | `claude-opus-4-6`       |

### 

2025-01-21: Claude 2, Claude 2.1, and Claude Sonnet 3 models

These models were retired July 21, 2025.

On January 21, 2025, we notified developers using Claude 2, Claude 2.1, and Claude Sonnet 3 models of their upcoming retirements.

| Retirement Date | Deprecated Model           | Recommended Replacement |
|-----------------|----------------------------|-------------------------|
| July 21, 2025   | `claude-2.0`               | `claude-opus-4-6`       |
| July 21, 2025   | `claude-2.1`               | `claude-opus-4-6`       |
| July 21, 2025   | `claude-3-sonnet-20240229` | `claude-opus-4-6`       |

### 

2024-09-04: Claude 1 and Instant models

These models were retired November 6, 2024.

On September 4, 2024, we notified developers using Claude 1 and Instant models of their upcoming retirements.

| Retirement Date  | Deprecated Model     | Recommended Replacement     |
|------------------|----------------------|-----------------------------|
| November 6, 2024 | `claude-1.0`         | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-1.1`         | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-1.2`         | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-1.3`         | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-instant-1.0` | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-instant-1.1` | `claude-haiku-4-5-20251001` |
| November 6, 2024 | `claude-instant-1.2` | `claude-haiku-4-5-20251001` |

Was this page helpful?

- 

- [Overview](#overview)

- [Migrating to replacements](#migrating-to-replacements)

- [Notifications](#notifications)

- [Auditing model usage](#auditing-model-usage)

- [Best practices](#best-practices)

- [Deprecation downsides and mitigations](#deprecation-downsides-and-mitigations)

- [Model status](#model-status)

- [Deprecation history](#deprecation-history)

- [2025-12-19: Claude Haiku 3.5 model](#2025-12-19-claude-haiku-3-5-model)

- [2025-10-28: Claude Sonnet 3.7 model](#2025-10-28-claude-sonnet-3-7-model)

- [2025-08-13: Claude Sonnet 3.5 models](#2025-08-13-claude-sonnet-3-5-models)

- [2025-06-30: Claude Opus 3 model](#2025-06-30-claude-opus-3-model)

- [2025-01-21: Claude 2, Claude 2.1, and Claude Sonnet 3 models](#2025-01-21-claude-2-claude-2-1-and-claude-sonnet-3-models)

- [2024-09-04: Claude 1 and Instant models](#2024-09-04-claude-1-and-instant-models)

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
