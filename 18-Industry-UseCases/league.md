---
title: "League Claude case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/league"
category: "18-Industry-UseCases"
fetched_at: "2026-11-18T06:28:59Z"
tags: ["case-studies", "evaluation"]
---

# League cuts product development cycle times in half with Claude

[Try Claude](https://claude.ai)

Industry:  
Healthcare

Company size:  
Medium

Product:  
[Claude Enterprise](enterprise.md)[Claude Code](../15-Claude-AI-Features/product-claude-code.md)

Location:  
North America

Cycle times cut in half

from idea through pull request across League’s product organization

98% Claude adoption,

up from 80% when League’s company-wide rollout began

[League](https://league.com/) builds the consumer health experiences that health plans and providers put in front of their members. Over the past six months, the company has rebuilt itself around Claude: development cycle times are down by half, 98% adoption of AI tools, and processes from engineering to finance run on agents.

## With Claude, League:

- Cut product development cycle times in half, from idea through pull request
- 98% adoption of Claude, up from ~80% when the company-wide rollout began in March 2026
- Reduced vendor security risk assessments from multiple weeks to 15 minutes, with 49 of the last 53 validated as safe by Claude, and then signed off by a human.
- Runs overnight autonomous coding sessions through Swarm, League’s internal orchestration tool built on Claude Code
- Delivered a customer implementation two months ahead of schedule
- Automated more than 60 finance processes, built largely by the finance team itself
- Stood up the security foundation for company-wide AI access in under a quarter

## The challenge

## Finding efficiency in a regulated industry

League has spent almost 12 years building digital health experiences for organizations that answer to regulators: benefits navigation, care programs, and member apps that run on protected health information. Every new tool clears a high compliance bar before touching real work, which kept AI adoption cautious even as employees gained access to AI assistants. “We had those tools, and it was creating tiny little pockets of efficiency for people in their day-to-day,” said Signy Roland, AVP of AI Transformation at League. “But it wasn’t transformational by any means.”

Security reviews backed up about three weeks. Customer implementations ran on traditional healthcare timelines. League saw the market was headed towards agentic member experiences and knew that traditional software approaches would no longer be viable.

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Read more](https://claude.com/healthcare)

## The solution

## A company-wide commitment instead of a formal evaluation

That changed in December, when a new generation of Claude models arrived. Teams already experimenting saw a step change in what agents could carry, and leadership made a call that cut against enterprise habit. The usual enterprise move is a formal head-to-head evaluation, weeks of pitting tools against each other before committing. League decided to skip it. “The pace of change is so fast that your bake-off is going to be wrong as soon as you finish the bake-off,” explained Jordan Christensen, SVP, Data and AI Engineering. “We’d rather pick the direction we believe in and go deep.”

New releases keep proving the point. “I went into Fable the day it came out and started using it, and I was unlocked even further,” Christensen said of Claude Fable 5. “Anthropic keeps delivering and keeps opening up these new things. It was really changing the way that I was working.”  
  
League signed its Claude Enterprise agreement on a Friday and had the whole company live by Monday. The security work took longer, about a quarter. Patient data is kept in a separate environment that Claude does not have access to, and League placed strict limits on what agents could do as controls were put in place. “We’re a company that’s been around for almost 12 years, and it took us less than a quarter to stand up all of the security things we needed to become AI-native,” Roland said.

## Shipping to production in 48 hours

The forcing function came in March: a 48-hour company event League named the Accelatron. “It was not a hackathon,” said Dan Galperin, CTO and co-founder. “The brief was: go into your backlogs, take real problems, and see if you can get from the backlog to production in 48 hours.” Teams shipped real fixes and features that week, and the event set the expectation: this is the new normal speed.

Two-week sprints gave way to micro-sprints: pods of three or four people scoping, building, and landing production-ready code behind a feature flag in a single sitting. “What we would have called two weeks of scope, we now practice doing in three hours,” Galperin added. For larger builds, engineers turn to Swarm, League’s internal orchestration tool built on the Claude Platform. A lead agent breaks the work down and spawns a team of agents to execute it in parallel, running overnight. An engineer reviews the work the next morning. To prevent review from becoming the bottleneck, a principal engineer built a Claude-based bot that triages every pull request by the scale of the change and the risk.

15 minutes

for a Claude skill to complete vendor security risk assessments, down from weeks

## The outcome

## Everyone becomes a product developer

Adoption outside engineering didn’t need a mandate. League’s chief operating officer scheduled Claude to run tasks overnight, and when the results started appearing in Slack, the most common reply was a request for access. The finance team has since automated more than 60 of its own processes. A designer who kept spotting UI bugs mentioned never having opened a pull request; the answer was to ask Claude to open one, and designers now ship fixes directly. “The walls between the functions are coming down,” Galperin explained. “Everyone is becoming a product developer.”

The same shift cleared operational backlogs. A Claude skill now completes vendor security risk assessments that used to take multiple weeks in 15 minutes, with 49 of the last 53 assessments validated as safe by Claude, and then signed off by a human. The security team’s response times went down from 3+ weeks to a few hours. “Nothing is intimidating anymore,” said Roland, who has led the rollout without a technical background. “I actually love every aspect of my job now.”

## Half the cycle time and 98% AI-authored code

In the four months since the Accelatron, cycle times from idea through pull request have fallen by half, and the share of code that is AI-authored has climbed from roughly 70% to 98%, tracked on the company’s engineering metrics platform. Engineers merge roughly two to three times as many pull requests per week as before the rollout.

Customers feel the speed directly. One customer implementation landed two months ahead of schedule, and when a health plan needed a more streamlined way to coordinate non-emergency medical transportation across tens of thousands of member requests, League designed and built a working demo agent in days. “Before, we would show up with a PowerPoint or a Figma prototype,” Galperin noted. “Now we’re showing up with the working prototype.”

That capacity is changing what League considers a reasonable bet. “How ambitious can we be?” Christensen said. “Let’s take the constraints off, while still maintaining the level of safety our industry requires.”

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/product-claude-code.md)

## Related stories


### How League went all in on Claude in a regulated industry


### How can a medical lab keep patients at the center of its work while the caseload keeps growing?


### How Zingage automates care coordination for 400+ home care agencies with Claude


### A conversation with Seth Hain about Epic’s internal AI adoption
