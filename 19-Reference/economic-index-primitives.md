---
title: "Economic Index: New building blocks for AI use \\ Anthropic"
source_url: "https://www.anthropic.com/news/economic-index-primitives"
category: "19-Reference"
fetched_at: "2026-09-30T06:32:25Z"
tags: ["news-research"]
---

# Anthropic Economic Index: New building blocks for understanding AI use

Jan 15, 2026

[Read the full report](anthropic-economic-index-january-2026-report.md)

Is artificial intelligence really making people faster at work? What sort of tasks does AI support best? And how might it change the nature of people’s occupations?

At Anthropic, we’re measuring real-world AI use on an ongoing basis to answer questions exactly like these. Our privacy-preserving [analysis method](clio.md) allows us to learn more about conversations on [Claude.ai](http://claude.ai/redirect/website.v1.07a8bfc3-a24d-4467-9a8b-549ca087f428) (capturing uses by consumers) and our first-party API (mostly capturing uses by businesses).^([1](#footnote-1)) In past reports, we’ve assessed AI tasks by [occupation and wage level](the-anthropic-economic-index.md), looked more closely at [software development](impact-software-development.md), and studied AI use [by country and by US state](economic-index-geography.md).

We’re now adding a new level of detail to our Economic Index. In our fourth report, we’re introducing what we’ve called **economic primitives**: a set of five simple, foundational measurements to track the economic impacts of Claude over time. Our initial set includes task complexity, skill level, purpose (work, education, or personal use), AI autonomy, and success.^([2](#footnote-2)) We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample for this report.

These primitives provide a leading indicator of AI’s potential economic impacts—and allow us to answer far more complex questions about how AI is already changing jobs. Our latest report, which samples conversations from November 2025 (predominantly using Claude Sonnet 4.5), uses our primitives to explore a wide range of questions that we wouldn’t otherwise be able to answer—including how Claude’s task-level success rates change for more complex tasks, and whether the use of Claude to date might portend a net-deskilling effect on many jobs.

You can read the fourth Economic Index report [here](anthropic-economic-index-january-2026-report.md). Below, we summarize its results.

## **What we’ve learned from our economic primitives**

We applied our economic primitives to questions about individual tasks, occupations, and then the possible aggregate impacts of the changes we observe. (Our full methodology—including details on how we tested the accuracy of our primitives—is described in chapter two of the [full report](https://www.anthropic.com/news/anthropic.com/research/anthropic-economic-index-january-2026-report).)

### Tasks

#### **Which tasks does AI speed up, and by how much?**

We found that more complex tasks were sped up the most by Claude. We measure this by what Claude estimates as the number of years of schooling required to understand the conversation’s inputs: in Claude.ai, tasks with prompts requiring a high school education (12 years) were sped up by a factor of 9, while those requiring a college degree (16 years) were sped up by a factor of 12. (On the API, the speedup was greater still.) These results imply that AI’s productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the [evidence](https://www.nber.org/papers/w32966) that white collar professionals are more likely to use AI at work.

This same trend holds—albeit in weaker form—when we adjust for tasks’ success rates. Claude successfully completes tasks that require a college degree 66% of the time, compared to 70% for those tasks that require less than a high school education. This reduces, but doesn’t eliminate, the overall effect: Claude’s impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate.

#### **What are the time horizons over which Claude can support tasks?**

[METR](https://metr.org/)’s measure of AI’s [task horizons](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) shows that longer tasks are harder for AI models to complete. But the length of time over which AI models can work is steadily increasing as models get better: this measure has now become a key indicator of AI progress.

We’re able to complement METR’s analysis using our economic primitives. In the graph below, we show Claude’s task-level success rates relative to the amount of time a human would take to do the same task, both on [Claude.ai](http://claude.ai/redirect/website.v1.07a8bfc3-a24d-4467-9a8b-549ca087f428) and on our API:

METR’s benchmark suggests that Claude Sonnet 4.5 (the model in our own analysis) achieves 50% success rates on tasks of 2 hours. By contrast, our own API data finds that Claude is 50% successful at tasks that take nearly twice as long (around 3.5 hours), and on Claude.ai, the duration is vastly longer still—around 19 hours. But this might not be as discordant as it seems: our methodology is different to METR’s in some important ways. In our sample, users can break down complex tasks into smaller steps, creating a feedback loop that allows Claude to correct course. And rather than a fixed set of tasks, our sample contains a form of selection bias: users bring tasks to Claude that they’re more confident will work.

Our analysis shows how Claude’s *effective* time horizons might look different to those found in a study with a consistent set of tasks. We’ll track this indicator in further reports.

#### **How does the nature of Claude’s work vary across countries?**

We find that Claude completes very different kinds of tasks in countries at different stages of economic development. In countries with higher GDP per capita, Claude is used much more frequently for work or for personal use—whereas countries at the other end of the spectrum are more likely to use it for educational coursework. This fits a straightforward “adoption curve” story, in which lower-income countries show a large share of AI use on education and on a smaller number of work tasks, while AI use diversifies towards personal purposes as countries become richer.

These results align with recent work [by Microsoft](http://microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf) that associates AI use in education with lower per-capita income, and AI use for leisure with higher incomes. Our [recent partnership](rwandan-government-partnership-ai-education.md) with the Rwandan government and ALX, a technology training provider, is designed with this in mind: participants begin by developing AI literacy, and we’re piloting a program for granting some graduates year-long access to Claude Pro, supporting the transition from educational use to a broader range of applications.

### Occupations

#### **Coverage**

In our [first report](the-anthropic-economic-index.md), with data from January 2025, we found that 36% of jobs in our sample saw Claude being used for at least a quarter of their tasks. Pooling data across reports, this has risen to 49%. But once we account for Claude’s *success* *rate* (which we weight according to how often workers do that task and how long the task takes), we get a different picture of which jobs are most affected by the use of AI.

On the graph below, we plot that earlier measure of occupations’ task coverage along the *x* axis, and our new, adjusted measure on the *y* axis. Although the two are certainly correlated, we now find that some occupations (like data entry keyers and radiologists) are much more heavily affected by AI than task coverage alone would suggest, while others (like teachers and software developers) are relatively less affected.

That said, even our revised assessment is still limited: we only assess tasks that are performed on Claude.ai, and it’s not always clear how these conversations might map onto changes in the real world. This is an area we plan to dig into further in future.

#### **Task content**

A further question we asked is whether the tasks that AI covers represent the higher- or the lower-skilled components of a given occupation. Using an estimate that we create of the skill level required for each task, we find that Claude is relatively more likely to cover the tasks that require *higher* education levels—specifically, tasks that require an average of 14.4 years of education (equivalent to a US associate’s degree), relative to the economy’s average of 13.2 (shown below). This aligns with our earlier finding that Claude is used more frequently by white-collar workers.

As an experiment, we estimated how removing these Claude-covered tasks would shift the task composition of people’s jobs. As a first-order effect, this would *deskill* jobs on average, since it would remove those higher-education tasks. Professions like technical writers, travel agents, and teachers would be affected (as we discuss further in [the report](https://www.anthropic.com/news/anthropic.com/research/anthropic-economic-index-january-2026-report)), though a rarer few (like real estate managers) would see effects going the other way.

We’re not necessarily *predicting* that this deskilling will occur: it’s possible that *even if* AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn’t account for. (Of course, as models improve, the composition of tasks that AI covers will change, too.) That said, we think this offers a useful signal as to the most immediate effects that AI might have on occupations in the near future.^([3](#footnote-3))

### **Aggregate impact**

In our earlier research, we [estimated](estimating-productivity-gains.md) that the widespread adoption of AI could increase US labor productivity growth by 1.8 percentage points per year over the next ten years—around double the trend rate. Our new primitives allow us to revisit this analysis.

Based on our estimates of task speedups alone, we replicated our earlier finding of a 1.8 percentage point increase (even when we added in our API data). But when we account for task *reliability*—that is, when we adjust our estimate of task-level time savings by the probability that the task is *successful*, our estimate falls by about one-third for tasks completed on [Claude.ai](http://claude.ai/redirect/website.v1.07a8bfc3-a24d-4467-9a8b-549ca087f428) (to 1.2 percentage points per year), and by slightly more (to 1.0 percentage points) for the typically more challenging tasks completed on our API.

Even a 1 percentage point increase in annual labor productivity growth would still be notable: it would return US productivity growth to the rates of the late 1990s and early 2000s. And, as we mentioned in our [earlier research](estimating-productivity-gains.md), this top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher. Indeed, since our survey, Claude has become substantially more powerful, with the release of Claude Opus 4.5.

## **Updates on our previous measures**

In addition to our primitives, we collected a new round of data on the measures we’ve been tracking in our previous reports. This allows us to pick out trends in AI use over the course of 2025, from January to November. Here, we mostly find only small evolutions from the results of previous analyses, which pointed to an uneven distribution of Claude use.

First, we find that the use of Claude has remained highly concentrated among certain tasks: even though our sample includes 3,000 unique work tasks on Claude.ai, the top ten account for 24% of the set, which has steadily increased from 21% in January 2025. More specifically, computer and mathematical tasks continue to dominate Claude use: they’re about a third of all conversations on Claude.ai, and nearly half of our API traffic.

Second, our new report finds that augmentation (52% of conversations) has overtaken automation (45%) as the most popular pattern of interaction with Claude on [Claude.ai](http://claude.ai/redirect/website.v1.07a8bfc3-a24d-4467-9a8b-549ca087f428). This is a reversal of what we saw in our August sample (when automation led by 49% to 47%), but, when we assess this question over a longer time-frame, we still see a slow rise in *automation*’s share of tasks: augmentation led by 55% to 41% in January of last year, and by 55% to 42% in March.

Third, our latest analysis shows that the geographic concentration of AI use (as we [discussed last time](economic-index-geography.md)) remains evident. The US, India, Japan, the UK, and South Korea still lead in overall Claude.ai use, and adoption remains well-explained by GDP per capita. That said, in the US, we’ve observed greater changes: Claude use has become noticeably more evenly distributed across US states. In fact, if this trend was sustained, our model predicts that Claude use would be equalized across the country within two to five years. We discuss this model in more detail [in the report](https://www.anthropic.com/news/anthropic.com/research/anthropic-economic-index-january-2026-report).

## **Conclusion**

The most immediate conclusion from our latest Economic Index report is that the impact of AI on the global workforce remains a highly uneven one: AI use remains concentrated in specific countries and occupations, and it affects some occupations in a very different way to others, as the evidence on task coverage suggests.

More generally, this report has given us a new baseline against which to compare our future surveys. As Claude improves, we expect it’ll be asked to take on harder tasks, and that it’ll likely find greater success. We also expect that tasks might move from [Claude.ai](http://claude.ai/redirect/website.v1.07a8bfc3-a24d-4467-9a8b-549ca087f428) to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it’ll give us another possible indication of coming economic impacts, given the importance of business adoption for AI’s effect on productivity. Through our primitives, we’ll be able to measure how changes like these are beginning to impact real-world outcomes, including the nature of people’s work, and which people (and where) are likely to be most affected during this period of rapid technological transition.

In the meantime, researchers, journalists, and the public can use our data to inform their own research and thinking, and to provide an empirical foundation for the potential policy responses we might need. For much more detail on each of the areas we’ve discussed above, see our [full report](anthropic-economic-index-january-2026-report.md).

#### Footnotes

1.  As with previous reports, all our analysis is based on privacy-preserving analysis. Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as “consumer data” since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as “enterprise data” since it mostly represents enterprise use).[](#footnote-ref-1)
2.  More specifically,
    1.  **Task complexity** captures that tasks can vary in their complexity, including how long they take to complete and how difficult they are. A "debugging" task in O\*NET could refer to Claude fixing a small error in a function or comprehensively refactoring a codebase—with very different implications for labor demand. We measure complexity through estimated human time to complete tasks without AI, time spent completing tasks with AI, and whether users handle multiple tasks within a single conversation.
    2.  **Human and AI skills** address how automation interacts with skill levels. If AI disproportionately substitutes for tasks requiring less expertise while complementing higher-skilled work, it could be another form of skill-biased technical change—increasing demand for highly skilled workers while displacing lower skilled workers. We measure whether users could have completed tasks without Claude, and the years of education needed to understand both user prompts and Claude's responses.
    3.  **Use case** distinguishes professional, educational, and personal use. Labor market effects most directly follow from workplace use, while educational use may signal where the future workforce is building AI-complementary skills.
    4.  **AI autonomy** measures the degree to which users delegate decision-making to Claude. Our latest report documented rising "directive" use where users delegate tasks entirely. Tracking autonomy levels—from active collaboration to full delegation—helps forecast the pace of automation.
    5.  **Task success** measures Claude’s assessment of whether Claude completes tasks successfully. Task success helps assess whether tasks can be automated effectively (can a task be automated at all?) and efficiently (how many attempts would it take to automate a task?). That is, task success matters for both the feasibility and the cost of automating labor tasks.

    [](#footnote-ref-2)
3.  Indeed, some [historical evidence](https://www.michaelwebb.co/webb_ai.pdf) suggests that when technologies automating job tasks appear in patent data, employment and wages subsequently fall for exposed occupations.[](#footnote-ref-3)


## Related content

### What do you want from AI?

We’re launching a new study using Anthropic Interviewer to learn from your experiences with AI, and we invite you to participate.

[Read more](your-thoughts-on-ai.md)

### GLM-5.3 and the spread of advanced cyber capabilities

Like Claude Mythos Preview, GLM-5.3 has strong capabilities for autonomously building end-to-end cyber exploits. But GLM-5.3 is unlike other frontier models in that it has been released without meaningful safeguards to limit misuse.

[Read more](glm-5-3-and-the-spread-of-advanced-cyber-capabilities.md)

### Yes, Claude can do Nine Loops

Guest writer and physicist Matt von Hippel shares what happened when he issued a challenge to AI companies to solve a problem in his former subfield of theoretical physics.

[Read more](yes-claude-can-do-nine-loops.md)

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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

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
- [Sales](../18-Industry-UseCases/sales.md)
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
- [Developer blog](https://claude.dev)
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
