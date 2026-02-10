---
category: "19-Reference"
fetched_at: "2026-02-08T20:52:08Z"
source_url: "https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler"
title: "Does Anthropic crawl data from the web, and how can site owners block the crawler? | Claude Help Center"
---

[](/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

EnglishFrançaisDeutschBahasa IndonesiaItaliano日本語한국어PortuguêsPусский简体中文Español繁體中文

English

Search for articles...

[All Collections](/en/)

[Privacy and Legal](https://support.claude.com/en/collections/4078534-privacy-and-legal)

Does Anthropic crawl data from the web, and how can site owners block the crawler?

# Does Anthropic crawl data from the web, and how can site owners block the crawler?

Updated yesterday

As per industry standard, Anthropic uses a variety of robots to gather data from the public web for model development, to search the web, and to retrieve web content at users’ direction. Anthropic uses different robots to enable website owner transparency and choice. Below is information on the three robots that Anthropic uses and how to set your site preferences to enable those you want to access your content and limit those you don’t.

[TABLE]

As part of our mission to build safe and reliable frontier systems and advance the field of responsible AI development, we’re sharing the principles by which we collect data as well as instructions on how to opt out of our crawling going forward:

- Our collection of data should be *transparent*. Anthropic uses the Bots described above to access web content.

- Our crawling should *not* *be* *intrusive or disruptive*. We aim for minimal disruption by being thoughtful about how quickly we crawl the same domains and respecting Crawl-delay where appropriate.

- Anthropic’s Bots *respect “do not crawl”* signals by honoring industry standard directives in robots.txt.

- Anthropic’s Bots *respect anti-circumvention technologies* (e.g., we will not attempt to bypass CAPTCHAs for the sites we crawl.)

To limit crawling activity, we support the non-standard Crawl-delay extension to robots.txt. An example of this might be:

User-agent: ClaudeBot

Crawl-delay: 1

To block a Bot from your entire website, add this to the robots.txt file in your top-level directory. Please do this for every subdomain that you wish to opt out from. An example of this is:

User-agent: ClaudeBot

Disallow: /

Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file in the manner above. Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file. Additionally, we do not currently publish IP ranges, as we use service provider public IPs. This may change in the future.

You can learn more about our data handling practices and commitments at our [Help Center](https://support.anthropic.com/en/collections/4078534-privacy-legal). If you have further questions, or believe that our Bots may be malfunctioning, please reach out to [\[email protected\]](/cdn-cgi/l/email-protection#0f6c636e7a6b6a6d607b4f6e617b677d607f666c216c6062). Please reach out from an email that includes the domain you are contacting us about, as it is otherwise difficult to verify reports.

You can be notified when this article is updated by clicking here and completing the form:

[Subscribe to updates](https://docs.google.com/forms/d/e/1FAIpQLScQk_jt1NrI0AZU3RfBCDkCe4RBS2lAzMVILBICWdi4xwBaRw/viewform)

------------------------------------------------------------------------

Related Articles

[](https://support.claude.com/en/articles/7996906-reporting-blocking-and-removing-content-from-claude)

Reporting, Blocking, and Removing Content from Claude

[](https://support.claude.com/en/articles/9015913-how-to-get-support)

How to get support

[](https://support.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller)

Does Anthropic Act as a Data Processor or Controller?

[](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)

Reporting, Blocking, and Removing Content from Claude

[](https://support.claude.com/en/articles/11596036-anthropic-connectors-directory-faq)

Anthropic Connectors Directory FAQ

Did this answer your question?

😞

😐

😃

[](/en/)

- [Product](https://www.anthropic.com/product)
- [Research](https://www.anthropic.com/research)
- [Company](https://www.anthropic.com/company)
- [News](https://www.anthropic.com/news)
- [Careers](https://www.anthropic.com/careers)

- [Terms of Service - Consumer](https://www.anthropic.com/terms)
- [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Privacy Policy](https://www.anthropic.com/privacy)
- [Usage Policy](https://www.anthropic.com/aup)
- [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Compliance](https://trust.anthropic.com/)
