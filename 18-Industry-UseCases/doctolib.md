---
title: "Doctolib Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/doctolib"
category: "18-Industry-UseCases"
fetched_at: "2026-11-18T06:28:52Z"
tags: ["case-studies", "claude-code"]
---

# Doctolib accelerates developer productivity with Claude Code

[Try Claude](https://claude.ai)

Industry:  
Healthcare

Company size:  
Large

Product:  
Claude Code

Location:  
Europe

47% more pull requests per engineer

handled on average between January and September 2026

25% shorter change lead time

across Doctolib engineering over the same period

Since 2013, Doctolib has been transforming healthcare across Europe, serving 580,000 health professionals and 90 million patients. The platform provides practitioners with an operating system that organizes their workflows through electronic health records, diagnostic support, prescription management, and AI-powered clinical solutions. Patient management tools handle scheduling, teleconsultation, and practice operations. For patients, Doctolib simplifies access to care with secure, proactive health management.

### With Claude, Doctolib:

- Raised the average number of pull requests each engineer handles by 47% between January and September 2026
- Cut change lead time by 25% over the same period
- Has about 90% of its roughly 900 tech and product staff using Claude every day
- Runs its own remote coding agents, built on Claude Code and powered by Claude Opus 5.5, which now open 10% of all pull requests
- Found in A/B tests that Opus 5.5 produced better results at 2.5 times lower cost per pull request than its previous default model
- Roughly halved the share of engineers’ time spent writing code over about a year, by internal estimates, shifting that time toward review and specifications
- Lets product managers and designers ship changes by describing what they want, with the agents handling the code
- Keeps technical documentation current automatically with every code change

## The challenge

### Keeping review up with the pace of code

Doctolib first brought in Claude Code to take repeatable work off engineers’ plates. Documentation, tests, pull request reviews, and technical debt kept pulling developers away from the problems that matter most on a healthcare platform. “Engineers were spending valuable time on repeatable tasks instead of solving complex healthcare challenges,” said Jean-Claude Kuo, Staff Product Manager at Doctolib.

That rollout worked, and it moved the bottleneck. Once writing code got faster, the hard part became everything around it: reviewing each change with the care healthcare software demands, checking it for privacy and security risk, and confirming it behaves once it ships. Those checks protect 580,000 health professionals and their patients, so cutting corners was never an option. Running every check on every change by hand was not realistic either. “Our goal is to implement comprehensive checks that humans cannot consistently perform due to time constraints,” said Nicolas Klarman, Staff Engineer at Doctolib.

## The solution

### Opus 5.5 for the work where quality is not negotiable

The foundation was already in place. After a pilot with 30 engineers, Doctolib rolled Claude Code out to its whole development team, and engineers self-onboard in under five minutes from VS Code, JetBrains, or the command line. The platform team maintains a shared repository of prompts, custom commands, and subagents that every engineer pulls at setup. Today, about 90% of Doctolib’s roughly 900 tech and product staff use Claude every day, and Claude Code remains the most-used AI tool in Doctolib engineering.

The team revisits its default configuration as new models arrive. “The Opus plan mode currently brings the best setup possible between quality of results and cost optimization,” Klarman noted.

The bigger decision concerned Doctolib’s remote coding agents, which handle pull request reviews, risk analysis, security checks, post-merge checks, and implementation. “For these tasks, the quality of the final result is not negotiable,” Kuo said. “We want to push adoption of the remote agents as the new default for delivery.”

To pick the model behind them, the team ran A/B tests across a set of real tasks. Opus 5.5 produced clearly better results than Sonnet 5.0, the agents’ previous default, at 2.5 times lower cost per pull request. Doctolib made Opus 5.5 the default for its remote agents and now favors it for high-impact tasks.

### Agents that carry a ticket from first change to production check

Doctolib’s own remote agents run on Claude Code in headless mode through GitHub Actions, and they work as a connected system rather than a set of single-purpose bots. Starting from one ticket, they generate a code change with the right context, update the pull request, work through feedback left in review comments, and run a full check once the code is in production. Their scope covers code review, risk assessment, documentation, and bug resolution. They now account for 10% of all pull requests at Doctolib, and for every bug identified, an agent proposes a fix. Half of those fixes are accepted and merged by the team that owns the affected product.

Review is changing shape too. Instead of one review agent, Doctolib is building a multi-agent risk assessment framework, with agents covering privacy, security, and other critical dimensions, to decide how much attention each change needs. “This approach allows us to collect concrete evidence of what works in practice, while progressively strengthening the security and reliability of our entire system,” Klarman explained.

The agents build on workflows that have run for more than a year. A scheduled job updates technical documentation with every code change, and automated Claude reviews run on Doctolib’s main infrastructure repository. Early on, the team used Claude Code to replace its entire legacy visual regression testing infrastructure. “We completed the migration in hours, not weeks,” Klarman said.

The agents are also opening delivery to people outside engineering. Because a pull request no longer has to belong to the person who writes the code, product managers and designers can ship changes by stating clearly what they want. The agent breaks the work down and adjusts the requirements to fit the codebase, best practices, and guardrails. It opens the pull request, keeps it current, and folds in feedback from human reviewers and review agents. Once the change is approved, the agent merges it and runs checks to confirm the outcome.

## The outcome

### More changes, moving faster, with closer review

Between January and September 2026, the average Doctolib engineer handled 47% more pull requests, while change lead time fell by 25%. Teams are shipping more, and each change spends less time waiting.

The work itself looks different. By Doctolib’s own estimates, writing code took 40 to 45% of an engineer’s time before AI. About a year later, it takes roughly 20%, and the time spent on review and specifications has grown. “Overall, this shift illustrates how Claude is helping our teams move from execution-heavy workflows toward more thoughtful, review-driven, and cross-functional ways of working,” Kuo said.

Doctolib’s next priorities follow the bottleneck. The team is replacing line-by-line code review with a risk-based model, where AI assesses how much scrutiny each change requires, and then turning to the stages after review: deploying and validating code.

“Our vision is a software factory where engineers build and maintain the agentic loops,” said Mike Aidane, VP of Platform Engineering at Doctolib. “Agents write most of the code. Engineers decide when to step in, steer, or raise a concern. The next step is focusing human attention where it matters most.”

## Related stories


### How League went all in on Claude in a regulated industry


### League cuts product development cycle times in half with Claude


### How can a medical lab keep patients at the center of its work while the caseload keeps growing?


### How Zingage automates care coordination for 400+ home care agencies with Claude
