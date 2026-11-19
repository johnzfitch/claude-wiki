---
title: "Research Plan: NLL Resummation of the Sudakov"
source_url: "https://www-cdn.anthropic.com/2595299ccf7f8b9a9c74823c24faaa5d9b216804.pdf"
category: "19-Reference"
fetched_at: "2026-11-18T06:28:47Z"
tags: ["news-research", "search"]
---

Research Plan: NLL Resummation of the Sudakov
            Shoulder in the C-Parameter


                                      December 19, 2025


                                            Abstract
      This document presents a comprehensive research plan for deriving a factorization formula
   and performing next-to-leading logarithmic (NLL) resummation of the Sudakov shoulder in
   the C-parameter distribution for e+ e− annihilation. The methodology follows and extends the
   analysis established for thrust and heavy jet mass by Bhattacharya, Schwartz, and Zhang. The
   C-parameter exhibits a step discontinuity at its LO phase space boundary C = 3/4, making it
   a particularly interesting case with unique features.


Contents


                                                1
1     Project Overview

     Project Goal

     Derive and validate a factorization theorem and NLL resummed expression for the Sudakov
     shoulder in the C-parameter distribution in e+ e− annihilation, following and extending the
     thrust/HJM shoulder analysis.


1.1     Core Ingredients Required

    (i) Precise characterization of the shoulder region at fixed order

 (ii) A SCET-based factorization theorem around the symmetric three-jet configuration

(iii) One-loop hard/jet/soft functions and their anomalous dimensions

(iv) NLL resummation, matching, and numerical implementation

 (v) Validation against fixed-order codes and analysis of systematic effects


1.2     Project Milestones

M1: Reproduce and understand the thrust/HJM shoulder analysis in the reference paper

M2: Complete NLO shoulder analysis for C and identify the logarithmic structure

M3: Derive and verify the factorization theorem for C in the shoulder limit

M4: Compute/assemble all one-loop ingredients and perform NLL resummation

M5: Implement numerical code and perform phenomenological/consistency checks


2     Observable Definition and Shoulder Kinematics
     C-Parameter Definition
     The C-parameter is defined by:

                               3 X |⃗
                                    pi ||⃗
                                         pj |
                          C=             2
                                              sin2 θij = 3(λ1 λ2 + λ2 λ3 + λ3 λ1 )                (1)
                               2      Q
                                  i,j

                                                                                     P pαj pβj
     where λi are eigenvalues of the linearized momentum tensor Θαβ = P 1|⃗pk |        j |⃗
                                                                                          pj |   with
     P                                                                      k

       i λi = 1.
     At leading order for three massless partons: 0 ≤ C ≤ Csh with Csh = 3/4.


                                                    2
          Key Insight: Discontinuity vs. Kink

          Unlike thrust and heavy jet mass, which exhibit a kink (discontinuity in the first deriva-
          tive) at their LO phase space boundary, the C-parameter has a step discontinuity in the
          distribution itself at C = 3/4. This fundamental difference may alter the structure of the
          resummed kernel.


      2.1    Shoulder Variables

      Define the shoulder variable for the right shoulder (NLO and beyond):
                                                    3
                              ∆ ≡ C − Csh = C −       >0    (right shoulder region)                    (2)
                                                    4
      and for the left shoulder (where LO contributes):
                                               3
                               c ≡ Csh − C =     −C >0      (left shoulder region)                     (3)
                                               4

      3     Stage I: Warm-Up and Kinematic Analysis

      Objective: Fix conventions, fully understand the geometry of the C-parameter shoulder, and bench-
      mark against the thrust/HJM case.


      3.1    Literature and Reference Analysis

 Task 1.1: Review the thrust/HJM shoulder paper (arXiv:2205.05702) in detail

 Task 1.2: Review original C-parameter literature (Catani–Webber, hep-ph/9710333)

 Task 1.3: Map notation and conventions between C-parameter literature and the reference paper

 Task 1.4: Summarize similarities/differences: sensitivity to global soft radiation, recoil issues, number
           of hard directions

 Task 1.5: Identify which arguments carry over trivially vs. which are C-specific


      3.2    Three-Parton Kinematics

 Task 1.6: Parameterize 3-body phase space using sij = (pi + pj )2 /Q2 with s12 + s13 + s23 = 1

 Task 1.7: Derive C in terms of invariants: verify C = 6 s12 s13 s23

 Task 1.8: Confirm Csh = 3/4 at symmetric trijet: s12 = s13 = s23 = 1/3

 Task 1.9: Derive the LO distribution analytically and confirm step discontinuity behavior:
                                                            
                                           1 dσ         3
                                                  ∝θ      − C × f (C)                                  (4)
                                          σ0 dC         4

