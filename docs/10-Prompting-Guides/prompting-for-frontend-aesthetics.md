::: {.cell .markdown}
# Frontend Aesthetics: A Prompting Guide

Claude can generate high-quality frontends, but without guidance it
tends toward generic, conservative designs. This guide shows you how to
prompt Claude to produce more distinctive, polished output.
:::

::: {.cell .markdown}
## Prompting for Better Outputs

Claude has strong knowledge of design principles, typography, and color
theory, but defaults to safe choices unless explicitly encouraged
otherwise. Through experimentation, we\'ve found three strategies that
consistently produce better results:

1.  **Guide specific design dimensions** - Direct Claude\'s attention to
    typography, color, motion, and backgrounds individually
2.  **Reference design inspirations** - Suggest sources like IDE themes
    or cultural aesthetics without being overly prescriptive\
3.  **Call out common defaults** - Explicitly tell Claude to avoid its
    tendency toward generic choices

The prompt below applies these strategies across four key design areas.
:::

::: {.cell .markdown}
## The Prompt

To implement these changes, you can append this prompt section to your
system prompt or CLAUDE.md file.
:::

::: {.cell .code execution_count="4"}
``` python
DISTILLED_AESTHETICS_PROMPT = """
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight. Focus on:

Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.

Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.

Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.

Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!
</frontend_aesthetics>
"""
```
:::

::: {.cell .markdown}
## Results

Here are the results of UI generations both with and without the prompt
section above.

Without guidance, Claude often defaults to simplistic designs with white
and purple backgrounds. With the aesthetics prompt, it produces more
varied and visually interesting designs.

### Example 1: SaaS Landing Page

**Prompt:** `"Create a SaaS landing page for a project management tool"`

<table>
<tr>
<td width="50%" valign="top">

**Without Aesthetics Prompt**

![Baseline output without aesthetics guidance](../images/frontend_aesthetics/baseline_saas.png)

</td>
<td width="50%" valign="top">

**With Aesthetics Prompt**

![Enhanced output with distilled aesthetics prompt](../images/frontend_aesthetics/distilled_saas.png)

</td>
</tr>
</table>

### Example 2: Blog Post

**Prompt:**
`"Build a blog post layout with author bio, reading time, and related articles"`

<table>
<tr>
<td width="50%" valign="top">

**Without Aesthetics Prompt**

![Baseline portfolio without aesthetics guidance](../images/frontend_aesthetics/baseline_portfolio.png)

</td>
<td width="50%" valign="top">

**With Aesthetics Prompt**

![Enhanced portfolio with distilled aesthetics prompt](../images/frontend_aesthetics/distilled_portfolio.png)

</td>
</tr>
</table>

### Example 3: Admin Table

**Prompt:**
`"Create an admin panel with a data table showing users, their roles, and action buttons"`

<table>
<tr>
<td width="50%" valign="top">

**Without Aesthetics Prompt**

![Baseline dashboard without aesthetics guidance](../images/frontend_aesthetics/baseline_dashboard.png)

</td>
<td width="50%" valign="top">

**With Aesthetics Prompt**

![Enhanced dashboard with distilled aesthetics prompt](../images/frontend_aesthetics/distilled_dashboard.png)

</td>
</tr>
</table>
:::

::: {.cell .markdown}
## Try It Yourself

First, set up the helper functions:
:::

::: {.cell .code execution_count="2"}
``` python
import html
import os
import re
import time
import webbrowser
from datetime import datetime
from pathlib import Path

from anthropic import Anthropic
from IPython.display import HTML as DisplayHTML
from IPython.display import display

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def save_html(html_content):
    os.makedirs("html_outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"html_outputs/{timestamp}.html"
    with open(filepath, "w") as f:
        f.write(html_content)
    return filepath


def extract_html(text):
    pattern = r"```(?:html)?\s*(.*?)\s*```"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches[0] if matches else None


def open_in_browser(filepath):
    abs_path = Path(filepath).resolve()
    webbrowser.open(f"file://{abs_path}")
    print(f"🌐 Opened in browser: {filepath}")


def generate_html_with_claude(system_prompt, user_prompt):
    print("🚀 Generating HTML...\n")

    full_response = ""
    start_time = time.time()
    display_id = display(DisplayHTML(""), display_id=True)

    with client.messages.stream(
        model="claude-sonnet-4-5-20250929",
        max_tokens=64000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    ) as stream:
        for text in stream.text_stream:
            full_response += text
            escaped_text = html.escape(full_response)
            display_html = f"""
            <div id="stream-container" style="border: 2px solid #667eea; border-radius: 8px; padding: 16px; background: #f8f9fa; max-height: 500px; overflow-y: auto;">
                <pre style="margin: 0; font-family: monospace; font-size: 12px; color: #2d2d2d; white-space: pre-wrap; word-wrap: break-word;">{escaped_text}</pre>
            </div>
            <script>
                requestAnimationFrame(() => {{
                    const container = document.getElementById('stream-container');
                    if (container) {{
                        container.scrollTop = container.scrollHeight;
                    }}
                }});
            </script>
            """
            display_id.update(DisplayHTML(display_html))

    elapsed = time.time() - start_time
    escaped_text = html.escape(full_response)
    final_html = f"""
    <div style="border: 2px solid #28a745; border-radius: 8px; padding: 16px; background: #f8f9fa; max-height: 500px; overflow-y: auto;">
        <pre style="margin: 0; font-family: monospace; font-size: 12px; color: #2d2d2d; white-space: pre-wrap; word-wrap: break-word;">{escaped_text}</pre>
    </div>
    """
    display_id.update(DisplayHTML(final_html))

    print(f"\n✅ Complete in {elapsed:.1f}s\n")

    html_content = extract_html(full_response)
    if html_content is None:
        print("❌ Error: Could not extract HTML from response.")
        raise ValueError("Failed to extract HTML from Claude's response.")

    filepath = save_html(html_content)
    print(f"💾 HTML saved to: {filepath}")
    open_in_browser(filepath)

    return filepath
```
:::

