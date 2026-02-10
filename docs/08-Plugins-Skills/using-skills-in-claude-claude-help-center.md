Skills extend Claude's capabilities by giving it access to specialized knowledge and workflows. This guide shows you how to enable, discover, and use Skills in Claude.

## Prerequisites

**For Enterprise plans:** Owners must first enable both **Code execution and file creation** and **Skills** in [Admin settings > Capabilities](https://claude.ai/admin-settings/capabilities). Owners can also upload skills to provision them organization-wide — these skills automatically appear for all users. Once Skills are enabled at the organization level, individual members can toggle on example skills, access provisioned skills, and upload their own personal skills in [Settings > Capabilities](https://preview.claude.ai/settings/capabilities).

**For Team plans:** This feature is enabled by default at the organization level. Once enabled, individual members can toggle on example skills and upload their own in [Settings > Capabilities](https://preview.claude.ai/settings/capabilities).

**For Max, Pro, and free plans:** You can enable example skills and upload your own in [Settings > Capabilities](https://claude.ai/settings/capabilities).

## How to enable Skills

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781692976/3986c09def54467a7419e9cfd68e/8e4fa130-9c44-4067-bf12-520986644135?expires=1769938200&signature=6e1b12f3d9a54495e17eb9be2cd6b13680e58f9b410ce1cc218a90fd2caed92c&req=dScvF893n4hYX%2FMW1HO4zXi3CDvf9EB6mT2qapKX2kFdvKjtf3upP5kFf%2Fa6%0AeU2%2BRRSEygmkAjNKVHQ%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781692976/3986c09def54467a7419e9cfd68e/8e4fa130-9c44-4067-bf12-520986644135?expires=1769938200&signature=6e1b12f3d9a54495e17eb9be2cd6b13680e58f9b410ce1cc218a90fd2caed92c&req=dScvF893n4hYX%2FMW1HO4zXi3CDvf9EB6mT2qapKX2kFdvKjtf3upP5kFf%2Fa6%0AeU2%2BRRSEygmkAjNKVHQ%3D%0A)

## Organization provisioned skills (Team and Enterprise plans)

Organization Owners can provision skills for all users. These skills appear in your individual Skills list with a team indicator — you can toggle them on or off based on your preferences. For information on provisioning skills for your organization, see [Provisioning and managing Skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization#h_4dea113421).

## Using Anthropic Skills

Anthropic provides several built-in skills that are available to all users, including:

With **Code execution and file creation** on, Claude will automatically use these tools when relevant. You don't need to explicitly invoke them—Claude determines when each skill is needed based on your request.

For example, if you ask Claude to "Create a PowerPoint presentation about Q3 results," Claude will automatically use the PowerPoint skill if the capability is enabled.

## Adding and using custom skills

You can also create and upload your own skills to teach Claude your specific workflows:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1782364123/a16cc51c623f6dc7ecef8974d629/98c13ee7-c134-4109-905c-384ab75a9ac6?expires=1769938200&signature=8c7bc1af65306a267dfe421f5b682d1162ddf03ccef4bfeca9452449877fd015&req=dScvFMp4mYBdWvMW1HO4zRUki%2BjxgQ6X%2BfMHhPHscm47spCpsyxhIzvp9n29%0AWT%2FuQvE9rUoVLi66d7Y%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1782364123/a16cc51c623f6dc7ecef8974d629/98c13ee7-c134-4109-905c-384ab75a9ac6?expires=1769938200&signature=8c7bc1af65306a267dfe421f5b682d1162ddf03ccef4bfeca9452449877fd015&req=dScvFMp4mYBdWvMW1HO4zRUki%2BjxgQ6X%2BfMHhPHscm47spCpsyxhIzvp9n29%0AWT%2FuQvE9rUoVLi66d7Y%3D%0A)

## How Claude uses Skills

Claude automatically identifies and loads relevant skills based on your task. Refer to [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) to learn how this works.

## Discovering skills from the Skills Directory

The Skills Directory features professionally-built skills from leading platforms like Notion, Figma, and Atlassian. These partner skills are designed to work with their respective MCP connectors, enabling powerful workflows that combine Claude's capabilities with your existing tools.

**To install a skill from the Skills Directory:**

## Managing your Skills

### Viewing your Skills

## Enabling and disabling your Skills

Toggle any skill on or off using the switch next to it. Disabled skills won't be available to Claude.

### Removing custom Skills

To remove a custom skill you've uploaded:

## Privacy and security details

For Team and Enterprise plans, organization Owners can provision skills for all users through Admin settings. Individual peer-to-peer skill sharing is not currently available — users cannot directly share skills with specific colleagues. For personal skills, each individual must upload them to their own account. Skills in Claude and the API operate in Claude's secure sandboxed environment with no data persistence between sessions.

Note that skills may include, or instruct Claude to install, third-party packages and software for Claude to use when completing a task. See [here](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1) for details onClaude’s container environment and [here](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool#containers) for API’s container environment.

### What are the primary risks of using Skills?

The most significant risks are prompt injection, which allows Claude to be manipulated to execute unintended actions, and data exfiltration, caused by malicious package code or prompt-injected data leaks. We’ve implemented several mitigations to these risks. Refer to [our security considerations for code execution](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1) for more information.

When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

## Troubleshooting

### Skills section not visible

Ensure code execution is enabled in [Settings > Capabilities](https://claude.ai/settings/capabilities). Skills require the code execution environment to function.

### Claude isn’t using a Skill

### Upload errors

Common reasons for upload failures:

### Skills greyed out

If Skills appear greyed out, code execution or Skills may be disabled at the organization level (for Team and Enterprise plans) or individually. Check with your organization's Owner or make sure to enable code execution in your settings.

## Best Practices

### Start Simple

Begin with Anthropic's pre-built Skills to understand how they work before creating custom skills.

### Be Specific

Write clear descriptions when writing custom skills. A specific description tells Claude when to invoke your skill.

### Test Your Skills

After uploading a custom skill, test it with a few different prompts to ensure it works as expected.

### Organize by Purpose

Create separate skills for different purposes rather than a single skill that’s meant to do everything.

## Learn more about using Skills

___

Related Articles

[

Create and edit files with Claude

](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)[

What are Skills?

](https://support.claude.com/en/articles/12512176-what-are-skills)[

How to create custom Skills

](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)[

How to use the single-cell-rna-qc skill with Claude

](https://support.claude.com/en/articles/12621831-how-to-use-the-single-cell-rna-qc-skill-with-claude)[

Provisioning and managing Skills for your organization

](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)