Task 1.10: Compute the explicit coefficient f (C) to set normalization for resummed calculation

                                                        3
       3.3     Four-Parton Onset

Task 1.11: Characterize the first 4-parton configurations populating ∆ > 0

Task 1.12: Introduce expansion parameter λ controlling deviations from symmetric trijet

Task 1.13: Relate ∆ (or c) to soft/collinear kinematic variables at leading power

Task 1.14: Determine whether left shoulder, right shoulder, or both require resummation


       4     Stage II: NLO Fixed-Order Analysis

       Objective: Isolate the regions of four-parton phase space that generate shoulder logarithms and
       extract their structure at O(αs2 ).


       4.1     Phase-Space Classification

 Task 2.1: Enumerate all 4-parton topologies: q q̄gg, q q̄q ′ q̄ ′ , q q̄q q̄

 Task 2.2: Separate regions continuously connected across C = 3/4 from those that are not

 Task 2.3: Identify which regions can produce large ln ∆ through phase-space squeezing

 Task 2.4: Derive phase space constraints analogous to W(mj , ki , c) > 0 from reference paper


       4.2     Soft/Collinear Power Counting

 Task 2.5: Define power counting: soft (ps ∼ Qλ), collinear (pc ∼ Q(λ2 , 1, λ)), soft-collinear

 Task 2.6: Express C in terms of sij /Q2 and expand around symmetric trijet point

 Task 2.7: Derive leading-power relation between ∆ and soft/collinear variables

 Task 2.8: Document which integration regions contribute logarithms


       4.3     Matrix Elements in Limiting Regions

 Task 2.9: Compute |Mγ ∗ →qq̄gg |2 in collinear limit with polarization structure

Task 2.10: Compute |Mγ ∗ →qq̄gg |2 in soft limit with correct color structure

Task 2.11: Compute soft-collinear overlap for subtraction

Task 2.12: Handle q q̄q ′ q̄ ′ and identical-quark channels

Task 2.13: Verify consistency with splitting functions


                                                                4
       4.4    Extraction of NLO Shoulder Logarithms

Task 2.14: Perform leading-power phase-space integrals

Task 2.15: Extract αs2 ln2 ∆ and αs2 ln ∆ coefficients

Task 2.16: Separate by color structure: CF2 , CF CA , CF TF nf

Task 2.17: Run EVENT2 with high statistics (> 1012 events, cutoff ∼ 10−12 )

Task 2.18: Compare analytic predictions to EVENT2 numerical results

Task 2.19: Create comparison plots analogous to Fig. 6 in reference paper


       5     Stage III: Factorization Theorem in SCET

       Objective: Derive a SCET factorization theorem that captures the shoulder dynamics in terms of
       hard, jet, and soft functions.


       5.1    Mode Structure

 Task 3.1: Specify three collinear directions ni from LO 3-parton configuration

 Task 3.2: Define scaling of collinear momenta in shoulder regime

 Task 3.3: Define scaling of soft momenta

 Task 3.4: Clarify whether collinear-soft or Glauber-like modes are required or can be excluded

 Task 3.5: Contrast with dijet limit (C → 0) to ensure shoulder-specific kinematics captured


       5.2    SCET Operator Basis

 Task 3.6: Write leading-power SCET current for three hard partons

 Task 3.7: Identify associated Wilson coefficient (hard function)

 Task 3.8: Discuss mapping between 3-jet hard function for thrust/HJM and that needed for C


       5.3    Measurement Function and Additive Decomposition

           Key Insight: Additive Decomposition

           A key step is deriving how the observable decomposes into collinear and soft contributions:

                                         ∆ = fcoll (m2i /Q2 ) + fsoft (ks /Q)                        (5)

           This additive structure is essential for the convolution form of the factorization theorem.


 Task 3.9: Express C in terms of SCET collinear and soft momenta at leading power

                                                          5
