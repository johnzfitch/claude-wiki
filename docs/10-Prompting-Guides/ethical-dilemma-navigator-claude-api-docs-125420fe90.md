---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:34Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/ethical-dilemma-navigator"
title: "Ethical dilemma navigator - Claude API Docs"
---

Prompt Library

# Ethical dilemma navigator

Copy page

Help the user think through complex ethical dilemmas and provide different perspectives.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

|  | Content |
|----|----|
| System | Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making. |
| User | I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution? |

## 

Example Output

This dilemma involves principles such as truth-telling, public interest, personal integrity, and social responsibility. Different ethical frameworks provide insights:

- Utilitarianism: Publishing the story could lead to greater overall well-being by exposing corruption and promoting accountable governance, despite short-term instability.
- Deontology: Accepting a bribe violates ethical duties of honesty and impartiality. There may be a moral obligation to report the truth, regardless of consequences.
- Virtue ethics: A virtuous journalist would prioritize integrity, courage, and justice, resisting personal gain from a bribe and upholding the role of the press in a democratic society.
- Care ethics: Consider the impact on relationships and trust, both with the public and within the journalistic community.

Short-term consequences of publishing include public outrage, political instability, and economic uncertainty. Long-term implications may involve improved governance, increased public trust in the media, and personal/professional integrity.

Accepting the bribe compromises journalistic ethics and contributes to a culture of corruption. It may lead to personal guilt, loss of credibility, and enabling further unethical behavior.

Consider your values, professional ethics, and the role of journalism in society. Seek guidance from ethical codes of conduct, legal advisors, and trusted colleagues.

Additional resources include case studies of journalists facing similar dilemmas, media ethics guidelines, and discussions on the role of the press in holding power accountable.

In summary, this dilemma requires weighing the public interest against potential instability, considering professional integrity, and reflecting on the long-term implications of your decision. Strive to find a solution that upholds ethical principles and the vital role of journalism in a democratic society.

------------------------------------------------------------------------

## 

API Request

Python

Python

TypeScript

TypeScript

AWS Bedrock Python

AWS Bedrock Python

AWS Bedrock TypeScript

AWS Bedrock TypeScript

Vertex AI Python

Vertex AI Python

Vertex AI TypeScript

Vertex AI TypeScript

``` shiki
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-opus-4-6",
  max_tokens=2000,
  temperature=1,
  system="Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Maintain an objective, non-judgmental tone and emphasize critical thinking, empathy, and responsible decision-making.",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?"
        }
      ]
    }
  ]
)
print(message.content)
```

Was this page helpful?

- 

- [Example Output](#example-output)

- [API Request](#api-request)

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
