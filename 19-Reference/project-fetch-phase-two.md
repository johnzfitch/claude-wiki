---
title: "Project Fetch: Phase two \\ Anthropic"
source_url: "https://www.anthropic.com/research/project-fetch-phase-two"
category: "19-Reference"
fetched_at: "2026-08-02T07:11:00Z"
tags: ["news-research"]
---

# Project Fetch: Phase two

Jun 18, 2026

*Michael Ilie, C. Daniel Freeman, and Kevin K. Troy*

In August 2025, we ran an [experiment](project-fetch-robot-dog.md) to see how much Claude could help Anthropic employees—who were not robotics experts—perform sophisticated (and amusing) tasks with an off-the-shelf robotic quadruped (henceforth, a robodog). We called this Project Fetch. We found that access to our state-of-the-art model at the time (Claude Opus 4.1) helped one team substantially outperform the other, who had to rely only on the internet and their own ingenuity. The Claude-enabled team got more done, faster.

Before we dragged our colleagues to a warehouse for the experiment, we double checked whether Opus 4.1 could do the tasks entirely on its own. Unquestionably, it could not. Much like our team without Claude, it got hung up on the preliminary task of figuring out how to connect to the robot.

But AI models are moving fast—even faster than the runaway robodog that almost rammed into one of our human teams back in August.

We figured it was time to revisit Project Fetch to see if our newer models could outperform the previous generation. Not only did they do that, but **Claude Opus 4.7—operating without human assistance—was about 20 times faster than the fastest human team at all tasks completed by our participants less than a year ago**.

This doesn’t mean that LLMs have now solved robotics. Far from it. The latest Claude models still struggled with using the robot to precisely move the beach ball—the “fetching” part of Project Fetch. And none of the tasks in these experiments implicate the more challenging, low-level elements of robotic control, such as developing a specific actuation policy. However, once again, we are seeing a pattern whereby first, models are helpful to humans. Then, humans are helpful to models. Finally, models are largely able to do things themselves. We have seen this in [cybersecurity](2026-mythos-preview.md) and now the same dynamics are starting to take shape at the intersection of AI and the physical world.

## What did we do?

The original Project Fetch had teams of Anthropic employees (randomly assigned to work with or without Claude) do the following steps: operate the robodog using the manufacturer-provided controller, connect to the robodog’s video and lidar sensors, write and operate a program to manually control the robodog, develop a way to monitor the robodog’s path through space, write a program to detect the beach ball, and finally put it all together to autonomously retrieve the ball.

For this autonomous update, we couldn’t ask Claude to use a physical controller, nor did we evaluate the time it took a researcher to use the Claude-programmed controller to retrieve the ball (though we did confirm that it worked as intended). On the remaining subset of tasks, we ran three trials of Opus 4.7 using adaptive thinking with effort set to maximum in Claude Code. We measured the elapsed time for each objective and qualitatively assessed the models’ success.

The role of our researcher was limited to plugging a laptop running Claude Code into the robodog, entering the initial prompt, approving commands, and approving the model to go to the next task.

## Where did Claude excel?

Very simply: on every task that was completed by at least one human team in August, Opus 4.7 completed the same task at least ten times faster.¹ If you consider the four tasks that were completed by both human teams, Opus 4.7 was, on average, more than 37 times faster than Team Claude-less and more than 18 times faster than Team Claude.

The table compares the speed of the original teams (Team Claude and Team Claude-less) to Opus 4.7 on all of the tasks we tested as part of Phase Two.

Whereas the humans struggled to choose between multiple different approaches to interface with the dog’s sensors, Opus 4.7 was able to quickly identify the best path. Much of the code it wrote was effective on the first try (which was not the case for Team Claude or Team Claude-less in the original experiment). Indeed, we can see evidence of Opus 4.7’s efficiency when we look at the volume of code it generated: it was as or more successful than both human teams while producing almost ten times less code than Team Claude.