Task 3.10: Derive the additive decomposition relating ∆ to jet masses and soft radiation
Task 3.11: Define measurement functions for collinear and soft sectors separately


       5.4    Factorized Cross Section

           Factorization Formula
                                      Z                   3
                     dσ                                   Y
                                          [dm2i ][dks ]         Ji (m2i , µ) SC (ks , µ) δ ∆ − F(m2i , ks )
                                                                                                           
                        = HC (Q, µ)                                                                            (6)
                     d∆
                                                          i=1

           where F encodes the C-parameter measurement function.


Task 3.12: Derive the factorization formula with explicit measurement function
Task 3.13: Show hard 3-parton phase space factors from soft/collinear integrals
Task 3.14: Verify observable remains global at leading power (absence of non-global logs)
Task 3.15: Define 6-sextant decomposition of soft radiation (as in Fig. 4 of reference)
Task 3.16: Write 2-parameter trijet hemisphere soft function


       5.5    Recoil Sensitivity Analysis

           Recoil Sensitivity Warning

           Naive convolution pictures like σ(C) ∼ dm2 σLO (C − m2 )J(m2 ) can be ambiguous beyond
                                                 R

           leading-log level. We must factorize phase space rather than just convolve with emission
           cross sections.


Task 3.17: Understand how soft/collinear emissions shift C-parameter value
Task 3.18: Analyze whether holding jet energy vs. momentum fixed gives different results
Task 3.19: Verify the measurement constraint F properly captures kinematics without ambiguity


       6     Stage IV: One-Loop Ingredients and Anomalous Dimensions

       Objective: Assemble all perturbative building blocks needed for NLL resummation.


       6.1    Hard Function

 Task 4.1: Identify appropriate 3-jet hard function HC (Q, µ) and relation to thrust/HJM
 Task 4.2: Collect one-loop expression and anomalous dimension from literature
 Task 4.3: Translate conventions as needed
 Task 4.4: Verify RG consistency (cusp and non-cusp pieces)

                                                                 6
       6.2   Jet Functions

 Task 4.5: Determine if standard inclusive quark/gluon jet functions suffice

 Task 4.6: If yes, import known one-loop expressions and anomalous dimensions

 Task 4.7: If modifications needed, compute one-loop jet function with C-measurement

 Task 4.8: Extract anomalous dimensions γJq , γJg


       6.3   Soft Function for C-Parameter Shoulder

 Task 4.9: Define soft function SC as matrix element of soft Wilson lines in 3 collinear directions

Task 4.10: Define measurement function M (k, qi ) with 6 sextant regions

Task 4.11: Specify projection vectors for each region

Task 4.12: Compute 4 independent integrals I1 , I2 , I3 , I4 (as in reference paper Fig. 5)

Task 4.13: Extract UV poles and finite parts using dimensional regularization

Task 4.14: Check for transcendental constants (Gieseking’s constant κ, etc.)

Task 4.15: Combine with color structures for gluon-jet and quark-jet channels

Task 4.16: Extract cusp and non-cusp anomalous dimensions


       6.4   RG Consistency Check

Task 4.17: Verify anomalous dimension sum rule:

                                             γ H + γ J1 + γ J2 + γ J3 + γ S = 0                       (7)

Task 4.18: Check whether soft function differs from thrust/HJM at NLL level


       7     Stage V: NLL Resummation and Analytic Structure

       Objective: Perform NLL resummation of shoulder logarithms and analyze the resulting kernel.


       7.1   RG Evolution Kernels

 Task 5.1: Write RG-evolved expressions for HC , Ji , SC with Sudakov exponents

 Task 5.2: Retain cusp terms to two loops, non-cusp to one loop (NLL accuracy)

 Task 5.3: Define Sudakov kernel S(ν, µ) and AΓ (ν, µ)


                                                          7
       7.2   Canonical Scale Choices and Profile Functions

          Canonical Scales
                                                          √
                                     µh = Q,       µj =        ∆ Q,        µs = ∆ Q                (8)
          These minimize logarithms in matching conditions and capture relevant physics at each scale.


 Task 5.4: Verify canonical scales by examining log structure in each function

 Task 5.5: Design profile functions for smooth transition to fixed-order region

 Task 5.6: Implement scale variations for uncertainty estimation


       7.3   Shoulder Kernel and Core Integrals

 Task 5.7: Perform soft/collinear integrals with measurement function

 Task 5.8: Obtain master kernel of form:

                                         ∆1+ηeff KC (ηeff ),          ηeff ∝ αs Γ0 ln ∆                  (9)

 Task 5.9: Compare to thrust integral (Eq. 129) and HJM integrals (Eqs. 130–131)

