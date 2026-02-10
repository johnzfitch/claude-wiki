---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:05:35Z"
source_url: "https://platform.claude.com/docs/en/resources/prompt-library/meeting-scribe"
title: "Meeting scribe - Claude API Docs"
---

Prompt Library

# Meeting scribe

Copy page

Distill meetings into concise summaries including discussion topics, key takeaways, and action items.

Copy page

> Copy this prompt into our developer [Console](/dashboard) to try it for yourself!

[TABLE]

## 

Example Output

Meeting Summary: Reconciliation and Peace in Verona Date: Late 16th century, Verona, Italy

Attendees:

- Lord Capulet (Head of the Capulet family)
- Lord Montague (Head of the Montague family)
- Prince Escalus (Ruler of Verona)
- Friar Laurence (Religious advisor)

Key Takeaways:

- Prince Escalus addressed the ongoing feud between the Capulet and Montague families, warning of severe consequences for further violence.
- Friar Laurence revealed the secret marriage between Romeo Montague and Juliet Capulet, urging the families to consider the potential for their love to heal the rift.
- Prince Escalus proposed a formal truce between the families, threatening severe punishments for any violations.
- The tragic deaths of Romeo and Juliet were discussed, with Lord Capulet and Lord Montague acknowledging their role in the heartbreaking outcome.
- Prince Escalus called for forgiveness and unity in honor of Romeo and Juliet's memory, urging the families to work together for lasting peace in Verona.

Action Items:

- Lord Capulet and Lord Montague:
  - Lay down arms and cease all hostile actions against one another.
  - Work towards reconciliation and embrace forgiveness.
  - Attend regular meetings to discuss progress and address challenges.
- Prince Escalus:
  - Enforce the truce and ensure its adherence.
  - Administer swift justice for any violations of the truce.
- Friar Laurence:
  - Provide mediation and spiritual guidance to support the families in their healing and reconciliation process.

Next Steps:

- The attendees will meet regularly to monitor the progress of reconciliation efforts and address any arising challenges.

## 

API request

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
    max_tokens=4000,
    temperature=0.5,
    system="Your task is to review the provided meeting notes and create a concise summary that captures the essential information, focusing on key takeaways and action items assigned to specific individuals or departments during the meeting. Use clear and professional language, and organize the summary in a logical manner using appropriate formatting such as headings, subheadings, and bullet points. Ensure that the summary is easy to understand and provides a comprehensive but succinct overview of the meeting's content, with a particular focus on clearly indicating who is responsible for each action item.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Meeting notes:  \n  \nDate: Verona, Italy - Late 16th century  \n  \nAttendees:  \n- Lord Capulet (Head of the Capulet family)  \n- Lord Montague (Head of the Montague family)  \n- Prince Escalus (Ruler of Verona)  \n- Friar Laurence (Religious advisor)  \n  \nAgenda:  \n1. Address the ongoing feud between the Capulet and Montague families  \n2. Discuss the secret marriage of Romeo Montague and Juliet Capulet  \n3. Develop a plan to bring peace to Verona  \n4. Address the tragic deaths of Romeo and Juliet  \n  \nDiscussion:  \n- Prince Escalus opened the meeting by expressing his grave concern over the long-standing feud between the Capulet and Montague families. He admonished both Lord Capulet and Lord Montague for the recent violent clashes that have disturbed the peace in Verona's streets. The Prince warned that further violence would result in severe consequences, including heavy fines and potential exile for the perpetrators.  \n- Friar Laurence then broached the topic of the between Romeo Montague and Juliet Capulet, which had taken place under his guidance. Lord Capulet and Lord Montague evidently had not known about it, and reacted with anger and disbelief. However, Friar Laurence urged them to consider the profound and tragic love shared by their children and the potential for this love to heal the rift between the families going forward.  \n- Prince Escalus proposed a formal truce between the Capulet and Montague families. He demanded that both sides lay down their arms and cease all hostile actions against one another. The Prince declared that any violation of the truce would result in severe punishments, including the possibility of exile or even execution. Lord Capulet and Lord Montague, recognizing the wisdom in the Prince's words and the necessity of peace for the well-being of their families and the city, grudgingly agreed to the terms of the truce.  \n- The meeting took a somber turn as the tragic deaths of Romeo and Juliet were addressed. Friar Laurence recounted the unfortunate series of events that led to the young lovers taking their own lives, emphasizing the devastating impact of the families' hatred on their innocent children. Lord Capulet and Lord Montague, overcome with grief and remorse, acknowledged that their blind hatred had ultimately caused the loss of their beloved children.  \n- Prince Escalus called upon the families to learn from this heartbreaking tragedy and to embrace forgiveness and unity in honor of Romeo and Juliet's memory. He urged them to work together to create a lasting peace in Verona, setting aside their long-standing animosity. Friar Laurence offered his support in mediating any future disputes and providing spiritual guidance to help the families heal and move forward.  \n- As the meeting drew to a close, Lord Capulet and Lord Montague pledged to put an end to their feud and work towards reconciliation. Prince Escalus reaffirmed his commitment to ensuring that the truce would be upheld, promising swift justice for any who dared to break it.  \n- The attendees agreed to meet regularly to discuss the progress of their reconciliation efforts and to address any challenges that may arise."
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

- [API request](#api-request)

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
