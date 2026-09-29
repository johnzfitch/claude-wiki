---
title: "Cyera Claude Cowork case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/cyera-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:55Z"
tags: ["agents", "case-studies", "claude-code", "enterprise", "security"]
---

# Cyera on making Claude Cowork the front door to 40 tools

[Try Claude](https://claude.ai)

Industry:  
Cybersecurity

Company size:  
Large

Product:  
[Claude Cowork](../15-Claude-AI-Features/product-cowork.md)[Claude Enterprise](enterprise.md)

Partner:  
AWS

Location:  
North America

40 tools connected

to Claude Cowork

88% weekly active usage

of Claude

Case Study: Cyera

Read how Cyera scales agentic AI across 1,500 employees with Claude Enterprise.

[Read more](cyera.md)

[Cyera's](https://www.cyera.com/) AI security platform finds and classifies an enterprise's data, mapping what's sensitive, where it lives, and who can access it. Inside the company, everyone has Claude access; R&D using Claude Code primarily and everyone else using Claude Cowork, which Cyera has connected to 40 tools across its stack. We spoke with Joe Tustin, Cyera's Principal Technologist for Applied AI, and Steve Klementowski, VP of AI, about why the company standardized on Cowork, the workflows teams have built with it, and what it takes to bring 1,500 people along.

## Anthropic: Claude Code took off with your engineers first. What happened when it started spreading beyond R&D?

**Joe Tustin, Cyera:** When I joined last year, it was R&D folks internally on Claude Code. I started bringing it over to non-R&D, and the challenge is education: how do you get non-technical people in the terminal? It was great to see them understand where they were from a file directory perspective, but they were scared to run commands and connect to Snowflake through an API. These were all new things for them.

I constantly say that if the only thing you have is a hammer, everything looks like a nail. In this new AI world, to have a toolbox that meets users where they are is incredibly important, so they can know how to use it and it just feels intuitive.

## Anthropic: So what tipped the decision to standardize on Claude Cowork?

**Steve Klementowski, Cyera:** We knew AI adoption was important to the company. We wanted a general-purpose agentic tool so that people could solve their own workflows. And the cat was out of the bag with Claude Code: it started to leak into non-R&D, they saw the promise of it, and they were asking for it. Cyera’s technical teams were already heavy Claude users, so it made the most sense to expand that tool to the whole company. There were some other tools out there, but there was not much for business users.

**Tustin:** I took a first stab at it and found some open-source projects. There's no shortage of code harnesses, but a UI that's not very clearly built by engineers is pretty hard to find. It makes a lot of sense for someone who understands what a routine is or what a cron job is. These things appear obvious, but if you've never done that before, you won't know how to use the tool. Once I saw Cowork, I said to myself, ‘Okay, this meets us exactly where we are.’

## Anthropic: A lot of the tools you've connected already have AI built in. Why route work through Claude Cowork instead of the AI inside each one?

**Tustin:** Claude is now the aggregator. Claude knows everything about me as an employee, and connected to the Snowflake tables and Salesforce data that we already have, all the Google Drive files, all the Slack conversations, along with everything else. Having Claude as the central force between everything, and the context of how they work, makes it much more powerful.

**Klementowski:** It's true of any tool that has AI built in: it's good for working in that tool sometimes. But we've connected 40 tools now to Claude, and we have built four or five homegrown MCP servers. It's tough to replicate that. You can only create so many central focal points.

## Anthropic: You’re at 88% adoption just a month or so after roll out. How did you make that happen?

**Klementowski:** A few things really made it successful. First was investing in employee enablement: about 20 department-specific sessions, office hours twice a week, as well as someone on call from the AI engineering and data side 24/7 to fix pressing issues. We even got creative with a day-long livestreaming session with Joe showing off all these capabilities of Cowork. Executive buy-in was also big, I had the chance to speak at a few all-hands about why we were doing this and when it was happening so everyone was prepared.

## Anthropic: Your marketing team runs more than 1,000 events a year. Walk us through what that looks like inside Cowork.

**Tustin:** Our marketing team runs everything from exec dinners to lunch and learns, all the way up to DataSecAI events, which include hundreds of executives, all over the country. Imagine running more than a thousand events: it’s a lot of spreadsheets and a lot of Slack messages.

A recent one was in New York. Marketing leadership queried all of Salesforce for the tri-state area, every single opportunity, every single contact, created a list of 3,500 people that fit the demographic we're going after, and then reached out to every single salesperson with their list. And now that's reported publicly within the Slack channel for the event. We went from maybe 105 attendee confirmations to over 400 in one day.

## Anthropic: You've also got agents talking to other agents in Asana. How does that work?

**Tustin:** Every week we'd have at least an hour-long meeting going through all the different tickets. Now everyone has their Asana agent, and the person who manages the Asana call, her agent goes out, hits everyone else's agents, and makes sure everything's up to date. That call runs so much smoother now. It saved her around 12 hours a week, which is insane, on top of everything else that she's doing. Communication is flowing, and Claude's doing that heavy lifting.

One thing I'm pushing very hard is that there are no more errors in tickets when they get submitted. I started to see, specifically for the design team, people were not attaching their Figma files, and this ticket that was supposed to be quite easy has now been back and forth four times because I didn't go and add in a URL. Now we have gatekeeper agents that check to see if there are any errors before the ticket is allowed to go into Asana.?

## Anthropic: Those are team systems. What are people building just for themselves?

**Tustin:** One of my favorites is our privacy and GRC analyst. He generates a ton of content, and it's extremely technical, but it becomes outdated quickly whenever a new policy is released, and it invalidates something he posted a while ago that he won’t think to update. Sales reaches out and lets him know that the content is now incorrect. Now he has his Claude agent. Anytime he posts something new, it scans every possible thing that's ever been posted within this domain, calls it out, opens up tickets, and assigns them to him to fix. Something he'd maybe do once a month is now running automatically every week.

**Klementowski:** I have a DM triage that I run manually. It looks through all of my DMs: has Steve responded yet? Does he need to respond? If I need to respond, it will go and do research in my calendar and Google Drive and Notion, past call recordings, and Snowflake, and it will draft a response for me. Then I just go into Slack and hit send. Per run it probably saves me 30 minutes.

## Anthropic: What happened when you opened up data analysis to the whole company?

**Klementowski:** People are going wild doing their own data analytics. It's this pent-up need for the ability to do data analysis. It's really helped scale our analytics team: they focus less on doing the analytics and more on how we provide people the data and the context around the data. Everyone in the company is doing self-service analytics now.

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Read more](../15-Claude-AI-Features/product-cowork.md)

## Anthropic: Self-service data analysis usually ends in spreadsheet sprawl. How do you keep it trustworthy?

**Klementowski:** We have a very strong data engineering team that has created a beautiful semantic layer over our go-to-market and enterprise data in Snowflake, which we connected directly to Claude. The data consists of 30 or 40 tables, all very well defined and documented. We have one schema per department, so we can control which tables different departments are getting, and we've implemented role-level security so people can't see data outside of their region.

We also have shared context on how to interpret the data: when we say monthly active users or ARR, what do we mean? We serve that as a Claude skill in every team plugin, so before anyone queries Snowflake, the skill fires and loads the context. We haven't quite cracked context management in Cowork yet, but it seems to be working pretty well.

It does present other challenges, like a proliferation of dashboards, and even with a great semantic layer the interpretation of data can be off. But directionally, if you can do self-service analytics and get something that helps point you in the right direction, that's amazing. That's a very hidden velocity gain for the company.

## Anthropic: What's the internal reception been like? Not everyone loves being handed a new tool.

**Tustin:** The whole spectrum. Some people were already Claude users or using some sort of AI, so once we enabled it, there was a huge spike in users. The other group has been very interesting: it's a new tool and they don't trust it. We hosted 18 hours of livestreaming where people could come in whenever, and we just sat there and worked through problems. People worked with Claude live, and once they had the aha moment, it was, oh wow, I'm now prepped for my next call, and this is a big call.

People are finding it's not that it was never part of their job, but that they never had time to do that part of their job. Once people get to that point where they're like, now I'm creating things because I'm having fun, I think people are enjoying it a lot more.

**Klementowski:** Joe did an amazing full-day session, and the first section was a lot of reps who had never been in an agentic AI tool. So we have that cohort within the company, and we also have AI engineers who know ten times more than I can ever hope to know. It's super hard: how do you let AI fluent employees run while also bringing along the earlier adopters? That's one of the biggest challenges I think we'll continue to face in the next few months.

## Anthropic: Where does this go next for Cyera?

**Klementowski:** Claude Cowork is great for being a personal agent.

**Tustin:** There's different functionality that's required for some more teamwork, like a team agent. One thing I'm seeing often is that for folks who support executives, their agents produce a lot of work. What happens when that person goes on vacation and their laptop isn't open any longer? Maybe there's a graduation process that needs to take place for agents: from an agent one person uses to something the whole business can use without their help. Graduation is an earned process that uses traditional software engineering gates to make sure agents last.

## Anthropic: What advice would you give another company rolling out agentic AI this broadly?

**Tustin:** Really make sure that leaders understand that learning these tools requires time, and that time is either going to come from the work bucket or the personal bucket. We want people to be really proficient at using AI, so we have to invest in enablement.

If you're worried about shadow AI, create a sandbox environment to test in. I don't think shadow AI is a bad metric. It shows you have innovative employees who see the possibilities in front of them.

## Related stories


### Vega's cyber defense platform returns 67% of analysts' time with Claude


### Cyera scales agentic AI across 1,500 employees with Claude Enterprise


### Kai delivers preemptive exposure management with Claude


### How Artemis helps security teams cut incident resolution time by 96%

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