::: {.cell .markdown}
Generate with the aesthetics prompt:
:::

::::::: {.cell .code execution_count="3"}
```` python
BASE_SYSTEM_PROMPT = """
You are an expert frontend engineer skilled at crafting beautiful, performant frontend applications.

<tech_stack>
Use vanilla HTML, CSS, & Javascript. Use Tailwind CSS for your CSS variables.
</tech_stack>

<output>
Generate complete, self-contained HTML code for the requested frontend application. Include all CSS and JavaScript inline.

CRITICAL: You must wrap your HTML code in triple backticks with html language identifier like this:
```html
<!DOCTYPE html>
<html>
...
</html>
```

Our parser depends on this format - do not deviate from it!
</output>
"""

USER_PROMPT = "Create a SaaS landing page for a project management tool"

# Generate with distilled aesthetics prompt
generate_html_with_claude(BASE_SYSTEM_PROMPT + "\n\n" + DISTILLED_AESTHETICS_PROMPT, USER_PROMPT)
````

::: {.output .stream .stdout}
    🚀 Generating HTML...
:::

::: {.output .display_data}

    <div style="border: 2px solid #28a745; border-radius: 8px; padding: 16px; background: #f8f9fa; max-height: 500px; overflow-y: auto;">
        <pre style="margin: 0; font-family: monospace; font-size: 12px; color: #2d2d2d; white-space: pre-wrap; word-wrap: break-word;">```html
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Momentum — Project Management Reimagined&lt;/title&gt;
    &lt;script src=&quot;https://cdn.tailwindcss.com&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;preconnect&quot; href=&quot;https://fonts.googleapis.com&quot;&gt;
    &lt;link rel=&quot;preconnect&quot; href=&quot;https://fonts.gstatic.com&quot; crossorigin&gt;
    &lt;link href=&quot;https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&amp;family=DM+Sans:wght@400;500;700&amp;display=swap&quot; rel=&quot;stylesheet&quot;&gt;
    &lt;style&gt;
        :root {
            --primary: #FF6B35;
            --primary-dark: #E85A2A;
            --secondary: #004E89;
            --accent: #FFD23F;
            --dark: #1A1A2E;
            --light: #F8F9FA;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: &#x27;DM Sans&#x27;, sans-serif;
            background: var(--light);
            color: var(--dark);
            overflow-x: hidden;
        }

        h1, h2, h3, h4 {
            font-family: &#x27;Syne&#x27;, sans-serif;
            font-weight: 800;
        }

        /* Animated background */
        .hero-bg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #004E89 0%, #1A1A2E 50%, #FF6B35 100%);
            z-index: 0;
        }

        .hero-bg::before {
            content: &#x27;&#x27;;
            position: absolute;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(255, 107, 53, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(255, 210, 63, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(0, 78, 137, 0.3) 0%, transparent 50%);
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            33% { transform: translate(30px, -30px) rotate(120deg); }
            66% { transform: translate(-20px, 20px) rotate(240deg); }
        }

        .mesh-gradient {
            background: 
                radial-gradient(at 27% 37%, hsla(215, 98%, 61%, 0.3) 0px, transparent 50%),
                radial-gradient(at 97% 21%, hsla(125, 98%, 72%, 0.2) 0px, transparent 50%),
                radial-gradient(at 52% 99%, hsla(354, 98%, 61%, 0.3) 0px, transparent 50%),
                radial-gradient(at 10% 29%, hsla(256, 96%, 67%, 0.2) 0px, transparent 50%);
        }

        /* Fade in animations */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 0.8s ease forwards;
        }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .delay-1 { animation-delay: 0.1s; }
        .delay-2 { animation-delay: 0.2s; }
        .delay-3 { animation-delay: 0.3s; }
        .delay-4 { animation-delay: 0.4s; }
        .delay-5 { animation-delay: 0.5s; }
        .delay-6 { animation-delay: 0.6s; }

        /* Feature cards */
        .feature-card {
            background: white;
            border-radius: 24px;
            padding: 2rem;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .feature-card::before {
            content: &#x27;&#x27;;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }

        .feature-card:hover::before {
            transform: scaleX(1);
        }

        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            border-color: var(--primary);
        }

        /* CTA Button */
        .cta-button {
            background: var(--primary);
            color: white;
            padding: 1rem 2.5rem;
            border-radius: 50px;
            font-weight: 700;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(255, 107, 53, 0.3);
            position: relative;
            overflow: hidden;
        }

        .cta-button::before {
            content: &#x27;&#x27;;
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }

        .cta-button:hover::before {
            width: 300px;
            height: 300px;
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(255, 107, 53, 0.4);
        }

        .cta-button span {
            position: relative;
            z-index: 1;
        }

        /* Stats counter animation */
        .stat-number {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Testimonial cards */
        .testimonial {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
            transition: transform 0.3s ease;
        }

        .testimonial:hover {
            transform: scale(1.02);
        }

        /* Icon styles */
        .icon-circle {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 1rem;
        }

        /* Navbar scroll effect */
        .navbar {
            transition: all 0.3s ease;
        }

        .navbar.scrolled {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        }

        /* Pricing cards */
        .pricing-card {
            background: white;
            border-radius: 24px;
            padding: 3rem 2rem;
            transition: all 0.4s ease;
            border: 2px solid #e5e7eb;
        }

        .pricing-card.featured {
            border-color: var(--primary);
            transform: scale(1.05);
            box-shadow: 0 20px 60px rgba(255, 107, 53, 0.2);
        }

        .pricing-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        }

        /* Dashboard mockup */
        .dashboard-mockup {
            background: white;
            border-radius: 20px;
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.2);
            padding: 1rem;
            position: relative;
            transform: perspective(1000px) rotateY(-5deg) rotateX(5deg);
            transition: transform 0.5s ease;
        }

        .dashboard-mockup:hover {
            transform: perspective(1000px) rotateY(0deg) rotateX(0deg);
        }

        .mockup-header {
            display: flex;
            gap: 8px;
            margin-bottom: 1rem;
        }

        .mockup-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }

        .mockup-content {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 12px;
            height: 400px;
            position: relative;
            overflow: hidden;
        }

        .mockup-element {
            position: absolute;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;!-- Navigation --&gt;
    &lt;nav class=&quot;navbar fixed w-full top-0 z-50 py-4 px-8&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto flex items-center justify-between&quot;&gt;
            &lt;div class=&quot;flex items-center gap-2&quot;&gt;
                &lt;div class=&quot;w-10 h-10 rounded-full bg-gradient-to-br from-orange-500 to-yellow-400 flex items-center justify-center&quot;&gt;
                    &lt;span class=&quot;text-white font-bold text-xl&quot;&gt;M&lt;/span&gt;
                &lt;/div&gt;
                &lt;span class=&quot;text-2xl font-bold&quot;&gt;Momentum&lt;/span&gt;
            &lt;/div&gt;
            &lt;div class=&quot;hidden md:flex items-center gap-8&quot;&gt;
                &lt;a href=&quot;#features&quot; class=&quot;text-gray-700 hover:text-orange-500 transition font-medium&quot;&gt;Features&lt;/a&gt;
                &lt;a href=&quot;#pricing&quot; class=&quot;text-gray-700 hover:text-orange-500 transition font-medium&quot;&gt;Pricing&lt;/a&gt;
                &lt;a href=&quot;#testimonials&quot; class=&quot;text-gray-700 hover:text-orange-500 transition font-medium&quot;&gt;Testimonials&lt;/a&gt;
                &lt;a href=&quot;#&quot; class=&quot;text-gray-700 hover:text-orange-500 transition font-medium&quot;&gt;Login&lt;/a&gt;
                &lt;a href=&quot;#&quot; class=&quot;cta-button&quot;&gt;&lt;span&gt;Start Free Trial&lt;/span&gt;&lt;/a&gt;
            &lt;/div&gt;
            &lt;button class=&quot;md:hidden text-gray-700&quot;&gt;
                &lt;svg width=&quot;24&quot; height=&quot;24&quot; fill=&quot;none&quot; stroke=&quot;currentColor&quot; stroke-width=&quot;2&quot; stroke-linecap=&quot;round&quot; stroke-linejoin=&quot;round&quot;&gt;
                    &lt;line x1=&quot;3&quot; y1=&quot;12&quot; x2=&quot;21&quot; y2=&quot;12&quot;&gt;&lt;/line&gt;
                    &lt;line x1=&quot;3&quot; y1=&quot;6&quot; x2=&quot;21&quot; y2=&quot;6&quot;&gt;&lt;/line&gt;
                    &lt;line x1=&quot;3&quot; y1=&quot;18&quot; x2=&quot;21&quot; y2=&quot;18&quot;&gt;&lt;/line&gt;
                &lt;/svg&gt;
            &lt;/button&gt;
        &lt;/div&gt;
    &lt;/nav&gt;

    &lt;!-- Hero Section --&gt;
    &lt;section class=&quot;relative min-h-screen flex items-center justify-center overflow-hidden pt-20&quot;&gt;
        &lt;div class=&quot;hero-bg&quot;&gt;&lt;/div&gt;
        
        &lt;div class=&quot;relative z-10 max-w-7xl mx-auto px-8 py-20&quot;&gt;
            &lt;div class=&quot;grid md:grid-cols-2 gap-12 items-center&quot;&gt;
                &lt;div class=&quot;text-white&quot;&gt;
                    &lt;h1 class=&quot;text-6xl md:text-7xl leading-tight mb-6 fade-in&quot;&gt;
                        Build momentum.&lt;br/&gt;
                        &lt;span class=&quot;text-yellow-300&quot;&gt;Ship faster.&lt;/span&gt;
                    &lt;/h1&gt;
                    &lt;p class=&quot;text-xl mb-8 text-gray-200 fade-in delay-1&quot;&gt;
                        The project management tool that adapts to your team&#x27;s rhythm. Stop managing tasks. Start building momentum.
                    &lt;/p&gt;
                    &lt;div class=&quot;flex flex-wrap gap-4 fade-in delay-2&quot;&gt;
                        &lt;a href=&quot;#&quot; class=&quot;cta-button&quot;&gt;&lt;span&gt;Get Started Free&lt;/span&gt;&lt;/a&gt;
                        &lt;a href=&quot;#&quot; class=&quot;bg-white/10 backdrop-blur text-white px-8 py-4 rounded-full font-bold hover:bg-white/20 transition inline-block&quot;&gt;
                            Watch Demo
                        &lt;/a&gt;
                    &lt;/div&gt;
                    &lt;div class=&quot;flex items-center gap-8 mt-12 fade-in delay-3&quot;&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;stat-number text-white&quot;&gt;50k+&lt;/div&gt;
                            &lt;div class=&quot;text-gray-300&quot;&gt;Active Teams&lt;/div&gt;
                        &lt;/div&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;stat-number text-white&quot;&gt;4.9&lt;/div&gt;
                            &lt;div class=&quot;text-gray-300&quot;&gt;Average Rating&lt;/div&gt;
                        &lt;/div&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;stat-number text-white&quot;&gt;99%&lt;/div&gt;
                            &lt;div class=&quot;text-gray-300&quot;&gt;Uptime&lt;/div&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;
                
                &lt;div class=&quot;fade-in delay-4&quot;&gt;
                    &lt;div class=&quot;dashboard-mockup&quot;&gt;
                        &lt;div class=&quot;mockup-header&quot;&gt;
                            &lt;div class=&quot;mockup-dot bg-red-500&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-dot bg-yellow-400&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-dot bg-green-500&quot;&gt;&lt;/div&gt;
                        &lt;/div&gt;
                        &lt;div class=&quot;mockup-content&quot;&gt;
                            &lt;div class=&quot;mockup-element&quot; style=&quot;top: 20px; left: 20px; width: 200px; height: 60px;&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-element&quot; style=&quot;top: 100px; left: 20px; width: 150px; height: 100px;&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-element&quot; style=&quot;top: 100px; right: 20px; width: 150px; height: 100px;&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-element&quot; style=&quot;top: 220px; left: 20px; width: 320px; height: 80px;&quot;&gt;&lt;/div&gt;
                            &lt;div class=&quot;mockup-element&quot; style=&quot;bottom: 20px; right: 20px; width: 100px; height: 60px; background: linear-gradient(135deg, #FF6B35, #FFD23F);&quot;&gt;&lt;/div&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- Features Section --&gt;
    &lt;section id=&quot;features&quot; class=&quot;py-32 px-8 bg-white&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto&quot;&gt;
            &lt;div class=&quot;text-center mb-20&quot;&gt;
                &lt;h2 class=&quot;text-5xl md:text-6xl font-bold mb-6&quot;&gt;Everything you need.&lt;br/&gt;Nothing you don&#x27;t.&lt;/h2&gt;
                &lt;p class=&quot;text-xl text-gray-600 max-w-2xl mx-auto&quot;&gt;Powerful features that don&#x27;t get in your way. Built for teams who want to focus on work, not tools.&lt;/p&gt;
            &lt;/div&gt;

            &lt;div class=&quot;grid md:grid-cols-3 gap-8&quot;&gt;
                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-orange-100 text-orange-500&quot;&gt;⚡&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Lightning Fast&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;Native performance across all devices. No lag, no loading spinners. Just instant productivity.&lt;/p&gt;
                &lt;/div&gt;

                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-blue-100 text-blue-500&quot;&gt;🎯&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Smart Workflows&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;AI-powered automation that learns from your team&#x27;s patterns and suggests optimizations.&lt;/p&gt;
                &lt;/div&gt;

                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-purple-100 text-purple-500&quot;&gt;🔗&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Seamless Integration&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;Connect with 1000+ tools your team already uses. Slack, GitHub, Figma, and more.&lt;/p&gt;
                &lt;/div&gt;

                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-green-100 text-green-500&quot;&gt;📊&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Real-time Analytics&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;Visualize progress with beautiful dashboards that update in real-time as work happens.&lt;/p&gt;
                &lt;/div&gt;

                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-pink-100 text-pink-500&quot;&gt;🎨&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Customizable Views&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;Board, list, timeline, calendar - switch between views instantly. See work your way.&lt;/p&gt;
                &lt;/div&gt;

                &lt;div class=&quot;feature-card&quot;&gt;
                    &lt;div class=&quot;icon-circle bg-yellow-100 text-yellow-600&quot;&gt;🔒&lt;/div&gt;
                    &lt;h3 class=&quot;text-2xl font-bold mb-4&quot;&gt;Enterprise Security&lt;/h3&gt;
                    &lt;p class=&quot;text-gray-600&quot;&gt;SOC 2 Type II certified. Your data encrypted at rest and in transit. Always.&lt;/p&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- Social Proof / Stats --&gt;
    &lt;section class=&quot;py-24 px-8 bg-gradient-to-br from-gray-900 to-gray-800 text-white&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto&quot;&gt;
            &lt;div class=&quot;text-center mb-16&quot;&gt;
                &lt;h2 class=&quot;text-4xl md:text-5xl font-bold mb-4&quot;&gt;Trusted by teams worldwide&lt;/h2&gt;
                &lt;p class=&quot;text-xl text-gray-300&quot;&gt;Join thousands of companies building better products&lt;/p&gt;
            &lt;/div&gt;
            
            &lt;div class=&quot;grid grid-cols-2 md:grid-cols-4 gap-8 mb-16&quot;&gt;
                &lt;div class=&quot;text-center&quot;&gt;
                    &lt;div class=&quot;text-5xl font-bold mb-2 text-yellow-400&quot;&gt;2.5M+&lt;/div&gt;
                    &lt;div class=&quot;text-gray-400&quot;&gt;Projects Created&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class=&quot;text-center&quot;&gt;
                    &lt;div class=&quot;text-5xl font-bold mb-2 text-yellow-400&quot;&gt;50K+&lt;/div&gt;
                    &lt;div class=&quot;text-gray-400&quot;&gt;Active Teams&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class=&quot;text-center&quot;&gt;
                    &lt;div class=&quot;text-5xl font-bold mb-2 text-yellow-400&quot;&gt;150+&lt;/div&gt;
                    &lt;div class=&quot;text-gray-400&quot;&gt;Countries&lt;/div&gt;
                &lt;/div&gt;
                &lt;div class=&quot;text-center&quot;&gt;
                    &lt;div class=&quot;text-5xl font-bold mb-2 text-yellow-400&quot;&gt;99.9%&lt;/div&gt;
                    &lt;div class=&quot;text-gray-400&quot;&gt;Uptime SLA&lt;/div&gt;
                &lt;/div&gt;
            &lt;/div&gt;

            &lt;div class=&quot;flex flex-wrap justify-center items-center gap-12 opacity-60&quot;&gt;
                &lt;div class=&quot;text-3xl font-bold&quot;&gt;Stripe&lt;/div&gt;
                &lt;div class=&quot;text-3xl font-bold&quot;&gt;Notion&lt;/div&gt;
                &lt;div class=&quot;text-3xl font-bold&quot;&gt;Figma&lt;/div&gt;
                &lt;div class=&quot;text-3xl font-bold&quot;&gt;Webflow&lt;/div&gt;
                &lt;div class=&quot;text-3xl font-bold&quot;&gt;Linear&lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- Testimonials --&gt;
    &lt;section id=&quot;testimonials&quot; class=&quot;py-32 px-8 bg-gray-50&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto&quot;&gt;
            &lt;div class=&quot;text-center mb-20&quot;&gt;
                &lt;h2 class=&quot;text-5xl font-bold mb-6&quot;&gt;Loved by teams everywhere&lt;/h2&gt;
                &lt;p class=&quot;text-xl text-gray-600&quot;&gt;Don&#x27;t just take our word for it&lt;/p&gt;
            &lt;/div&gt;

            &lt;div class=&quot;grid md:grid-cols-3 gap-8&quot;&gt;
                &lt;div class=&quot;testimonial&quot;&gt;
                    &lt;div class=&quot;flex items-center gap-1 mb-4&quot;&gt;
                        &lt;span class=&quot;text-yellow-400 text-xl&quot;&gt;★★★★★&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;p class=&quot;text-gray-700 mb-6&quot;&gt;&quot;Momentum completely changed how our team works. We shipped our last feature 40% faster than usual. The automation is brilliant.&quot;&lt;/p&gt;
                    &lt;div class=&quot;flex items-center gap-3&quot;&gt;
                        &lt;div class=&quot;w-12 h-12 rounded-full bg-gradient-to-br from-purple-400 to-pink-400&quot;&gt;&lt;/div&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;font-bold&quot;&gt;Sarah Chen&lt;/div&gt;
                            &lt;div class=&quot;text-sm text-gray-500&quot;&gt;Head of Product, TechCorp&lt;/div&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;

                &lt;div class=&quot;testimonial&quot;&gt;
                    &lt;div class=&quot;flex items-center gap-1 mb-4&quot;&gt;
                        &lt;span class=&quot;text-yellow-400 text-xl&quot;&gt;★★★★★&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;p class=&quot;text-gray-700 mb-6&quot;&gt;&quot;Finally, a project management tool that doesn&#x27;t feel like homework. Our team adoption rate was 100% in the first week.&quot;&lt;/p&gt;
                    &lt;div class=&quot;flex items-center gap-3&quot;&gt;
                        &lt;div class=&quot;w-12 h-12 rounded-full bg-gradient-to-br from-blue-400 to-cyan-400&quot;&gt;&lt;/div&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;font-bold&quot;&gt;Marcus Rodriguez&lt;/div&gt;
                            &lt;div class=&quot;text-sm text-gray-500&quot;&gt;Engineering Manager, StartupXYZ&lt;/div&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;

                &lt;div class=&quot;testimonial&quot;&gt;
                    &lt;div class=&quot;flex items-center gap-1 mb-4&quot;&gt;
                        &lt;span class=&quot;text-yellow-400 text-xl&quot;&gt;★★★★★&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;p class=&quot;text-gray-700 mb-6&quot;&gt;&quot;The real-time collaboration features are next level. It&#x27;s like Google Docs, but for project management. Game changer.&quot;&lt;/p&gt;
                    &lt;div class=&quot;flex items-center gap-3&quot;&gt;
                        &lt;div class=&quot;w-12 h-12 rounded-full bg-gradient-to-br from-green-400 to-emerald-400&quot;&gt;&lt;/div&gt;
                        &lt;div&gt;
                            &lt;div class=&quot;font-bold&quot;&gt;Aisha Patel&lt;/div&gt;
                            &lt;div class=&quot;text-sm text-gray-500&quot;&gt;Design Lead, CreativeStudio&lt;/div&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- Pricing --&gt;
    &lt;section id=&quot;pricing&quot; class=&quot;py-32 px-8 bg-white&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto&quot;&gt;
            &lt;div class=&quot;text-center mb-20&quot;&gt;
                &lt;h2 class=&quot;text-5xl md:text-6xl font-bold mb-6&quot;&gt;Simple, transparent pricing&lt;/h2&gt;
                &lt;p class=&quot;text-xl text-gray-600&quot;&gt;No hidden fees. Cancel anytime. Start with a 14-day free trial.&lt;/p&gt;
            &lt;/div&gt;

            &lt;div class=&quot;grid md:grid-cols-3 gap-8 max-w-6xl mx-auto&quot;&gt;
                &lt;div class=&quot;pricing-card&quot;&gt;
                    &lt;div class=&quot;text-sm font-bold text-gray-500 mb-2&quot;&gt;STARTER&lt;/div&gt;
                    &lt;div class=&quot;mb-6&quot;&gt;
                        &lt;span class=&quot;text-5xl font-bold&quot;&gt;$12&lt;/span&gt;
                        &lt;span class=&quot;text-gray-500&quot;&gt;/user/month&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;ul class=&quot;space-y-4 mb-8&quot;&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Up to 10 team members&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Unlimited projects&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Basic integrations&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;5GB storage&lt;/span&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                    &lt;a href=&quot;#&quot; class=&quot;block text-center bg-gray-900 text-white py-3 rounded-full font-bold hover:bg-gray-800 transition&quot;&gt;
                        Start Free Trial
                    &lt;/a&gt;
                &lt;/div&gt;

                &lt;div class=&quot;pricing-card featured&quot;&gt;
                    &lt;div class=&quot;text-sm font-bold text-orange-500 mb-2&quot;&gt;PROFESSIONAL&lt;/div&gt;
                    &lt;div class=&quot;mb-6&quot;&gt;
                        &lt;span class=&quot;text-5xl font-bold&quot;&gt;$29&lt;/span&gt;
                        &lt;span class=&quot;text-gray-500&quot;&gt;/user/month&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;ul class=&quot;space-y-4 mb-8&quot;&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Unlimited team members&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Advanced automation&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;All integrations&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;100GB storage&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Priority support&lt;/span&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                    &lt;a href=&quot;#&quot; class=&quot;block text-center bg-orange-500 text-white py-3 rounded-full font-bold hover:bg-orange-600 transition&quot;&gt;
                        Start Free Trial
                    &lt;/a&gt;
                &lt;/div&gt;

                &lt;div class=&quot;pricing-card&quot;&gt;
                    &lt;div class=&quot;text-sm font-bold text-gray-500 mb-2&quot;&gt;ENTERPRISE&lt;/div&gt;
                    &lt;div class=&quot;mb-6&quot;&gt;
                        &lt;span class=&quot;text-5xl font-bold&quot;&gt;Custom&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;ul class=&quot;space-y-4 mb-8&quot;&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Everything in Pro&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Advanced security&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Custom integrations&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Unlimited storage&lt;/span&gt;
                        &lt;/li&gt;
                        &lt;li class=&quot;flex items-center gap-2&quot;&gt;
                            &lt;span class=&quot;text-green-500&quot;&gt;✓&lt;/span&gt;
                            &lt;span&gt;Dedicated support&lt;/span&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                    &lt;a href=&quot;#&quot; class=&quot;block text-center bg-gray-900 text-white py-3 rounded-full font-bold hover:bg-gray-800 transition&quot;&gt;
                        Contact Sales
                    &lt;/a&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- CTA Section --&gt;
    &lt;section class=&quot;py-32 px-8 bg-gradient-to-br from-orange-500 to-yellow-400 text-white&quot;&gt;
        &lt;div class=&quot;max-w-4xl mx-auto text-center&quot;&gt;
            &lt;h2 class=&quot;text-5xl md:text-6xl font-bold mb-6&quot;&gt;Ready to build momentum?&lt;/h2&gt;
            &lt;p class=&quot;text-2xl mb-12 text-white/90&quot;&gt;Join 50,000+ teams shipping faster with Momentum&lt;/p&gt;
            &lt;div class=&quot;flex flex-wrap gap-4 justify-center&quot;&gt;
                &lt;a href=&quot;#&quot; class=&quot;bg-white text-orange-500 px-10 py-5 rounded-full font-bold text-lg hover:bg-gray-100 transition inline-block&quot;&gt;
                    Start Free Trial
                &lt;/a&gt;
                &lt;a href=&quot;#&quot; class=&quot;bg-white/10 backdrop-blur text-white px-10 py-5 rounded-full font-bold text-lg hover:bg-white/20 transition inline-block&quot;&gt;
                    Schedule Demo
                &lt;/a&gt;
            &lt;/div&gt;
            &lt;p class=&quot;mt-8 text-white/80&quot;&gt;No credit card required • 14-day free trial • Cancel anytime&lt;/p&gt;
        &lt;/div&gt;
    &lt;/section&gt;

    &lt;!-- Footer --&gt;
    &lt;footer class=&quot;bg-gray-900 text-white py-16 px-8&quot;&gt;
        &lt;div class=&quot;max-w-7xl mx-auto&quot;&gt;
            &lt;div class=&quot;grid md:grid-cols-4 gap-12 mb-12&quot;&gt;
                &lt;div&gt;
                    &lt;div class=&quot;flex items-center gap-2 mb-4&quot;&gt;
                        &lt;div class=&quot;w-10 h-10 rounded-full bg-gradient-to-br from-orange-500 to-yellow-400 flex items-center justify-center&quot;&gt;
                            &lt;span class=&quot;text-white font-bold text-xl&quot;&gt;M&lt;/span&gt;
                        &lt;/div&gt;
                        &lt;span class=&quot;text-2xl font-bold&quot;&gt;Momentum&lt;/span&gt;
                    &lt;/div&gt;
                    &lt;p class=&quot;text-gray-400&quot;&gt;Building momentum for teams that ship.&lt;/p&gt;
                &lt;/div&gt;
                
                &lt;div&gt;
                    &lt;h4 class=&quot;font-bold mb-4&quot;&gt;Product&lt;/h4&gt;
                    &lt;ul class=&quot;space-y-2 text-gray-400&quot;&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Features&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Pricing&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Integrations&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Changelog&lt;/a&gt;&lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/div&gt;
                
                &lt;div&gt;
                    &lt;h4 class=&quot;font-bold mb-4&quot;&gt;Company&lt;/h4&gt;
                    &lt;ul class=&quot;space-y-2 text-gray-400&quot;&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;About&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Blog&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Careers&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Contact&lt;/a&gt;&lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/div&gt;
                
                &lt;div&gt;
                    &lt;h4 class=&quot;font-bold mb-4&quot;&gt;Legal&lt;/h4&gt;
                    &lt;ul class=&quot;space-y-2 text-gray-400&quot;&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Privacy&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Terms&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;Security&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href=&quot;#&quot; class=&quot;hover:text-white transition&quot;&gt;GDPR&lt;/a&gt;&lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            
            &lt;div class=&quot;border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4&quot;&gt;
                &lt;p class=&quot;text-gray-400&quot;&gt;© 2024 Momentum. All rights reserved.&lt;/p&gt;
                &lt;div class=&quot;flex gap-6&quot;&gt;
                    &lt;a href=&quot;#&quot; class=&quot;text-gray-400 hover:text-white transition&quot;&gt;Twitter&lt;/a&gt;
                    &lt;a href=&quot;#&quot; class=&quot;text-gray-400 hover:text-white transition&quot;&gt;LinkedIn&lt;/a&gt;
                    &lt;a href=&quot;#&quot; class=&quot;text-gray-400 hover:text-white transition&quot;&gt;GitHub&lt;/a&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/footer&gt;

    &lt;script&gt;
        // Navbar scroll effect
        const navbar = document.querySelector(&#x27;.navbar&#x27;);
        window.addEventListener(&#x27;scroll&#x27;, () =&gt; {
            if (window.scrollY &gt; 50) {
                navbar.classList.add(&#x27;scrolled&#x27;);
            } else {
                navbar.classList.remove(&#x27;scrolled&#x27;);
            }
        });

        // Smooth scroll for anchor links
        document.querySelectorAll(&#x27;a[href^=&quot;#&quot;]&#x27;).forEach(anchor =&gt; {
            anchor.addEventListener(&#x27;click&#x27;, function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute(&#x27;href&#x27;));
                if (target) {
                    target.scrollIntoView({
                        behavior: &#x27;smooth&#x27;,
                        block: &#x27;start&#x27;
                    });
                }
            });
        });

        // Intersection Observer for fade-in animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: &#x27;0px 0px -50px 0px&#x27;
        };

        const observer = new IntersectionObserver((entries) =&gt; {
            entries.forEach(entry =&gt; {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = &#x27;1&#x27;;
                    entry.target.style.transform = &#x27;translateY(0)&#x27;;
                }
            });
        }, observerOptions);

        document.querySelectorAll(&#x27;.feature-card, .testimonial, .pricing-card&#x27;).forEach(el =&gt; {
            el.style.opacity = &#x27;0&#x27;;
            el.style.transform = &#x27;translateY(30px)&#x27;;
            el.style.transition = &#x27;opacity 0.6s ease, transform 0.6s ease&#x27;;
            observer.observe(el);
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```</pre>
    </div>
    
