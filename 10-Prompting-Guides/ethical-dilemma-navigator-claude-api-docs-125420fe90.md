---
category: "10-Prompting-Guides"
fetched_at: "2026-03-03T14:56:17Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/ethical-dilemma-navigator"
title: "Ethical dilemma navigator - Claude API Docs"
---

# Ethical dilemma navigator


Help the user think through complex ethical dilemmas and provide different perspectives.


> Copy this prompt into the developer [Console](/dashboard) to try it for yourself!

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
                    "text": "I am a journalist who has uncovered evidence of corruption involving a high-ranking government official. Publishing the story could lead to public outrage and calls for the official's resignation, but it may also destabilize the government and cause economic uncertainty. The official has offered me a significant bribe to keep the story quiet. Should I accept the bribe, publish the story, or find another solution?",
                }
            ],
        }
    ],
)
print(message.content)
```
