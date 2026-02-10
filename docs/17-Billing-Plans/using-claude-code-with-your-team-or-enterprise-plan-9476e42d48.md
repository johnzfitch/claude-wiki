---
category: "17-Billing-Plans"
source_url: "https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan"
---


What is Claude Code?

Claude Code is a command line tool that gives you access to Claude models directly in your terminal, allowing you to delegate complex coding tasks while maintaining transparency and control.

Claude Code is included with every Team plan seat. Premium seats offer more usage for team members with heavier workloads. For Enterprise plans, Claude Code is available on Chat + Claude Code seats (usage-based billing) and Premium seats (seat-based billing).

With a Team or Enterprise plan, you can access Claude on the web, desktop, and mobile apps, plus Claude Code in your terminal—all with one unified subscription.

 

Why use Claude and Claude Code?

Combine two powerful AI products in one unified subscription:

Use Claude for writing, research, analysis, and collaboration across teams.

Use Claude Code for terminal-based coding workflows and development tasks.

 

 

How to connect Claude Code to your Team or Enterprise plan
Step 1: Purchase Chat + Claude Code / Premium seats (Enterprise plans only)

Enterprise plan owners can purchase Chat + Claude Code / Premium seats that include Claude Code access, and manage seat allocation in Admin settings > Organization.

 

Step 2: Download and install Claude Code

Note: If you already have Claude Code installed on your computer, proceed to Step 3.

Once you have Claude Code access, visit the Claude Code page.

Click the link to install Node.js 18+.

Open your terminal, then run: npm install -g @anthropic-ai/claude-code

 

Step 3: Authenticate with the Team or Enterprise account

Type claude within your Terminal window to start a Claude Code session.

When prompted during setup or first use, select a login method.

If you're already logged in to Claude Code via a different account, run /login to select a different login method.

Select “Claude account with subscription” to be routed to an OAuth prompt.

Select your Team or Enterprise plan and click “Authorize.”

Your premium seat subscription will be linked to Claude Code.

 

Having trouble using your Team or Enterprise account to access Claude Code?

If you're not seeing the option to authenticate with your preferred account, follow these steps to update Claude Code:

Log out of your active session completely using the /logout command.

Run claude update.

Restart your terminal completely for the change to take effect.

Run claude and select the correct account to use Claude Code.

 

 

What happens when you hit usage limits

Your Team or seat-based Enterprise organization can enable extra usage to allow team members on all seat types to continue working with Claude and Claude Code after reaching their included usage limits. See this article for more information: Extra usage for Team and seat-based Enterprise plans.

Related Articles
What is the Team plan?
What is the Enterprise plan?
Using Claude Code with your Pro or Max plan
Claude Code usage analytics
Purchasing and managing seats on Enterprise plans