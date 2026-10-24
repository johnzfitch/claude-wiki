---
title: "Testing safety defenses with a bug bounty \\ Anthropic"
source_url: "https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:15Z"
tags: ["news-research", "testing"]
---

# Testing our safety defenses with a new bug bounty program

- Published

  May 14, 2025

- Category

  [Safeguards](safeguards.md)

- Topics

  - [Jailbreaks](https://www.anthropic.com/search?topic=jailbreaks)
  - [Red teaming](https://www.anthropic.com/search?topic=red-teaming)
  - [Constitutional AI](https://www.anthropic.com/search?topic=constitutional-ai)
  - [CBRN risks](https://www.anthropic.com/search?topic=cbrn-risks)
  - [Responsible Scaling Policy](https://www.anthropic.com/search?topic=responsible-scaling-policy)
  - [Safeguards](https://www.anthropic.com/search?topic=safeguards)

  See more...

Related articles

- Alignment

  Jan 9, 2026

  [Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks](next-generation-constitutional-classifiers.md)

[View more](https://www.anthropic.com/search?topic=jailbreaks)

Today, we're launching a new bug bounty program to stress-test our latest safety measures. Similar to the program we announced last [summer](model-safety-bug-bounty.md), we're challenging researchers to find universal jailbreaks in safety classifiers that we haven't yet deployed publicly. These safeguards are part of the advanced protections we’ve developed to help us meet the AI Safety Level-3 (ASL-3) Deployment Standard as part of our [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md), the framework that governs how we develop and deploy increasingly capable AI models safely.

The bug bounty program, which is in partnership with [HackerOne](https://www.hackerone.com/), will test an updated version of our [Constitutional Classifiers](constitutional-classifiers.md) system. Constitutional Classifiers are a technique we built to guard against jailbreaks that could elicit information related to CBRN (chemical, biological, radiological, and nuclear) weapons. This system follows a list of principles that define what type of content should and shouldn’t be allowed when interacting with Claude, and focus narrowly on specific harms.

Participants will receive early access to test our classifiers on Claude 3.7 Sonnet. We’re offering bounty rewards up to \$25,000 for verified universal jailbreaks found on the unreleased system. A universal jailbreak is a vulnerability that consistently bypasses Claude’s safety measures across many topics. For this initiative, we're interested in universal jailbreaks that could be exploited to enable misuse on CBRN-related topics.

Our models are becoming increasingly capable, and as we’ve [shared before](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf), we believe some future models may require the advanced ASL-3 security and safety protections outlined in our Responsible Scaling Policy. This bug bounty initiative will help contribute to the work we’ve done over the last several months to iterate and stress-test our ASL-3 safeguards.

We’ve kicked off this new bug bounty initiative with participation from the researchers who joined our earlier program last year and are offering the opportunity for new researchers to participate. If you're an experienced red teamer or have demonstrated expertise in identifying jailbreaks in language models, we encourage you to apply for an invitation through our [application form](https://forms.gle/3ocTorSkkuvcGePn9). Detailed instructions and feedback will be shared with selected participants. Applications open today, and the program will run through Sunday, May 18. This initiative is invite-only so we can respond to submissions with timely feedback.

We're grateful to the security community for its partnership in helping us make AI systems safer.

### Update on May 22, 2025

The bug bounty program in this post has concluded. Participants will transition to a new bug bounty initiative we’re rolling out today that’s focused on stress-testing our [Constitutional Classifiers system](constitutional-classifiers.md) on the new Claude Opus 4 model and testing other safety systems we may develop. We’re still accepting applications to participate in this new invite-only program. You can apply for an invite through our [application form](https://forms.gle/3ocTorSkkuvcGePn9).

To further advance AI safety, we are also accepting reports of universal jailbreaks for ASL-3 uses of concern (meaning those which elicit information related to biological threats) found on public platforms or forums, such as social media. For more information, see [here](https://docs.google.com/forms/d/e/1FAIpQLSfJAE2lJC0uKkkrKemR2ef_Q0yFFqiwjzcSE4lzMTdDQDuPcQ/viewform).