Opus 4.7 was not perfect. For example, it defaulted to using an outdated object detection algorithm. But even then, it was able to work around this and arrive at an effective solution.

We observed little within-task variance (in absolute terms) on completion times for steps the model finished. (Though the aforementioned suboptimal algorithm selection is likely why one of the beach ball detection trials took substantially longer than the others.) Overall, for the tasks in this experiment within its capability envelope, Claude is now quite reliable. (See the next section for an analysis of what Claude is still unable to do.)

It is worth underscoring (as we did in our previous post) that this progress is not the result of a concerted effort to improve the robotics capabilities of our models. These improvements, like so many others in the history of LLM development, have emerged from much more general scaling.

## Where did Claude struggle?

When using their hands, and with some practice, our humans were able to pilot the robodogs to gently nudge a beach ball back to the home base (a patch of fake grass) where the robots started. This required the ability to quickly perceive if the ball had gone off course, how that error related to the previous command, where the ball was now, and then how to adjust future inputs to more precisely move the ball. This is a kind of closed loop at which people excel (at least after making some mistakes and learning from them).

In our Phase Two experiments, Claude struggled to capture this subtlety. Like the humans who reached the phase of needing to write a program for autonomous beach ball retrieval, Claude was able to move the robot behind the ball and position it to knock the ball back to the starting point. But the efforts to do so were poorly controlled and (again, like our human participants) not successful.

One of our researchers with more robotics experience than our Phase One volunteers successfully accomplished the task of programming autonomous fetching. With more time and additional scaffolding, we think it is very likely that current generations of Claude could do the same. What we will be watching for next, though, is the ability of the models to accomplish this final task with the same speed and reliability they displayed on the other elements of Project Fetch.

## What does this mean?

Writing about Phase One, we emphasized how LLMs could provide uplift to non-expert humans needing to use robots. This is even more true now than before. Models now complete what was previously pair-programming work between humans and models much more quickly by themselves, which means that people can more quickly transition to controlling and using the robots. And for some tasks, a human in the loop controlling the robot may still outstrip the AI model with its (virtual) hand on the D-pad.

What is interesting and different is that we now seem much closer to a world where models will be able to use off-the-shelf physical tools with relative ease—at least for limited purposes. This is similar to how AI models used existing software editing tools like string-replace when they made the transition to more agentic coding. We are plausibly entering the early era of *physical* agentic AI.

More research is needed to understand models’ ability to make these physical tools more bespoke, whether by writing control policies tailored to particular tasks or by designing robotic systems. And there may be substantial barriers to this more generalized vision of physically capable and adaptable language models. But as we have seen, apparently large distances in model capability can be traversed quickly. Models building their own software tools might have seemed outlandish not long ago, but it is happening. It would be unwise to rule out the same trajectory in hardware.

*Updated Jun 18:* Corrected the date of the first phase of Project Fetch.

#### Footnotes

1.  We report results from Claude Opus 4.7 because it was our most advanced non-Mythos-class model at the time we ran this experiment. Preliminary trials with Claude Mythos Preview showed that it would not provide an apples-to-apples comparison with other models because of how we had set up the experiment and how the model was served.


## Related content

### Discovering cryptographic weaknesses with Claude

cryptographic algorithms. The first attack significantly weakens HAWK, a digital signature scheme that was built for a future world where quantum computers are able to break existing standards. The second identifies a new way to attack round-reduced AES, the most widely used symmetric cipher.

[Read more](discovering-cryptographic-weaknesses.md)

### Project Pilot: Can AI control a drone?

Working with Andon Labs, we’ve developed a new series of evaluations that assess AI models’ ability to use a flying drone, culminating in a new benchmark: Drone-Bench.

[Read more](project-pilot.md)

### How Canada uses Claude: Findings from the Anthropic Economic Index

[Read more](how-canada-uses-claude.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

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
- [Claude for Chrome](https://claude.com/chrome)
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
- [Courses](https://www.anthropic.com/learn)
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
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
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