Task 5.10: Identify sin(πη)/ sin(π(ηℓ + ηh )) structure if present

Task 5.11: Handle UV/IR divergences via analytic continuation


       7.4   Sudakov–Landau Pole Analysis

Task 5.12: Identify location of singularity ηℓ + ηh = 1 in terms of ∆

Task 5.13: Estimate numerical value: ∆pole = exp(−const/αs )

Task 5.14: Compare to QCD Landau pole (different origin: cusp anomalous dimension vs. β-function)

Task 5.15: Determine valid range of ∆ for NLL predictions


       7.5   Non-Global Logarithm Analysis

Task 5.16: Repeat shoulder-region analysis with auxiliary variables

Task 5.17: Show large logs arise only from regions continuously connected across shoulder

Task 5.18: Demonstrate configurations with unconstrained hard radiation don’t generate ln ∆

Task 5.19: Conclude whether non-global logs are absent at leading power

Task 5.20: Document any subleading-power non-global structures


                                                          8
      7.6   Final NLL Formula

Task 5.21: Combine all ingredients into complete resummed expression

Task 5.22: Write separate formulas for gluon and quark channels

Task 5.23: Define subtracted distribution:
                                             dσ sub
                                                                      
                                                      dσ          dσ
                                                    =    −∆                                       (10)
                                              d∆      d∆          d∆       ∆=1


Task 5.24: Verify µ-independence at O(αs )


      8     Stage VI: Matching, Power Corrections, and Phenomenology

      Objective: Produce a usable prediction by matching to fixed order, estimating uncertainties, and
      comparing to data if available.


      8.1   Matching to Fixed Order

 Task 6.1: Implement matching formula:
                                                             
                           dσ              dσ         dσ         dσ
                                       =          +         −                                     (11)
                           d∆ matched      d∆ res     d∆ FO      d∆ res expanded

 Task 6.2: Decide NLO vs. NNLO fixed-order input

 Task 6.3: Test matching in overlap region

 Task 6.4: Verify smooth transition away from shoulder


      8.2   Power Corrections

 Task 6.5: Analyze subleading-power terms in soft/collinear expansion

 Task 6.6: Show that for η ∼ O(1), power-suppressed terms become O(1)

 Task 6.7: Derive first subleading power contribution (analogous to Eq. 169 in reference)

 Task 6.8: Demonstrate explicit pole cancellation when power corrections included

 Task 6.9: Estimate window in ∆ where leading-power NLL is reliable

Task 6.10: Discuss ΛQCD /Q non-perturbative corrections


                                                      9
       8.3   Numerical Implementation

Task 6.11: Design modular code structure (Python or C++)

Task 6.12: Implement RG evolution kernels (reuse thrust/HJM code where possible)

Task 6.13: Implement hard, jet, and soft functions

Task 6.14: Implement shoulder convolution integrals

Task 6.15: Implement profile functions for scale transitions

Task 6.16: Include scale-variation machinery for uncertainties

Task 6.17: Validate against analytic limits


       8.4   Validation and Cross-Checks

Task 6.18: Expand NLL resummed result to O(αs2 ) and O(αs3 )

Task 6.19: Compare to EVENT2/EERAD3 in shoulder limit

Task 6.20: Verify RG-scale independence at expected order

Task 6.21: Check all color structures separately


       8.5   Comparison to Data (Optional)
                                                  √
Task 6.22: Generate predictions for LEP energies ( s = 91.2 GeV, etc.)

Task 6.23: If suitable data exist near C = 3/4, perform exploratory comparisons

Task 6.24: Study theoretical uncertainties: scale variation, higher orders, power corrections

