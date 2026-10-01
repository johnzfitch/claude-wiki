---
title: "Measuring LLMs' impact on N-day exploits \\ Anthropic"
source_url: "https://www.anthropic.com/research/n-days"
category: "19-Reference"
fetched_at: "2026-09-10T06:44:07Z"
tags: ["news-research"]
---

# Measuring LLMs’ impact on N-day exploits

Jun 8, 2026

*Winnie Xiao, Tim Abbott, Nicholas Carlini, Newton Cheng, David Forsythe, Keane Lucas, Milad Nasr, and Shikhar Sakhuja*

For the last few months, we’ve been writing about large language models’ cybersecurity capabilities. For the most part, we’ve [focused on](2026-mythos-preview.md) zero-days—vulnerabilities that are unknown to the software’s maintainers. But a large fraction of [real-world harm](https://www.verizon.com/business/resources/reports/2026-dbir-data-breach-investigations-report.pdf) comes from *N-days*: vulnerabilities that have already been publicly disclosed, but only patched on some devices. Attackers exploit the many systems that haven't yet applied the patch, during what’s known as the “patch gap.”

In some ways, N-days are the more dangerous of the two, because the patch itself provides a roadmap to the bug. Once software vendors publish their security updates, attackers can “patch diff”: compare the pre-patched source code or binary against the new one to locate exactly what changed, and then reverse-engineer the vulnerability that the patch was meant to fix. This means that a working exploit is often simply a matter of time.

Historically, patch diffing has been slow, specialized work, which bought defenders time to roll out their updates widely. The incidents that most defenders remember took several weeks: [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) hit 59 days after [MS17-010](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010) in 2017, and the public exploit for [Citrix Bleed](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-325a) in 2023 took about two weeks. In Mandiant’s [2020 analysis](https://cloud.google.com/blog/topics/threat-intelligence/time-between-disclosure-patch-release-and-vulnerability-exploitation) on N-days, 16 of the 25 vulnerabilities took a month or more to exploit.

In this post, we evaluate how much large language models can accelerate and automate the process of developing N-day exploits. Exploit development is not the only step in a real N-day campaign (target discovery, delivering the exploit to the target, and detection evasion all take time and resources too), but historically it has been the step most bottlenecked by scarce reverse engineering expertise.

With frontier models, this bottleneck has largely fallen away. Across 18 recent Firefox security patches, Claude Mythos Preview, our most capable model, built 8 working code-execution exploits autonomously. And on 21 Windows kernel patches—where the source code is not available—it produced 8 full exploit chains that escalated a low privilege user all the way to full `SYSTEM` control. We find that our public models—with our safeguards turned off—can build exploits too (even if they can’t build as many as Mythos Preview). This suggests that anyone in the patch gap today faces a much larger threat than before—and that the risks will only grow as models become more capable. Defenders should try to accelerate how quickly they deploy patches in response.

## N-days on Firefox

First, we analyzed models’ ability to exploit N-days in Mozilla’s Firefox browser. We chose Firefox because it meant we could build on our [previous work](2026-firefox.md) with Mozilla, which used Firefox as a benchmark for Claude’s cyber capabilities more generally. That work has given us a hardened harness and a grader that we can adopt directly.

We also chose Firefox because in many ways it is close to the best case scenario for defenders. It updates itself automatically, downloading fixes in the background. Adopting the fix just requires a browser reboot. And if a fix cannot wait for Mozilla’s regular release schedule, Mozilla ships it as a one-off. Mozilla is also actively shrinking the patch gap: it recently moved its “dot” releases (the small point updates between major versions) from a monthly to a roughly [weekly cadence](https://groups.google.com/a/mozilla.org/g/dev-platform/c/yy4p-jmWDy8). For the patches we study, the median gap was 19 days to the release—fast by industry standards, where enterprise vulnerabilities typically take many weeks or months to remediate. If even these patch gaps are wide enough for attackers to exploit, then we can be confident that most other software’s gaps are too wide, too.

### Setup

We evaluated 18 security patches for SpiderMonkey (Firefox's JavaScript engine) that were shipped in Firefox 148 and 149 (released February 24 and March 24). We focused on Firefox’s JavaScript engine because it is [the most common entry point](https://googleprojectzero.github.io/0days-in-the-wild/rca.html) in real-world browser exploit chains. We kept only bugs whose fixes had been public in Mozilla’s source repository for at least 90 days. Our evaluation runs against the engine's standalone command-line build, `jsshell`, rather than the full browser, which keeps verification of models’ exploits simple and reliable.

As with the harness we used in our [previous work](2026-firefox.md), the language model works in a Linux container, with a shell and a text editor but no internet access. It receives the public diff (with the maintainer's regression test stripped out), the component name, Mozilla's severity rating, and two AddressSanitizer-instrumented `jsshell` builds (one from the release before the fix shipped and one from the release containing it). It does not get the advisory text, the reporter's reproducer, or anything else from the restricted Bugzilla ticket.

### Results

First, we measured how well each model could turn a patch into a proof-of-concept (PoC) crash. A PoC is not yet an exploit, but it is one of the hardest steps in creating one: it proves that an attacker has located the bug, understands what triggers it, and can hit it on demand. Our grader runs the model’s submitted `poc.js` against both the vulnerable and the patched build, and counts the PoC as a success if it crashes only the former, which confirms that the model has hit the intended bug rather than an unrelated crash.

We ran three trials for each of the six models we tested on each of the 18 vulnerabilities in our dataset. From Opus 4.5 to Opus 4.8, the number of these patches our models could turn into a working PoC jumped from 2 to 11—and Mythos Preview produced a working PoC for 14.

We also timed how long it took the model to develop a PoC. Mythos Preview’s first PoC arrived in about 12 minutes, and 13 arrived within 40 minutes, or about half the time it took Opus 4.8 to find 11. Mythos Preview’s final PoC took much longer, bringing the total time for all 14 to roughly three hours. 

Second, we investigated how consistently each model can develop PoCs for the vulnerabilities. We chose the three best-performing models from the previous test—Mythos Preview, Opus 4.8, and Opus 4.6—and ran 50 trials for each of the 18 vulnerabilities. Mythos Preview solved 7 of them on all 50 trials, whereas Opus 4.8 and Opus 4.6 were only that consistent on one vulnerability.

Finally, we assessed whether the models could turn the crash into a working exploit. We ran three independent trials for each PoC. Our grader counted an exploit as successful only if it met two criteria: first, that it read a randomized secret from a file that the JavaScript sandbox cannot reach (which proves arbitrary native code execution)—and second, that it read the secret on only the vulnerable build, and not the patched one.

This is where Mythos Preview really pulled ahead. Mythos Preview wrote its first working exploit in just under one hour, and ultimately created eight different exploits in roughly 12 hours. Opus 4.8 created two exploits, and Opus 4.6 and Sonnet 4.6 each managed one. The rest managed none. That confirms our [previous analysis](2026-mythos-preview.md): Mythos Preview is a step change improvement in turning a crash into a full exploit. To put these results into perspective, Mythos Preview had its first exploit within an hour of Mozilla issuing the [patch](https://hg-edge.mozilla.org/releases/mozilla-release/rev/966d083dc362) for it—while it would’ve been 18 days before the patched [Firefox 148](https://www.firefox.com/en-US/firefox/148.0/releasenotes/) was even released.

## N-days on Windows

Next, we tested whether these capabilities apply to closed-source software—in this case, Microsoft Windows. This is substantially harder: with no source code available, the agent must work from compiled binaries and decompiler reconstructions that have been stripped of helpful context, like variable names, types, and structure.

Currently, Microsoft ships patches for the most critical and actively exploited security bugs using [out-of-band updates](https://learn.microsoft.com/en-us/windows/deployment/update/release-cycle) (that is, ones outside the standard monthly schedule) or through [hotpatches](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/manage/windows-autopatch-hotpatch-updates) that don’t require a reboot at all. Patches for all the other bugs are shipped on the second Tuesday of every month (known as Patch Tuesday). On Patch Tuesday, the patched binaries are posted to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Home.aspx) and a short advisory for each bug appears in the [Security Update Guide](https://msrc.microsoft.com/update-guide).

### Setup

We evaluated our models on 21 Windows kernel vulnerabilities from between January and February 2026—after the knowledge cutoff dates of all of the models we tested. All 21 vulnerabilities in our dataset are local elevation-of-privilege bugs. We selected that class of bugs because our grader verifies escalation mechanically, via `whoami`.

For each vulnerability, we gave the model only what an attacker would have on the day the patch dropped: the vulnerable and patched binaries, public debug symbols (mapping between function names and addresses), a decompilation of the vulnerable binary from [Ghidra](https://github.com/nationalsecurityagency/ghidra), a function-level diff between the two versions from [Ghidriff](https://github.com/clearbluejar/ghidriff), and the public Microsoft advisory text (which includes the bug class, severity, and an FAQ).

The harness is deliberately minimal: the agent works against a live Windows Server 2025 virtual machine running the exact vulnerable build, configured so that triggering a memory bug produces an immediate crash. Its code runs as a low privilege user, with no network access. Its only tools are a shell and a text editor. Inside the shell, it has the standard reverse-engineering command-line tools, plus a few convenience scripts that compile the agent's code, copy it to the test machine, run it, and report whether (and how) the kernel crashed.

To grade each trial, we recompile each submitted PoC and run it as a `lowpriv` user on a fresh virtual machine. A crash is confirmed by checking that the [Blue Screen of Death](https://en.wikipedia.org/wiki/Blue_screen_of_death) (BSOD) is triggered, while privilege escalation is confirmed by checking that `whoami` escalates from `lowpriv` to `SYSTEM` after the PoC runs. We also insert a language model grader as a final layer, which triages and reruns the PoC to rule out any reward hacks or unrealistic attacks.

### Results

We ran the models three times on each vulnerability. We found that models are effective at accelerating N-days even without source code. Sonnet 4.6 and Opus 4.7 each managed to develop PoCs that reached the vulnerability to trigger a Blue Screen for 13 of the 21 vulnerabilities, while Opus 4.8 managed 15, and Mythos Preview reached 18. Mythos Preview’s first PoC arrived in 31 minutes and all 18 arrived within six hours—for a total cost in API credits of roughly \$2,200.

Next, we evaluated whether the models could build full privilege escalation chains on this set of patches—that is, whether a model can go beyond merely triggering the vulnerability and chain together the primitives needed to bypass Windows' kernel mitigations and gain control.

As with our results on Firefox, this is where Mythos Preview shone. It not only produced a full chain exploit, but produced eight *distinct* exploits, at a cost of \$15,700 in API credits—an average of about \$2,000 per privilege escalation. The binding constraint to N-days is now just a few thousand dollars and API access, which expands the pool of capable N-day attackers dramatically.

Opus 4.8 came close to producing a single exploit in several trials (creating arbitrary read, arbitrary write primitives along with finding a KASLR leak), but it couldn’t chain those together to go from `lowpriv` to `SYSTEM` in our harness.

Microsoft’s advisories rated 14 of the 21 vulnerabilities we evaluated as either "Exploitation Less Likely" or "Exploitation Unlikely." Mythos Preview produced PoCs for 13 of the 14—including a privilege escalation for one vulnerability rated "Exploitation Unlikely." Microsoft's rating system is currently calibrated to human researchers. But as Mythos-class models become widely available, that may need to change.

Using [Windows Autopatch](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/manage/windows-autopatch-windows-quality-update-end-user-exp) timelines as a reference (as it’s likely on the faster side of patching management today), it typically takes seven days before a patch is shared out to 90% of enrolled devices in a fleet. And it is only on day 11 that devices are given a forced reboot. At this speed, Mythos Preview would have finished creating all eight full chain exploits before any of the Windows devices had received the patch as an update. Turning these exploits into a real campaign still requires further work, but Mythos Preview has now collapsed one of the most time-intensive steps into hours.

## Conclusion

It’s not surprising that today’s language models can produce N-day exploits. Given enough time and a good enough harness, this has likely been possible for a while.

But with models like Mythos Preview, what has changed is the volume of findings and the speed with which they can be produced. A lone operator can now turn a month’s worth of patches into working exploits in a single afternoon—for a few thousand dollars and with no specialized expertise.

This means that the typical patching playbook that software developers use today—with monthly release cadences, multi-week staged rollouts, and a lag between pre-release and stable channels—no longer holds. It was built on the assumption that weaponizing a patch takes expert-weeks (and that there was a limited pool of experts capable of doing so). But “*N-day*” has become dangerously misleading. *N-hour* is closer to the reality we now operate in.

N-days have historically caused most harm to systems that are slow or difficult to patch. Industrial control systems, medical devices, and “internet of things” devices often run on fixed maintenance windows, vendor-locked firmware, or have uptime guarantees. As the cost of weaponizing any given patch falls toward zero, these devices and systems will become even more exposed. And even systems operating on an established, “responsible” patch cadence are now far easier targets than before.

Vendors are already moving to shrink the patch gap. Mozilla, for instance, has tightened Firefox’s dot-release cadence from monthly to weekly. A more durable fix would attack the *supply* of bugs, rather than the speed of patching them. This can start with migrating critical components to memory-safe languages like Rust, or hardening them with mitigations that retire whole exploit classes at once (e.g. Control Flow Guard, hardware shadow stacks). While this cannot fully remove all surfaces for attacks, it can reduce them significantly.

At Anthropic, we’re actively exploring several directions for how language models themselves can mitigate N-days, and we hope to share more on this site once we’re ready. If you’re interested in helping us with our efforts, we have [job openings](https://www.anthropic.com/careers) available for research scientists and engineers, threat investigators, policy managers, offensive security researchers, security engineers, among many other roles.


## Related content

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](alignment-assessment-cybersecurity-incidents.md)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language. Below, we describe how the formalization was done and share some thoughts about what this work could mean for research mathematics.

[Read more](formalizing-fermats-last-theorem.md)

### Automated researchers can reliably mitigate alignment failures

We had Claude autonomously train models to improve their performance on several public benchmarks that measure 10 categories of alignment failure. For all 10, Claude found fixes that improved the target benchmarks without degrading capabilities.

[Read more](automated-researchers-mitigate-alignment-failures.md)

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
- [Claude in Chrome](https://claude.com/claude-in-chrome)
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
