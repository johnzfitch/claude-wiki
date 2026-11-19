---
title: "Firecrawl Case Study | Claude by Anthropic | Claude by Anthropic"
source_url: "https://www.claude.com/customers/firecrawl"
category: "18-Industry-UseCases"
fetched_at: "2026-11-18T06:28:54Z"
tags: ["case-studies"]
---

# Firecrawl turns private AI sessions into shared team work with Claude Tag

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Tag](../15-Claude-AI-Features/product-tag.md)

Location:  
North America

770+

pull requests opened through Claude Tag since late June

80%

of pull requests reviewed and merged

Firecrawl helps more than 1.5 million users pull information from the live web into the AI tools they already work in, and its customers include Replit, Zapier and Retell. Its Alexandria library gives AI agents a single API for official data providers, Firecrawl’s own indexes and the live web. Firecrawl’s own team of about 45 tags Claude into the Slack threads where its work already happens, through Claude Tag, Anthropic’s agent for team channels.  
  
With Claude, Firecrawl:

- Opened 770+ pull requests through Claude Tag since late June 2026 and merged 620 of them, about 80%
- Went from a screenshot of a layout bug to a tested pull request in 9 minutes 30 seconds, then reviewed and merged it in under 18 minutes
- Took a support-tool change from first request to merged pull request in about three hours, with a teammate’s test and an edge-case fix in the same thread

## The challenge

### AI work stuck in one person’s session

Before Claude Tag, Firecrawl’s engineers worked in Claude Code, teammates ran their own Claude chats, and in January the company built a Claude-powered bot for its support system. Most of that work happened in sessions only one person could see, so the weak point was the handoff. “Someone could investigate a problem with AI, but the rest of the team saw only the answer or the pull request they chose to share,” said Eric Ciarla, cofounder and Chief Growth Officer at Firecrawl. Whoever picked up the work next had to rebuild the background, assumptions and failed attempts still sitting in the first person’s session.

Support felt the cost most, because one customer question can need code knowledge, account context and product history, often pulling several people in. Each time, an engineer had to stop and reconstruct the problem before work on an answer could start, and support’s own requests for better internal tools added one more handoff before a customer got an answer.

## The solution

### Claude where the team already talks

In late June, Firecrawl began moving work from its own bot to Claude Tag one workflow at a time. Claude Tag reads the whole Slack thread and posts its work back into it, where the team can see and steer it, which Firecrawl’s bot couldn’t do. Firecrawl also doesn’t have to maintain the sandboxes Claude Tag runs in, and it now keeps its own bot only for jobs wired into its support system. Firecrawl moved Claude Tag from Claude Opus 5 to Claude Opus 5.5, with its 1M-token context window, within two days of its September release, because it is faster, does better work and costs less to run.

The rollout began in the support and engineering channels and in the channel for Firebrain, Firecrawl’s internal collection of company knowledge, skills and tools. The team then connected GitHub and read-only BigQuery analytics. Each channel carries its own shared instructions and tool access, so a new teammate can tag Claude with no local setup.

“Claude posts its investigations and progress as an agent in the thread, which helps people see what it did and what still needs review,” Ciarla explained.

### One thread from screenshot to merge

On September 15, Ciarla posted a screenshot in \#ai-engineers showing divider lines spilling into Firecrawl’s navigation and tagged @Claude. Claude traced the problem to four settings cards and had a pull request up 9 minutes 30 seconds later with 127 unit tests passing. Because the live page sat behind a login, it reported that it had checked the layout on an isolated copy, so Ciarla knew what was still unverified. He reviewed and merged the fix less than 18 minutes after posting the screenshot.

The thread works for requests from outside engineering too. Micah Stairs, Head of Support Engineering, asked Claude for a way to look up teams by their slug, a short text identifier, in his team’s admin panel, and Gaurav Chadha, a Developer Support Engineer, tested the pull request. Chadha found that generated default slugs needed to work too, and Claude updated the same pull request. The change merged about three hours after the first request, all in one conversation.

The thread also keeps wrong turns visible. In Firecrawl’s agent product, a follow-up question was showing the previous answer’s results table. Claude first blamed how the frontend polled for results, while flagging the server as a possibility. When Claude tested its own fix, the bug was still there, so it kept looking and found the real cause in the agent’s backend sandbox, which saved files one folder too deep. Its nine-line fix passed all four production QA checks, and the team closed the frontend pull request instead of shipping a fix that wouldn’t have worked.

## The outcome

### Investigations the whole team can steer

Since late June, Claude has opened 773 pull requests through Claude Tag, and as of November 5 the team had reviewed and merged 620 of them. For a company of about 40 people, that averages more than 30 merged changes a week, and the pace is growing: in October alone, Claude opened 310 pull requests through Claude Tag and the team merged 252.

Work also moves between people differently: support engineers now take their own tool requests to a merged fix in a single thread. “A teammate can start an investigation in Slack and leave the working context visible for someone else to steer,” Ciarla said. “The AI session can become part of a team handoff.”

Next, the team is building more systematic pull request testing. “I would like to extend the workflows that help across the company, from gathering research to preparing launch material and answering questions about our data,” he noted.

## Related stories


### A conversation with Jaclyn Rice Nelson and Pooja Brown about scaling Tribe AI on Claude


### Zendesk built custom agents on Claude and reached 1 million agent executions in 7 weeks


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud
