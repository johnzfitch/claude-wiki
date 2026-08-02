---
title: "Claude Science beta | Claude by Anthropic"
source_url: "https://www.claude.com/product/claude-science"
category: "15-Claude-AI-Features"
fetched_at: "2026-08-02T05:42:25Z"
tags: ["search"]
---

# Claude Science beta

## Your research partner for rigorous science

The Claude Science app runs analyses, searches databases, and traces every step from data wrangling to publication, so you can spend time on science.

Download now

Mac (Apple Silicon)

[Mac (Apple Silicon)](https://downloads.claude.ai/claude-science/latest/mac-arm64.dmg)

Mac (Apple Silicon)

Mac (Intel)

[Mac (Intel)](https://downloads.claude.ai/claude-science/latest/mac-x64.dmg)

Mac (Intel)

Linux

[Linux](https://downloads.claude.ai/claude-science/latest/linux-x64)

Linux


[Contact sales](/contact-sales/life-sciences)


[Play video](#)

Play video

## Built for scientific research

### Rich scientific artifacts, fully reproducible

View proteins, structures, and molecules natively, with every result reproducible and traced to its code.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Cross-species Samosa — file viewer

Claude Science

Beta

Cross-species Samosa

New

Customize

Files

Today

Samosa Manuscript

Samosa Editorial Review

Samosa Model Training

Samosa Benchmarking

samosa_fig1a.png

samosa_fig1a.png

1

1

Send

samosa_fig1a.png

v2

Code

Execution Log

Messages

Environment

Review

Download script

Inputs

fig4_atlas_callouts.csv

fig4_atlas_centroids_m138ea.csv

#### Execution Log · v2

10:42:07.118INFOLoading environment · python 3.11.8, matplotlib 3.9.2

10:42:07.669INFOread_csv fig4_atlas_centroids_m138ea.csv → 5,672 rows

10:42:07.902INFOread_csv fig4_atlas_callouts.csv → 16 rows

10:42:08.331INFOapply_nature_style() · font.family = sans-serif

10:42:09.774WARN3 callout labels overlap in the “muscle” inset — nudging

10:42:11.205INFORendering 3 inset panels (i, ii, iii)

10:42:12.840DONESaved samosa_fig1a.png (2161×2244, 300 dpi) in 5.72s

#### Messages

S

You · 10:41

Rebuild Fig 1a as a single shared UMAP across all 138 species. Colour by cell-type family and box the three insets.

C

Claude · 10:42

Done — one embedding, 5,672 cell types coloured by family (neuron, muscle, immune, ciliated, germline, stem/progenitor). Added callout insets i–iii and a phylum palette. Rendered to samosa_fig1a.png.

S

You · 10:44

The family labels on the scatter are hard to read against the dense points. Can you add a white halo?

#### Environment

python3.11.8

matplotlib3.9.2

pandas2.2.2

numpy1.26.4

scanpy1.10.1

umap-learn0.5.6

#### Review checklist

Single shared embedding across all 138 species

Colour mapping matches HERO family palette

Inset boxes i–iii aligned to centroid callouts

Legend order & phylum palette (PHYL_PAL2) verified

Approved — 4 of 4 checks passing. Ready to place in the manuscript.

### Every artifact ships with its history 

Figures, tables, and notebooks include the exact code, environment, and conversation that produced them, so they can be reproduced, edited, or defended months later.

### Built-in scientific renderers

Inspect proteins, alignments, genomic tracks, chemical structures, and PDFs in their native form, with no extra installation required.

### Results that check and correct themselves 

A background reviewer flags incorrect citations, untraceable numbers, and figures that don’t match their underlying code.

### Figure iteration in plain language

Annotate a figure to request edits or ask a question. The agent reads the code that produced it and edits directly.

### Draft manuscripts in one place

Write up results alongside the analysis that produced them, with rendered Markdown and LaTeX previews.

### Manages your compute and scales on demand

Builds environments and manages compute on your laptop, your cluster, or GPUs.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

SCVI Hyperparameter Screen — Claude Science

SCVI Hyperparameter Screen

Claude Science

Beta

scRNA-seq

New

Customize

Files

Active

SCVI Hyperparameter Screen

8

Dispatching the 8-arm scVI sweep to lab_cluster A100s — n_latent ∈ {10, 20, 30, 50} × n_layers ∈ {1, 2} , 40k cells × 2,000 HVGs, batch_key="sample_id" , 50 epochs, seed 0.

arm

n_latent

n_layers

label

Remote · 8

8 running · 16m 2s

Notebook

pbmc-pipeline

Shared with the agent

Live

Live

Idle

\[28\]

python

**Note to the agent.** This kernel is the working **pbmc-pipeline** session. The reduced object covid_pbmc_40k_hvg.h5ad (counts + obs + var only) is on disk and loaded as a. All 8 scVI arms read from it; nothing else is mutated. Inspect a.obs and the HVG panel before adding a step.

Shared variables

aAnnData · 40,000 × 2,000

cleanAnnData · counts + obs + var

keep_obslist\[str\] · 8 columns

batch_keystr · "sample_id"

armslist · 8 scVI configs

output

wrote covid_pbmc_40k_hvg.h5ad

Python — pbmc-pipeline kernel

Connected to the agent’s live kernel — variables and state are shared. Type an expression and press Enter.

### Works wherever your data lives

Claude manages the environments each analysis needs, whether on your laptop, a Linux box, or an HPC login node.

### From one GPU to hundreds

Writes batch scripts, then submits and manages jobs over SSH on your own machine or HPC cluster, or through your Modal account.

### Persistent Python and R kernels

Variables, dataframes, and loaded models stay in memory across the whole analysis, so iteration is fast.

### Domain-ready on day one

Connects to databases and tools your lab needs, so you can start work in your field right away.

Prompt

Can you tell me ...

Attachments

Document

84kb

TXT

Document

105 lines

TXT

Literature review — Claude Science

Claude Science

Beta

Literature review

New

Customize

Files

Active

Cross-species scRNA-s…

Cross-species scRNA-seq Integration…

Write a literature review on cross-species single-cell RNA-seq integration. Pull the primary methods papers and recent benchmarks. Output the report as a LaTeX doc and a compiled PDF.

Ran 4 searches, loaded 2 skills, managed environments, +2 more 10 steps

search pubmed "cross-species scRNA-seq integration" → 38 hits

search biorxiv "orthology-free single-cell embedding" → 12 hits

skill load literature-synthesis@1.4 ok

skill load latex-report-builder@0.9 ok

env create cellxgene-census (py3.11) ready

env mount /work/refs rw

Dispatching five parallel literature-retrieval tracks — PubMed primary methods, bioRxiv preprints, OpenAlex citation counts, CELLxGENE multi-species atlas inventory, and orthology-free embedding methods.

Dispatching PubMed bioRxiv OpenAlex CELLxGENE sub-agents 142 lines of output

pubmed-agent → 24 primary-methods papers (2018–2025)

biorxiv-agent → 9 preprints, 3 with matched benchmarks

openalex-agent → citation counts resolved for 21/24

cellxgene-agent → 15 species pairs, 6 benchmarked atlases

merge → deduped to 24 refs, wrote refs.csv ✓

Reviewer  ·  1 finding

Warn PMID 31178118 assigned to both LIGER and Seurat v3 integration in the plan

In the generate_plan PubMed delegation step the agent writes "LIGER (31178118), Seurat v3 integration (31178118)" — the same PMID for two distinct primary methods papers. The same plan's OpenAlex step assigns them different DOIs (Seurat v3 10.1016/j.cell.2019.05.031, LIGER 10.1016/j.cell.2019.05.006), so the plan is internally inconsistent and at least one PMID is wrong. None of the PMIDs or DOIs in msg\[10\] trace to any in-window tool output — no PubMed/CrossRef/OpenAlex lookup has run (exec-log rows 04449b53, 57baea0a, 254f1378 are the two skill kernel.py auto-loads and the env-filter bash; msg\[4\] tool_results are skill-catalog listings only).

The agent reads these findings and self-corrects in its next message.

Acknowledged — the plan listed PMID 31178118 for both; the PubMed sub-agent caught the swap and the saved CSV carries the corrected pair (LIGER 31178122, Seurat v3 31178118).

all 5 agents done

Reviewing

review.pdf

### Pre-configured for your domain

Genomics, single-cell, proteomics, structural biology, cheminformatics, and more. Reads literature and can query 60+ scientific databases, so you pull what you need without learning each one.

### Built to be extended

Save any pipeline as a reusable skill, or connect to your lab’s preferred tool with a connector, and every future session inherits it automatically.

### Capabilities from bench to boardroom 

Includes fully sourced indication dossiers available today, and a growing set of skills that build the case behind every program.

Introducing Claude Science

One research environment for your lab: connect to scientific databases, research tools, ELNs, protein and structure models, your HPC, and more. Available now for macOS and Linux.

Read the blog

[Read the blog](https://www.anthropic.com/news/claude-science-ai-workbench)

Read the blog

## How researchers use Claude Science

The app is pre-configured for every major domain in life sciences. When a project spans disciplines, it can help solve hard problems.

Single-cell RNA-seq

Evolutionary analysis

Protein structure

Cheminformatics

Active

Prompt

Design a comprehensive study guide with summaries, practice questions, and memory aids from my course materials.

Attachments

Tabula Sapiens

# Tabula Sapiens

1,136,218 cells · 28 organs · CELLxGENE

## Cell-type markers

Hover a tissue island or a marker dot to explore

### Single-cell RNA-seq analysis

Cluster and annotate millions of cells across tissues, surface marker genes, and trace every figure back to the code that made it.

Prompt

Design a comprehensive study guide with summaries, practice questions, and memory aids from my course materials.

Attachments

Rhodopsin (RHO) — 46 vertebrates · IQ-TREE

# Rhodopsin (RHO) — 46 vertebrates · IQ-TREE

a

b

## Spectral-tuning residues

### Phylogenetic and evolutionary analysis

Align orthologs, infer maximum-likelihood trees, and map functional residues onto the phylogeny in a single reproducible session.

Prompt

Design a comprehensive study guide with summaries, practice questions, and memory aids from my course materials.

Attachments

# KRAS

P01116 · GTPase KRas · *Homo sapiens*

**189 aa**length

**91.5**mean pLDDT

**1**Pfam domain

**99**pathogenic variants

pLDDT very high (≥90) high (70–90) low (50–70) very low (\<50) oncogenic hotspot

### Domain architecture & pathogenic variants

Pfam domains and ClinVar/UniProt pathogenic missense positions along the 189-residue sequence

### Model confidence

AlphaFold per-residue pLDDT distribution

91.5mean

78% ≥90 15% 70–90 5% 50–70 2% \<50

### Pfam domains

1 domain · InterPro

Ras family5–164PF00071

### Top pathogenic variants

99 pathogenic missense at 32 positions · ClinVar/UniProt

| Residue | Substitutions | \#  |
|---------|---------------|-----|
| G12     | A/C/D/R/S/V   | 6   |
| G13     | A/C/D/R/S/V   | 6   |
| G60     | A/C/D/R/S/V   | 6   |
| Q61     | E/H/K/L/P/R   | 6   |
| A146    | E/G/P/S/T/V   | 6   |
| Q22     | E/K/L/R       | 4   |
| T50     | A/I/P/S       | 4   |
| A59     | L/P/S/T       | 4   |

### Structure source

AlphaFold DB

**AF-P01116-F1** · v6

GTPase KRas

### Protein structure and language model work

Pull predicted structures, layer on domains and clinical variants, and explore the model interactively in 3D.

Prompt

Design a comprehensive study guide with summaries, practice questions, and memory aids from my course materials.

Attachments

KRAS inhibitors · Ketcher

kras_inhibitors.ket ‹ v4 ›

Ketcher Chemistry › open_sketcher

Help Save

34% ▾

▸ A⁺ A⁻ ▸ T

H C N O S P F Cl Br I

SL

### Cheminformatics and molecular design

Search bioactivity data, compute properties and similarities, and draw or refine structures in a live 2D sketcher.

“With Claude Science I can go from raw data to a publication-quality figure in a single session — running the analysis, generating exploratory plots, and refining them all within a single project. The code and the conversation behind each figure are welded to it, making every version fully reproducible so I can iterate, revert, and fork as much as needed.”

Mike Nichols, Computational Biologist, Manifold Bio

“Claude Science is enabling analyses that simply wouldn’t have been feasible for me as a non-computational biologist. Honestly, it’s really transformative. Its ability to run these analyses, fluidly navigate the existing websites, and consider the science carefully is quite impressive… I’ve found myself thinking of questions I’ve had for years and rushing to Claude Science to start a project.”

Iain Cheeseman, Professor of Biology, Whitehead Institute and Department of Biology, MIT

“Claude Science is, without exaggeration, the most impressive AI-integrated scientific computing environment I have encountered.”

Prasad Shirvalkar, Associate Professor of Neurosurgery and Anesthesiology, UCSF

“Claude Science immediately found a laboratory virus contaminant in our bulk RNA-seq data. We spun our wheels on this for the better part of a year, and it came out as one of the first key findings.”

Stephen Francis, Principal Investigator, UCSF

“New agentic fact-checking capabilities in Claude Science have helped our team build confidence in the biomedical outputs. This makes Claude particularly useful for our triage and medical review work.”

Elliott Sharp, Director of Pipeline Strategy, Every Cure

“Xaira is building AI-native capabilities across the full arc of drug discovery and development, from predictive models to physical AI systems that learn from biology at scale, powered by agentic workflows designed to create the next generation of medicines. Claude Code and Claude Science are accelerating that work, compressing the path from hypothesis to validation and advancing our therapeutic pipeline, enabling our scientists to focus on the discoveries that matter most and bring innovative medicines to patients faster.”

Xaira

“Claude Science helps me turn biological questions into first-pass literature reviews and genomics analyses that are well cited, hypothesis-generating, and ready for team critique.”

Trygve Bakken, Associate Investigator, Allen Institute

“LatchBio provides agent-native data infrastructure to store, process, and visualize large molecular datasets from their favorite interfaces. Connecting LatchBio to Claude Science via MCP allows researchers to leverage verified bioinformatics tools deployed in collaboration with assay developers like Vizgen, TakaraBio and AtlasXOmics to complete agent workflows with high scientific accuracy.”

Kenny Workman, Co-founder & CTO, LatchBio

“Helix® is building the largest linked clinico-genomic dataset in the world - currently over 500,000 records and on a trajectory to multiple millions. By making deep genetic and phenotypic data available to Claude Science through an MCP server, we’re letting researchers discover our data inside a single, AI-native environment. Many of these researchers use Claude as their go to platform for discovery and this brings the full depth of our data to where the science actually gets done.”

James Lu, MD, PhD. Chief Executive Officer & Co-founder, Helix

“Claude Science is accelerating the way we design experiments and identify new treatments. It’s dramatically speeding up the time it takes to go from genetic signal to potential therapy.”

Professor Joseph Powell, Garvan Institute

[Prev](#)

Prev

0/5


## Works with your stack

Connectors bring your internal APIs, ELNs, and bespoke pipelines into the workflow, so the Claude Science app works with the tools your lab already runs.

Explore connectors

[Explore connectors](/connectors)

Explore connectors

## FAQs

### Is Claude Science a new model?

No. Claude Science is a public beta app, not a model. It uses the same Claude models your plan includes. What’s new is everything around them: the scientific tools, database connections, and compute integrations that let Claude run full analyses on your own infrastructure.

### What can the Claude Science app do that a general AI assistant can’t?

General AI assistants can discuss biology, but they can’t run a pipeline, navigate scientific databases, orchestrate cluster jobs, or keep track of what happened in a previous session. Claude Science manages compute environments per specialist, and saves full provenance on every result. The app ships with analysis specialists for genomics, single-cell, proteomics, structural biology, cheminformatics, and more. It can connect natively to 60+ scientific databases and domain-specific open models. Claude Science uses the skills in NVIDIA’s [BioNeMo Agent Toolkit](https://nvidianews.nvidia.com/news/nvidia-launches-bionemo-agent-toolkit-giving-ai-agents-the-tools-to-accelerate-scientific-discovery) to connect natively to the life sciences models and libraries in [BioNeMo](https://github.com/NVIDIA-BioNeMo), including Evo 2, Boltz-2, and OpenFold3.

### What about the pipelines and code I already have? 

The Claude Science app is designed to work with what you’ve already built. Connect your existing tools, ELNs, and internal systems through connectors. Bring your own scripts—it can read, run, and build on existing Python, R, and shell workflows without requiring you to rebuild anything from scratch.

### Does this replace specialized tools?

No. The Claude Science app is the workbench where specialized tools work together. Scientific tools, platforms, and domain-specific open models can plug in as skills or connectors. You keep what works and fill in the gaps.

### Is my research data private?

The Claude Science app runs on your infrastructure; raw datasets and compute stay local; content included in prompts and model responses is processed by Anthropic under standard retention. Contact sales to discuss your team's specific needs.

### Where does the Claude Science app run?

Install the app wherever your data lives: your laptop, a lab Linux box, an HPC login node, or a cloud VM. Connect from your browser. Jobs run on local kernels, your Slurm cluster over SSH, or through your Modal account.

### What does ‘provenance’ mean?

Every artifact the Claude Science app produces includes the exact code that generated it, the environment it ran in, a plain-language description of what was done, and the conversation that led there. Results are reproducible months later, by anyone on your team. A background reviewer also flags any claim it can’t trace to evidence before results surface.

### Is this available now?

Yes. The Claude Science app is in beta for macOS and Linux on Pro, Max, Team, and Enterprise plans. Team and Enterprise users need their admin to enable it first.

### Is there a discount for academic or nonprofit labs?

Yes. The discounted [Claude Team plan for research labs](https://claude.com/programs/claude-team-plan-for-research-labs) includes access to the Claude Science app, and is available to active scientific labs at academic institutions and nonprofit research organizations. Specifically, biomedical and basic science labs are being prioritized in addition to the hard sciences including chemistry, math, computer science, and physics. Eligibility is verified through the lab’s principal investigator.

If you are a for-profit company, contract research organization, or industry R&D team, please see our [Team and Enterprise plans](https://claude.com/pricing#team-&-enterprise).

### Is there enterprise support?

Yes. The Claude Science app is available on the Enterprise plan with SSO, SCIM provisioning, custom roles, and usage analytics. It’s currently in beta, so admins should review the [documentation](http://claude.com/docs/claude-science) before rolling out. Contact sales to discuss your team’s requirements.

### Where can I learn more?

Start with the [documentation](http://claude.com/docs/claude-science). It covers installation, connecting your tools and compute, and admin setup for Team and Enterprise.

[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)

Button Text

Learn

[Button Text](#)

Button Text

Code

[Button Text](#)

Button Text

Write

- Help me develop a unique voice for an audience


  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style


  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas


  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply


  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas


  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview


  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept


  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips


  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me


  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies


  This is another test

- Write grant proposals


  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts


  this is a test

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Design

  [Claude Design](/product/design)
  Claude Design

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Features

- Claude for Chrome

  [Claude for Chrome](/claude-for-chrome)
  Claude for Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

- Skills

  [Skills](/skills)
  Skills

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Solutions

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Enterprise

  [Enterprise](/solutions/enterprise)
  Enterprise

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Legal

  [Legal](/solutions/legal)
  Legal

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Claude Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://platform.claude.com/docs)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Ecosystem

  [Ecosystem](/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Console login

  [Console login](https://platform.claude.com/)
  Console login

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Community

  [Community](/community)
  Community

- Connectors

  [Connectors](/connectors)
  Connectors

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](/plugins)
  Plugins

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/partners/services)
  Service partners

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
  Use cases

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Policy on the AI Exponential