Task 6.25: Explore implications for αs extraction


       9     Stage VII: Documentation and Extensions

       Objective: Document results and identify future directions.

 Task 7.1: Write up derivation of factorization theorem

 Task 7.2: Document all one-loop results and anomalous dimensions

 Task 7.3: Prepare figures comparing to fixed-order codes

 Task 7.4: Discuss phenomenological implications

 Task 7.5: Outline extensions: NNLL, joint resummation, other observables


                                                       10
  Stage                   Duration      Weeks     Key Deliverable
  I: Kinematics           2 weeks       1–2       C-parameter in 4-parton kinematics
  II: NLO Analysis        3 weeks       3–5       Extracted log coefficients, EVENT2 comparison
  III: Factorization      3 weeks       6–8       Complete factorization formula
  IV: One-Loop            2 weeks       9–10      1-loop functions, anomalous dimensions
  V: Resummation          3 weeks       11–13     NLL resummed formula, kernel analysis
  VI: Matching            3 weeks       14–16     Matched predictions, numerical code
  VII: Documentation      2 weeks       17–18     Final writeup

                     Table 1: Project timeline with milestones (18 weeks total)


10     Timeline and Deliverables

11     Key Challenges and Open Questions

  1. Step vs. Kink: The C-parameter has a step discontinuity at LO, unlike the kink for
     thrust/HJM. How does this affect the structure of shoulder logarithms and resummation?

  2. Measurement Function Complexity: The C-parameter measurement may lead to more
     complex convolution integrals. What is the analog of the sin(πη) structure?

  3. Additive Decomposition: Can we cleanly separate collinear and soft contributions to ∆
     as required for the factorization formula?

  4. Phenomenological Window: The Sudakov–Landau pole limits the valid range. Is there a
     useful window for precision predictions?

  5. Connection to Catani–Webber: How does the NLL formula connect to the original
     double-log resummation?

  6. Left vs. Right Shoulder: Does C-parameter have structure on both sides of C = 3/4?
     Which is phenomenologically relevant?

  7. Profile Functions: What is the optimal profile function design for transitioning between
     resummation and fixed-order regions?

  8. αs Extraction: Can shoulder resummation improve αs fits from C-parameter data?


12     Complete Task List

For reference, here is the complete ordered list of all tasks:


Stage I: Warm-Up and Kinematic Analysis (Tasks 1.1–1.14)

 1.1 Review the thrust/HJM shoulder paper (arXiv:2205.05702) in detail

 1.2 Review original C-parameter literature (Catani–Webber, hep-ph/9710333)


                                                  11
 1.3 Map notation and conventions between C-parameter literature and the reference paper
 1.4 Summarize similarities/differences: sensitivity to global soft radiation, recoil issues
 1.5 Identify which arguments carry over trivially vs. which are C-specific
 1.6 Parameterize 3-body phase space using sij with constraint s12 + s13 + s23 = 1
 1.7 Derive C in terms of invariants: verify C = 6 s12 s13 s23
 1.8 Confirm Csh = 3/4 at symmetric trijet
 1.9 Derive the LO distribution analytically and confirm step discontinuity behavior
1.10 Compute the explicit coefficient f (C) to set normalization
1.11 Characterize the first 4-parton configurations populating ∆ > 0
1.12 Introduce expansion parameter λ controlling deviations from symmetric trijet
1.13 Relate ∆ to soft/collinear kinematic variables at leading power
1.14 Determine whether left shoulder, right shoulder, or both require resummation


Stage II: NLO Fixed-Order Analysis (Tasks 2.1–2.17)

 2.1 Enumerate all 4-parton topologies
 2.2 Separate regions continuously connected across C = 3/4 from those that are not
 2.3 Identify which regions can produce large ln ∆
 2.4 Derive phase space constraints analogous to W(mj , ki , c) > 0
 2.5 Define power counting for soft, collinear, and soft-collinear modes
 2.6 Express C in terms of sij /Q2 and expand around symmetric trijet point
 2.7 Derive leading-power relation between ∆ and soft/collinear variables
 2.8 Document which integration regions contribute logarithms
 2.9 Compute |M|2 in collinear limit with polarization structure
2.10 Compute |M|2 in soft limit with correct color structure
2.11 Compute soft-collinear overlap for subtraction
2.12 Handle q q̄q ′ q̄ ′ and identical-quark channels
2.13 Verify consistency with splitting functions
2.14 Perform leading-power phase-space integrals
2.15 Extract αs2 ln2 ∆ and αs2 ln ∆ coefficients by color structure
2.16 Run EVENT2 with high statistics near C = 3/4
2.17 Compare analytic predictions to EVENT2 and create comparison plots

                                                    12
