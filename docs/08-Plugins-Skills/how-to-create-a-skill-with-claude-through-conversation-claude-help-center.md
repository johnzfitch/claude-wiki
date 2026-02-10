With Skills, you are able to teach Claude specific workflows, tools, and processes. By creating a skill, you're giving Claude a playbook it can reference whenever you need a particular type of help—whether that's generating reports in your company's format, cleaning and using data the way you normally do, or pulling and analyzing CRM data your way.

  
This guide focuses on the other path: creating skills through conversation with Claude. You describe your process naturally, and Claude handles the formatting and structure. This approach makes Skills accessible to anyone, regardless of technical background.

<iframe src="https://www.youtube.com/embed/kS1MJFZWMq4" frameborder="0" allowfullscreen="allowfullscreen" referrerpolicy="strict-origin-when-cross-origin"></iframe>

## **Creating a skill through conversation**

Creating a skill with Claude means having a conversation where you explain your approach and share any materials you want included. Claude translates this into a properly formatted skill that can work in future chats.

### 1\. Start a conversation

Open a new chat and say something like "I want to create a skill for quarterly business reviews" or "I need a skill that knows how to analyze customer feedback."  


If you have materials that show your approach—templates you use, examples of work you're proud of, brand guidelines you follow, data files you reference—upload them. You can also mention any connected tools Claude should use. If you are unsure of what else to include, ask Claude for guidance.  


### 2\. Answer Claude's questions

Claude will ask about your process. Provide enough detail that someone capable but unfamiliar could follow your approach.  


You'll get questions about concrete usage ("Can you give examples of when you'd use this skill?") or about your process ("What makes output good for this type of work?").  


### 3\. Claude builds the Skill

In Claude's thinking, you will see it read a _skill-creator_ skill to follow best practices in creating a properly structured skill_._ Claude will create a SKILL.md file (the instruction file every skill needs), organize any materials you've provided, and generate code for operations you've described that need to happen consistently. Claude then packages everything into a skill file.  


### 4\. Activate and test the skill

Save the the skill file that Claude creates. In [Settings > Capabilities > Skills](https://claude.ai/settings/capabilities), you can view your library of skills and turn them on or off as needed.  


Try using your skill by describing a task the skill should address. See if Claude recognizes the situation (you'll see "Using \[skill name\]" in Claude's thinking) and whether it produces the expected outcome. If something's off, ask Claude to update the skill with your desired changes. Repeat this process until your skill works effectively.  


## **Skills you can build**

You can build skills for a range of tasks. Skills can capture how your organization works, enable specialized expertise you don't personally have, or work together to handle complex workflows.

## **What you can include within a skill**

Skills bundle three types of content together—instructions, reference materials, and scripts. Knowing these components helps you articulate what you need when creating a skill with Claude.  


[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781727755/40d01224cb2a1653189d5211e731/380d5eae-c159-4643-80e3-ce1be19b6d57?expires=1769938200&signature=603cfdc4a4840cc814ab019ca29db3c885afc4993316416ea3acd2d8fc877e15&req=dScvF858moZaXPMW1HO4zRjaAoeXjgWff1HwTII0D0GXuU%2B0FlxyWFfSyonq%0A0co8vQJXVUOC4D1kog4%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781727755/40d01224cb2a1653189d5211e731/380d5eae-c159-4643-80e3-ce1be19b6d57?expires=1769938200&signature=603cfdc4a4840cc814ab019ca29db3c885afc4993316416ea3acd2d8fc877e15&req=dScvF858moZaXPMW1HO4zRjaAoeXjgWff1HwTII0D0GXuU%2B0FlxyWFfSyonq%0A0co8vQJXVUOC4D1kog4%3D%0A)

  
**Instructions —** Every skill needs a SKILL.md file that explains your process. When asking Claude to create a skill, describe your process for Claude to structure it into proper instructions. At the top of your [SKILL.md](http://skill.md/) file, will be the skill's name and what it does. Claude scans this information first to decide whether or not to load and use the full skill during your conversations. Below that are clear instructions on how to do the task.

**Reference materials and assets —** Sometimes instructions alone aren't enough and Claude needs actual files to reference or use in the output. To include these, upload any relevant files or information when creating your Skill. Claude determines whether to embed guidance in the SKILL.md instructions or bundle it as a reference file.

**Scripts —** These are executable code files that Claude can run to handle complex operations more reliably than instructions alone. You don't need to write these yourself. When you describe tasks that need scripts, Claude recognizes them and creates the code automatically. Examples include:

## **Additional Resources**

#### Getting started

#### Going deeper

___

Related Articles

[

What are Skills?

](https://support.claude.com/en/articles/12512176-what-are-skills)[

Using Skills in Claude

](https://support.claude.com/en/articles/12512180-using-skills-in-claude)[

How to create custom Skills

](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)[

Teach Claude your way of working using skills

](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)[

Claude for Financial Services Skills

](https://support.claude.com/en/articles/12663107-claude-for-financial-services-skills)