:::

::: {.output .stream .stdout}

    ✅ Complete in 98.2s

    💾 HTML saved to: html_outputs/20251021_101010.html
    🌐 Opened in browser: html_outputs/20251021_101010.html
:::

::: {.output .execute_result execution_count="3"}
    'html_outputs/20251021_101010.html'
:::
:::::::

::: {.cell .markdown}
## Isolated Prompting

The full aesthetics prompt works well for general use, but sometimes you
want targeted control. You can isolate specific dimensions (typography,
color, motion) or lock in a particular theme. This gives you faster
generation times and more predictable outputs.

### Example 1: Typography Only

Isolate a single design dimension when you want to improve one aspect
without changing others:
:::

::: {.cell .code}
``` python
TYPOGRAPHY_PROMPT = """
<use_interesting_fonts>
Typography instantly signals quality. Avoid using boring, generic fonts.

**Never use:** Inter, Roboto, Open Sans, Lato, default system fonts

**Impact choices:**
- Code aesthetic: JetBrains Mono, Fira Code, Space Grotesk
- Editorial: Playfair Display, Crimson Pro, Fraunces
- Startup: Clash Display, Satoshi, Cabinet Grotesk
- Technical: IBM Plex family, Source Sans 3
- Distinctive: Bricolage Grotesque, Obviously, Newsreader

**Pairing principle:** High contrast = interesting. Display + monospace, serif + geometric sans, variable font across weights.

**Use extremes:** 100/200 weight vs 800/900, not 400 vs 600. Size jumps of 3x+, not 1.5x.

Pick one distinctive font, use it decisively. Load from Google Fonts. State your choice before coding.
</use_interesting_fonts>
"""

# Generate with typography-only guidance
generate_html_with_claude(BASE_SYSTEM_PROMPT + "\n\n" + TYPOGRAPHY_PROMPT, USER_PROMPT)
```
:::

::: {.cell .markdown}
### Example 2: Theme Constraint

Lock in a specific aesthetic when you want consistent theming across
generations:
:::

::: {.cell .code}
``` python
SOLARPUNK_THEME_PROMPT = """
<always_use_solarpunk_theme>
Always design with Solarpunk aesthetic:
- Warm, optimistic color palettes (greens, golds, earth tones)
- Organic shapes mixed with technical elements
- Nature-inspired patterns and textures
- Bright, hopeful atmosphere
- Retro-futuristic typography
</always_use_solarpunk_theme>
"""

# Generate with theme constraint
generate_html_with_claude(
    BASE_SYSTEM_PROMPT + "\n\n" + SOLARPUNK_THEME_PROMPT,
    "Create a dashboard for renewable energy monitoring",
)
```
:::

::: {.cell .markdown}
## Summary

Claude has strong design capabilities but defaults to safe, generic
choices. The techniques in this guide - targeting specific design
dimensions, referencing concrete inspirations, and explicitly avoiding
common defaults - reliably produce more distinctive output. The full
aesthetics prompt works well as a baseline. For more control, use
isolated prompts to focus on individual aspects or lock in specific
themes across multiple generations.
:::