Stage III: Factorization Theorem (Tasks 3.1–3.16)

 3.1 Specify three collinear directions ni from LO configuration

 3.2 Define scaling of collinear momenta in shoulder regime

 3.3 Define scaling of soft momenta

 3.4 Clarify whether collinear-soft or Glauber modes are required

 3.5 Contrast with dijet limit to ensure shoulder-specific kinematics captured

 3.6 Write leading-power SCET current for three hard partons

 3.7 Identify associated Wilson coefficient (hard function)

 3.8 Discuss mapping to thrust/HJM hard function

 3.9 Express C in terms of SCET momenta at leading power

3.10 Derive the additive decomposition for ∆

3.11 Define measurement functions for collinear and soft sectors

3.12 Derive the factorization formula with explicit measurement function

3.13 Verify observable remains global at leading power

3.14 Define 6-sextant decomposition of soft radiation

3.15 Analyze recoil sensitivity: how emissions shift C-parameter value

3.16 Verify measurement constraint captures kinematics without ambiguity


Stage IV: One-Loop Ingredients (Tasks 4.1–4.14)

 4.1 Identify 3-jet hard function and relation to thrust/HJM

 4.2 Collect one-loop hard function expression and anomalous dimension

 4.3 Translate conventions as needed

 4.4 Verify hard function RG consistency

 4.5 Determine if standard jet functions suffice

 4.6 Import or compute one-loop jet functions

 4.7 Extract jet function anomalous dimensions

 4.8 Define soft function with 6 sextant measurement

 4.9 Specify projection vectors for each sextant region

4.10 Compute 4 independent soft integrals I1 , I2 , I3 , I4


                                                   13
4.11 Extract UV poles, finite parts, and transcendental constants

4.12 Combine with color structures for all channels
                                                 P
4.13 Verify anomalous dimension sum rule: γH + γJ + γS = 0

4.14 Check whether soft function differs from thrust/HJM at NLL


Stage V: NLL Resummation (Tasks 5.1–5.18)

 5.1 Write RG-evolved expressions with Sudakov exponents

 5.2 Define Sudakov kernel to NLL accuracy

 5.3 Verify canonical scales by examining log structure

 5.4 Design profile functions for transition to fixed-order region

 5.5 Implement scale variations for uncertainties

 5.6 Perform soft/collinear integrals with measurement function

 5.7 Obtain master kernel ∆1+ηeff KC (ηeff )

 5.8 Compare to thrust/HJM kernel structure

 5.9 Identify sin(πη) structure if present

5.10 Handle UV/IR divergences via analytic continuation

5.11 Identify Sudakov–Landau pole location

5.12 Estimate numerical value of ∆pole

5.13 Determine valid range of ∆ for NLL predictions

5.14 Analyze non-global logarithm structure

5.15 Conclude whether non-global logs are absent at leading power

5.16 Combine all ingredients into complete resummed expression

5.17 Write separate formulas for gluon and quark channels

5.18 Verify µ-independence at O(αs )


Stage VI: Matching and Phenomenology (Tasks 6.1–6.18)

 6.1 Implement matching formula

 6.2 Decide NLO vs. NNLO fixed-order input

 6.3 Test matching in overlap region

 6.4 Verify smooth transition away from shoulder

                                                14
 6.5 Analyze subleading-power terms

 6.6 Show power-suppressed terms become O(1) when η ∼ O(1)

 6.7 Derive first subleading power contribution

 6.8 Demonstrate explicit pole cancellation with power corrections

 6.9 Estimate window where leading-power NLL is reliable

6.10 Discuss non-perturbative corrections

6.11 Design modular numerical code

6.12 Implement RG evolution kernels

6.13 Implement hard, jet, and soft functions

6.14 Implement shoulder convolution integrals

6.15 Validate code against analytic limits

6.16 Expand NLL result and compare to EVENT2/EERAD3

6.17 Verify RG-scale independence

6.18 Generate predictions and compare to data if available


Stage VII: Documentation (Tasks 7.1–7.5)

 7.1 Write up derivation of factorization theorem

 7.2 Document all one-loop results and anomalous dimensions

 7.3 Prepare figures comparing to fixed-order codes

 7.4 Discuss phenomenological implications

 7.5 Outline extensions: NNLL, joint resummation, other observables


                                                15
