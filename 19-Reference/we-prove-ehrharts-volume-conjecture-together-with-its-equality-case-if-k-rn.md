---
title: "We prove Ehrhart’s volume conjecture together with its equality case: if K ⊂ Rn…"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/cfcc6aabc79542930d3a37fec61db8f5bdc35fe4.pdf"
category: "19-Reference"
fetched_at: "2026-08-09T06:48:24Z"
tags: ["news-research"]
---

We prove Ehrhart’s volume conjecture together with its equality case: if K ⊂ Rn is a
      convex body whose centroid lies in Zn and is the only point of Zn in the interior of K, then
      vol(K) ≤ (n + 1)n /n!, with equality if and only if K is unimodularly equivalent to the simplex
      −1 + (n + 1) · conv{0, e1 , . . . , en }. Part I (Sections 1–7) proves the inequality by a complex-
      analytic scheme built on the Monge–Ampère (moment-measure) potential of K, a rank-
      one property of the associated weighted Bergman space, Berndtsson’s plurisubharmonicity
      theorem, and an equilibrium mass bound for envelopes with prescribed Lelong number. Part
      II (Sections 8–12) proves the equality case: the saturation identities forced by equality yield
      a sharp energy bound for the contact threshold, which is upgraded—via a spectral gap
      with constant exactly one and a boundary-positive ∂-Neumann ¯           saturation argument—to a
      real-analytic eigenfunction with holomorphic gradient field, whose Laurent-mode structure
      and Monge–Ampère rigidity pin K to the simplex.

Theorem (Main). Let K ⊂ Rn be a convex body       R (a compact nconvex set with nonempty
                                               1
interior). Suppose that the centroid b(K) = vol(K) K x dx lies in Z and that b(K) is the only
point of Zn in the interior of K. Then

                                                          (n + 1)n
                                           vol(K) ≤                ,
                                                             n!
with equality if and only if K is unimodularly equivalent to the simplex

   S := −1 + (n + 1) · conv{0, e1 , . . . , en } = {x ∈ Rn : xj ≥ −1 (1 ≤ j ≤ n),
                                                                                              P
                                                                                                j xj ≤ 1}.

(“Unimodularly equivalent” means equal up to a map x 7→ Ax + t with A ∈ GLn (Z), t ∈ Zn .)
   Translating by −b(K) ∈ Zn we normalize b(K) = 0 throughout; the hypotheses become
                                 Z
                              1
               (i) b(K) :=          y dy = 0,         (ii) int K ∩ Zn = {0},
                            vol K K

and since unimodular maps preserve (i), (ii) and volume, and a unimodular affine map x 7→ Ax + t
carrying S to a body with centroid 0 forces t = A b(S) + t = b(AS + t) = 0, the equality statement
to be proved is: vol(K) = (n + 1)n /n! forces K = A(S) for some A ∈ GLn (Z).
    This paper is organized as follows. Part I (Sections 1–7) proves the inequality n! vol(K) ≤
(n + 1)n by a complex-analytic scheme, with complete proofs. Part II (Sections 8–12) proves the
equality case: Section 8 records the easy direction and the exact saturation identities (E1), (E2)
forced by equality; Section 9 converts them into a sharp energy bound for the contact threshold;
Section 10 upgrades this, via a spectral gap with constant exactly one (the only further use of the
                                              ¯
lattice hypothesis) and a boundary-positive ∂-Neumann      saturation argument, to a real-analytic
eigenfunction with holomorphic gradient field; Section 11 extracts the Laurent-mode structure of
the eigenfunction — finitely many modes at lattice points, exact functional equations for the
dual potential — and closes the equality case by Monge–Ampère rigidity: the dual potential is
an exact Guillemin-type log-affine potential whose facet data is balanced and integral, products
of lower-dimensional factors are excluded by the already-proved inequality, and the volume pins
K = A(S); Section 12 assembles the proof.

                                                      1
    Throughout, “psh” abbreviates plurisubharmonic, and classical results are used with attribu-
tion: the moment-measure existence theorem (Cordero-Erausquin–Klartag, building on Wang–Zhu
and Berman–Berndtsson), Caffarelli’s interior regularity theory for the real Monge–Ampère equa-
tion, Berndtsson’s theorem on plurisubharmonicity of Bergman kernels, the Bedford–Taylor
pluripotential calculus (comparison principle, decreasing convergence, plurifine locality), the
Perron–Bremermann–Walsh solution of the homogeneous complex Monge–Ampère Dirichlet prob-
lem on balls, and the Green function of a plane annulus; and, in Part II: Hörmander–Demailly
weighted L2 estimates for ∂¯ on weakly pseudoconvex Kähler manifolds, the classical ∂-Neumann
                                                                                    ¯
graph-density lemma (Chen–Shaw; Folland–Kohn; Hörmander), Kato’s representation theorem
for closed forms, the spectral theorem, Weyl’s lemma, elliptic and analytic-elliptic regularity
(Morrey, Hopf, Morrey–Nirenberg), and the Alexandrov estimate for Monge–Ampère measures of
convex functions (as in Figalli’s monograph).


Part I. The inequality

1    Notation and pluripotential preliminaries
Let T := (C∗ )n , and let
                  L : T → Rn ,        L(z) := (log |z1 |2 , . . . , log |zn |2 ),     x := L(z).
            Vn     dzj               2
With Ω :=      j=1 zj    set µΩ := in Ω ∧ Ω. In polar coordinates zj = exj /2+iθj ,
                                         Y dVj
                             µΩ = 2n                  = dx ⊗ dθ,          θ ∈ [0, 2π)n ,             (1.1)
                                             |zj |2
                                         j

where dV is Lebesgue measure on Cn ∼                                          ¯ n denotes
                                   = R2n . For u psh and locally bounded, (i∂ ∂u)
the Bedford–Taylor Monge–Ampère measure, and we normalize
                                                         1         ¯ n.
                                             mu :=             (i∂ ∂u)                               (1.2)
                                                      (2π)n n!
                  ¯ n = n! 2n det(u ) dV .
For u ∈ C 2 , (i∂ ∂u)              j k̄
Lemma 1.1 (Invariant dictionary). If ψ : Rn → R is smooth and convex and Ψ = ψ ◦ L, then
                  ¯ n = n! det D2 ψ(L(z)) dx dθ,
              (i∂ ∂Ψ)                                           hence         L∗ mΨ = det D2 ψ dx.
Proof. Locally Lj = log zj + log z̄j , so Ψj k̄ = ψjk (L)/(zj z̄k ), whence
                                                             Y
                               ¯ n = n! 2n det(ψjk (L))
                           (i∂ ∂Ψ)                                 |zj |−2 dV ;
                                                                      j

now use (1.1). Integrating out θ produces the factor (2π)n cancelled by (1.2).

Lemma 1.2 (Stokes mass equality). Let B ⊂ Cn be Ra ball and u, vR psh and locally bounded
                                                          ¯ n = (i∂ ∂v)
near B, with u = v on a neighbourhood N of ∂B. Then B (i∂ ∂u)         ¯ n.
                                                                 B

Proof. Choose a concentric ball B ′ ⊃ B with B ′ \ B ⊂ N and χ ∈ Cc∞ (B ′ ) with χ ≡ 1 on a
neighbourhood of B; then supp dχ ⊂ B ′ \ B ⊂ N (where dχ vanishes on an open set, χ is
                                   ¯ ⊆ supp dχ). By locality of the Monge–Ampère operator the
locally constant, so also supp(i∂R ∂χ)
two measures agree on N , so χ[(i∂ ∂u)   ¯ n − (i∂ ∂v)
                                                    ¯ n ] equals the difference of the masses over
B. Writing (i∂ ∂u) − (i∂ ∂v) = i∂ ∂(u − v) ∧ T with T = n−1
                ¯   n       ¯  n       ¯                                 ¯ k       ¯ n−1−k closed
                                                               P
                                                                 k=0 (i∂ ∂u) ∧ (i∂ ∂v)
positive,
     R two integrations by  R parts (legitimate for locally bounded psh functions, Bedford–Taylor)
           ¯ − v) ∧ T = (u − v) i∂ ∂χ
give χ i∂ ∂(u                            ¯ ∧ T = 0, since u − v ≡ 0 on supp dχ.


                                                          2
                                                         n            ε2
Lemma 1.3 (Model masses). (a) i∂ ∂¯ log(|z|2 + ε2 ) = n! 2n (|z|2 +ε     2 )n+1 dV , of total mass

(2π) on C , concentrating at 0 as ε ↓ 0. (b) For s > 0, vs := max(log |z|2 , −s) has (i∂ ∂v
    n     n                                                                                   ¯ s )n
supported on {|z| = e−s/2 } with total mass (2π)n . (c) For λ > 0, a ∈ Cn , s > 0, the truncated
model λ max(log |z − a|2 , −s) has Monge–Ampère mass λn (2π)n carried by {|z − a| = e−s/2 }; in
the normalization (1.2) its m-mass is λn /n!.
                                                                                            δ          z̄ z
Proof. (a) With u = log(|z|2 +ε2 ), det(uj k̄ ) = ε2 (|z|2 +ε2 )−(n+1) (the matrix is |z|2jk
                                                                                          +ε2
                                                                                              − (|z|2j+εk2 )2 ,
                        2
with eigenvalues (|z|2ε+ε2 )2 (once, on the eigenvector z̄) and |z|21+ε2 (n − 1 times)). Substituting
                                      2π n
                                            R∞
z = εw and using Vol(S 2n−1 ) = (n−1)!     , 0 r2n−1 (1 + r2 )−n−1 dr = 2n 1
                                                                             , the total mass is (2π)n ;
the same substitution shows the mass outside any fixed ball tends to 0. (b) vs is constant on
{|z| < e−s/2 } and maximal ((i∂ ∂¯ log |z|2 )n = 0) on {|z| > e−s/2 }, so by locality the measure
sits on the sphere. For the mass: vsε := max(log(|z|    2     2
                                                      R + ε ), −s)     agrees with log(|z|2 + ε2 ) near
                                                                ¯  ε
∂B(0, 1) for small ε, so by Lemma 1.2 and (a), B(0,1) (i∂ ∂vs ) → (2π)n ; by locality and (a)
                                                                      n

the part of this mass on {|z| > ρ1 } tends to 0 for every fixed ρ1 > e−s/2 , while on {|z| < ρ0 }
with ρ0 < e−s/2 the measure vanishes for small ε (vsε ≡ −s there once ρ20 + ε2 < e−s ). Fix
ρ0 < e−s/2 < ρ1 < 1 and χ ∈ Cc (B(0, 1)), 0 ≤ χ ≤ 1, χ ≡ 1 on Ra neighbourhood of the
closed annulus {ρ0 ≤ |z| ≤  R ρ1 }; theε sandwich   µε ({ρ0 ≤ |z| ≤ ρ1 }) ≤ χ dµε ≤ µε (B(0, 1)) for
          ¯  ε n                    ¯    n         n
µε := (i∂ ∂vs ) then gives χ (i∂ ∂vs ) → (2π) . Since vsε ↓ vs with all functions locally bounded,
Bedford–Taylor    decreasing convergence gives weak∗ convergence of the Monge–Ampère measures,
           ¯ s ) = (2π)n ; as this measure sits on the sphere, where χ ≡ 1, its total mass is (2π)n .
                n
   R
so χ (i∂ ∂v
                              ¯
(c) Translate and scale: (i∂ ∂(λu))              ¯ n.
                                      n = λn (i∂ ∂u)


Lelong numbers. For u psh near p, Mu (r) := sup|z−p|=r u is, as a function of t = log r2 , convex
and nondecreasing. Define
                       νp (u) := sup{c ≥ 0 : u ≤ c log |z − p|2 + O(1) near p}.
(So νp (log |z − p|2 ) = 1; this convention differs by a factor 2 from the one based on log |z − p|.)
Lemma 1.4 (Slope lemma). Let u be psh near B(p, r0 ) with u ≤ M0 there. If νp (u) ≥ λ then
                                            |z − p|2
                             u(z) ≤ λ log            + M0        (|z − p| ≤ r0 ).                         (1.3)
                                               r02
                                                                
Conversely (1.3) implies νp (u) ≥ λ. Moreover νp (1 − t)u0 + tu1 ≥ (1 − t)νp (u0 ) + tνp (u1 ) for
t ∈ [0, 1].

Proof. Let m(t) = Mu (et/2 ), convex nondecreasing in t, t0 = log r02 . For c < λ there is C with
m(t) ≤ ct + C for t near −∞; convexity then forces every slope of m to be ≥ c (a slope < c at
some t1 would give m(t) ≥ m(t1 ) + α(t − t1 ), α < c, for t ≤ t1 , contradicting m(t) ≤ ct + C as
t → −∞). Hence m(t) ≤ m(t0 ) + c(t − t0 ) ≤ M0 + c(t − t0 ) for t ≤ t0 ; let c ↑ λ. The converse
and the concavity statement are immediate from the definition.

    We freely use: the regularized supremum (supα uα )∗ of a family of psh functions locally
uniformly bounded above is psh (or ≡ −∞) and equals sup uα off a pluripolar (hence Lebesgue-
null) set; a decreasing limit of psh functions on a connected open set is psh or ≡ −∞; and u ≥ v
a.e. implies u ≥ v everywhere for psh u, v.


2    The Monge–Ampère potential

Theorem 2.1 (Wang–Zhu; Berman–Berndtsson; Cordero-Erausquin–Klartag). Let K
be a convex body with b(K) = 0. There is a convex ϕ : Rn → R, an Alexandrov solution of
             det D2 ϕ = e−ϕ on Rn ,                      (∇ϕ)∗ e−ϕ dx = 1K dy,
                                                                     
                                       ∇ϕ(Rn ) = K,

                                                      3
unique up to translation of the variable. Conversely solvability forces b(K) = 0.
     This is the moment-measure theorem of Cordero-Erausquin–Klartag applied to µ = 1K dy
(finite, barycenter 0, not supported on a hyperplane). Three standard deductions turn their
statement (an essentially continuous convex ϕ : Rn → (−∞, +∞] with moment measure 1K dy)
into the form quoted: (a) ϕ is finite on all of Rn : int dom ϕ ̸= ∅ (else the moment measure would
be null, not 1K dy); on int dom ϕ every subgradient lies in the compact K (by the argument in
(b) below, which uses only the pushforward identity and — via Rockafellar, Thms. 25.5/25.6,
valid for finite convex functions on open convex sets — applies verbatim on int dom ϕ), so ϕ is
globally RK -Lipschitz there, RK := maxy∈K |y|. If dom ϕ ̸= Rn , then dom ϕ is a convex set with
nonempty interior, not all of Rn , so ∂(dom ϕ) is locally the graph of a Lipschitz function and
has positive Hn−1 -measure. At every x ∈ ∂(dom ϕ): the Lipschitz bound gives a finite limit of
ϕ from inside, and lower semicontinuity forces ϕ(x) ≤ lim inf < ∞, so ϕ(x) is finite; yet every
neighbourhood of x meets {ϕ = +∞}, so ϕ is discontinuous at x. Thus the discontinuity set
of ϕ contains ∂(dom ϕ), of positive Hn−1 -measure — exactly what CEK’s essential continuity
(lower semicontinuity    plus Hn−1 -null discontinuity set) excludes. (b) The Alexandrov form
|∂ϕ(E)| = E e dx. Write µ := e−ϕ dx, let D be the full-measure set where ϕ is differentiable,
            R −ϕ

and T := ∇ϕ : D → Rn . First, every subgradient lies in K: T (x) ∈ K for a.e. x ∈ D by the
pushforward identity; the set {x ∈ D : T (x) ∈ K} is therefore dense, and since T is continuous
relative to D (Rockafellar, Convex Analysis, Thm. 25.5) and K is closed, T (x) ∈ K for every
x ∈ D; finally, for any x0 , ∂ϕ(x0 ) is the convex hull of limits of gradients T (xk ), xk ∈ D, xk → x0
(Rockafellar, Thm. 25.6, applied on the open set int dom ϕ — which is all of Rn once (a) is in
place, and which is how (a) itself invokes this argument), hence ∂ϕ(x0 ) ⊆ K. Consequently, with
M ϕ(E) := |∂ϕ(E)| the Monge–Ampère measure, M ϕ(Rn ) = |∂ϕ(Rn )| ≤ |K| = µ(Rn ). Second,
M ϕ ≥ µ setwise: for Borel E, E ∩ D ⊆ T −1 (T (E ∩ D)), so

         µ(E) = µ(E ∩ D) ≤ µ T −1 (T (E ∩ D)) = T (E ∩ D) ∩ K ≤ |∂ϕ(E)| = M ϕ(E)
                                                   

(here: ∂ϕ(E) is Lebesgue measurable and E 7→ |∂ϕ(E)| is a countably additive Borel measure —
the classical Alexandrov facts, see e.g. Figalli, The Monge–Ampère Equation and Its Applications,
Thm. 2.3; images of Borel sets under the Borel map T are analytic, hence universally measurable,
by Lusin–Sierpiński, and the pushforward identity extends to such sets by squeezing between Borel
hulls B1 ⊆ A ⊆ B2 with (T∗ µ)(B2 \B1 ) = 0). Two finite Borel measures with M ϕ ≥ µ setwise and
M ϕ(Rn ) ≤ µ(Rn ) coincide (pass to complements). Hence M ϕ = e−ϕ dx. Moreover ∇ϕ(Rn ) = K:
once Proposition 2.2 below gives smoothness and strict convexity (it uses only the Alexandrov
form just proved and the local pinching of e−ϕ ), U := ∇ϕ(Rn ) ⊆ K is open with |K \ U | = 0
(pushforward), and an open subset of K of full measure has closure containing int K, hence equal
to K. (c) In the necessity computation below no pointwise decay is needed: g := e−ϕ       ∈   L1 (Rn )
(its pushforward is 1K dy, of finite mass), and |∇g| = |∇ϕ| e          −ϕ  ≤ maxy∈K |y| e   −ϕ  ∈ L1
since all subgradients lie in K by (b); hence g ∈ W 1,1 (Rn ), and for cutoffs χR (x) = χ(x/R),
    g ∂i χR ≤ ∥∇χ∥
  R                  ∞
                       R                       R
                 R       {R≤|x|≤2R} g → 0, so Rn ∂i g = 0 for each i. Variationally one minimizes
           1       ∗ dy − log e−ϕ dx, which is invariant under ϕ 7→ ϕ + c (the two terms shift by
              R               R
J(ϕ) = volK    K ϕ
−c and +c) and — precisely because b(K) = 0 — under translations ϕ 7→ ϕ(· − x0 ) (which add
⟨x0 , b(K)⟩ to the first term);   writing ψ = ϕ∗ , J is convex along linear interpolation of ψ (by
                               R −ψ ∗
Prékopa–Leindler, ψ 7→ log e          dx is concave)R and coercive after a John normalization, and its
Euler–Lagrange equation — after normalizing e−ϕ =R vol K by the ϕ R7→ ϕ + c invariance        R — is
                                                                 −ϕ
the stated moment-measure equation. Necessity: 0 = ∇(e )dx = − ∇ϕ e dx = − K y dy. −ϕ

Proposition 2.2 (Regularity). The ϕ of Theorem 2.1 is smooth and strictly convex, with
D2 ϕ > 0.

Proof. ϕ is convex finite on Rn , hence locally Lipschitz, so f = e−ϕ is locally Lipschitz and
locally pinched between positive constants. If ϕ were not strictly convex, it would agree with a
supporting affine ℓ on a closed convex set W with more than one point; by Caffarelli’s localization

                                                  4
theorem (Caffarelli, A localization property of viscosity solutions to the Monge–Ampère equation
and their strict convexity, Ann. of Math. 131 (1990): if 0 < λ ≤ M ϕ ≤ Λ locally, the contact set
of a supporting affine function has no exposed points in the interior of the domain) W has no
exposed point in the (here: full) domain — the density e−ϕ is pinched between positive constants
on every section compactly contained in Rn , as that theorem requires; by Straszewicz’s theorem
(exposed points are dense in the extreme points of a closed convex set) W then has no extreme
point either, and a closed convex set with more than one point and no extreme point contains a
line x0 + Rv (Rockafellar, Thm. 18.5). For any x and any subgradient y ∈ ∂ϕ(x), comparing
the affine-in-t functions ℓ(x0 + tv) = ϕ(x0 + tv) ≥ ϕ(x) + ⟨y, x0 + tv − x⟩ forces ⟨y, v⟩ = ⟨∇ℓ, v⟩;
thus ∇ϕ(Rn ) lies in a hyperplane H — but then the pushforward (∇ϕ)∗ (e−ϕ dx) = 1K dy would
be carried by H, while |K| > 0: contradiction. Caffarelli’s interior theory (strictly convex
                                                                                   2,α
Alexandrov solutions with locally Hölder, locally pinched right-hand side are Cloc     ; see Figalli’s
                                                 2,α
monograph, Thms. 4.20 and 4.42) then gives Cloc      , and bootstrapping the now uniformly elliptic
equation with smooth dependence gives C ∞ ; det D2 ϕ > 0 with D2 ϕ ≥ 0 gives D2 ϕ > 0.

    From now on K satisfies (i)+(ii), ϕ is the potential above, and

                        V := vol(K),       τ := (n!V )1/n ,     Φ0 := ϕ ◦ L.

The inequality to prove is τ ≤ n + 1.
Lemma 2.3. (a) Rn e−ϕ dx = V . (b) ϕ(x) ≤ ϕ(0) + hK (x) for all x, hK the support function.
                    R

(c) Φ0 ∈ C ∞ (T ) is strictly psh and, with m := mΦ0 ,
                                                       Z
                            1    −Φ0
                   m=          e     µΩ ,   m(T ) = V,    e−Φ0 µΩ = (2π)n V.          (2.1)
                         (2π)n                          T
                                                                     R1
Proof. (a) Total masses in (∇ϕ)∗ (e−ϕ dx) = 1K dy. (b) ϕ(x) − ϕ(0) = 0 ⟨∇ϕ(tx), x⟩dt ≤ hK (x)
                                                       ¯ 0 )n = n!e−Φ0 µΩ ; integrate using (1.1)
since ∇ϕ ∈ K. (c) Lemma 1.1 and the equation give (i∂ ∂Φ
and (a).

    Write β := m/V , a probability measure; dβ = e−Φ0 µΩ /((2π)n V ).
Lemma 2.4 (Legendre package). Let ϕ∗ (y) := supx (⟨x, y⟩ − ϕ(x)) be the Legendre transform.
Then: (a) 0 = b(K) ∈ int K. (b) int K ⊆ dom ϕ∗ ⊆ K, so int dom ϕ∗ = int K, and ϕ∗ is convex,
locally bounded on int K. Moreover ϕ is proper: for every r with B̄(0, r) ⊂ int K there is Cr
with ϕ(x) ≥ r|x| − Cr . (c) ∇ϕ : Rn → int K is a C ∞ diffeomorphism; ϕ∗ ∈ C ∞ (int K) with
                                        −1
∇ϕ∗ = (∇ϕ)−1 and D2 ϕ∗ (y) = D2 ϕ(x)        at y = ∇ϕ(x); ∇ϕ∗ maps int K onto Rn and is
proper: if yk → y ∈ ∂K then |∇ϕ (yk )| → ∞. (d) ϕ(x) = supy∈int K ⟨x, y⟩ − ϕ∗ (y) for every
                 ∗                ∗

x.

Proof. (a) If 0 ∈
                / int K, a supporting hyperplane at 0 gives a unit u with ⟨u, y⟩ ≤ 0 on K; since
|K| > 0, K ̸⊆ {⟨u, ·⟩ = 0}, so ⟨u, y⟩ < 0 on a set of positive measure, whence ⟨u, b(K)⟩ < 0 —
contradicting b(K) = 0.
   (b) If y ∈
            / K, pick a unit u with ⟨u, y⟩ > h  K (u); by Lemma 2.3(b), ϕ(tu) ≤ ϕ(0)n + t hK (u),
     ∗
so ϕ (y) ≥ supt>0 t⟨u, y⟩ − ϕ(0) − t hK (u) = +∞. If y ∈ int K: since ∇ϕ(R ) is dense
in K (Theorem 2.1) we may choose y0 , . . . , yn ∈ ∇ϕ(Rn ), yi = ∇ϕ(xi ), whose convex hull
contains B(y, δ) for some δ > 0; the gradient inequalities ϕ(x) ≥ ϕ(xi ) + ⟨yi , x − xi ⟩ give
ϕ(x) ≥ maxi ⟨yi , x⟩ − C ≥ ⟨y, x⟩ + δ|x| − C (as y + δ |x|x
                                                            ∈ conv{yi }), whence ϕ∗ (y) ≤ C < ∞,
locally uniformly near y. The same estimate with y = 0 and δ = r is the properness claim.
   (c) ∇ϕ is injective (⟨∇ϕ(x1 ) − ∇ϕ(x2 ), x1 − x2 ⟩ > 0 by strict convexity) and a local diffeomor-
phism (D2 ϕ > 0, inverse function theorem), so U := ∇ϕ(Rn ) is open, U ⊆ K, hence U ⊆ int K.
Conversely for y ∈ int K = int dom ϕ∗ the subdifferential ∂ϕ∗ (y) is nonempty (Rockafellar, Thm.
23.4), and x ∈ ∂ϕ∗ (y) ⇐⇒ y ∈ ∂ϕ(x) = {∇ϕ(x)} (the inversion rule, Rockafellar, Thm. 23.5),


                                                  5
so y ∈ U : thus U = int K and ∇ϕ : Rn → int K is a smooth bijective local diffeomorphism,
i.e. a diffeomorphism. Its inverse is ∇ϕ∗ (by the inversion rule ∂ϕ∗ (y) = {(∇ϕ)−1 (y)}, a single
point, so ϕ∗ is differentiable on int K with that gradient, and smoothness follows from the inverse
function theorem), and differentiating ∇ϕ∗ ◦ ∇ϕ = id gives D2 ϕ∗ (y) = (D2 ϕ(x))−1 . Surjectivity
of ∇ϕ∗ is the bijectivity just proved. Properness: if yk → y ∗ ∈ ∂K while xk := ∇ϕ∗ (yk ) stays in
a compact set, a subsequence xk → x̄ gives ∇ϕ(x̄) = y ∗ ∈ ∂K — contradicting ∇ϕ(Rn ) = int K.
    (d) ϕ is convex and continuous, so ϕ = ϕ∗∗ = supy∈dom ϕ∗ (⟨x, y⟩ − ϕ∗ (y)). For y ∈ dom ϕ∗
and t ∈ (0, 1], yt := (1 − t)y ∈ int K (segment from the interior point 0, by (a)),        and convexity
gives ϕ∗ (yt ) ≤ (1 − t)ϕ∗ (y) + tϕ∗ (0), so ⟨x, yt ⟩ − ϕ∗ (yt ) ≥ (1 − t) ⟨x, y⟩ − ϕ∗ (y) − tϕ∗ (0); letting
t ↓ 0 shows the sup over int K is no smaller than over dom ϕ∗ .


3    The rank-one property
For ψ psh on T let Hψ := {f ∈ O(T ) : ∥f ∥2ψ :=                         2 −ψ µ    < ∞}, and for m ∈ Zn ,
                                                              R
                                                                  T |f | e    Ω
J(m) := Rn e⟨m,x⟩−ϕ(x) dx.
        R

Lemma 3.1. J(0) = V < ∞, and J(m) = ∞ for every m ∈ Zn \ int K.

Proof. By Lemma 2.3(b), e⟨m,x⟩−ϕ(x) ≥ e−ϕ(0) e−hK ′ (x) with K ′ = K − m. If m ∈         / intK then
0∈        ′
  / intK , so some unit u has hK ′ (u) ≤ 0; on Σ := {tu + w : t ≥ 0, |w| ≤ 1}, subadditivity gives
hK ′ (tu + w) ≤ t hK ′ (u) + hK ′ (w) ≤ c := max|w|≤1 hK ′ (w), so the integrand is ≥ e−ϕ(0)−c > 0 on
a set of infinite measure. (The statement holds for every real m ∈   / intK; the lattice plays no role
here.)

Lemma 3.2 (Rank one). If int K ∩ Zn = {0} then HΦ0 = C · 1.

Proof. Expand f = m∈Zn cm z m (the Laurent expansion of a holomorphic function on the
                      P
Reinhardt domain (C∗ )n , converging locally uniformly; see e.g. Range, Holomorphic Func-
tions and Integral Representations in Several Complex Variables, II.1).       R The weight is θ-
independent and |z m |2 = e⟨m,x⟩ , so for compact E ⊂ Rn , Parseval in θ gives L−1 (E) |f |2 e−Φ0 µΩ =
(2π)n m |cm |2 E e⟨m,x⟩−ϕ dx; let E ↑ Rn : ∥f ∥2Φ0 = (2π)n m |cm |2 J(m). Finiteness kills every
      P        R                                             P
cm with J(m) = ∞, i.e. all m ̸= 0 by Lemma 3.1 and (ii). And ∥1∥2Φ0 = (2π)n V < ∞.


4    Envelopes with prescribed Lelong number
Fix a base point p ∈ T . (The standard choice is p = (1, . . . , 1); all constructions below depend
on p, and in Part II we will vary p, every choice being admissible. By invariance of Φ0 under the
compact torus, constructions at p and at p′ with L(p) = L(p′ ) are carried to each other by the
rotation z 7→ (eiαj zj ).)
    For open Ω ⊆ T containing p (the letter Ω is used for open subsets of T in this section only;
no confusion with the holomorphic form Ω of Section 1 will arise) put
                                                                              ∗
     Fλ (Ω) := {Γ ∈ PSH(Ω) : Γ ≤ Φ0 , νp (Γ) ≥ λ},       PλΩ :=        sup Γ ,        Pλ := PλT ,
                                                                          Γ∈Fλ (Ω)

with sup ∅ := −∞. Fix once and for all r0 ∈ (0, 12 ] with B(p, r0 ) ⊂ T and M0 := supB(p,r0 ) Φ0 <
∞.
Lemma 4.1. (a) P0 = Φ0 ; PλΩ ≤ Φ0 ; λ 7→ PλΩ is nonincreasing. (b) (Uniform singularity
bound; for Ω ⊇ B(p, r0 ), which holds in every use below) Every Γ ∈ Fλ (Ω), and PλΩ itself,
                          2
satisfies Γ ≤ λ log |z−p|
                      r2
                            + M0 on B(p, r0 ); in particular νp (PλΩ ) ≥ λ and PλΩ ∈ Fλ (Ω) whenever
                       0
PλΩ ̸≡ −∞. (c) (Concavity) For fixed z, λ 7→ PλΩ (z) is concave on [0, ∞). (d) (Interval property)
If Pλ1 (z) = Φ0 (z) and 0 ≤ λ ≤ λ1 then Pλ (z) = Φ0 (z).

                                                     6
Proof. (a) Φ0 ∈ F0 ; the bound PλΩ ≤ Φ0 survives regularization because Φ0 is continuous. (b)
For each r < r0 , Γ is psh on a neighbourhood of B(p, r) ⊂ Ω with Γ ≤ Φ0 ≤ M0 there, so
                                  2
Lemma 1.4 gives Γ ≤ λ log |z−p|r2
                                    + M0 on B(p, r); let r ↑ r0 . The continuous majorant passes
to the regularized sup; the converse part of Lemma 1.4 gives νp ≥ λ. (c) If Γi ∈ Fλi , then
(1−t)Γ0 +tΓ1 ∈ F(1−t)λ0 +tλ1 by Lemma 1.4; take sups and use that regularization changes nothing
off a pluripolar, hence Lebesgue-null, set (Choquet’s lemma plus Bedford–Taylor: negligible sets
are pluripolar),
        R            R extend the a.e. inequality u ≥ v between psh functions to everywhere via
                  then
v(z) ≤ −B(z,r) v ≤ −B(z,r) u ↓ u(z) as r ↓ 0. (Degenerate ≡ −∞ cases are trivially consistent.)
(d) Interpolate λ = (1 − λλ1 ) · 0 + λλ1 λ1 in (c).

Definition 4.2. Cλ := {Pλ = Φ0 } (closed, since Pλ − Φ0 is u.s.c.), and
                λ∗ (z) := sup{λ ∈ [0, τ ) : z ∈ Cλ } ∈ [0, τ ]          (sup ∅ := 0; C0 = T ).

Lemma 4.3. λ∗ is Borel, {λ∗ > λ} ⊆ Cλ ⊆ {λ∗ ≥ λ} for λ ∈ (0, τ ), and for every finite Borel
measure µ,                     Z         Z                 τ
                                             λ∗ dµ =           µ(Cλ ) dλ.
                                         T             0

Proof. By Lemma 4.1(d) the sup defining λ∗ may be taken over rational λ, so {λ∗ > c} =
                                              ∗                   τ ); hence λ∗ is Borel, and
S
  λ∈Q∩(c,τ ) Cλ for every c ∈ [0, τ )R (and {λ R > c} = ∅ for c ≥ R
                                                 τ                  τ
the inclusions hold. Layer-cake: λ∗ dµ = 0 µ({λ∗ > λ})dλ = 0 µ({λ∗ ≥ λ})dλ (the two
integrandsR differ only at the at most countably many atoms of the law of λ∗ ), and both ends
             τ
sandwich 0 µ(Cλ )dλ; each integrand, being monotone in λ, is measurable.


5    The ray and the convexity engine

Construction 5.1. On X := H × T , H := {ζ : Re ζ > 0}, define
                                              Ψ := U ∗ (joint u.s.c. regularization).
                                           
     U (ζ, z) := sup Pλ (z) + Re ζ (λ − τ ) ,
                   λ∈[0,τ ]

U , hence Ψ, depends only on s := Re ζ; write Ψs (z).
Lemma 5.2. (a) Ψ is psh on X ; each Ψs is psh on T . (b) Φ0 − sτ ≤ Ψs ≤ Φ0 ; s 7→ Ψs (z) is
convex and nonincreasing; and the Danskin bound holds:
                          Ψs (z) ≥ Φ0 (z) + s(λ∗ (z) − τ )            (z ∈ T, s > 0).            (5.1)
(c) (Well bound) For s > 0: Ψs ≤ M0 − sτ on Bs := {|z − p| < r0 e−s/2 }.
Proof. (a) Each (ζ, z) 7→ Pλ (z) + Reζ(λ − τ ) with Pλ ̸≡ −∞ is psh on X (the λ’s with Pλ ≡ −∞
may be discarded from the family without changing the sup — the λ = 0 term is present),
and the family is locally bounded above by Φ0 ; so Ψ = U ∗ is psh unless ≡ −∞, excluded by
U ≥ Φ0 − sτ . Since U is invariant under ζ 7→ ζ + it and this symmetry commutes with the
local lim sup regularization, Ψ depends only on s = Re ζ, as claimed in Construction 5.1. (b)
Φ0 − sτ ≤ U ≤ Φ0 pointwise; continuity of Φ0 preserves the upper bound under regularization.
Convexity: for fixed z, s 7→ U (s, z) is a sup of affine functions with slopes λ − τ ≤ 0, hence
convex nonincreasing; regularize jointly (for s0 = (1 − t)s1 + ts2 and (s, z) → (s0 , z0 ), write
s′i = si + (s − s0 ), use U (s, z) ≤ (1 − t)U (s′1 , z) + tU (s′2 , z), and take lim sup). Monotonicity
of s 7→ Ψs (z) then follows for free: a finite convex function on (0, ∞) that is bounded above
(here by Φ0 (z)) is nonincreasing. (5.1): for λ < λ∗ (z), z ∈ Cλ (Lemma 4.1(d)), so Ψs (z) ≥
U (s, z) ≥ Φ0 (z) + s(λ − τ ); let λ ↑ λ∗ (z). (c) For z ∈ Bs and any λ ∈ [0, τ ], Lemma 4.1(b) gives
                                 2
Pλ (z) + s(λ − τ ) ≤ λ(log |z−p|
                             r02
                                   + s) + M0 − sτ ≤ M0 − sτ , the bracket being ≤ 0 on Bs . The set
{(s, z) : z ∈ Bs } is open in (0, ∞) × T , so the bound survives joint regularization.

                                                       7
     Define                           Z
                                            e−Ψs µΩ (s > 0),          g(0) := − log (2π)n V .
                                                                                           
                      g(s) := − log
                             T
By Lemma 5.2(b) and (2.1), e 0 ≤ e−Ψs ≤ esτ e−Φ0 , so g is finite and
                            −Φ


                                                 |g(s) − g(0)| ≤ sτ.                                    (5.2)

Theorem 5.3 (Berndtsson). Let D ⊆ Cζ × Cnz be pseudoconvex and φ psh on D. For ζ
in the base let Kζ (z, w) be the Bergman kernel of the holomorphic functions on the fiber Dζ
square-integrable against e−φ(ζ,·) dV . Then log Kζ (z, z) is psh (or ≡ −∞) on D.
    We use Theorem 5.3 for weights that are merely upper semicontinuous psh (our φ below).
This is covered by the theorem as published: Berndtsson (Ann. Inst. Fourier 56 (2006), Theorem
1.1) assumes only that the weight is plurisubharmonic on the pseudoconvex domain D — no
smoothness or boundedness — and that the domain is pseudoconvex; we cite it in exactly that
generality.
Theorem 5.4 (Rank-one convexity). If HΦ0 = C · 1, then g is convex on [0, ∞).

Proof.R Step 1. For s > 0: Ψs ≤ Φ0 gives ∥f ∥Φ0 ≤ ∥f ∥Ψs , so HΨs ⊆ HΦ0 = C · 1; and 1 ∈ HΨs
since e−Ψs µΩ ≤ esτ (2π)n V . So HΨs = C · 1.
    Step 2. For R > 0 let AR := {e−R < |t| < eR }, DR := AnR P          ⋐ T , and on the pseudoconvex
D (R) := {Reζ > 0}×DR take the psh weight φ(ζ, z) := Ψ(ζ, z)+ i log |zi |2 . By (1.1), e−Ψs µΩ =
                                                                                              (R)
2n e−φ dV , so DR |f |2 e−φ(ζ,·) dV = 2−n DR |f |2 e−Ψs µΩ . Theorem 5.3 makes log Kζ (z, z) psh
               R                          R

on D(R) ; it depends only on Reζ.
    Step 3. Write ∥f ∥2DR ,ζ := DR |f |2 e−φ(ζ,·) dV , and ∥f ∥2T,ζ for the integral over T , = 2−n ∥f ∥2Ψs .
                                  R
                                                                                                (R)
Since Kζ (z0 , z0 ) = sup{|f (z0 )|2 : ∥f ∥ ≤ 1} and norms increase with the domain, Kζ (z0 , z0 ) ≥
  (R′ )
Kζ        (z0 , z0 ) ≥ KζT (z0 , z0 ) for R < R′ , where K T is the kernel of HΨs in the norm ∥ · ∥T,ζ . Note
  (R)
Kζ (z0 , z0 ) > 0 (constants are candidates of finite norm), so we may take extremals fR with
                                      (R)
∥fR ∥DR ,ζ = 1, |fR (z0 )|2 = Kζ (z0 , z0 ) (attained: the weight is bounded above on compacts
of DR , so a maximizing sequence in the unit ball is locally uniformly bounded; Montel and
Fatou
   R produce     a maximizer in the unit ball). On any fixed DR1 the weight is bounded above,
             2
so DR |fR | dV is bounded uniformly in R > R1 ; the sub-mean-value property bounds |fR |
       1
locally uniformly on DR1 ; a diagonal extraction over the exhaustion {DR1 }R1 ∈N and Montel give
a subsequence → F ∈ O(T ) locally uniformly, and Fatou on each DR1 followed by monotone
                                                                          (R)
convergence gives ∥F ∥T,ζ ≤ 1, so F ∈ HΨs = C · 1 and |F (z0 )|2 = limR Kζ (z0 , z0 ) ≤ KζT (z0 , z0 )
(the full limit exists and equals the subsequential one by monotonicity in R). Hence
                              (R)                                     1
                            Kζ (z, z) ↓ KζT (z, z) =            R               = 2n eg(s) ,
                                                          2−n       T e −Ψs µ
                                                                              Ω

the kernel of the line C · 1. A decreasing limit of psh functions being psh, (ζ, z) 7→ n log 2 + g(Reζ)
is psh; a subharmonic function of ζ depending only on Reζ is convex in it. So g is convex on
(0, ∞), and (5.2) extends convexity to [0, ∞) by continuity at 0.

Lemma 5.5 (Well estimate). There is C with g(s) ≤ −(τ − n)s + C for all s ≥ 0.

Proof. By Lemma 5.2(c), T e−Ψs µΩ ≥ esτ −M0 µΩ (Bs ). On B(p, r0 ) the quantities |zj | are
                                R

bounded above by Rp := maxj supB(p,r0 ) |zj | < ∞, so (1.1) gives µΩ ≥ c0 (p) dV with c0 (p) =
2n Rp−2n , whence µΩ (Bs ) ≥ c0 (p)c2n r02n e−ns (c2n = unit-ball volume; for the standard p =
(1, . . . , 1) and r0 ≤ 12 one may take c0 = 2n (3/2)−2n ). Take logs; C depends on p but the slope
−(τ − n) does not. (The proof gives s > 0; the case s = 0 follows by letting s ↓ 0 using the
continuity (5.2).)

                                                         8
                                                    ∗
                                                 R
Proposition 5.6. If HΦ0 = C · 1 then             T λ dβ ≤ n.

Proof. By convexity the difference quotient q(s) = g(s)−g(0)
                                                       s     is nondecreasing; Lemma 5.5 gives
lim sups→∞ q(s) ≤ −(τ − n), hence

                                       q(s) ≤ −(τ − n)  (s > 0).                               (5.3)
                               ∗                                   ∗)
From (5.1), e−Ψs ≤ e−Φ0 es(τ −λ ) , so g(s) − g(0)  − log T es(τ −λ   dβ. With X := τ − λ∗ ∈ [0, τ ]
                                                         R
                                                R ≥
(bounded Borel, by Lemma 4.3) and s ↓ 0: esX dβ = 1 + s Xdβ + O(s2 ) (uniformly, since
                                                                 R
                  2 2
esX ≤ 1 + sX + s 2τ esτ ) while, by (5.3),    e dβ ≥ es(τ −n)
                                            R sX
                                       R                   R ≥∗
                                                                 1 + s(τ − n) (valid for either sign
of τ − n); divide by s and let s ↓ 0: Xdβ ≥ τ − n, i.e. λ dβ ≤ n.


6    The equilibrium mass bound

Theorem 6.1. For every λ > 0,
                                         λn                                                 λn
                  m {Pλ < Φ0 }        ≤      ,       equivalently             m(Cλ ) ≥ V −      .
                                          n!                                                 n!
    Only smoothness and strict psh-ness of Φ0 are used. (If Pλ ≡ −∞ the convention is
{Pλ < Φ0 } = T ; the proof below covers this case.) We use the Bedford–Taylor comparison
principle   in the form:  if u, v are locally bounded psh on bounded open Ω and {u < v} ⋐ Ω, then
            ¯ n≤                ¯ n
R                   R
  {u<v} (i∂ ∂v)       {u<v} (i∂ ∂u) . This follows from the usual boundary form (Bedford–Taylor;
Guedj–Zeriahi, Degenerate Complex Monge–Ampère Equations, Cor. 3.30): choose open Ω′ with
{u < v} ⊂ Ω′ ⋐ Ω; then u ≥ v on a neighbourhood of ∂Ω′ , i.e. lim inf z→∂Ω′ (u − v) ≥ 0, and
the boundary form applies on Ω′ . We also use Bedford–Taylor decreasing convergence, plurifine
locality in the precise form 1{u>v} (i∂ ∂¯ max(u, v))n = 1{u>v} (i∂ ∂u)
                                                                    ¯ n for locally bounded psh u, v
— valid for the possibly non-open set {u > v} (Bedford–Taylor 1987; Guedj–Zeriahi, Prop. 3.27)
— the Perron–Bremermann solution on balls (existence, continuity and maximality: Bremermann,
Walsh, Bedford–Taylor), the gluing lemma, and the Green function gA (·, a) of a plane annulus.
We record once the normalization (i∂ ∂¯ log |z − p|2 )n = (2π)n δp , consistent with Lemma 1.3(c)
and with the Lelong convention of Lemma 1.4.

6.1 Bounded envelopes and Green bounds
Fix λ > 0 and R so large that B(p, r0 ) ⋐ DR = AnR . Put

               u := PλDR ,       σR (z) := 2 max gAR (zj , pj ) ∈ PSH(DR ),                σR ≤ 0,
                                                 1≤j≤n

where p = (p1 , . . . , pn ); for the standard p = (1, . . . , 1), σR (z) = 2 maxj gAR (zj , 1).
Lemma 6.2. Let CR := maxj maxt∈∂AR log |t − pj |, MR := supDR Φ0 , C ′ := λ(log n + 2CR ) −
                                                             2
inf DR Φ0 . (a) νp (σR ) = 1 and σR (z) ≥ log |z−p|
                                                n   − 2CR on DR . (b) For every ε > 0 there is
compact D′ ⊂ DR with σR > −ε on DR \ D′ . (c) Φ0 + λσR ∈ Fλ (DR ); consequently

                     Φ0 + λσR ≤ u ≤ Φ0 on DR ,                    u(z) ≥ λ log |z − p|2 − C ′ ,      (6.1)

so u ∈ Fλ (DR ), u is locally bounded on DR \ {p}, and for j > 0,

                                                                             MR + C ′ − j
                 {u ≤ Φ0 − j} ⊆ B(p, rj ) ∩ DR ,                 log rj2 =                (rj ↓ 0)
                                                                                 λ
(only large j, for which B(p, rj ) ⊂ DR , will be used).


                                                         9
Proof. (a) hj := gAR (·, pj ) − log | · −pj | has a removable singularity at pj , hence extends harmon-
ically across pj ; since the two boundary circles of AR are regular, gAR (·, pj ) extends continuously
to AR with boundary value 0, so hj is continuous on AR with hj = − log |t − pj | ≥ −CR on
∂AR ; thus hj ≥ −CR by the minimum principle. Near p, σR = log(maxj |zj − pj |2 ) + O(1)
and n1 |z − p|2 ≤ maxj |zj − pj |2 ≤ |z − p|2 , so νp (σR ) = 1 and the global lower bound fol-
lows. (b) gAR (·, pj ) is continuous up to ∂AR where           it vanishes; pick compact A′j ⊂ AR
with gAR (·, pj ) > −ε/2 outside A′j , and let D′ =          A′j : if z ∈
                                                                        / D′ then some zj ∈   / A′j and
                                                          Q
σR (z) ≥ 2gAR (zj , pj ) > −ε. (c) Φ0 + λσR is psh, ≤ Φ0 , with νp ≥ λ by (a) (Φ0 smooth); so it
competes, giving the lower bounds; Lemma 4.1(b) gives νp (u) ≥ λ. If u(z) ≤ Φ0 (z) − j then
λ log |z − p|2 − C ′ ≤ MR − j.

6.2 Maximality off the contact set
               ¯ n = 0 on W := {u < Φ0 } \ {p}.
Lemma 6.3. (i∂ ∂u)

Proof. Fix z0 ∈ W , ρ′ > 0 with B(z0 , ρ′ ) ⊂ W , and set δ := minB(z0 ,ρ′ ) (Φ0 − u) > 0 (positive:
Φ0 − u is l.s.c. and > 0 on the compact), A := supB(z0 ,ρ′ ) ∆Φ0 (note A > 0 since Φ0 is strictly
psh), r := min(ρ′ , 2nδ/A), B := B(z0 , r).
                   p

    Claim: every w ∈ PSH(B) with lim supz→ζ w(z) ≤ u(ζ) for all ζ ∈ ∂B satisfies w ≤ u
on B. First, w ≤ HB [Φ0 ] − δ where HB [Φ0 ] is the harmonic extension of Φ0 |∂B (as w is
                                                                                   A
subharmonic with boundary values ≤ u ≤ Φ0 − δ). The function HB [Φ0 ] − Φ0 − 4n       (r2 − |z − z0 |2 )
is subharmonic on B (Laplacian = −∆Φ0 + A ≥ 0 in R2n ) with zero boundary values, hence
                             2
≤ 0; so HB [Φ0 ] ≤ Φ0 + Ar             δ                    δ
                           4n ≤ Φ0 + 2 and w ≤ Φ0 − 2 on B. Glue: w           b := max(w, u) on B,
:= u elsewhere on DR ; psh by the boundary condition; w       b ≤ Φ0 ; w
                                                                       b = u near p (as p ∈ / B), so
    b ≥ λ; hence w
νp (w)                              b ≤ PλDR = u, i.e. w ≤ u on B.
                   b ∈ Fλ (DR ), so w
    Now choose continuous hk ↓ u|∂B (u.s.c. on a compact), and Perron–Bremermann solutions
uk ∈ PSH(B) ∩ C(B), uk |∂B = hk , (i∂ ∂u ¯ k )n = 0. Then u ≤ uk (u competes for data hk ), uk
decreases to some ũ ≥ u with lim supz→ζ ũ ≤ hk (ζ) ∀k, so ≤ u(ζ); the Claim gives ũ ≤ u, so uk ↓ u
on B, all bounded on B; Bedford–Taylor decreasing convergence gives (i∂ ∂u) ¯ n = lim(i∂ ∂u¯ k )n = 0
on B. Cover W by such balls; since W is open, hence σ-compact, countably many suffice, and
the measure vanishes on W .

6.3 The comparison scheme
Proof of Theorem 6.1. Fix λ, ε, δ > 0 and R as above; keep the notation of Lemma 6.2 and set

    O := {z ∈ DR : u(z) < Φ0 (z) − ε} (open),          uj := max(u, Φ0 − j) ∈ PSH ∩ L∞
                                                                                     loc (DR ).

    Step 0 (compact containment). By (6.1) and Lemma 6.2(b) with ε/λ, there is compact D′
with u ≥ Φ0 − ε off D′ ; so O ⊆ D′ ⋐ DR , and {uj < Φ0 − ε} = O for j > ε.
    Step 1 (global comparison). The comparison principle on DR for the pair (uj , Φ0 − ε) (both
locally bounded, {uj < Φ0 − ε} = O ⋐ DR ) gives
                                  Z             Z
                                        ¯    n
                                    (i∂ ∂Φ0 ) ≤ (i∂ ∂u¯ j )n .                             (6.2)
                                        O              O

   Step 2 (localization at p). Split O by {u > Φ0 − j} and its complement. On DR \ {p}, u and
                                                                        ¯ j )n = 1{u>Φ −j} (i∂ ∂u)
Φ0 − j are locally bounded, and plurifine locality gives 1{u>Φ0 −j} (i∂ ∂u                     ¯ n
                                                                                      0
there; on O \ {p} ⊆ W this vanishes by Lemma 6.3. Also p ∈      / {u > Φ0 − j} (u(p) = −∞). By
Lemma 6.2(c), O ∩ {u ≤ Φ0 − j} ⊆ B(p, rj ). Hence
                                 Z                Z
                                         ¯ j )n ≤
                                     (i∂ ∂u                ¯ j )n .
                                                       (i∂ ∂u                                  (6.3)
                                    O               B(p,rj )


                                                  10
   Step 3 (model cap). Fix ρ1 ∈ (0, r0 ) with B(p, ρ1 ) ⊂ DR ; let M1 , m1 be the sup and inf of Φ0
on B(p, ρ1 ), λ̃ := (1 + δ)λ,
                                    |z − p|2
                   w(z) := λ̃ log            + M1 + 1,     w(m) := max(w, −m).
                                       ρ21
Choose κ0 > 0 with 2κ0 λ̃ < 12 . On the collar {ρ1 e−κ0 < |z − p| < ρ1 }, w(m) ≥ w > M1 + 12 >
Φ0 ≥ uj , so {w(m) < uj } ∩ B(p, ρ1 ) ⊆ B(p, ρ1 e−κ0 ) ⋐ B(p, ρ1 ). For m > j − m1 we have
uj ≥ m1 − j > −m on B(p, ρ1 ), so {w(m) < uj } = {w < uj } there. Comparison on B(p, ρ1 ) for
(w(m) , uj ) plus Lemma 1.3(c) (for large m the mass-carrying sphere of w(m) lies in B(p, ρ1 ), total
mass λ̃n (2π)n ) give
                  Z                         Z
                                    ¯    n
                                (i∂ ∂uj ) ≤            ¯ (m) )n = (1 + δ)n λn (2π)n .
                                                   (i∂ ∂w                                       (6.4)
                 {w<uj }∩B(p,ρ1 )               B(p,ρ1 )

Finally B(p, rj ) ⊆ {w < uj } ∩ B(p, ρ1 ) for large j: on B(p, rj ) ⊂ B(p, ρ1 ), uj ≥ m1 − j while
          r2
w ≤ λ̃ log ρj2 + M1 + 1 = (1 + δ)(MR + C ′ − j) + c1 , so w − uj ≤ −δj + O(1) < 0 for j ≥ j0 (δ).
             1
    Fix ε, δ > 0 and (admissible, large) R; take j ≥ max(j0 (δ), ε, j1 ) where j1 ensures rj < ρ1 ;
then take m > max(j − m1 , m∗ (j)), with m∗ (j) large enough that the mass-carrying sphere
of w(m) lies in B(p, ρ1 ). Combining (6.2)–(6.4) for such j, m (the final bound is j, m-free) and
dividing by (2π)n n!:
                                (1 + δ)n λn
          m {PλDR < Φ0 − ε} ≤                     (for all admissible R and all ε, δ > 0).      (6.5)
                                      n!
    Step 4 (limits). For R < R′ (taking R ∈ N, say) restriction maps Fλ (DR′ ) into Fλ (DR ) and
                                       D ′
global competitors restrict, so Pλ ≤ Pλ R ≤ PλDR on DR : the pointwise limit Q := limR PλDR ≥
Pλ exists on T . If Q ̸≡ −∞, Q is psh (locally a decreasing limit), ≤ Φ0 , and satisfies the uniform
bound of Lemma 4.1(b) (its constants don’t depend on R), so νp (Q) ≥ λ, Q ∈ Fλ (T ), Q ≤ Pλ ;
in all cases Q = Pλ . Hence {PλDR < Φ0 − ε} ↑ {Pλ < Φ0 − ε}, and letting R ↑ ∞ in (6.5), then
ε ↓ 0, then δ ↓ 0, gives the theorem.

Remark 6.4. Taking λ < τ shows m(Cλ ) ≥ V − λn /n! > 0, so Cλ ̸= ∅ and Pλ ̸≡ −∞ for λ < τ .


7    Proof of the inequality
We now combine the pieces. The standing hypotheses (i)+(ii) are in force: by Lemma 3.2
(hypothesis (ii)), HΦ0 = C · 1, so Theorem 5.4 and Proposition 5.6 apply; and by Lemma 2.3
(hypothesis (i), through Theorem 2.1) we have the identities m(T ) = V , τ n = n!V , and m = V β
— the last being precisely the Kähler–Einstein/moment-measure equation (i∂ ∂Φ ¯ 0 )n = n! e−Φ0 µΩ
of (2.1), which identifies the Monge–Ampère normalization of m with the weighted-measure
normalization of β. By Lemma 4.3 with µ = m (λ 7→ m(Cλ ) is monotone by Lemma 4.1(d),
hence measurable) and Theorem 6.1,
                      Z τ              Z τ
                                                 λn               τ n+1
           Z
                ∗                                                              n
              λ dm =      m(Cλ )dλ ≥         V −      dλ = V τ −           =        τ V,    (7.1)
            T           0               0        n!              (n + 1)!     n+1
                     τ n+1   τV
using τ n = n!V (so (n+1)! = n+1 ). By Proposition 5.6 and m = V β,
                                       Z
                                          λ∗ dm ≤ nV.                                           (7.2)
                                            T
       n
Hence n+1 τ V ≤ nV and V > 0, i.e. τ ≤ n + 1:
                                     n! vol(K) ≤ (n + 1)n .     ■


                                                    11
Part II. The equality case
Notation for Part II. We refer to the results of Part I by the following labels. (P1) = the
Kähler–Einstein potential package (Theorem 2.1, Proposition 2.2, Lemma 2.3); (P2) = rank-
one-ness (Lemma 3.2); (P3) = the envelope bound of Lemma 4.1(b); (P4) = the mass bound
(Theorem 6.1); (P5) = the ray package of Section 5; (P6) = the inequality (Section 7); (E1),
(E2) = the saturation identities of Proposition 8.2; (F1)–(F9) = the facts recalled at the start of
Section 9 ((F1) sandwich/convexity of the ray, (F2) Danskin, (F3) wells, (F4) = (E1)–(E2), (F5)
properties of λ∗ , (F6) the first-derivative identity of Lemma 9.1(e), (F7) rank-one with Parseval,
(F8) the support-function/Legendre facts of Part I (Lemma 2.3(b) and Lemma 2.4), (F9) the
                                n
extremal-model data); c := n+2     , N := n + 1, m, β as in Sections 2 and 9.


8         Equality: the easy direction and the saturation identities
                                                                                  P
Lemma 8.1 (The simplex attains equality). S = {x : xj ≥ −1,                         j xj   ≤ 1} satisfies
b(S) = 0, int S ∩ Zn = {0}, and vol(S) = (n + 1)n /n!.

Proof. S = −1 + (n + 1)∆ with ∆ = conv{0, e1 , . . . , en }: vol(S) = (n + 1)n vol(∆) = (n + 1)n /n!;
the centroid of (n + 1)∆ is the vertex-average 0+(n+1)e1n+1  +···+(n+1)en
                                                             P            = 1, so b(S) = 0. Interior
                            int((n + 1)∆) = {y : yj > 0,
lattice points of (n + 1)∆: P                                    j yj < n + 1}, and an integer point
there has every mj ≥ 1 and j mj ≤ n, forcing m = 1; translating by −1, int S ∩ Zn = {0}.

      Assume now, for the rest of Part II, that K satisfies (i), (ii) and

                                        (n + 1)n
                             vol(K) =            ,        i.e.   τ = n + 1.
                                           n!
                                                                                            (p)   (p)
All constructions of Part I are available for every base point p ∈ T ; we write Pλ , Cλ , λ∗p ,
    (p)
Ψs , gp when the dependence matters.
                                                                         (p) λn
Proposition 8.2 (Saturation). For every p ∈ T : (E1) m Cλ                        = V −
                                                                                  for all but
                                                                              n!
                                                       (p)
countably many λ ∈ (0, n + 1); equivalently m({Pλ < Φ0 }) = λn /n! for the same co-countable
                                                                λn−1
set of λ. Consequently λ∗p has under m the exact distribution (n−1)!  dλ on [0, n + 1]. (E2)
gp (s) = gp (0) − (τ − n)s = gp (0) − s for all s ≥ 0.
                                                                 n
Proof. With τ = n + 1 the outer bounds in (7.1)–(7.2) coincide: n+1 τ V = nV . Hence both are
equalities:                    Z τ
                                                  λn 
                                    m(Cλ ) − V +       dλ = 0,
                                0                 n!
with nonnegative integrand (Theorem 6.1), so m(Cλ ) = V − λn /n! for a.e. λ; since λ 7→ m(Cλ )
is nonincreasing (Lemma 4.1(d)) and the right side is continuous, equality holds at every
continuity point of the left side, i.e. off a countable set. For the distributional consequence,
write G(λ) := m({λ∗ > λ}), G− (λ) := m({λ∗ ≥ λ}), F (λ) := V − λn /n!; by Lemma 4.3, G(λ) ≤
m(Cλ ) ≤ G− (λ) on (0, τ ). Fix λ0 ∈ (0, τ ). Letting λ ↓ λ0 through values with m(Cλ ) = F (λ)
(a co-countable, hence dense, set): from {λ∗ ≥ λ} ⊆ {λ∗ > λ0 }, F (λ) ≤ G− (λ) ≤ G(λ0 ), so
F (λ0 ) ≤ G(λ0 ) by continuity of F . Letting λ ↑ λ0 through such values: {λ∗ ≥ λ0 } ⊆ {λ∗ > λ}
gives G− (λ0 ) ≤ G(λ) ≤ m(Cλ ) = F (λ), so G− (λ0 ) ≤ F (λ0 ). With G ≤ G− , all three coincide:
G = G− = F on (0, τ ). Thus the survival function of λ∗ under m is exactly V − λn /n!, there are
no atoms (none at the endpoints either, by the limits G → V , 0), and the law of λ∗ under m
                                                       n
            λn−1
is exactly (n−1)! dλ on [0, n + 1], of total mass (n+1)
                                                    n!   = V — i.e. the normalized law under β


                                                     12
      n−1
   nλ                                                            −                         n
is (n+1) n dλ. (A byproduct: being squeezed between G and G , in fact m(Cλ ) = V − λ /n! for

every λ ∈ (0, τ ).)
    For (E2): equality in (7.2) reads λ∗ dβ R= n, i.e. X dβ      = τ − n with X = τ − λ∗ . In the
                                      R                   R

proof of Proposition 5.6, g(s) − g(0) ≥ − log esX dβ = −s Xdβ + O(s2 ) = −(τ − n)s + O(s2 )
                                                              R

as s ↓ 0, so the nondecreasing quotient q satisfies q(0+ ) ≥ −(τ − n); with (5.3), q ≡ −(τ − n), i.e.
g is affine with slope −(τ − n) = −1.

    Sections 9–10 derive from Proposition 8.2, at a single base point p, the exact analytic
structure of the contact threshold: the sharp energy bound, the spectral pinching to a real-
analytic eigenfunction, and the holomorphy of its gradient field. Section 11 converts this into
the Laurent-mode structure of the eigenfunction (11A) and closes the equality case (11B): the
unique base-zero theorem, log-affine rigidity of ∇ϕ∗ , balance and integrality of the facet data,
exclusion of products, and the volume pinch give K = A(S). Section 12 assembles the proof.


9     The energy bound at s = 0
Standing notation for Part II: ω0 := i∂ ∂Φ  ¯ 0 , a smooth strictly positive (1, 1)-form; by Lemma
                                                                                           n
                         ¯ 0 )n , i.e. the measure (2π)n m is the Riemannian volume ω0 of ω0 ; in
2.3(c), e−Φ0 µΩ = n! (i∂ ∂Φ
                   1
                                                                                          n!
the log chart below, Ric(ω0 ) = −i∂ ∂¯ log det(ϕjk (x)) = i∂ ∂ϕ¯ = ω0 by det D2 ϕ = e−ϕ : (T, ω0 )
                                                                                       n
is Kähler–Einstein with constant 1, noncompact, of finite volume. Set c := n+2           ; fix p ∈ T ,
        ∗     ∗         (p)
write λ = λp , Ψ = Ψ . Standing assumption of Part II: τ = n + 1, so (E1), (E2) of
Proposition 8.2 hold for every p.
    Throughout this section we write (9.Fk) for the fact (Fk) from the Notation for Part II; in
particular (9.F1) is the sandwich Φ0 − sτ ≤ Ψs ≤ Φ0 with convexity of the ray (Lemma 5.2(b)),
(9.F2) is the Danskin bound (5.1), (9.F5) records 0 ≤ λ∗ ≤ τ with the contact inclusions of
Lemma 4.3, (9.F6) is the first-derivative identity Ψ̇0+ = λ∗ − τ (proved in Lemma 9.1(e) below),
and (9.F9) is the model data for K = S: in the p-centered coordinate on T = C∗ with u = up
the Fubini–Study potential,
                                           ¯ 2 = u(n+1−u) .
                                         |∂u|                                                   (9.F9)
                                             ω0
                                                      n+1

9.0 Conventions
(C1) Coordinates and frames. T = (C∗ )n , log coordinates ζj with zj = eζj , xj = 2 Re ζj =
log |zj |2 , θj = Im ζj . The vector fields ∂ζj := zj ∂zj , ∂ζ̄j := z̄j ∂z̄j are a global holomorphic frame
and its conjugate; in (x, θ),

                                 ∂ζj = ∂xj − 2i ∂θj ,        ∂ζ̄j = ∂xj + 2i ∂θj .

µΩ = dx dθ. Both operators are µΩ -divergence free:
                      Z              Z
                         ∂ζj F µΩ =     ∂ζ̄j F µΩ = 0                 (F ∈ Cc1 (T )).                 (C1.1)
                             T                T

(C2) Metric and norms. gj k̄ := ∂ζj ∂ζ̄k Φ0 = ϕjk (x) > 0 (real symmetric, smooth; D2 ϕ > 0
                                     P j
                                        W ∂ζj : |W |2ω0 :=     gj k̄ W j W k . For (0, 1)-forms α =
                                                            P                                       P
by (P1)). For (1, 0)-fields W =                                                                       ak̄ dζ̄k
we set |α|ω0 := |U |ω0 , where U is the unique field with ak̄ = j gj k̄ U ; equivalently |α|2ω0 =
          2           2                                                              j
                                                                           P

                                                          ¯ 2 .
supW ̸=0 | k ak̄ W k |2 /|W |2ω0 . For real u, |∂u|2ω0 = |∂u|
          P
                                                              ω0
(C3) Measures. dm0 := e−Φ0 µΩ , m0 (T ) = (2π)n Rn e−ϕ dx = (2π)n V by (P1); m = (2π)−n m0 ,
                                                          R

β = m0 /((2π)n V ).
(C4) Ray parameter. σ = s + it ∈ H = {Re σ > 0}; ∂σ = 12 (∂s − i∂t ), ∂σ ∂σ̄ = 14 (∂s2 + ∂t2 ). On
X := H × T the global frame is e0 := ∂σ , ej := ∂ζj , and the reference measure is Vol := ds dt µΩ .


                                                        13
Ψ is u.s.c. psh on X, a function of (s, z); Ψs (z) := Ψ(s + i0, z); by (9.F1): Φ0 − sτ ≤ Ψs ≤ Φ0 ,
Ψ0 = Φ0 , s 7→ Ψs (z) convex nonincreasing.
   R Distributions on T (resp. X) are defined against µΩ (resp. Vol): e.g. ⟨∂ζ̄k u, F ⟩ :=
(C5)
− T u ∂ζ̄k F µΩ . In any simply connected product chart these conventions agree with the standard
coordinate ones up to theR harmless global constant µΩ = 2n · Leb.
(C6) Energy. E0 (u) := T |∂u| ¯ 2 dβ if ∂u
                                         ¯ (distributional) is represented by an L2 form with
                                  ω0                                                 loc
finite such integral; +∞ otherwise.

Lemma 9.1 (Pointwise structure in s; measurability)
    For every z ∈ T , write Fz (s) := Ψs (z).
    (a) Fz is finite, convex, nonincreasing on [0, ∞), Lipschitz with constant τ , Fz (0) = Φ0 (z).
The difference quotients vs (z) := Ψs (z)−Φ   s
                                                0 (z)
                                                      ∈ [−τ, 0] are nondecreasing in s, and v0 (z) :=
Ψ̇0+ (z) = lims↓0 vs (z) = inf s>0 vs (z) ∈ [−τ, 0] exists everywhere.
    (b) For s > 0 the one-sided derivatives Ψ̇s± (z) exist, are nondecreasing in s, take values
in [−τ, 0], satisfy vs ≤ Ψ̇s− ≤ Ψ̇s+ , and lims↓0 Ψ̇s± (z) = v0 (z). Moreover Ψb (z) − Ψa (z) =
Rb
 a Ψ̇u+ (z) du for 0 ≤ a ≤ b.                                                       R∞
    (c) There is a unique positive Radon measure νz on (0, ∞) with χ dνz = 0 Ψs (z)χ′′ (s) ds
                                                                         R

for all χ ∈ Cc2 ((0, ∞)); and νz (a, b) = Ψ̇b− (z) − Ψ̇a+ (z) for 0 < a < b, while
                                         

                                       
                              νz (0, h) = Ψ̇h− (z) − v0 (z)      (h > 0).                       (9.1.1)

    (d) The maps (s, z) 7→ Ψs (z), vs (z), Ψ̇s± (z) and z 7→ v0 (z) are Borel.
    (e) vs ≥ λ∗ − τ for all s > 0, hence v0 ≥ λ∗ − τ pointwise on T ; and v0 = λ∗ − τ β-a.e.
(hence µΩ -a.e.).
    (f ) For each s ≥ 0, Ψs ∈ PSH(T ) ∩ L∞loc ; Ψs → Φ0 uniformly as s ↓ 0, with ∥Ψs − Φ0 ∥∞ ≤ sτ .

Proof. (a) Finiteness, convexity, monotonicity, and the sandwich are (9.F1). Chord slopes of
a convex function are nondecreasing; the chord over [0, s] has slope ≥ −τ (sandwich) and ≤ 0
(monotonicity), and any chord over [s, s′ ] ⊂ [0, ∞) has slope between the chord slope over
[0, s] and 0; hence all chord slopes lie in [−τ, 0], giving the τ -Lipschitz bound and vs ∈ [−τ, 0].
Monotonicity of s 7→ vs is convexity; the monotone bounded limit v0 exists everywhere.
    (b) Standard convex analysis gives existence and monotonicity of Ψ̇s± , the bound [−τ, 0]
(limits of chord slopes), and vs ≤ Ψ̇s− ≤ Ψ̇s+ (chord over [0, s] vs. derivative at s). For the
limit as s ↓ 0: for 0 < u < s, Ψ̇u+ ≤ Fz (s)−F
                                             s−u
                                                 z (u)
                                                       → vs as u ↓ 0 (continuity of Fz at 0 from the
sandwich), so limu↓0 Ψ̇u+ ≤ inf s vs = v0 ; conversely Ψ̇u+ ≥ vu ≥ v0 . Squeezing, and Ψ̇u− between
vu and Ψ̇u+ . The FTC holds because Fz is τ -Lipschitz on [0, b], hence absolutely continuous,
with a.e. derivative equal to Ψ̇u+ (convexity).
    (c) Fz is locally Lipschitz; integrating by parts once, Fz χ′′ = − Fz′ χ′ , where Fz′ is the
                                                                  R           R

(a.e.-defined, nondecreasing, bounded) derivative; a second Lebesgue–Stieltjes       R integration    by
parts against the right-continuous monotone modification u 7→ Ψ̇u+ gives − Fz′ χ′ = χ dνz
                                                                                              R

with νz := d(Ψ̇· + ). Then νz ((a, b)) = Ψ̇b− − Ψ̇a+ is classical, and (9.1.1) follows from (b):
lima↓0 Ψ̇a+ = v0 .
    (d) Ψ is u.s.c. on X, hence Borel; (s, z) 7→ Ψs (z) is Borel (composition with the continuous
section s 7→ s + i0); vs is Borel. Since r 7→ Ψs+r (z)−Ψr
                                                            s (z)
                                                                   is nondecreasing and continuous in
r (convex functions are continuous on open intervals), Ψ̇s+ (z) = inf r∈Q∩(0,1) Ψs+r (z)−Ψ  r
                                                                                               s (z)
                                                                                                     , a
countable infimum of Borel functions; similarly Ψ̇s− (z) = supr∈Q∩(0,min(1,s)) Ψs (z)−Ψ
                                                                                      r
                                                                                        s−r (z)
                                                                                                — the
guard r < s keeps the quotient inside the domain, and each quotient, extended by −∞ for r ≥ s,
is a globally defined Borel function of (s, z) — and v0 (z) = inf r∈Q+ vr (z).
    (e) The Danskin bound (9.F2) gives Ψs R≥ Φ0 + s(λ∗ − τ ), i.e. vs R≥ λ∗ − τ ; let s ↓ 0. For
the β-a.e. equality we first verify g ′ (0+ ) = v0 dβ: writing e−g(s) = T e−Φ0 e−svs µΩ , one has


                                                  14
 e−svs −1
      s      ≤ τ esτ pointwise (from |vs | ≤ τ ) with the finite dominating measure e−Φ0 µΩ , while
e−svs (z) −1
      s      → −v0 (z) pointwise (since svs = Ψs − Φ0 → 0 and vs → v0 ); dominated convergence
                                   d
                                         e−g(s) = − T v0 e−Φ0 µΩ , i.e. g ′ (0+ ) = v0 dβ. By (E2),
                                                    R                              R
on difference quotients gives ds      0+
g ′ (0+ ) = −1, while (E1) gives (λ∗ − τ )dβ = n − (n + 1) = −1; the integrand v0 − (λ∗ − τ )
                                    R

is nonnegative with zero integral. Since dβ has smooth positive density w.r.t. µΩ , “β-a.e.” =
“µΩ -a.e.”.
    (f) Ψs is the restriction of the psh Ψ to the complex submanifold {s + i0} × T ; it is psh or
≡ −∞ on the connected T , and the sandwich excludes −∞ and gives local boundedness and the
uniform convergence.


Lemma 9.2 (exact remainder budget)
  Let Rh := Ψh − Φ0 − h(λ∗ − τ ), h > 0. Then Rh is Borel and

                                   0 ≤ Rh ≤ τ h pointwise on T,                               (9.2.1)
                                1
and there are h0 = h0 (n) := 2(n+1)  and an explicit C1 = C1 (n) (e.g. C1 = (n + 1)3 + 2(n + 1))
such that
                                       c
                            Eβ [Rh ] − h2 ≤ C1 h3       (0 < h ≤ h0 ).                    (9.2.2)
                                       2
Proof. Borel: Lemma 9.1(d) and (9.F5). Lower bound in (9.2.1): Lemma 9.1(e) (vh ≥ λ∗ − τ ).
Upper: Rh = (Ψh − Φ0 ) + h(τ − λ∗ ) ≤ h(τ − λ∗ ) ≤ hτ , using Ψh ≤ Φ0 and 0 ≤ λ∗ ≤ τ (9.F5).
   Set X := n + 1 − λ∗ ∈ [0, n + 1] (in this proof only, X denotes this random variable, as in
Proposition 5.6 —R not the manifold H × T of (C4)). Pointwise, e−Ψh = e−Φ0 ehX e−Rh , so by
(E2) (in the form T e−Ψh µΩ = (2π)n V eh , (9.F4)), dividing by (2π)n V :

                                           Eβ ehX e−Rh = eh .
                                                     
                                                                                              (9.2.3)

All integrands are bounded Borel, so (9.2.3) is a legitimate identity of finite integrals. By
                               nλn−1
(E1) ((9.F4)), λ∗ has law (n+1)                                                            ∗
                                   n dλ on [0, n + 1] under β; direct integration gives E[λ ] = n,

E[(λ∗ )2 ] = n+2
              n
                 (n + 1)2 , hence

                                   E[X] = 1,        E[X 2 ] = 1 + c.

Taylor with remainder, using 0 ≤ X ≤ n + 1 and ehX ≤ e(n+1)h ≤ e1/2 ≤ 2 for h ≤ h0 :
                                                                   3                  3
          M (h) := E[ehX ] = 1 + h + 1+c 2
                                      2 h + r1 ,       0 ≤ r1 ≤ h6 E[X 3 ehX ] ≤ (n+1)
                                                                                   3   h3 ,
                   2                   3                               3
and eh = 1 + h + h2 + r2 , 0 ≤ r2 ≤ h3 . Hence with C0 := (n+1)
                                                             3
                                                                +1
                                                                   ,

                       E ehX (1 − e−Rh ) − 2c h2 = M (h) − eh − 2c h2 ≤ C0 h3 .
                                       
                                                                                              (9.2.4)

Now use 1 ≤ ehX and 1 − e−t ≥ t(1 − 2t ) for t ≥ 0, with t = Rh ≤ τ h and τ2h ≤ 41 :

                             E ehX (1 − e−Rh ) ≥       1 − (n+1)h
                                                                
                                                             2      E[Rh ],

whence, by (9.2.4) and (1 − x)−1 ≤ 1 + 2x for x ≤ 12 ,

                     E[Rh ] ≤ 2c h2 + C0 h3 1 + (n + 1)h ≤ 2c h2 + C1 h3 .
                                                       


Conversely 1 − e−Rh ≤ Rh and ehX ≤ e(n+1)h give

               E[Rh ] ≥ e−(n+1)h E ehX (1 − e−Rh ) ≥ e−(n+1)h 2c h2 − C0 h3 .
                                                                         


                                                  15
Two cases. If 2c h2 − C0 h3 ≥ 0, then multiplying e−(n+1)h ≥ 1 − (n + 1)h by the nonnegative
bracket,

      E[Rh ] ≥ 1 − (n + 1)h 2c h2 − C0 h3 ≥ 2c h2 − C0 + c(n+1)
                                                                    3
                                                                    h ≥ 2c h2 − C1 h3 .
                                           
                                                                2

If 2c h2 − C0 h3 < 0, then also 2c h2 − C1 h3 < 0 ≤ E[Rh ] (by (9.2.1) and C1 > C0 ), and the lower
bound holds trivially. One checks C1 = (n + 1)3 + 2(n + 1) suffices for both bounds (since 2c ≤ 12 ,
           3
C0 ≤ (n+1)
        3
           +1
              , h ≤ h0 ≤ 21 ).


Lemma 9.3 (Tauberian step)
  Define, for h > 0,

                                                      q − (h) := Eβ Ψ̇h− − Ψ̇0+ .
                                                                            
                     q(h) := Eβ Ψ̇h+ − Ψ̇0+ ,

Then q, q − are well defined with values in [0, τ ], q is nondecreasing, q − ≤ q,
                                Z h
                                    q(u) du = Eβ [Rh ]       (h > 0),                           (9.3a)
                                   0

and there are h1 = h1 (n), C2 = C2 (n) with
                                                                                                −
|q(h)−ch| ≤ C2 h3/2 ,   |q − (h)−ch| ≤ C2 h3/2   (0 < h ≤ h1 ); in particular lim q(h)    q (h)
                                                                                   h = lim h    = c.
                                                                                h↓0       h↓0
                                                                                                (9.3b)

Proof. By Lemma 9.1(b,e), D̃u (z) := Ψ̇u+ (z) − v0 (z) ∈ [0, τ ] is jointly Borel (Lemma 9.1(d)),
nondecreasing in u; thus q(u) = Eβ [D̃u ] ∈ [0, τ ] is nondecreasing, and q − ≤ q since Ψ̇h− ≤ Ψ̇h+ .
   By the FTC of Lemma 9.1(b) with a = 0, for every z:
                                                          Z h
                           Ψh (z) − Φ0 (z) − h v0 (z) =       D̃u (z) du.
                                                            0

The left side equals Rh (z) − h v0 (z) − (λ∗ (z) − τ ) , and the bracket vanishes for β-a.e. z (Lemma
                                                   

9.1(e), one fixed null set independent of h). Integrating in β and applying Tonelli (nonnegative,
jointly Borel) gives (9.3a).
    Tauberian step. Fix 0 < ε ≤ 1 and 0 < h ≤ h1 := h0 /4, so (1 + ε)h ≤ 2h ≤ h0 . By
monotonicity and (9.3a), (9.2.2):
                          Z (1+ε)h
                                   q = E[R(1+ε)h ] − E[Rh ] ≤ 2c 2ε + ε2 h2 + 9C1 h3 ,
                                                                        
               εh q(h) ≤
                           h
                                                 √
hence q(h) ≤ ch + 2c εh + 9Cε 1 h2 ; choosing ε = h, q(h) ≤ ch + ( 2c + 9C1 )h3/2 . Similarly
          Z h
εh q(h) ≥       q ≥ 2c (2ε − ε2 )h2 − 2C1 h3 ⇒ q(h) ≥ ch − 2c εh − 2Cε 1 h2 ≥ ch − ( 2c + 2C1 )h3/2
            (1−ε)h
           √
with ε = h. Set C2 := 1 + 9C1 . For q − : q − (h) ≤ q(h), and for u < h, Ψ̇h− ≥ Ψ̇u+ pointwise,
so q − (h) ≥ supu<h q(u) ≥ ch − C2 h3/2 (let u ↑ h in the lower bound for q(u)).


Lemma 9.4 (Coefficient measures of a psh function; Cauchy–Schwarz)
     Let Y be either X = H × T (frame e0 = ∂σ , ej = ∂ζj , measure Vol, N = n + 1) or T (frame
∂ζj , measure µΩ , N = n), and let u ∈ PSH(Y ) ∩ L1loc . Define distributions
                              Z
                 Tab̄ (F ) :=   u ∂ea ∂ēb F d(reference measure),    F ∈ Cc∞ (Y ).
                               Y


                                                 16
Then:
     (a) Each Tab̄ is (represented by) a complex Radon       measure; Taā ≥ 0; Tbā = Tab̄ ; for
every relatively compact Borel E the matrix Tab̄ (E) a,b is Hermitian positive semidefinite, and
|Tab̄ |(E) ≤ 12 Taā (E)
                                  
                       P+ Tbb̄ (E) .                                 
     (b) With Λ := a Taā and τab̄ := dTab̄ /dΛ, the matrix τab̄ (w) is Hermitian psd for Λ-a.e.
w.
     (c) For every bounded Borel f ≥ 0 with compact support and bounded Borel fields ξ, η :
Y → CN , all integrals below are finite, the two right-hand factors are ≥ 0, and
                  XZ                 2   XZ                  X Z                   
                            a b                     a ¯b
                         f ξ η̄ dTab̄ ≤          f ξ ξ dTab̄          f η a η̄ b dTab̄ .  (9.4a)
                  a,b                           a,b                        a,b

Proof. (a) In a simply connected product chart the frame is the coordinate frame and the reference
measure is 2n ·Lebesgue, so all claims are chart-local statements about the classical Hessian
coefficients of a psh function, scaled by a positive constant; distributions defined
                                                                                 P a ¯bby the single
global formula automatically agree on overlaps. For constant ξ, P (ξ) :=              ξ ξ Tab̄ ≥ 0 as a
distribution: positivity is local, and in a chart the Euclidean mollification u ∗ ρε (equivalently,
on T = Cn /2πiZn , the global group convolution, which preserves pshP         since translations are
biholomorphic) is smooth psh with pointwise psd complex Hessian, so             ξ a ξ¯b ∂a ∂b̄ (u ∗ ρε ) ≥ 0
pointwise; since u ∗ ρε → u in L1loc , the limit distribution is positive; positive distributions
                                                                                                P a b are
positive Radon measures (Riesz–Markov). Polarization for the sesquilinear B(ξ, η) =                ξ η̄ Tab̄ ,
                                                      3
                                                      X
                                      B(ξ, η) = 14          ik P (ξ + ik η),
                                                      k=0

exhibits every Tab̄ as a finite combination of positive measures, hence a complex Radon measure.
Hermitian
P a ¯b      symmetry follows from u real and the commuting frame fields. The identity of measures
   ξ ξ Tab̄ = P (ξ) holds because both sides are Radon measures agreeing on Cc∞ ; evaluating at
any relatively compact
                   √        Borel E gives psd matrices M (E) = (Tab̄ (E)); psd Hermitian matrices
satisfy |Mab | ≤ Maa Mbb ≤ 12 (Maa + Mbb ), and taking suprema over partitions yields the
total-variation bound.
   (b) ByP (a),   Tab̄ ≪ Λ; for each ξ with coordinates in Q + iQ, the density of P (ξ) w.r.t. Λ,
namely       a ¯b
            ξ ξ τab̄ , is ≥ 0 Λ-a.e.; discard the countable union of null sets and use continuity of
the quadratic form in ξ.
                                           τab̄ ξ a η̄ b dΛ; finiteness is clear (f bounded with compact
                                  R     P               
   (c) Write each integral as f
support, Λ Radon, fields bounded). Apply, pointwise Λ-a.e., the Cauchy–Schwarz inequality for
psd Hermitian forms, then Cauchy–Schwarz in L2 (f dΛ).


Lemma 9.5 (block evaluation on the slab)
                                                                          ∞
    Fix a smooth compactly supported (1, 0)-field W on
                                            ∞
                                                           R T ; fix ρ ∈ Cc (T ) with 0 ≤ ρ ≤ 1, ρ ≡ 1
on a neighborhood of supp W ; fix κ ∈ Cc (R), κ ≥ 0, κ dt = 1. Fix h > 0 and for 0 < δ < h/2
let χδ ∈ Cc∞ ((0, h)), 0 ≤ χδ ≤ 1, be the edge cutoff χδ (s) = ψ(s/δ)ψ((h − s)/δ), where ψ ∈ C ∞ ,
                                                                          −
ψ ≡ 0 on (−∞, 14 ], ψ ≡ 1 on [ 34 , ∞), 0 ≤ ψ ′ ≤ 4; then χ′δ ds = µ+δ − µδ with probability measures
                      −
µ+         3δ                    3δ
  δ on (0, 4 ] and µδ on [h − 4 , h).
    Let Tab̄ be the coefficient measures (Lemma 9.4) of Ψ on X, and set f := χδ (s)κ(t)ρ(z)e−Φ0 (z) ∈
Cc∞ (X), f ≥ 0. Define
                 Z                       XZ                              XZ
         Aδ := f dTσσ̄ ,         Mδ :=               k
                                                f W dTσk̄ ,       Bδ :=        f W j W k dTj k̄ ,
                                            k                                    j,k


                                                       17
and on T : Gk := e−Φ0 W k , Hjk := e−Φ0 W j W k (note ρGk = Gk , ρHjk = Hjk ),
                     XZ                                        XZ
             L(s) :=         vs ∂ζ̄k Gk µΩ (s > 0),    L(0) :=      v0 ∂ζ̄k Gk µΩ ,
                              k   T                                               k   T

                                                 XZ
                                       b(s) :=             Ψs ∂ζj ∂ζ̄k Hjk µΩ .
                                                 j,k   T

Then:
                                                                               (2π)n V −
                          Z           hZ                 Z
                      1                          i     1
                              ρe−Φ0                        e−Φ0 Ψ̇h− − v0 µΩ =
                                                                         
    (i) 0 ≤ Aδ =                           χδ dνz µΩ ≤                                 q (h) ≤
                      4   T                            4 T                        4
(2π)n V
           q(h).
    4
                     1 ∞ ′
                         Z
                                                        h
    (ii) Mδ =               χδ (s) s L(s) ds −−−→ − L(h). Moreover |L(s)| ≤ τ CW with CW :=
P                    2 0                       δ↓0      2
  k ∥∂ ζ̄k G k ∥L1 (µ Ω ) < ∞; L  is continuous on  (0, ∞); and L(s)
                                                                   P→ L(0) as s ↓ 0.
    (iii) b ≥ 0 on [0, ∞), |b(s) − b(0)| ≤ sτ CW    ′ with C ′ :=
                                                              W        j,k ∥∂ζj ∂ζ̄k Hjk ∥L1 (µΩ ) < ∞,
                                          Z                   Z
                                                2   −Φ0
                                  b(0) =    |W |ω0 e    µΩ =     |W |2ω0 dm0 ,
                                            T                        T
                Z ∞                                        ′
                                                       τ CW
and 0 ≤ Bδ =          χδ (s) b(s) ds ≤ h b(0) +              h2 .
                 0                                       2
Proof. Throughout, each quantity equals the distribution Tab̄ applied to a smooth compactly
supported test function (the measure represents the distribution), and the defining double
integrals converge absolutely (Ψ is bounded on the compact support by supsupp |Φ0 | + hτ ), so
Fubini applies freely.
   (i) With F = χδ κ G, G              −Φ0               1   ′′         ′′
                             R :=′′ ρe R: ∂σ ∂σ̄ F = 4 (χδ κ + χδ κ )G. Integrating in t first and using
that Ψ is t-independent, κ = 0, κ = 1:

                      1
                         Z        hZ ∞                     i             1
                                                                           Z   hZ       i
               Aδ =         G(z)         χ′′δ (s) Ψs (z) ds µΩ (dz) =        G    χδ dνz µΩ ,
                      4 T             0                                  4 T
                                                                                  R
by Lemma 9.1(c) applied for each fixed z. Since 0 ≤ χδ ≤ 1(0,h) , χδ dνz ≤ νz ((0, h)) =
Ψ̇h− (z) − v0 (z) by (9.1.1); since 0 ≤ G ≤ e−Φ0 and the integrand is ≥ 0, the stated chain follows,
the last identity by (C3) and the definition of q − ; q − ≤ q by Lemma 9.3. (All integrands are
Borel by Lemma 9.1(d).) Positivity Aδ ≥ 0: Tσσ̄ ≥ 0, f ≥ 0.
   (ii) With Fk := χδ κ Gk (note f W k = χδ κGk because ρ ≡ 1 on supp W k ): ∂ζ̄k Fk = χδ κ ∂ζ̄k Gk
and ∂σ (χδ κ) = 12 (χ′δ κ − iχδ κ′ ). Integrating in t ( κ′ = 0, κ = 1):
                                                           R          R

                                        1 ∞ ′ hX
                                         Z                  Z                i
                              Mδ =              χδ (s)          Ψs ∂ζ̄k Gk µΩ ds.
                                        2 0                   T
                                                            k
                                                                                 R ′
Write Ψs = Φ0 + s vs . The Φ0 -part contributes 12                                 χδ ds = 0, since χ′δ =
                                                              P R                                  R
                                                                 k Φ0 ∂ζ̄k Gk µΩ
0. Hence Mδ = 12 χ′δ (s) s L(s) ds. Bounds: |vs | ≤ τ gives |L(s)| ≤ τ CW . Continuity on
                          R

(0, ∞): s 7→ vs (z) is continuous for each z (Lemma 9.1(a), convexity) and bounded; dominated
convergence.
            R Limit at     0:Rvs ↓ v0 pointwise     (Lemma 9.1(a)); dominated convergence. Edge limit:
         1                +                 −
                  sL(s)dµδ − sL(s)dµδ ; the first term is ≤ 3δ
                                              
Mδ = 2                                                               4 τ CW → 0; the second converges to
h L(h) because sL(s) is continuous at h and µ−           δ  → δh  weakly.
    (iii) With Fjk := χδ κHjk (again f W j W k = χRδ κHjk by the choice of ρ): ∂ζj ∂ζ̄k Fjk =
χ
Pδ κ ∂ζj ∂ζ̄k Hjk ; Fubini and t-integration give Bδ = χδ (s) b(s) ds. Positivity of b(s): b(s) =
   j,k (Θs )j k̄ (Hjk ) where (Θs )j k̄ are the coefficient measures of Ψs ∈ PSH(T ) (Lemma 9.1(f)); this
equals j,k (ρe−Φ0 ) W j W k d(Θs )j k̄ ≥ 0 by Lemma 9.4(c) on T with ξ = η = W , f0 = ρe−Φ0 .
         P R


                                                           18
                                       PR
The Lipschitz estimate: b(s) − b(0) =      (Ψs − Φ0 )∂ζj ∂ζ̄k Hjk µΩ and ∥Ψs − Φ0 ∥∞ ≤ sτ (Lemma
9.1(f)). The value b(0): integrate by parts twice using (C1.1) (all data smooth, compactly
supported — no boundary terms, no flux at infinity):
                  XZ                          XZ                            Z
                                                     gj k̄ W j W k e−Φ0 µΩ = |W |2ω0 dm0 .
                                    
          b(0) =         ∂ζ̄k ∂ζj Φ0 Hjk µΩ =
                     j,k   T                            j,k

               Rh                     ′
                                   τ CW
Finally Bδ ≤                            2
                   0 b ≤ hb(0) +     2 h using χδ ≤ 1(0,h) , b ≥ 0.


Theorem 9.6 (the s = 0 energy bound).
Under the standing equality assumption τ = n + 1, for every p ∈ T : the distributional
            ¯ 0 = ∂¯Ψ̇0+ , which coincides with ∂λ
(0, 1)-form ∂v                                  ¯ ∗ in D′ (T ), is represented by a form α ∈ L2 ,
                                                  p                                           (0,1)
unique as an L2 -class, with
                                                   Z
                                                                           n
                                     E0 (λ∗p ) =        ¯ ∗ |2 dβ ≤
                                                       |∂λp ω0
                                                   T                      n+2
               Z                                              Z
                     ¯ ∗ |2 dm0 ≤    n                               ¯ ∗ |2 dm ≤    n
equivalently        |∂λp ω0             (2π)n V and                 |∂λp ω0            V.
               T                    n+2                       T                    n+2
Proof. Step 1 (slab Cauchy–Schwarz). Fix W, ρ, κ as in Lemma 9.5, and 0 < h ≤ h1 ,
0 < δ < h/2. Apply Lemma 9.4(c) on X to u = Ψ (psh and locally bounded by (9.F1)),
with weight f = χδ κρe−Φ0 , constant field ξ = (1, 0, . . . , 0) (= ∂σ -direction) and field η =
(0, W 1 (z), . . . , W n (z)):
                                    |Mδ |2 ≤ Aδ · Bδ .
By Lemma 9.5(i),(iii), the right side is bounded uniformly in δ:
                                                                       ′
                                           (2π)n V                τ CW    
                               |Mδ |2 ≤            q(h) · h b(0) +       h2 .
                                              4                      2
Let δ ↓ 0 and use Lemma 9.5(ii):

h2           (2π)n V            τ C′                                q(h)       τ C′ 
   |L(h)|2 ≤         q(h) h b(0)+ W h2 ,                          i.e.   |L(h)|2 ≤ (2π)n V
                                                                             b(0)+ W h .
4               4                  2                                   h            2
                                                                                    (9.5a)
   Step 2 (h ↓ 0). By Lemma 9.5(ii), L(h) → L(0); by Lemma 9.3, q(h)/h → c. Hence
                                               Z
                          |L(0)|2 ≤ c (2π)n V     |W |2ω0 dm0 .                     (9.5b)
                                                                    T

   Step 3 (Riesz representation). Define, on smooth compactly supported fields,
                                       XZ
                                              v0 ∂ζ̄k e−Φ0 W k µΩ .
                                                              
                    ℓ(W ) := −L(0) = −
                                                        k     T


This is conjugate-linear in W and, by (9.5b) (the bound is independent of the auxiliary ρ),
                            p                                  Z
                                                        2
                                   n
                  |ℓ(W )| ≤ c (2π) V ∥W ∥m0 ,       ∥W ∥m0 :=     |W |2ω0 dm0 .
                                                                                T

Let L2 Γ be the Hilbert space of measurable (1, 0)-fields with finite ∥ · ∥m0 (the fiber metric is
smooth, m0 is σ-finite), and H the closure of the smooth compactly supported fields. Extending


                                                         19
ℓ continuously to H and applying the Riesz representation theorem for bounded conjugate-linear
functionals, there is a unique U ∈ H ⊂ L2 Γ with
          Z                   XZ
  ℓ(W ) = ⟨U, W ⟩ω0 dm0 =           gj k̄ U j W k e−Φ0 µΩ ∀W test,   ∥U ∥2m0 ≤ c (2π)n V. (9.5c)
            T                  j,k       T

                             ¯ 0 ). Fix k0 and take W = F ∂ζ , F ∈ C ∞ (T ). Given arbitrary
   Step 4 (identification of ∂v                              k0        c
G ∈ Cc (T ), choose F := e G (smooth, compactly supported); then e−Φ0 F = G, and (9.5c)
      ∞                   Φ0

becomes
              Z               Z                                        X
           − v0 ∂ζ̄k G µΩ =      ak̄0 G µΩ    ∀G ∈ Cc∞ (T ),    ak̄ :=   gj k̄ U j .
                        0
                T                    T                                        j

Since g is smooth with locally bounded inverse and U ∈ L2 Γ, each ak̄ ∈ L2loc (µΩ ). Thus, in
D′ (T ) (convention (C5); in charts, µΩ is a constant multiple of Lebesgue, so this is the ordinary
distributional statement):
                                                                   X
              ∂ζ̄k v0 = ak̄ (k = 1, . . . , n), i.e.   ¯ 0 = α :=
                                                       ∂v              ak̄ dζ̄k ∈ L2loc .
                                                                          k

By the musical isomorphism of (C2), |α|2ω0 = |U |2ω0 pointwise, so by (9.5c)
        Z                                                   Z
             ¯    2            2           n                     ¯ 0 |2 dβ ≤ c =    n
            |∂v0 |ω0 dm0 = ∥U ∥m0 ≤ c (2π) V,       i.e.        |∂v   ω0               .
           T                                                          T            n+2

    Step 5 (transfer to λ∗ ). By Lemma 9.1(e), v0 = λ∗ − τ µΩ -a.e.; both are bounded Borel,
hence equal in L1loc , hence have the same distributional derivatives; τ is constant. Therefore
¯ ∗ = ∂v
∂λ     ¯ 0 = α in D′ (T ), and all three displayed normalizations follow from (C3). Uniqueness of
     2
the L -representative is immediate (it is determined as a distribution).


Remark 9.7 (ζ- vs. s-conventions)
    On t-independent data, ∂σ ∂σ̄ = 14 ∂s2 and ∂σ = 12 ∂s . Accordingly, the penultimate inequality
of Step 1 reads:
    ζ(=σ)-convention (current blocks):
               Z                  Z                Z
                              2
                 f T (∂σ , W ) ≤ f T (∂σ , ∂σ ) · f T (W, W ),           T = i∂ ∂¯σ,z Ψ,

with f T (∂σ , ∂σ ) ≤ 14 Qρ (h), f T (∂σ , W ) → − h2 L(h), f T (W, W ) ≤ Ih , where Qρ (h) :=
       R                           R                              R
       −Φ0 ν ((0, h)) µ and I := h b(s) ds.
R                                    R
  T ρe      z          Ω     h         0
     s-convention: the factors ( 12 )2 = 14 cancel identically, leaving

                                         h2 |L(h)|2 ≤ Qρ (h) · Ih ,

with no residual factor of 2 or 4. In the limit, in the two normalizations:
                                                                Z
            ¯ ∗        2      n        n        2                    ¯ ∗ |2 dβ ≤ n .
          ⟨∂λ , W ⟩m0 ≤           (2π) V ∥W ∥m0         ⇐⇒          |∂λ   ω0
                            n+2                                  T              n+2

The only places where the choice of conventions could have introduced factors are: (a) the 14 / 12
above (they cancel exactly); (b) µΩ = 2n Lebesgue in charts (it enters all three blocks linearly and
the Cauchy–Schwarz inequality is quadratically homogeneous, so it cancels); (c) m0 (T ) = (2π)n V
(it cancels between (9.5b) and the definition of β). Proposition 9.8 verifies the net outcome
against the model.

                                                    20
Proposition 9.8 (The n = 1 model)
    Let K = S = [−1, 1], n = 1, τ = 2, V = 2, c = 13 ; use the model data of (9.F9): in the
p-centered coordinate w, r := log |w|2 , t := |w|2 = er , f (r) = 2 log(1 + er ), local potential of ω0
equal to f (r) + pluriharmonic, Ψs = f (r + s) − 2s (+ the same pluriharmonic), λ∗ = 1+t    2t
                                                                                               = f ′ (r).
Then each constant of Lemmas 9.1–9.3 and Theorem 9.6 is exact:
                                  2 dt dθ                4π                            dt dθ
   1. Measure and law. ω0 = (1+t)       2 , so m-mass = 2π = 2 = V , and dβ = 2π(1+t)2 . Hence
                                                                             n−1
      β(λ∗ < λ) = β t < 2−λ
                         λ
                              = λ2 : the law is uniform on [0, 2], exactly (n+1)
                                                                           nλ               ∗
                            
                                                                                 n dλ; E[λ ] = 1 = n,

      Var = 31 = c.

   2. First-derivative identity (9.F6). v0 = lims↓0 f (r+s)−f
                                                            s
                                                              (r)−2s
                                                                     = f ′ (r) − 2 = λ∗ − τ —
      exact, with empty null set.

   3. Lemma 9.2. Rh = f (r + h) − f (r) − hf ′ (r) ∈ [0, 2h]. The identity (9.2.3): ehX e−Rh =
      e2h ef (r)−f (r+h) and
                                          Z ∞                       Z ∞
                                                1 + t 2 dt                  dt
                                                                                      = e−h ,
                       f (r)−f (r+h) 
                    Eβ e                =            h           2
                                                                   =            h t)2
                                           0   1 + e   t (1 + t)      0  (1 + e
                                                                                       2
      so E[ehX e−Rh ] = e2h e−h = eh — (E2) verified exactly. Budget: E[Rh ] = h2 E[f ′′ (r)] + O(h3 )
                              λ∗ (2−λ∗ )                R2
      and f ′′ (r) = (1+t)
                       2t
                          2 =      2     , so E[f ′′ ] = 0 λ(2−λ)
                                                              2
                                                                  dλ   1               c 2      3
                                                                   2 = 3 = c: E[Rh ] = 2 h + O(h ).
                                                                                           Rh
   4. Lemma 9.3. q(h) = E[f ′ (r + h) − f ′ (r)], so q(h)/h → E[f ′′ ] = 13 = c;            0 q = E[Rh ]
      trivially.
                                                                                    ¯ ∗ |2 =
   5. Theorem 9.6 and item (9.F9). gww̄ = f ′′ (r)/|w|2 , ∂w̄ λ∗ = f ′′ /w̄, hence |∂λ   ω0
      |w|2 (f ′′ )2          λ∗ (2−λ∗ )
                      ′′
       f ′′ · |w|2 = f (r) =      2     — exactly (9.F9)’s u(n+1−u)
                                                              n+1   — and

                                        E0 (λ∗ ) = Eβ [f ′′ ] = 13 = n+2
                                                                      n
                                                                         .

Thus the model saturates Theorem 9.6, so the constants of Lemmas 9.1–9.3 and Theorem 9.6
are sharp. □


10     The spectral gap and the holomorphic gradient field
This section proves: the sharp spectral-gap inequality on T (Theorem 10.5 — where the lattice
hypothesis (ii) does its work in Part II); the eigenfunction package for the contact threshold
(Theorem 10.7); and, unconditionally, the Matsushima-type holomorphy of its gradient field (The-
                                             ¯
orem 10.14), proved by a boundary-positive ∂-Neumann     (Morrey–Kohn–Hörmander) argument
on smoothed convex torus boxes combined with a saturation argument forced by the spectral
pinching — no flux-decay at infinity is needed.

10.0 Conventions
                                                                                                n
                                                             n
Throughout, τ = n + 1 (equality case), p ∈ T is fixed, c := n+2 , V = vol(K) = (n+1)
                                                                                 n! .
                                x
Coordinates. zj = eζj , ζj = 2j +iθj , so xj = log |zj |2 = ζj +ζ̄j . For f = f (x): ∂ζj f = ∂ζ̄j f = fxj .
One checks i dζj ∧dζ̄j = dxj ∧dθj , hence µΩ = dx dθ = j i dζj ∧dζ̄j equals 2n ·(Lebesgue measure
                                                          Q
of the ζ-chart) (globally on the cover Cn ), consistently with (C5) of Section 9; only its translation-
invariance in ζ is used below.
Metric and measures. ω0 = i∂ ∂Φ     ¯ 0 = i g dζ j ∧ dζ̄ k with g = ϕjk (x) (as in (C2) of Section
                                               j k̄                   j k̄
9). The volume form is dVω0 = ω0n /n!; from Lemma 10.8 through the proof of Theorem

                                                      21
10.14 we abbreviate dV := dVω0 (not Euclidean Lebesgue measure, which is not used there).
                1
Measures: m = (2π)   −Φ0 µ , β = m/V .
                  ne      Ω

Norms, gradient, Laplacian. For a (0, 1)-form α = αk̄ dζ̄ k : |α|2ω0 := g j k̄ αk̄ αj̄ . For u:
¯ = u dζ̄ k , and for real u, |∂u|   ¯ 2 = g j k̄ uj u . Energy: E0 (u) :=         ¯ 2
                                                                               R
∂u      k̄                             ω0             k̄                        T |∂u|ω0 dβ. Complex
Laplacian: ∆u := g j k̄ ∂j ∂k̄ u (so ∆ = 12 ∆Laplace–Beltrami ). Gradient field: grad1,0 u := g j k̄ uk̄ ∂ζj ,
and
 Vp := grad1,0
           ω0 up           (Vpj = g j k̄ ∂k̄ up ; a constant phase rotation of Vp is immaterial in all uses).
                     ¯ u ∈ L1 has ∂u          ¯ = α distributionally if u ∂ χ dλζ = − α χ dλζ for all
                                                                          R                R
Distributional ∂:                  loc                                         k̄ R            k̄
χ ∈ Cc∞ , in every chart. L2(0,1) (ω0 , β) = measurable (0, 1)-forms with |α|2ω0 dβ < ∞. For a (0, 2)-
form η = 12 ηk̄l̄ dζ̄ k ∧dζ̄ l (antisymmetric coefficients) we use the norm |η|2ω0 := 12 g k̄j g l̄m ηk̄l̄ ηj̄ m̄ —
            P

the 12 -convention for antisymmetric two-tensors; similarly for two-tensors Sk̄l̄ without symmetry,
∥S∥2 := g k̄j g l̄m Sk̄l̄ Sj̄ m̄ dV (no 21 ).
          R

Standing hypotheses. We use (P1)–(P6), (E1)–(E2), (F1)–(F9) and Theorem 9.6 (∂λ                     ¯ ∗ ∈ L2 ,
                                                                                                            p
E0 (λ∗p ) ≤ c) throughout. Here s = Re ζ; Ψs enters only through (E1),(E2).

Lemma 10.1 (Structural identities of the KE metric)
(a) In ζ-charts, det(gj k̄ ) = det D2 ϕ = e−Φ0 ; hence dVω0 = e−Φ0 µΩ , and m = (2π)  1
                                                                                        n dVω0 : the
weighted measure is the metric volume.
(b) (Divergence identities.) ∂j det g g j k̄ = 0 and ∂k̄ det g g j k̄ =
                                                                      
                                                                           R 0. Consequently, for
any smooth compactly supported field Z = Z m̄ ∂ζ̄m (resp. Y = Y j ∂ζj ), T ∇m̄ Z m̄ dβ = 0 (resp.
        j
R
  T ∇j Y dβ = 0).
                                                 1
(c) (Drift cancellation.) For u ∈ C 2 , −Φ0 ∂j e−Φ0 g j k̄ ∂k̄ u = g j k̄ ∂j ∂k̄ u = ∆u. Thus the
                                                                
                                              e
Witten drift of the weight e−Φ0 relative to µΩ cancels exactly against the metric divergence: the
weighted adjoint operator is the metric Laplacian.
(d) Ric(ω0 ) := −i∂ ∂¯ log det g = i∂ ∂Φ
                                      ¯ 0 = ω0 , i.e. R = g .
                                                              j k̄   j k̄
(e) (Toric transport.) ϕ is proper: since b(K) = 0, 0 ∈ int K, pick r > 0 with B̄(0, r) ⊂ int K;
then ϕ(x) ≥ sup|y|≤r (⟨x, y⟩ − ϕ∗ (y)) ≥ r|x| − Cr by (F8). For torus-invariant f = f (x):
 ¯ |2 = ⟨(D2 ϕ)−1 ∇f, ∇f ⟩, and for any Borel G ≥ 0 on Rn ,
|∂f ω0
                    Z                 Z                Z
                                    1        −ϕ      1
                        G(x) dβ =        G e dx =            G(x(y)) dy,
                      T             V Rn             V int K
via the moment diffeomorphism y = ∇ϕ(x), dy = e−ϕ dx, with (D2 ϕ(x))−1 = D2 ψ(y), ψ := ϕ∗
(F8).

Proof. (a) is the KE/MA equation (P1). (b): ∂j (det g g j k̄ ) = det g [g lm̄ ∂j glm̄ g j k̄ − g j m̄ ∂j glm̄ g lk̄ ]
(by ∂j det g = det g tr(g −1 ∂j g) and ∂g −1 = −g −1 (∂g)g −1 ), and the Kähler symmetry ∂j glm̄ =
∂l gj m̄ (both equal Φ0,jlm̄ ) makes the bracket vanish after relabelling; the conjugate identity
follows by conjugation (det g real, g j k̄ = g kj̄ ). The integral statements follow from ∇m̄ Z m̄ =
   1               m̄          m̄
 det g ∂m̄ (det g Z ) (using Γ̄m̄l̄ = ∂l̄ log det g) and compact support, since µΩ is Lebesgue in ζ —
the ζ-chart being the universal cover, integrate over a fundamental domain Rn × [0, 2π)n ; the
θ-boundary terms cancel by periodicity and the x-boundary terms vanish by compact support.
(c) expand and use (b) with det g = e−Φ0 . (d) direct. (e) computations shown; smoothness of
ψ and of x(·) = ∇ψ is standard for smooth strictly convex ϕ with ∇ϕ a diffeomorphism onto
int K (F8); and Cr := sup|y|≤r ϕ∗ (y) < ∞ because B̄(0, r) ⊂ int K ⊆ int dom ϕ∗ (for convex C
with C̄ ⊇ K one has int K ⊆ int C̄ = int C) and convex functions are continuous, hence locally
bounded, on the interior of their domain.

                                                        22
Lemma 10.2 (Lefschetz commutator).
    On any hermitian n-dimensional space, [L, Λ] = (p + q − n) Id on (p, q)-covectors, where
L = ω ∧ · and Λ = L∗ . In particular [ω0 , Λω0 ] = Id on (n, 1)-forms.

Proof. Fix a unitary coframe e1 , . . . , en , ω = j iej ∧ ēj , L = j Lj . Since ej ∧ ēj is of even
                                                      P                   P
degree, Lj and Λj act on the j-th tensor factor of the monomial basis without Koszul signs, and
the inner product is multiplicative on monomials; hence for j =           ̸ k, [Lj , Λk ] = 0 (they act on
disjoint factors). For fixed j, on the four basis forms 1, e , ē , e ∧ ēj one computes Lj (1) = iej ∧ ēj ,
                                                                j  j   j

Λj (ej ∧ ēj ) = −i, Lj , Λj kill the rest; hence [Lj , Λj ] = (aj + bj − 1)Id where aj , bj ∈ {0, 1} record
                     j j
           P of e , ē (verified on each of the four basis elements: −1, 0, 0, +1). Summing,
the presence
[L, Λ] = j (aj + bj − 1) = (p + q − n)Id.


Lemma 10.3 (Exact unitary correspondences).
  Let Ω := dz            dzn    1            n
            z1 ∧ · · · ∧ zn = dζ ∧ · · · ∧ dζ (global holomorphic, nowhere zero). Then:
              1


       2                                            2
(a) in Ω ∧ Ω̄ = µΩ and |Ω|2ω0 dVω0 = in Ω ∧ Ω̄, hence |Ω|2ω0 = eΦ0 .
                                         Z                    Z                     Z
                                                2 −Φ0              2 −Φ0          n
               2
(b) For v ∈ Lloc and a (0, 1)-form α:       |vΩ|ω0 e   dVω0 = |v| e      µΩ = (2π)    |v|2 dm, and
|α ∧ Ω|2ω0 = |α|2ω0 |Ω|2ω0 , hence |α ∧ Ω|2 e−Φ0 dVω0 = (2π)n |α|2ω0 dm.
                                  R                          R

    ¯
(c) ∂(vΩ)      ¯ ∧ Ω distributionally, and α 7→ α ∧ Ω is injective pointwise.
           = (∂v)
                                                                          n                            2
Proof. (a) In a unitary coframe e = C dζ: ωn! = j (iej ∧ ēj ) = in e1···n ∧ ē1···n — reordering
                                                                              Q

(e1 , ē1 , . . . , en , ēn ) to (e1 , . . . , en , ē1 , . . . , ēn ) moves ē1 , . . . , ēn−1 past n−1       n
                                                                                                         P         
                                                                                                          j=1 j = 2 odd-degree
                                                                       2
                                             n(n−1)/2 = in . Since Ω = det(C −1 )e1···n and |e1···n | = 1,
factors, costing (−1)n(n−1)/2 , and in (−1)
                               2
both identities follow; in Ω ∧ Ω̄ = j (idζ j ∧ dζ̄ j ) = µΩ by §1.1. (b) For the second identity
                                        Q

                aj̄ ēj ; then α ∧ Ω = det(C −1 ) aj̄ ēj ∧ e1···n , an orthogonal expansion. (c) Ω is
            P                                    P
write α =
smooth with ∂Ω ¯ = 0; the product rule for distributions against smooth forms gives the identity;
injectivity is clear pointwise since Ω ̸= 0.


Theorem 10.4 (Hörmander estimate with constant one on T ).
                                  ¯ = 0 distributionally. Then there exists v ∈ L2 (β) with ∂v
    Let α ∈ L2(0,1) (ω0 , β) with ∂α                                                        ¯ =α
distributionally and                 Z              Z
                                                    |v|2 dβ ≤         |α|2ω0 dβ.
                                                T                 T

Proof. We invoke:

       Theorem H (Hörmander–Andreotti–Vesentini–Demailly). Let (X, ω) be
       a Kähler n-manifold admitting a smooth plurisubharmonic exhaustion. Let φ ∈
       C ∞ (X) with i∂ ∂φ¯ ≥ 0, and suppose A := [i∂ ∂φ,
                                                       ¯ Λω ] is positive definite on (n, 1)-
       forms. Then                                  2                 ¯ = 0 distributionally
                          every (n, 1)-form g with Lloc coefficients, ∂g
                    R for−1       −φ dV < ∞, there is an (n, 0)-form h with ∂h  ¯ = g and
       R M2 :=
       and           X ⟨A g, g⟩ω e      ω
                 −φ
        X |h|ω e    dVω ≤ M .
       (J.-P. Demailly, Complex Analytic and Differential Geometry, Ch. VIII, Thm (6.1) —
       the weakly pseudoconvex form quoted here, for arbitrary, possibly incomplete, Kähler
       ω; cf. also Estimations L2 pour l’opérateur ∂¯ . . . , Ann. Sci. ÉNS 15 (1982), Thm
       5.1 for the complete-metric version. The proof: Bochner–Kodaira–Nakano for the
                                      ¯
       complete metrics ωε = ω+εi∂ ∂(χ◦ψ)      ≥ ω — available since ψ is a psh exhaustion and
       Andreotti–Vesentini density applies on complete manifolds — followed by the limit
       ε ↓ 0, legitimate because for (n, q)-forms the quantity ⟨A−1 g, g⟩ dV is nonincreasing
       in the metric. Incompleteness of ω is thus covered by the theorem.)

                                                             23
    Verification of hypotheses. X = T is Stein; ψ := ϕ ◦ L is a smooth psh exhaustion (psh: ϕ
convex in x; exhaustion: Lemma 10.1(e) properness plus compactness of the θ-torus). ω = ω0
Kähler, φ = Φ0 smooth with i∂ ∂Φ  ¯ 0 = ω0 > 0. By Lemma 10.2, A = [ω0 , Λω ] = Id on (n, 1):
                                                                                   0
                          −1
positive definite, and ⟨A g, g⟩ = |g|2 .
    Apply Theorem H to g := α ∧ Ω (closed by Lemma 10.3(c);    L2loc since α ∈ L2 (β) and all densi-
                                                   n        2
                                                       R
ties are locally bounded above and below): M = (2π) V R |α|ω0 dβ < ∞ by Lemma       R 10.3(b).  Write
                                                             2         1 n supE Φ0        2 −Φ
the solution h = vΩ (Ω nonvanishing; on a compact E, E |v| dλζ ≤R2 e                 E |v| e
                                                                                               0 µΩ <
∞, so v ∈ L2loc ); Lemma 10.3(b),(c) give ∂v ¯ = α and (2π)n V |v|2 dβ ≤ M . Divide by
(2π)n V .


Theorem 10.5 (complex Brascamp–Lieb on T ).
                                                              ¯ lies in L2 (ω0 , β):
  For every u ∈ L2 (β) (real or complex) whose distributional ∂u         (0,1)
                                               Z
                                  Varβ (u) ≤        ¯ 2 dβ = E0 (u).
                                                   |∂u|ω0
                                               T

Proof. α := ∂u¯ is ∂-closed
                       ¯         distributionally (∂¯2 = 0 on distributions). Theorem 10.4 yields
            ¯ = α, ∥v∥2 2 ≤ E0 (u). Then w := u − v satisfies ∂w
v ∈ L2 (β), ∂v                                                       ¯ = 0 distributionally, hence
                           L (β)
(hypoellipticity Rof ∂¯ in bidegree (0, 0) — Weyl’s lemma for ∂)¯ w is a.e. equal to a holomorphic
function; since |w| e   2 −Φ 0            n      2
                               µΩ = (2π) V ∥w∥β < ∞, w ∈ HΦ0 = C · 1 by (P2)/(F7). This is
where hypothesis (ii) (the lattice condition) does its work (it is reused, in the same
rank-one form, in Lemma 10.6(c) and in Theorem 10.14, Step 2). Thus u = v + const a.e., so
Varβ (u) = Varβ (v) ≤ ∥v∥2L2 (β) ≤ E0 (u).


Lemma 10.6 (Form, operator, kernel, gap).
                          ¯ ∈ L2 (ω0 , β) distributionally} and Q(u, v) := ⟨∂u,
   Let D := {u ∈ L2 (β) : ∂u                                                ¯ ∂v⟩
                                                                                ¯ ω dβ.
                                                                          R
                               (0,1)                                               0
Then:
(a) (Q, D) is a densely defined, nonnegative, closed sesquilinear form; let L0 be the unique
self-adjoint operator associated with the closed form (Q, D) by the first representation theorem
(Kato, Perturbation Theory, Thm VI.2.1); all statements below refer to this L0 (the realization
with the maximal form domain — nothing below requires the minimal one).
(b) For u ∈ dom(L0 ), L0 u = −∆u distributionally, where −∆u is understood in divergence form
−eΦ0 ∂j (e−Φ0 g j k̄ ∂k̄ u), which for u ∈ C 2 equals −g j k̄ uj k̄ by Lemma 10.1(c).
(c) ker L0 = C1, and 1⊥ reduces L0 with spec(L0 |1⊥ ) ⊆ [1, ∞).

Proof. (a) Density: Cc∞ ⊂ D is dense in L2 (β) (β finite with smooth positive density). Closedness:
                         ¯ k → α in L2 , then both convergences hold in L1 of the charts
if uk → u in L2 (β) and ∂u              (0,1)                                      loc
(densities locally bounded below), so ∂u¯ = α distributionally and u ∈ D. (b) Test Q(u, v) =
⟨L0 u, v⟩ with v ∈ Cc∞ and integrate by parts in ζ (Lebesgue measure, compact support); then
apply Lemma 10.1(c). (c) Q(u) = 0 ⇒ ∂u      ¯ = 0 ⇒ u ∈ HΦ ∩ L2 = C (as in Theorem 10.5).
                                                                0
1 ∈ dom(L0 ), L0 1 = 0, and ⟨L0 u, 1⟩ = Q(u, 1) = 0, so 1⊥ reduces L0 . For u ∈ D ∩ 1⊥ , Theorem
10.5 gives Q(u) ≥ Varβ (u) = ∥u∥2 ; by the variational characterization, spec(L0 |1⊥ ) ⊆ [1, ∞).


Theorem 10.7 (pinching, eigenfunction, regularity, exact masses).
  Let u0 := λ∗p − n ∈ L2 (β). Then:
(i) Varβ (λ∗ ) = E0 (λ∗ ) = c = n+2
                                 n
                                    .
(ii) u0 ∈ dom(L0 ) and L0 u0 = u0 ; equivalently ∆λ∗ + λ∗ = n distributionally.

                                                   24
(iii) There is up ∈ C ω (T ) with up = λ∗p m-a.e., solving ∆up +up = n classically, with 0 ≤ up ≤ n+1
on T and Eβ [up ] = n, Varβ (up ) = E0 (up ) = c.
(iv) up (p) = 0 and dup (p) = 0.
                     λn
(v) m({up < λ}) =        for all λ ∈ [0, n + 1]; every level set {up = λ} is m-null; and
                    n!
m Dλ (p) △ {up < λ} = 0 for all λ ∈ (0, n + 1).
                                                               n−1
Proof. (i) By (E1)/(F4) the law of λ∗ under β is (n+1)
                                                 nλ                                  ∗
                                                      n dλ on [0, n + 1]; hence Eβ [λ ] =
          (n+1)n+1                            2
   n
(n+1)n ·    n+1    = n and Varβ (λ∗ ) = n(n+1)    2    n                            ∗
                                          n+2 − n = n+2 = c. By Theorem 9.6, λ ∈ D with
E0 (λ∗ ) ≤ c; by Theorem 10.5, c = Var ≤ E0 ≤ c.
    (ii) u0 ∈ D ∩ 1⊥ with ∥u0 ∥2 = Varβ (λ∗ ) = c = Q(u0 ). Let µ be the spectral measure of
                                                                                        1/2
L0 |1⊥ at u0 ; supp µ ⊆ [1, ∞) by Lemma 10.6(c), u0 lies in the form domain = dom(L0 ), so
              1/2
Q(u0 ) = R∥L0 u0 ∥2 =R t dµ by the second representation theorem (Kato, Thm VI.2.23), and
                        R

∥u   2
R 02∥ = dµ. Hence (t − 1) dµ = 0 with t − 1 ≥ 0 2on the R support, so µ = c δ{1} ; in particular
  t dµ = c < ∞, so u0 ∈ dom(L0 ), and ∥(L0 − 1)u0 ∥ = (t − 1)2 dµ = 0, i.e. L0 u0 = u0 . There
is no essential-spectrum escape: the extremizer is an explicit vector in the form domain and the
spectral calculus converts saturation into a genuine eigenvector. By Lemma 10.6(b), −∆u0 = u0
distributionally.
     (iii) u0 is a weak (Hloc          0
                                          ¯ 0 ∈ L2 and u0 real, so both ∂x - and ∂θ -derivatives lie in
                            1 , since u , ∂u
                                                 loc
L2loc ) solution of the linear divergence-form elliptic equation −∂j (e−ϕ g j k̄ ∂k̄ u0 ) = e−ϕ u0 . In the
real coordinates (x, θ) this is the scalar equation
                          −∂xj e−ϕ ϕjk ∂xk u0 − 14 ∂θj e−ϕ ϕjk ∂θk u0 = e−ϕ u0 ,
                                                                    

with no first-order terms: using ∂ζj = ∂xj − 2i ∂θj , the antisymmetric second-order cross terms
∂xj ∂θk −∂θj ∂xk cancel against the symmetric ϕjk , and the first-order cross term 2i j,k ∂xj (e−ϕ ϕjk ) ∂θk u0
                                                                                       P

vanishes because j ∂xj (e−ϕ ϕjk ) = 0 for each k — the differential identity of Lemma 10.1(b).
                    P
             ¯ 2 = ϕjk (ux ux + 1 uθ uθ ) for real u.) This is a genuine scalar divergence-form
(Likewise |∂u|  ω0          j   k    4 j k
equation on R2n , uniformly elliptic on compacts. Coefficients are real-analytic: ϕ ∈ C ∞ strictly
convex (P1/Caffarelli), and det D2 ϕ = e−ϕ is an analytic, elliptic-at-ϕ equation, so ϕ ∈ C ω by
the classical analyticity theorem for nonlinear analytic elliptic equations (E. Hopf 1932; Morrey,
Multiple Integrals, Thm 6.7.6). Interior L2 -regularity and bootstrap give u0 ∈ C ∞ , then C ω by
the linear analytic-regularity theorem (Morrey–Nirenberg). Set up := u0 + n: then up = λ∗ β-a.e.
(⇔ m-a.e.), and ∆up + up = n classically. Since 0 ≤ λ∗ ≤ n + 1 (F5) and β has full support
(positive smooth density), continuity forces 0 ≤ up ≤ n + 1 everywhere. E[up ] = n, Var = E0 = c
carry over from (i).
                                                                                     2
     (iv) For λ ∈ (0, n + 1), Pλ (p) = −∞ by the (P3) bound Pλ ≤ λ log |z−p|     r02
                                                                                       + M0 on B(p, r0 ),
so p ∈ Dλ := {Pλ < Φ0 }, which is open (Pλ usc, Φ0 continuous). By (F5), {λ∗ > λ} ⊆ Cλ , i.e.
Dλ ⊆ {λ∗ ≤ λ}. Hence up ≤ λ a.e. on the open set Dλ , so by continuity and full support up ≤ λ
on Dλ ; in particular up (p) ≤ λ for every λ > 0, so up (p) ≤ 0; with up ≥ 0, up (p) = 0. As an
interior minimum of a C 1 function, dup (p) = 0.                                           S
     (v) Let F (λ) := m({up < λ}), nondecreasing and left-continuous ({up < λ} = λ′ <λ {up <
λ′ }). By (E1)/(F4) and up = λ∗ a.e., F (λ) = λn /n! for all λ outside a countable set N . For
arbitrary λ ∈ (0, n + 1] pick λk ↑ λ, λk ∈    / N : left-continuity gives F (λ) = lim λnk /n! = λn /n!;
F (0) = 0 trivially. The right limit inf λ′ >λ F (λ′ ) = λn /n! likewise, so m({up = λ}) = 0 for every
λ. Finally {λ∗ < λ} ⊆ Dλ ⊆ {λ∗ ≤ λ} (F5) plus null levels give m(Dλ △{up < λ}) = 0.

Commutation identities and KE traces
All identities are verified in the global log frame (where g is the real matrix ϕjk (x)), a single
chart covering every point — which suffices, since all subsequent computations are performed in

                                                    25
that frame; the contracted combinations appearing below are in fact tensorial, because by (K1)
they arise as coefficients of tensorial commutators.
Lemma 10.8. For smooth functions u, (1, 0)-fields W , (0, 1)-forms γ:
(K0) Mixed second covariant derivatives of functions are plain: ∇j ∇k̄ u = ∂j ∂k̄ u; and [∇l̄ , ∇k̄ ] = 0
on (1, 0)-forms and on (0, 1)-forms (Kähler: curvature is type (1, 1)); in particular (∂γ)             ¯
                                                                                                         k̄l̄ =
∇k̄ γl̄ − ∇l̄ γk̄ .
(K1) [∇j , ∇k̄ ] γl̄ = − ∂j Γ̄m̄    γ , and [∇j , ∇k̄ ]W m = Rj k̄ m l W l with Rj k̄ m l = −∂k̄ Γm
                                  
                              k̄l̄ m̄                                                             jl .

(K2) (KE traces) g k̄j ∂j Γ̄k̄q̄ l̄ = −δl̄q̄ and Rj k̄ j l (= Rlk̄ ) = glk̄ .

Proof. (K0): direct computation using that only pure-type Christoffels are nonzero; precisely,
for a (1, 0)-form w: ∇k̄ wm = ∂k̄ wm and ∇l̄ (∇k̄ wm ) = ∂l̄ ∂k̄ wm − Γ̄l̄q̄k̄ ∂q̄ wm , symmetric in (¯l, k̄).
For a (0, 1)-form γ, antisymmetrizing ∇l̄ ∇k̄ γm̄ in (¯l, k̄) leaves − ∂l̄ Γ̄k̄r̄ m̄ − ∂k̄ Γ̄l̄r̄m̄ γr̄ + Γ̄l̄q̄m̄ Γ̄k̄r̄ q̄ −
                                                                                                   

Γ̄k̄q̄ m̄ Γ̄l̄q̄
            r̄ γ ; substituting Γ̄r̄ = g rp̄ ∂ g
                 
                   r̄             k̄m̄        k mp̄ , the second-derivative terms of the first bracket cancel
by symmetry of partials, and the remaining first-derivative terms match the second bracket
after ∂g −1 = −g −1 (∂g)g −1 and relabelling — so the commutator vanishes (equivalently: the
curvature of a Kähler metric is of type (1, 1), so its (0, 2)-part acting on (0, 1)-forms is zero).
(K1): expanding as in (K0), all terms cancel except the derivative of the Christoffel; e.g. for W :
∇j ∇k̄ W m − ∇k̄ ∇j W m = −(∂k̄ Γm              l
                                         jl )W . (K2): work in the real frame. First, Rlk̄ = −∂k̄ Γlm =
                                                                                                                    m

−∂l ∂k̄ log det G = glk̄ (§10.0); the fully lowered tensor Rj k̄lm̄ = −∂j ∂k̄ glm̄ + g p̄r (∂k̄ grm̄ )(∂j glp̄ )
has the Kähler symmetries j ↔ l, k̄ ↔ m̄ (using ∂j glp̄ = ∂l gj p̄ etc.), so both traces equal Ricci,
giving Rj k̄ j l = Rlk̄ = glk̄ . For the first trace: writing Γqkl = ϕqm ϕmkl ,
                      X                               hX            i
                          ϕkj ∂xj ϕqm ϕmkl = ϕqm           ϕkj ϕmklj − ϕqa tr Φa Φ−1 Φl Φ−1 ,
                                                                                                   

                   j,k                                    k,j

                                          ϕ ϕkjl = ∂xl log det Φ′′ = −ϕxl once more,
                                        P kj
where (Φa )bj := ϕabj . Differentiating
                             X
                                ϕkj ϕkjlm = −ϕlm + tr Φm Φ−1 Φl Φ−1 ,
                                                                     


and the two trace terms cancel, leaving ϕqm (−ϕlm ) = −δlq .


The boundary divergence formula and the Morrey–Kohn–Hörmander identity
(KE form)

Smoothed boxes. For R > log 2n set ρR (x) := log ni=1 exi −R + e−xi −R : smooth, convex
                                                       P                  

(log-sum-exp of affine functions), with ρR (0) < 0 and ρR+1 = ρR − 1. Let

                                          DR := {z ∈ T : ρR (x(z)) < 0}.

(Below, DR denotes these smoothed torus boxes; the polyannuli     n of Sections 5–6, for which
                                                  |x   |−R
                                                            P AxRi −R
the same symbol was used, do not reappear.) From e   j     ≤ i (e      + e−xi −R ) ≤ 2n e|x|∞ −R
one gets the sandwich

                                max |xj | − R ≤ ρR (x) ≤ |x|∞ − R + log 2n,
                                  j

which proves DR ⋐ T , {|x|∞ < R − log 2n} × Tn ⊆ DR , and DR ↑ T . Moreover ∂DR is smooth:
on {ρR = 0}, ∇x ρR ̸= 0 since a smooth convex function has nonvanishing gradient on any level
set above its minimum. The complex Hessian of ρ := ρR (x) is ρj k̄ = ∂x2j xk ρ ≥ 0 (convexity): DR
is pseudoconvex with Levi form ≥ 0 on all of Tz Cn , not just complex-tangentially.

                                                                26
Lemma 10.9 (divergence and flux). For a C 1 (1, 0)-field U on D, D = DR :
                Z                      Z
                       j                                  dSeuc (x) dθ
                   ∇j U dV = Fl(U ) :=      detG U j ρxj               ,
                 D                      ∂D                  |∇x ρ|

and the conjugate identity for (0, 1)-fields with ρk̄ = ρxk . Here ∇j U j = (det G)−1 ∂j (det G U j )
(contracted Christoffel = ∂ log det G).
                                    1
Proof. D ∇j U j dV = D̃ ∂xj + 2i      ∂θj (det G U j ) dx dθ with D̃ = {ρR (x) < 0} × Tn ; the θ-
       R                R               

derivatives integrate to zero by periodicity (no boundary in θ), and the x-part is the flat
Gauss–Green theorem on the smooth domain {ρR < 0} ⊂ Rnx , for each θ.

The Hilbert complex on D. Let H0 := L2 (D, dV ), H1 := L2(0,1) (D, ω0 , dV ), H2 :=
L2(0,2) (D, ω0 , dV ) (form norms as in §10.0, the (0, 2)-norm carrying the factor 12 ), and let
T = ∂¯0 : H0 → H1 , S = ∂¯1 : H1 → H2 be the maximal (distributional) closed ex-
tensions; Cc∞ ⊂ domains, so both are densely defined, and ran T ⊆ ker S (distributionally
∂¯2 = 0, and ∂(T ¯ u) = 0 ∈ L2 ). For γ smooth on D: by Lemma 10.9,
                         Z                Z
                  ¯
             ⟨γ, ∂f ⟩ =    W ∂j f dV = − (∇j W j )f¯ dV + Fl(W f¯),
                             j   ¯                                      W j := g k̄j γk̄ ,
                       D                     D

so a smooth γ lies in dom(T ∗ ) only if (and, by Friedrichs graph-density, in fact iff)

                                           W j ρj = 0 on ∂D                                      (Neu)

and then T ∗ γ = −∇j W j = −g k̄j ∇j γk̄ , which is also the interior distributional formula for T ∗ on
all of dom(T ∗ ) (test with f ∈ Cc∞ (D)).
    Necessity of (Neu): write h := W j ρj and dσ ′ := det G dSeuc        |∇
                                                                            (x) dθ
                                                                            x
                                                                                                  ¯
                                                                              ρ| , so that Fl(W f ) =
     h f¯ dσ ′ . If γ ∈ dom(T ∗ ), then for all f ∈ C ∞ (D),
R
 ∂D
                      Z
                            h f¯ dσ ′ ≤ ∥T ∗ γ∥L2 (D) + ∥∇j W j ∥L2 (D) ∥f ∥L2 (D) .
                                                                       
                       ∂D

Take fδ := hext η(ρ/δ), where hext ∈ C ∞ (D)R extends ′h|∂D
                                                                        ∞
                                                           R and η2 ∈ ′C (R), η(0) = 1, η ≡ 0 on
(−∞, −1], 0 ≤ η ≤ 1. Then f¯δ |∂D = h̄, so ∂D h f¯δ dσ = ∂D |h| dσR is independent of δ, while
∥fδ ∥2L2 (D) ≤ ∥hext ∥2∞ voldV ({−δ < ρ < 0}) → 0 as δ ↓ 0. Hence ∂D |h|2 dσ ′ = 0, i.e. h ≡ 0
on ∂D. (A purely normal concentration is essential here — isotropically shrinking bumps do
not violate boundedness for n ≥ 2; the collar functions fδ concentrate in the normal direction
only. This characterization of dom(T ∗ ) is classical: Chen–Shaw, Partial Differential Equations
in Several Complex Variables, Lemma 4.2.1.)
Lemma 10.10 (MKH identity, KE form). Let γ be a (0, 1)-form, smooth on D, satisfying
                               ¯
(Neu). Put Sk̄l̄ := ∇k̄ γl̄ (= ∇γ). Then
                                       Z
  ¯   2     ∗     2          2   ¯  2                                     dSeuc dθ
 ∥∂γ∥ + ∥T γ∥ = ∥γ∥ + ∥∇γ∥ +                ρj k̄ W j W k dσ, dσ := det G          ≥ 0, (MKH)
                                         ∂D                                |∇x ρ|

with all norms in L2 (D, dV ) and ρj k̄ = ∂x2j xk ρ ≥ 0. In particular the boundary term is ≥ 0.

Proof. Write A := ∥T ∗ γ∥2 = (∇j W j )(∇k W k ) dV = (∇j W j )(∇k̄ W k ) dV .
                            R                       R

   Step 1. Integrate by parts in ∇k̄ (Lemma 10.9, conjugate): the flux density is

          det G(∇j W j )W k ρk̄ /|∇ρ| = det G(∇j W j )W k ρk /|∇ρ| = 0 on ∂D by (Neu).

Hence A = − (∇k̄ ∇j W j )W k dV .
           R


                                                   27
   Step 2. Commute (Lemma 10.8, (K1)) and trace (K2): ∇k̄ ∇j W j = ∇j ∇k̄ W j − Rj k̄ j l W l =
∇j ∇k̄ W j − glk̄ W l . Therefore
                                       Z
                                  A = − (∇j ∇k̄ W j )W k dV + ∥γ∥2 .

    Step 3. Integrate by parts in ∇j with U j := (∇k̄ W j )W k :
            Z                                 Z
         − (∇j ∇k̄ W )W dV = −Fl(U ) + (∇k̄ W j ) (∇j̄ W k ) dV =: −Fl(U ) + C.
                       j   k


    Step 4 (boundary term). Let h := W j ρj ∈ C ∞ (D); by (Neu), h|∂D = 0. The complex
field W̄ := W k ∂k̄ satisfies W̄ (ρ) = W k ρk = 0 on ∂D (ρ real), i.e. W̄ is tangent to ∂D; hence
W̄ (h)|∂D = 0. Expanding W̄ (h) = W k (∇k̄ W j )ρj + W j ρj k̄ (mixed Hessian of ρ is tensorial),
                                                             

on ∂D:
                                                                       Z
            j                  j              j
                      k
           U ρj = W (∇k̄ W )ρj = −ρj k̄ W W      k   =⇒ −Fl(U ) =          ρj k̄ W j W k dσ.
                                                                            ∂D

     Step 5 (the crossed term). ∇k̄ W j = g m̄j Sk̄m̄ and ∇j̄ W k = ∇j W k , so C = ⟨S, S t ⟩
(transpose pairing), and with S = S s +S a (symmetric/antisymmetric parts — pointwise Hermitian-
orthogonal: the pairing is invariant under simultaneous transposition of both arguments, so
⟨S s , S a ⟩ = ⟨(S s )t , (S a )t ⟩ = −⟨S s , S a ⟩ = 0),
                                         C = ∥S s ∥2 − ∥S a ∥2 .
        ¯                            a                                                   1    ¯ 2 1   a 2
Since (∂γ)  k̄l̄ = Sk̄l̄ − Sl̄k̄ = 2Sk̄l̄ and the (0, 2)-form norm carries the factor 2 , ∥∂γ∥ = 2 ∥2S ∥ =
2∥S a ∥2 . Adding,
                                                                      Z
                          ¯     2             2        s 2      a 2
                                                                            ρj k̄ W j W k dσ,
                                                                    
                         ∥∂γ∥ + A = ∥γ∥ + ∥S ∥ + ∥S ∥ +
                                                                   ∂D
which is (MKH) since ∥∇γ∥   ¯ 2 = ∥S∥2 = ∥S s ∥2 + ∥S a ∥2 . Positivity of the boundary term:
         2
ρj k̄ = ∂xj xk ρR ≥ 0 as a matrix.

Lemma 10.11 (graph density; classical, cited). Forms smooth on D and belonging to
dom(T ∗ ) are dense in dom(T ∗ ) ∩ dom(S) for the graph norm γ 7→ ∥γ∥ + ∥T ∗ γ∥ + ∥Sγ∥.
                                                      ¯
    This is the classical graph-density lemma of the ∂-Neumann     theory (Chen–Shaw, Partial
Differential Equations in Several Complex Variables, Lemma 4.3.2; Folland–Kohn, The Neumann
Problem for the Cauchy–Riemann Complex ; going back to Hörmander 1965): its proof is local
(partition of unity, tangential mollification — here available globally in (x, θ) with θ-periodic
convolution — plus the normal-component correction near ∂D), and requires only a smooth
compact boundary and smooth hermitian data up to the boundary, both of which hold here.
Corollary 10.12 (closed MKH inequality). For every γ ∈ dom(T ∗ ) ∩ dom(S): the distribu-
       ¯ (in D) lies in L2 (D), and
tional ∇γ
                                 ∥Sγ∥2 + ∥T ∗ γ∥2 ≥ ∥γ∥2 + ∥∇γ∥
                                                            ¯ 2.                                     (‡1)
Proof. Take smooth γν → γ in graph norm (Lemma 10.11); being smooth on D and in dom(T ∗ ),
each γν satisfies (Neu) (by the necessity direction above), so (MKH) applies to it. By (MKH),
 ¯ ν ∥2 ≤ ∥Sγν ∥2 + ∥T ∗ γν ∥2 , bounded; extract ∇γ
∥∇γ                                               ¯ ν ⇀ η in L2 (D). Since ∇¯ is first order with
                                     2
smooth coefficients and γν → γ in L , η = ∇γ¯ distributionally in D. Pass to the limit in (MKH)
                                       ¯
using weak lower semicontinuity of ∥∇ · ∥ and dropping the boundary term (≥ 0).
   Remark. In particular (‡1) yields the basic estimate (‡0) of Lemma 10.13 below with
constant exactly 1, uniformly in R — the coefficient ∥γ∥2 comes from Ric(ω0 ) = ω0 (KE
normalization) and the sign of the boundary term from ρj k̄ ≥ 0; the saturation argument of
Theorem 10.14 depends on this uniformity.


                                                   28
Abstract lemma (Neumann solution with potentials)

Lemma 10.13. Let H0 , H1 , H2 be Hilbert spaces, T : H0 → H1 , S : H1 → H2 closed densely
defined with ran T ⊆ ker S, and suppose

                        ∥γ∥2 ≤ ∥T ∗ γ∥2 + ∥Sγ∥2            ∀ γ ∈ dom(T ∗ ) ∩ dom(S).                              (‡0)

Then for every α ∈ ker S there exists γ⋆ ∈ dom(T ∗ ) ∩ ker S such that v := T ∗ γ⋆ satisfies T v = α,
v is the minimal-norm solution of T v = α, and

                           ∥v∥2 = ⟨α, γ⋆ ⟩,       ∥γ⋆ ∥ ≤ ∥α∥,           ∥v∥ ≤ ∥α∥.

Proof. Let h := ker S (closed), α ∈ h. Since ran T ⊆ h, h⊥ ⊆ (ran T )⊥ = ker T ∗ ; hence the
orthogonal projection P onto h preserves dom(T ∗ ) and T ∗ P = T ∗ on dom(T ∗ ) (for γ ∈ dom(T ∗ ),
γ ′′ = (I − P )γ ∈ ker T ∗ ). In particular dom(T ∗ ) ∩ h is dense in h. On h, the form q(γ) := ∥T ∗ γ∥2 ,
domain dom(T ∗ ) ∩ h, is closed (T ∗ closed, h closed) and, by (‡0) with Sγ = 0, q(γ) ≥ ∥γ∥2 . Its
self-adjoint operator Λ ≥ 1 is boundedly invertible; set γ⋆ := Λ−1 α, so ∥γ⋆ ∥ ≤ ∥α∥, and for all
δ ∈ dom(q): ⟨T ∗ γ⋆ , T ∗ δ⟩ = ⟨α, δ⟩. Let v := T ∗ γ⋆ ; for w ∈ dom(T ∗ ), writing w = w′ + w′′ as
above: ⟨v, T ∗ w⟩ = ⟨v, T ∗ w′ ⟩ = ⟨α, w′ ⟩ = ⟨α, w⟩ (since α ⊥ h⊥ ). Hence v ∈ dom(T ∗∗ ) = dom(T )
and T v = α. v ∈ ran T ∗ ⊆ (ker T )⊥ , so v is minimal. Finally ∥v∥2 = q(γ⋆ ) = ⟨Λγ⋆ , γ⋆ ⟩ =
⟨α, γ⋆ ⟩ ≤ ∥α∥ ∥γ⋆ ∥ ≤ ∥α∥ ∥v∥ (using ∥γ⋆ ∥2 ≤ q(γ⋆ ) = ∥v∥2 ), so ∥v∥ ≤ ∥α∥.


The Matsushima theorem: holomorphy of the gradient field
                                                                    ¯ (smooth), and
Theorem 10.14 (Matsushima). Let u := up be as in Theorem 10.7, α := ∂u

                                  Vp := grad1,0
                                            ω0 up ,         Vpj := g k̄j ∂k̄ up .

Then:

                 ¯ p (with the convention ω0 = ig dζ j ∧ dζ̄ k ; authors normalizing the gradient as
   1. ιVp ω0 = i ∂u                                   j k̄
      −iVp obtain ιω0 = ∂u ¯ p ; nothing below depends on this factor); pointwise |Vp |2 = |∂u
                                                                                             ¯ p |2 ,
                                                                                       ω0         ω0
      hence              Z
                                                             n
                            |Vp |2ω0 dβ = E0 (λ∗p ) = c =        ̸= 0;  Vp (p) = 0.
                          T                                n + 2

   2. ∆up + up = n (already Theorem 10.7(ii); restated for completeness).

   3. (Holomorphy.) ∂V     ¯ p = 0, i.e. each component Vpj is holomorphic on T ; equivalently
        0,2                        ¯
      ∇ up ≡ 0. Moreover the ∂-Neumann           potentials of the exhaustion converge, γR ⇀ ∂u¯ p
                 2
      weakly in Lloc (full sequence; the limit form is smooth), and the integrated Bochner identity
      (⋆) holds:

            ∥∂¯β∗ α∥2L2 (β) − ∥α∥2L2 (β) = ∥∂V
                                            ¯ p ∥2 2
                                                 L (β) (= c − c = 0),               div Vp := ∇j Vpj = n − up .

                                                                           ¯ Pointwise, |V |2 = g V j V k =
Proof. (1) ιV (i gj k̄ dζ j ∧ dζ̄ k ) = i V j gj k̄ dζ̄ k = i uk̄ dζ̄ k = i∂u.                 ω0      j k̄
                 ¯ 2 (real frame: ϕjk ϕlj ϕmk u um = ϕml u um ). Integrate and use Theorem 10.7(i,iii).
g k̄j uj uk̄ = |∂u|  ω0                               l̄              l̄
Vp (p) = 0 since dup (p) = 0 (Theorem 10.7(iv)).
      (3) Work in L2 (dV ); recall E = (2π)n V c, and by Theorem 10.7(i,iii):
       Z
            |α|2ω0 dV = (2π)n V E0 (λ∗ ) = E,            min ∥u − c1 ∥2L2 (dV ) = (2π)n V Varβ (λ∗ ) = E.   (‡2)
        T                                         c1 ∈C


                                                      29
   Step 1 (Neumann data on DR ). On each DR (the smoothed boxes defined after Lemma 10.9)
apply Lemma 10.13 with T = ∂¯0 , S = ∂¯1 (maximal extensions); (‡0) holds by Corollary 10.12
and its Remark,R with constant 1 uniformly in R. Since α|DR ∈ ker S (distributional restriction)
with ∥α∥2R := DR |α|2 dV ≤ E, we obtain γR ∈ dom(T ∗ ) ∩ ker ∂¯1 and the minimal solution
               ¯ R = α on DR , with
vR = T ∗ γR of ∂v

                   PR := ∥vR ∥2L2 (DR ) = ⟨α, γR ⟩R ≤ ∥α∥2R ,      ∥γR ∥R ≤ ∥α∥R .                 (‡3)

By Corollary 10.12 with ∂¯1 γR = 0:

                            PR = ∥T ∗ γR ∥2 ≥ ∥γR ∥2R + ∥∇γ
                                                         ¯ R ∥2 2
                                                              L (DR ) .                            (‡4)

     Step 2 (saturation forced by pinching). Claim: PR → E. Upper bound: PR ≤ ∥α∥2R ≤ E.
Lower bound: along any subsequence, a further subsequence gives vR ⇀ w weakly in L2 (DS , dV )
                                                             ¯ = α on T (distributional limits
for every S (uniform bounds (‡3), diagonal extraction), with ∂w
           ∞                      2
against Cc test forms) and ∥w∥L2 (T ) ≤ lim inf PR (lsc on each DS , then S → ∞ by monotone
convergence). Now ∂(w ¯ − u) = 0 distributionally, so w − u is a.e. holomorphic (Weyl); and
it lies in L (dV ) — note L2 (dV ) = L2 (e−Φ0 µΩ ) by Lemma 10.1(a), with u ∈ L2 (dV ) because
            2

0 ≤ up ≤ n + 1 and dV (T ) = (2π)n V < ∞ — so by rank-one (Lemma 10.6(c), applied in the
equivalent weighted space) w − u is constant; so by (‡2), ∥w∥2 ≥ E. Thus lim inf PR ≥ E along
every subsequence, proving the claim; moreover then ∥α∥2R → E as well (PR ≤ ∥α∥2R ≤ E, and
∥α∥2R ↑ E by monotone convergence). From (‡3), ∥γR ∥R ≥ PR /∥α∥R , so with (‡4):

                           ¯ R ∥2 2                  PR2
                          ∥∇γ   L (DR ) ≤ PR −            −→ E − E = 0.                            (‡5)
                                                    ∥α∥2R

    Step 3 (limit potential). By (‡3), extract a subsequence with γR ⇀ γ and vR ⇀ w weakly
in L2 (DS ) for every S (and, by Step 2, w = u − c0 for some constant c0 ). For any compactly
supported smooth (0, 2)-type test tensor φ on T (support in some DS ):
                               ¯ ∗ φ⟩ = lim⟨γR , ∇
                           ⟨γ, ∇                 ¯ ∗ φ⟩ = lim⟨∇γ
                                                              ¯ R , φ⟩ = 0
                                         R                 R

by Cauchy–Schwarz and (‡5) (here ∇γ¯ R is the L2 (DR ) object of Corollary 10.12, which represents
                   ¯
the distributional ∇γR in the interior). Hence
                                   ¯ = 0 on T (distributions).
                                   ∇γ                                                              (‡6)

Also, testing T ∗ against Cc∞ : vR = −g k̄j ∇j γR,k̄ distributionally in the interior, so in the limit

                      u − c0 = w = −g k̄j ∇j γk̄ = −∇j W j ,      W j := g k̄j γk̄ .               (‡7)

     Step 4 (regularity of γ). From (‡6): for every smooth compactly supported (0, 1)-test ψ,
⟨γ, ∇¯ ∗ ∇ψ⟩
         ¯     = 0, i.e. γ ∈ L2loc solves the second-order system ∇ ¯ ∗ ∇γ
                                                                        ¯ = 0 in the very weak
                                                      0,1 2
(distributional) sense; its principal symbol is |ξ |ω0 · Id > 0 for real ξ =  ̸ 0 — diagonal to
                                                              ω
principal order — so the system is elliptic with smooth (C ) coefficients. Since γ is a priori only
L2loc (not Hloc1 ), we invoke hypoellipticity of elliptic operators with smooth coefficients

acting on distributions (parametrix construction; Hörmander, The Analysis of Linear Partial
Differential Operators I–III — elliptic operators are hypoelliptic, and the principal part here is
scalar): γ ∈ C ∞ (T ), and then (‡6) holds classically.
     Step 5 (identification Vp = W , holomorphy). With γ smooth, differentiate (‡7):

           ∂l̄ u = −∇l̄ ∇j W j = −∇j ∇l̄ W j − [∇l̄ , ∇j ]W j = −∇j ∇l̄ W j + Rj l̄ j m W m .
                                                                          


                                                  30
By (‡6), ∇l̄ W j = g k̄j ∇l̄ γk̄ = 0; by (K1)–(K2), Rj l̄ j m W m = gml̄ W m ; hence

                      ul̄ = gml̄ W m ,      i.e.     Vpj = g l̄j ul̄ = W j ,       ¯ p.
                                                                               γ = ∂u

Therefore ∂l̄ Vpj = ∇l̄ W j = 0: Vp is holomorphic, and equivalently ∇0,2 up = ∇           ¯ ∂u ¯ p = ∇γ
                                                                                                      ¯ =0
(the equivalence is the identity ∂k̄ V j = g l̄j ∇k̄ ∇l̄ u, proved by expanding ∂k̄ (g l̄j ul̄ ) with ∂k̄ g l̄j =
−g l̄m (∂k̄ gmq̄ )g q̄j and recognizing the barred Christoffel).
     Step 6 (the identities in (3)). divVp = ∇j Vpj = g k̄j ∇j uk̄ = ∆up = n − up (Theorem 10.7(ii));
comparing with (‡7) also fixes c0 = n — a consistency check. Finally, ∂¯β∗ α = L0 u0 = −∆up =
up − n (with u0 := up − n) (Lemma 10.6, Theorem 10.7), so ∥∂¯β∗ α∥2L2 (β) = Varβ (λ∗ ) = c,
∥α∥2L2 (β) = E0 = c, and ∥∂V     ¯ p ∥2 = ∥∇0,2 up ∥2 = 0: (⋆) holds with both sides equal to 0. (Also,
every weak limit point of (vR ) was identified as up − n and of (γR ) as ∂u   ¯ p ; a bounded sequence
with a unique weak limit point converges weakly, so the full sequences converge.)

Remark. Rank-one (lattice hypothesis) entered three times: Theorem 10.5; ker L0 = C; and Step
2 of Theorem 10.14 (identification of all limit solutions as u − const). The centroid hypothesis
entered only through (P1) (existence of the KE potential, Ric = ω0 ), which produced the exact
constant 1 in (MKH) and in Hörmander. Extremality (τ = n + 1) entered through (E1)–(E2)
via Theorem 9.6 and the pinching, which is what forces the saturation (‡5): the Levi flux of
the smooth approximants and the ∇-energy   ¯          are squeezed to zero by the spectral
equality — this is the rigorous form of “flux terms vanish along subsequences”, with no cutoff at
infinity required.


The model case (n = 1) revisited
                                                         |w|               2
Model: K = S, ω0 = (n + 1)ωF S on Pn ⊃ T , up = (n + 1) 1+|w|2.


                                     nλ               n−1                 n
   1. Law and moments. (E1): density (n+1) n on [0, n + 1]; E = n, Var = n+2 = c. n = 1:

       uniform on [0, 2], E = 1, Var = 31 . n = 2: density 2λ                         1
                                                            9 on [0, 3]: E = 2, Var = 2 = c.

   2. Eigen-equation, sign and eigenvalue. Model: gj k̄ (0) = (n + 1)δjk , u ≈ (n + 1)|w|2
                              1 P
      near w = 0, so ∆u(0) = n+1   j (n + 1) = n and u(0) = 0: ∆u + u = n; equivalently
      L0 (u − n) = −∆(u − n) = u − n: eigenvalue exactly 1 (consistent with Lemma 10.6’s
      L0 = −∆ and Theorem 10.5’s spectral gap at 1).

   3. Energy and gradient field (n = 1). |∂u|      ¯ 2 = u(2−u) ; with u uniform on [0, 2]: E0 =
                                                     ω0        2
      R 2 u(2−u) du
       0     2    2 = 1
                      3 = c = Var   (Theorem   10.7  pinching    saturated). V = grad1,0 u = w∂w :
                                          2|w|2        u(2−u)
      holomorphic, V (p) = 0; |V |2ω0 = (1+|w|                ; |V |2 dβ = 13 = c; divV = ∆u =
                                                                 R
                                               2 )2 =     2
      1 − u = n − u (at w = 0: 1 = n).
                                                                                      u u
   4. Hessian identities. The model Hessian identity uj k̄ = n+1−u          j k̄
                                                              n+1 gj k̄ − n+1−u gives ∆u = n−u
      and, with the law, |∇ u| dβ = (∆u)2 dβ (for n = 2: 19 E[(3 − 2u)2 + (3 − u)2 ] = 12 =
                          R 1,1 2       R

      E[(2 − u)2 ]), consistent with (MKH) (no extra curvature term between ∥∇1,1 u∥2 and
                                          ¯ 2 = c − c = 0: exactly (⋆) and Theorem 10.14(3).
      ∥∆u∥2 ), while ∥∇0,2 u∥2 = ∥∆u∥2 − ∥∂u∥

   5. Hörmander constant. Torus-invariant test functions in Theorem 10.5, transported by
      Lemma 10.1(e), reproduce the real Brascamp–Lieb inequality with constant 1.


This completes the proofs of Theorems 10.5, 10.7 and 10.14. The classical results cited in this
section are the Hörmander–Demailly weighted L2 estimate with constant 1 [Demailly CADG

                                                       31
VIII, Thm (6.1); Hörmander 1965], Kato’s representation theorems for closed forms [Kato VI.2.1,
VI.2.23], interior and analytic elliptic regularity (Morrey–Nirenberg; Morrey; Hopf; Hörmander),
                                               ¯
and the graph-norm density lemma for the ∂-Neumann         complex on smoothly bounded domains
[Hörmander 1965, Prop. 1.2.4; Folland–Kohn; Chen–Shaw], the last of which is the only cited
input specific to the boundary theory (its hypotheses — smooth compact boundary, smooth data
up to the boundary — hold for the smoothed boxes DR ).


11       Rigidity: the Laurent-mode structure of the eigenfunctions
         and the identification K = A(S)
This section completes the equality case. The logical chain is: 11A (the Laurent-mode structure
of up : representation, finite window, functional equations, supporting hyperplanes, spanning) →
11B (the unique base-zero theorem, the log-affine rigidity of ∇ϕ∗ , balance, integrality, exclusion
of products, and the conclusion K = A(S)).

11A. The Laurent-mode structure of up
Throughout this subsection u = up , Vp = grad1,0 up (holomorphic, by Theorem 10.14), v j :=
Vpj ∈ O(T ) with Laurent coefficients cjm , cm = (c1m , . . . , cnm ), Λ = Λ(p) := {m : cm =
                                                                                           ̸ 0},
σm (x) := ⟨m, x⟩, y = ∇ϕ(x), M (y) := D2 ϕ∗ (y), N := n + 1.


11A-I. Mode representation  R and pinning Theorem 11A.1 (representation). For every
m ∈ Zn let ûm (x) := (2π)−n u e−i⟨m,θ⟩ dθ. Then there are constants bm ∈ C with

                      ûm (x) = eσm (x)/2 ℓm (∇ϕ(x)),       ℓm (y) := ⟨cm , y⟩ + bm ,

and moreover b0 = n, c0 ∈ Rn , while for m ̸= 0

                             bm = −⟨m, cm ⟩,        ℓm (y) = ⟨cm , y − m⟩.

Also û−m = ûm , hence the pair relation

                         ℓ−m (y) = eσm (x) ℓm (y)        (y = ∇ϕ(x), x ∈ Rn ).                  (PR)

Proof. u ∈ C ω , 0 ≤ u ≤ N , so ûm ∈ C ∞ , |ûm | ≤ N . We use the following modewise calculus,
valid for w ∈ C 1 (Rn × Tn ): (∂\ xk w)m = ∂xk ŵm (differentiation under the integral, locally
           \
uniform); (∂                                               n
             θk w)m = imk ŵm (integration by parts on T ); multiplication by a θ-independent
                                                         ′
g(x) commutes with b· m ; and if w = m′ Am′ (x)ei⟨m ,θ⟩ converges normally on compacts then
                                       P
ŵm = Am (termwise integration and orthogonality). Laurent series of holomorphic functions on
(C∗ )n converge normally on compacts, so these rules apply to v j and, since ∆ = ϕjk (x) ∂xj −
 i
   ∂θ ∂x + i ∂θ , they give the commutation (∆u)  [ ei⟨m,θ⟩ = ∆ ûm ei⟨m,θ⟩ used below. From
                                                                           
2    j    k   2   k                                       m
                                             x
Vp = grad1,0 u: uk̄ = ϕjk v j . In ζj = 2j + iθj , ∂ζ̄k = ∂xk + 2i ∂θk ; mode extraction gives
  ∂xk − m2k ûm = ϕjk (x)cjm eσm /2 , i.e. ∇x e−σm /2 ûm = D2 ϕ(x) cm = ∇x ⟨cm , ∇ϕ⟩. Since Rn is
                                                        

connected, e−σm /2 ûm = ⟨cm , ∇ϕ⟩ + bm .
     Pinning: write ûm ei⟨m,θ⟩ = Gm (x)e   ⟨m,ζ⟩                            e⟨m,ζ⟩ is holomorphic,
          ⟨m,ζ⟩     jk
                                             ⟨m,ζ⟩, Gm = ℓm ◦ ∇ϕ. l Since
∆ Gm e          = ϕ ∂j ∂k Gm + mj ∂k Gm e           . Now ∂k Gm = ϕkl cm , ϕ ∂j ∂k Gm = clm ϕjk ϕjkl =
                                                                            jk

clm ∂xl log det D2 ϕ = −⟨cm , ∇ϕ⟩, and ϕjk mj ϕkl clm = ⟨m, cm ⟩. The mode-m part of ∆u = n − u is
−ûm for m =  ̸ 0 (resp. n−û0 ), whence −⟨cm , ∇ϕ⟩+⟨m, cm ⟩ = −⟨cm , ∇ϕ⟩−bm , i.e. bm = −⟨m, cm ⟩;
for m = 0, b0 = n, and reality of u forces c0 real. (PR) is û−m = ûm rewritten.


                                                    32
Corollary 11A.2. Λ := {m : cm =   ̸ 0} satisfies Λ = −Λ; qm := ℓm ℓ−m is, on intK, real-valued
with qm = e |ℓm | = |ûm | ∈ [0, N 2 ]; hence qm is a real quadratic polynomial, 0 ≤ qm ≤ N 2
           σm    2        2

on K, and |ℓm ◦ ∇ϕ| ≤ CK,m e−σm , |ûm | ≤ CK,m e−σm /2 with CK,m = supK |ℓ−m |.

Proof. If cm ̸= 0 then ûm ̸≡ 0 (ℓm nonconstant affine cannot vanish on the open set intK), so
û−m = ûm ̸≡ 0; if c−m = 0 then also b−m = −⟨−m, c−m ⟩ = 0 (the pinning identity of Theorem
11A.1, valid for every nonzero mode), so û−m ≡ 0 — contradiction; hence c−m ̸= 0. From
(PR), qm = eσm |ℓm |2 ≥ 0 and = |ûm |2 ≤ N 2 on intK; a polynomial real on an open set has real
coefficients. Finally |ℓm | = e−σm |ℓ−m | ≤ CK,m e−σm .


11A-II. The window: Λ is finite Theorem 11A.3. Λ ⊆ 2K ∩ Zn ; in particular |Λ| ≤
#(2K ∩ Zn ) < ∞.

Proof. Let m ∈ Λ \ {0}. Taking real or imaginary parts of ℓm , there exist a ∈ Rn \ {0}, b ∈ R
with
                        |⟨a, ∇ϕ(x)⟩ + b| ≤ N e−σm (x)/2   (x ∈ Rn ).                 (11A.2.1)
(If Re cm = 0 use Im; a nonzero constant is impossible in (11A.2.1).) Let Hs := {⟨m, x⟩ ≥ s}.
Since ∇ϕ is a diffeomorphism with (∇ϕ)# (e−ϕ dx) = dy|K ,

                                                                           2N (diamK)n−1 −s/2
      Z
             e−ϕ dx = ∇ϕ(Hs ) ≤ {y ∈ K : |⟨a, y⟩ + b| ≤ N e−s/2 } ≤                     e
        Hs                                                                       |a|

(the set on the right lies in a slab of width 2N e−s/2 /|a| orthogonal to e := a/|a|; by Fubini its
volume is at most that width times supt Hn−1 (K ∩ {⟨e, y⟩ = t}), and each section, convex of
diameter ≤ diam K, lies in an (n − 1)-cube of side diam K, so Hn−1 ≤ (diamK)n−1 ). Conversely,
let ξ be any unit vector with ⟨m, ξ⟩ > 0 and set xs := s+|m|
                                                           ⟨m,ξ⟩ ξ. The unit ball B1 (xs ) ⊆ Hs , and
on it hK ≤ (s+|m|)h
               ⟨m,ξ⟩
                    K (ξ)
                          + h̄ with h̄ := max|w|≤1 hK (w). Using ϕ ≤ ϕ(0) + hK ,
                          Z                                               
                                e−ϕ dx ≥ cn e−ϕ(0)−h̄ exp − (s+|m|)h
                                                                ⟨m,ξ⟩
                                                                     K (ξ)
                                                                             .
                           Hs

Comparing the exponential rates as s → ∞ forces hK (ξ)/⟨m, ξ⟩ ≥ 12 , i.e. ⟨m, ξ⟩ ≤ 2hK (ξ) —
for every unit ξ with ⟨m, ξ⟩ > 0; for units with ⟨m, ξ⟩ ≤ 0 the inequality is trivial (hK > 0 as
0 ∈ intK). Thus ⟨m, ξ⟩ ≤ h2K (ξ) for all ξ, i.e. m ∈ 2K.

Theorem 11A.4 (nontriviality). Λ \ {0} ̸= ∅.

Proof. If not, u = û0 = n + ⟨c0 , ∇ϕ(x)⟩. Then u ≥ 0 means ⟨c0 , y⟩ ≥ −n on the open set
intK = ∇ϕ(Rn ), and u(p) = 0 means the affine function ⟨c0 , ·⟩ attains the value −n — its infimum
over the open set int K — at the interior point ∇ϕ(L(p)), where L(p) := (log |p1 |2 , . . . , log |pn |2 )
denotes the log coordinates of p. An affine function attaining an interior minimum is constant,
so c0 = 0; but then u ≡ n, contradicting u(p) = 0 ̸= n.


                                                   33
11A-III. The functional equations; supporting hyperplanes; rows of D2 ϕ∗                 Theorem
11A.5. Let m ∈ Λ \ {0}. Then:

   1. ℓm has no zero in intK, and cm = eiχm am with am ∈ Rn \ {0} (real phase).

   2. With Λm (y) := εm ⟨am , y − m⟩ > 0 on intK (εm = ±1),

                                         Λ−m (y)
                             eσm (y) =           ,        σm (y) = ⟨m, ∇ϕ∗ (y)⟩,              (FE)
                                         Λm (y)

      and qm = Λm Λ−m ≤ N 2 on K.

   3. inf intK Λ±m = 0; hence Hm := {y : ⟨am , y⟩ = ⟨am , m⟩} is a supporting hyperplane of K
      containing the lattice point m. In particular m ∈    / intK: Λ \ {0} ⊆ (2K \ intK) ∩ Zn .

   4. Row formula: on intK,
                                                                    ε−m a−m   ε m am
               D2 ϕ∗ (y) m = ∇y log Λ−m (y) − ∇y log Λm (y) =               −        .       (ROW)
                                                                    Λ−m (y)   Λm (y)

Proof. (1) By Corollary 11A.2, qm = ℓm ℓ−m is a real quadratic, and qm ̸≡ 0 (both factors are
nonzero affine forms, by cm ̸= 0 and Corollary 11A.2). Conjugating, ℓ̄m ℓ̄−m = ℓm ℓ−m ; by
unique factorization in C[y], ℓ̄m is a scalar multiple of ℓm or of ℓ−m . Case (i): ℓ̄m = µℓm .
Conjugating again gives |µ| = 1; choosing χm with e2iχm = µ̄ makes e−iχm ℓm real — i.e. ℓm is a
real form times a phase, as claimed. (This covers the degenerate subcase ℓ−m ∝ ℓm , where both
alternatives reduce to case (i).) Case (ii): ℓ̄m = νℓ−m with ℓm not proportional to a real form.
Then ℓ−m = λℓ̄m (λ = ν −1 ), and (PR) reads λℓ̄m = eσm ℓ̄m on int K, so eσm ≡ λ off the zero set
of ℓ̄m , hence everywhere by continuity — contradicting that σm = ⟨m, ∇ϕ∗ (y)⟩ is unbounded on
int K (∇ϕ∗ is onto Rn ). So case (i) holds: ℓm = eiχm Lm , Lm = ⟨am , y − m⟩ real affine; likewise
— the dichotomy applied to −m, whose case (ii) (ℓ̄−m ∝ ℓm ) is, after conjugation, the same
proportionality as the case (ii) just excluded — ℓ−m = eiχ−m L−m with L−m real affine. Then
(PR) reads eiχ−m L−m = eσm e−iχm Lm ; with L±m real and eσm > 0, the phase factor must be
±1, so eσm = ±L−m /Lm on intK off zeros. If Lm (y 0 ) = 0, y 0 ∈ intK, finiteness and positivity
          0
of eσm (y ) force L−m (y 0 ) = 0; two affine hyperplanes meeting intK in the same nonempty set
coincide, giving L−m = cLm and eσm constant — contradiction. So L±m =        ̸ 0 on intK; fixing
                                      σ
signs ε±m and using positivity of e yields (FE), and qm = Λm Λ−m .
                                       m

     (3) σm is unbounded above on intK while Λ−m is bounded on K; by (FE), inf Λm = 0,
attained on K̄; since Λm > 0 on intK and vanishes exactly on Hm , Hm supports K̄, and
Λm (m) = 0, i.e. m ∈ Hm . A supporting hyperplane misses intK, so m ∈         / intK. The same
argument applied to −m (using unboundedness of σ−m = −σm ) gives inf intK Λ−m = 0 and the
supporting hyperplane H−m ∋ −m.
     (4) Differentiate (FE): ∇y σm = D2 ϕ∗ (y)m.

    (The next two propositions are consequences of (FE)/(ROW) that are not needed for the proof
of the main theorem.)
Proposition 11A.6 (difference identity). For m ∈ Λ \ {0} set

         fm := eσm ⟨M (y)−1 cm , c̄m ⟩ = eσm ⟨M (y)−1 am , am ⟩ (≥ 0, continuous on intK),

and f0 := ⟨M −1 c0 , c0 ⟩. Then, pointwise on intK,

                    fm − f−m = −Λm (y) ε−m ⟨a−m , m⟩ − Λ−m (y) εm ⟨am , m⟩

— an affine function, bounded on K. In particular fm is bounded (resp. ν-integrable for any finite
measure) iff f−m is.

                                                     34
Proof. From (ROW), εm am = e−σm ε−m a−m −Λm M m. Insert in ⟨M −1 am , am ⟩, expand, multiply
by eσm , use eσm Λ2m = Λm Λ−m and κm := ⟨M m, m⟩ = ε−mΛ⟨a−m
                                                         −m ,m⟩
                                                                − εm ⟨a
                                                                      Λm
                                                                        m ,m⟩
                                                                              , and note e−σm =
 σ
e −m .

Proposition 11A.7 (cage relations). For all m, m′ ∈ Λ \ {0}, symmetry of D2 ϕ∗ and (ROW)
give the rational identity on intK
                 ε−m ⟨a−m , m′ ⟩ εm ⟨am , m′ ⟩   ε−m′ ⟨a−m′ , m⟩ εm′ ⟨am′ , m⟩
                                −              =                −              .
                     Λ−m             Λm              Λ−m′             Λm′
Matching simple poles: for m′ ̸= ±m, either ⟨am , m′ ⟩ = 0 or Hm ∈ {Hm′ , H−m′ }.

Proof of the pole matching. Three ingredients. (a) Both sides of the displayed identity are global
rational functions of y agreeing on the open set intK, hence identical on Rn (off the pole locus).
(b) Hm ̸= H−m — so there is no internal cancellation between the two terms of one side: if
Hm = H−m then m, −m ∈ Hm (pinning), hence 0 = 12 (m + (−m)) ∈ Hm , impossible since Hm
supports K and 0 ∈ intK; likewise Hm′ ̸= H−m′ . (c) Now suppose Hm ∈    / {Hm′ , H−m′ }; multiply
the identity by Λm and let y → y , where y ∈ Hm \ (H−m ∪ Hm′ ∪ H−m′ ) — such y 0 exists
                                     0         0

since a hyperplane is not covered by finitely many other hyperplanes. The left side tends to
−εm ⟨am , m′ ⟩ and the right side to 0; hence ⟨am , m′ ⟩ = 0.

   Moreover, by Parseval and (∇ϕ)# (e−ϕ dx) = dy|K ,
                      Z                 X Z                      n
                         ⟨c0 , y⟩2 dy +       Λm Λ−m dy =           V.
                           K                                    n+2
                                         m∈Λ\0 K

                                                           −n −ϕ(x) dx dθ (Lemma 10.1(a) with
                         R −ϕ (i) In the chart, m = (2π) e
Proof of the Parseval identity.
µΩ = dx dθ), so m(T ) = e dx = V . (ii) u is real-analytic and nonconstant (a constant would
contradict the exact law of Theorem 10.7(v)), so {u = N } is a proper analytic subset, m-null;
                                                                            λn−1
with the exact law m({u < λ}) = λn /n! on [0, N ], the law of u under m is (n−1)! dλ, whence

                         N n+1                                    N n+2         n(n + 1)2
        Z                                     Z
            u dm =                   = nV,         u2 dm =                    =           V.
                     (n + 1)(n − 1)!                          (n + 2)(n − 1)!     n+2

                           in θ plus Tonelli: u2 dm = m |ûm |2 e−ϕ dx, and each term equals
                                                R          P R
(iii)
R Fiberwise Parseval    2     σm |ℓ |2 = q (y) is a function of y alone (by (PR)) and by the
  K qm dy since |ûm | = e         m         m                                               R
pushforward; the sum      is  finite by  the  window (Theorem 11A.3). (iv) For m = 0: K (n +
⟨c0 , y⟩)2 dy = n2 V + K ⟨c0 , y⟩2 dy, the cross term vanishing by b(K) = 0. Subtracting n2 V from
                        R
                      2
(ii) and using n(n+1)     2      n
                                                                        R        R
                 n+2 −n = n+2 yields the display. (As a byproduct, u dm = K (n+⟨c0 , y⟩)dy =
nV matches (ii), consistent with the chart normalization.)


11A-IV. Degeneracy exclusion:      then active modes span Lemma 11A.8 (spanning).
For every p ∈ T : spanR Λ(p) \ {0} = R .

Proof. Suppose W := spanR (Λ(p) \ {0}) has dim W = n − d with d ≥ 1 (the case Λ \ {0} = ∅ is
excluded by Theorem 11A.4). The θ-dependence of up is entirely through the characters ei⟨m,θ⟩ ,
m ∈ Λ(p) ⊆ W (Theorem 11A.1, with normal convergence of the mode series on compacts). Let

                        T⊥      iβ   1 n                         ◦
                         W := {e ∈ (S ) : ⟨m, β⟩ ∈ 2πZ ∀m ∈ Λ(p)} ,

the identity component of the annihilator subtorus; since the subgroup of Zn generated by Λ(p)
has rank ≤ n − d (for integer vectors, rank of the generated subgroup = dimension of the real

                                                  35
span), the annihilator is a closed subgroup of (S 1 )n with Lie algebra ⊇ W ⊥ , so dim T⊥W ≥ d ≥ 1.
Then up is invariant under the (isometric, Φ0 -preserving) action of TW : for e ∈ T⊥
                                                                               ⊥      iβ
                                                                                             W , the
continuous functions up (x, θ + β) and up (x, θ) of θ ∈ Tn have identical Fourier coefficients
(ûm 7→ ei⟨m,β⟩ ûm = ûm on the support Λ(p) ∪ {0} of the Fourier expansion — modes with cm = 0,
m= ̸ 0, vanish by pinning), hence are equal. By invariance and up (p) = 0, up vanishes identically
on the orbit O := p · T⊥                                               ′         ⊥
                         W , a compact embedded torus of dimension d = dim TW ≥ 1 (the rotation
action is free). Since moreover up ≥ 0, every point of O is a minimum: dup = 0 on O. Taylor
expansion with a uniform second-derivative bound on a compact tubular neighborhood gives
up ≤ C dist(·, O)2 there: with q the nearest point of O to z, up (z) ≤ 12 ∥D2 up ∥L∞ |z − q|2 , the
segment qz staying within distance |z − q| of O. Hence
                                                         p
                        {up < λ} ⊇ {z : dist(z, O) < λ/C}            (λ small).

The right side is a tube of radius r = λ/C about the compact d′ -manifold O. In the flat chart,
                                         p

O = {xp }×(θp +T⊥                                  n     p                   p   ⊥
                     W ), and the r-tube contains Br/2 (x )×{θ : distTn (θ, θ +TW ) < r/2}, of dx dθ-
                      ′
measure ≥ c rn · rn−d (any two smooth metrics are bi-Lipschitz on the compact neighborhood,
so the choice of dist is immaterial); since m has a smooth positive density there, its m-mass is
          ′                ′
≥ c0 r2n−d = c0 (λ/C)n−d /2 for small r. But m({up < λ}) = λn /n! exactly (Theorem 10.7), and
     ′
λn−d /2 /λn → ∞ as λ ↓ 0 when d′ ≥ 1: contradiction.

To summarize: for every p the active set Λ(p) ⊆ (2K \ intK) ∩ Zn ∪ {0} is finite, spans Rn ,
                                                                

and carries the exact functional equations (FE)/(ROW) with supporting hyperplanes of K at
lattice points.

11B. Conclusion of the equality case: from the spanning modes to K = A(S)

11B-A. Zeros of up : the unique base-zero theorem Theorem 11B.1 (unique base-
zero). u−1                             0 0
        p (0) = {p}. Moreover at p = (x , θ ), in the chart (x, θ),

                  uxx (p) = 12 D2 ϕ(x0 ),    uxθ (p) = 0,    uθθ (p) = 2D2 ϕ(x0 ).
                                                       x                       1
Proof. (1) Laplacian in the chart. With ζj = 2j + iθj one has ∂ζj = ∂xj + 2i     ∂θj , ∂ζ̄k =
       1                                                                    jk
∂xk − 2i ∂θk , hence (the mixed terms cancel against the symmetric ϕ ):
                                                                        
                             ∆u = ϕjk ∂ζ2j ζ̄k u = ϕjk uxj xk + 14 uθj θk .

(Cf. the n = 1 model in §11B-J.1.) At any zero q = (xq , θq ) of u: u(q) = 0 is a minimum of
u ≥ 0, so ∇u(q) = 0, the full (2n) × (2n) Hessian Hq ⪰ 0, and ∆u(q) = n − u(q) = n, i.e. with
Φ := D2 ϕ(xq ) and blocks A = uxx (q), B = uθθ (q), C = uxθ (q):

                                    tr(Φ−1 A) + 41 tr(Φ−1 B) = n.                         (11B:A.1)

    (2) Nondegeneracy of every zero. Suppose Hq e = 0 for√a unit vector e. Since u is smooth,
u(q + te) ≤ C3 |t|3 , and for nonnegative C 2 functions |∇u| ≤ 2M u holds on a neighbourhood
of q, with M := supB(q,2ρ) ∥D2 u∥ for a fixed small ρ > 0: for y ∈ B(q, ρ) with ∇u(y) ̸= 0, Taylor
along w := ∇u(y)/|∇u(y)| gives 0 ≤ u(y − tw) ≤ u(y) − t|∇u(y)| + M            2
                                                                           2 t for 0 ≤ t ≤ ρ, and the
choice t = |∇u(y)|/M — admissible (≤ √      ρ) near q since ∇u(q) = 0 — yields the bound. Hence
for |t| ≤ ε1 λ 1/3          ⊥
                   and s ∈ e with |s| ≤ ε2 λ,
                                                  p
                         u(q + te + s) ≤ C3 |t|3 + 2M C3 |t|3 |s| + M    2
                                                                    2 |s| < λ

for small fixed ε1 , ε2 . So {u < λ} contains a tube of Lebesgue measure ≥ c λ1/3 · λ(2n−1)/2 =
cλ n−1/6 ; since m has a locally positive smooth density, m({u < λ}) ≥ c′ λn−1/6 , and n − 61 < n
contradicts the exact law λn /n! as λ ↓ 0. Hence Hq ≻ 0 at every zero; zeros are isolated.

                                                 36
    (3) Local mass. Fix a finite set q1 , . . . , qN of zeros. By smoothness, u ≤ 12 ⟨Hqi σ, σ⟩ + Ci |σ|3
in local coordinates σ near qi ; hence on the ellipsoid Ei (λ, ε) := { 12 ⟨(Hqi + εI)σ, σ⟩ < λ} one
has u ≤ 21 ⟨(Hqi + εI)σ, σ⟩ − 2ε |σ|2 + Ci |σ|3 < λ provided |σ| ≤ ε/(2Ci ) — which holds on all
                                                     p
of Ei (λ, ε) for λ small, since Ei (λ, ε) ⊆ {|σ| ≤ 2λ/ε}. Thus for every ε > 0 and all small λ,
{u < λ} contains the ellipsoids Ei (λ, ε), pairwise disjoint for small λ (the zeros are isolated),
of Lebesgue volume ω2n (2λ)n det(Hqi + εI)−1/2 , ω2n = π n /n!. Using the density asymptotics
                           q
e−ϕ(x)            e−ϕ(x i )                                       n
(2π)n = (1 + o(1)) (2π)n on Ei (λ, ε), dividing the exact law by λ , letting λ ↓ 0, then ε ↓ 0:

                                     N      q
                                     X e−ϕ(x i )       2n ω2n    1
                                                     ·p        ≤    .                               (11B:A.2)
                                            (2π)n      det Hqi   n!
                                      i=1

    (4) Determinant bound from (11B:A.1) and KE. By Fischer’s inequality for psd
block matrices, det Hq ≤ det A det B. By AM–GM applied to the eigenvalues of Φ−1/2 AΦ−1/2
(resp. B): det A ≤ (a/n)n det Φ, det B ≤ (4b/n)n det Φ, where a := tr(Φ−1 A), b := 14 tr(Φ−1 B),
                                                                                       q
a + b = n by (11B:A.1). Hence, using ab ≤ n2 /4 and the KE equation det Φ = e−ϕ(x ) :
                                                (ab)n                  q
                                det Hq ≤ 4n        2n
                                                      (det Φ)2 ≤ e−2ϕ(x ) .                         (11B:A.3)
                                                 n
                                                                    n
Plugging (11B:A.3) into (11B:A.2): each summand is ≥ 2(2π)ω2n   1
                                                            n = n! , so N ≤ 1. Since u(p) = 0, p

is the unique zero; equality throughout forces a = b = n/2, C = 0, A = 21 Φ, B = 2Φ.

    (Theorem 11B.1 independently reproves Lemma 11A.8: a rank-deficient Λ would produce a
positive-dimensional torus of zeros.)


11B-B. The canonical log-affine representation of ∇ϕ∗ and the root patterns Lemma
11B.2 (independence). Let ℓ1 , . . . , ℓr be affine functions (write nα := ∇ℓα ̸= 0) with pairwise
distinct zero hyperplanes Hα = {ℓα = 0} ⊂ Rn , all ℓα > 0 on a nonempty open set U (so that the
logarithms are defined). Then {1, log ℓ1 , . . . , log ℓr } and {1/ℓ1 , . . . , 1/ℓr } (together with constants)
are linearly independent over R as functions on U (also with vector or matrix coefficients,
componentwise).
               P                                                                  Q
Proof. If c0 + cα log ℓα ≡ 0 on U , take gradients          and multiply by β ℓβ : a polynomial identity
on U , hence on Rn . Restrict to a point of Hα Q
                                                       S
                                                     \ β̸=α Hβ (nonempty: a hyperplane is not a finite
union of proper affine subsets of itself): cα nα β̸=α ℓβ = 0 there with the product ̸≡ 0 on Hα , so
cα = 0; then c0 = 0. The 1/ℓα case is identical.

Theorem 11B.3 (representation and patterns). There are finitely many pairwise distinct
supporting hyperplanes H1 , . . . , Hr of K (r ≤ 2n), affine ℓα > 0 on int K with Hα = {ℓα = 0},
vectors wα ∈ Rn \ {0} and κ ∈ Rn with
                                              r
                                              X
                               ∗
                           ∇ϕ (y) = κ +             wα log ℓα (y)       (y ∈ int K),                (11B:B.1)
                                              α=1

and this representation is unique (given the normalization of the ℓα ; rescalings are absorbed into
κ). Moreover {Hα } = {H±m : m ∈ Λ(p) \ 0} — in particular each Hα contains a lattice
point of 2K ∩ Zn — and for every m ∈ Λ(p) \ {0} there are indices α(m) ̸= α(−m) with
                                 
                                 −1, α = α(m)
                                 
                      ⟨m, wα ⟩ = +1, α = α(−m)            Hα(±m) = H±m .                 (11B:B.2)
                                 
                                    0,    else,
                                 


                                                       37
Proof. By Lemma 11A.8 choose a basis m(1) , . . . , m(n) ∈ Λ \ 0 with dual
                                                                      P basis ξ1 , . . . , ξn . By (FE)
                         (i)  ∗                                    ∗
                                                                                                      
(Theorem 11A.5(2)), ⟨m , ∇ϕ ⟩ = log Λ−m(i) −log Λm(i) , so ∇ϕ = i ξi log Λ−m(i) −log Λm(i) ,
which has the form (11B:B.1) with hyperplane list the distinct elements of {H±m(i) } (write
α(±m) for the index of the list with Hα(±m) = H±m ; each Λ±m = t±m ℓα(±m) with t±m > 0,
and the constants log t±m go into κ); a priori some coefficients could be 0. Uniqueness: given
two representations (11B:B.1) with possibly different lists and nonzero coefficient vectors, first
normalize the affine forms of coinciding hyperplanes to agree (rescalings shift constants into
κ), then subtract and apply Lemma 11B.2 componentwise to the merged family of distinct
hyperplanes on a small ball U ⊂ int K where all forms are positive: the coefficient of every
hyperplane appearing in only one list must vanish — contradicting nonzeroness — and the shared
coefficients and κ agree. By Theorem 11A.5(3) each listed H supports K and contains its lattice
point ±m(i) . Note Hm =   ̸ H−m always: otherwise Λ−m = cΛm and (FE) makes eσm constant,
impossible since σm = ⟨m, ∇ϕ∗ ⟩ is onto R (∇ϕ∗ is onto Rn ).
    Now take any m ∈ Λ \ 0 and match coefficients in (FE) against (11B:B.1) using Lemma 11B.2
applied to the union family {ℓα } ∪ {ℓH±m }: if Hm (or H−m ) were not in the list, the coefficient
of its log on the two sides would be 0 = −1 (resp. 0 = +1), absurd; hence H±m are in the list
and (11B:B.2) holds, together with ⟨m, κ⟩ = log(t−m /tm ). In particular wα ̸= 0 for every listed
α (each listed α is some α(±m(i) ), and ⟨m(i) , wα(m(i) ) ⟩ = −1).

Corollary 11B.4 (symmetry implies collinearity). Write nα := ∇ℓα . Then wα = γα nα
with γα ̸= 0, so
                                           X            nα nTα
                    M (y) := D2 ϕ∗ (y) =           γα          ,        and {nα } spans Rn .
                                               α
                                                        ℓα (y)

Proof. Differentiating (11B:B.1), M = α wα nTα /ℓα . Symmetry of M = D2 ϕ∗ plus Lemma
                                            P
11B.2 (for {1/ℓα }, matrix coefficients) gives wα nTα = nα wαT for each α, i.e. wα ∥ nα ; γα ̸= 0 since
                                     ∗    ∗
wα ̸= 0. Spanning: det M = e⟨y,∇ϕ ⟩−ϕ > 0 somewhere, and ran M ⊆ span{nα }.

    (Differentiating (11B:B.1) recovers (ROW) and Proposition 11A.7 — consistency with the
established facts.)


11B-C. Monge–Ampère rigidity: balance, integer exponents, polynomial identity
Let dα := ℓα (0) > 0 (centroid 0 ∈ int K). Integrating (11B:B.1):
                                       X
                     ϕ∗ (y) = ⟨κ, y⟩ +
                                                           
                                          γα ℓα log ℓα − ℓα + C on int K. (11B:C.1)
                                           α
                                                                                    ∗   ∗
Since ⟨nα , y⟩ − ℓα = −dα , the Legendre/KE relation det M = e⟨y,∇ϕ ⟩−ϕ becomes, on int K,
                   Y         X Y                 Y             P       Y
 P (y) := det M ·     ℓα =            γα det(nA )2    ℓα = e−C e α γα ℓα   ℓα1−γα dα , (11B:C.2)
                    α       |A|=n    α∈A                      α∈A
                                                               /                            α

using Cauchy–Binet; P is a polynomial, P > 0 on int K.
Lemma 11B.5   Q (exp-affine vs. polynomial). Let P ̸≡ Q     0 be a polynomial, L affine, eα ∈ R,
with P = eL α ℓαeα on a nonempty open subset U of { ℓα =          ̸ 0} on which every ℓα > 0
(distinct hyperplanes; the positivity makes  the real powers well  defined). Then ∇L = 0, and
                                        L
                                          Q kα
eα = kα := ordℓα P ∈ Z≥0 , and P = e       ℓα globally.
                   Q kα
Proof. Write P = ℓα Q, ℓα ∤ Q. Logarithmic differentiation and clearing denominators give
the polynomial identity
                   Y          X           Y             Y         X          Y
               ∇Q      ℓα + Q     k α nα    ℓβ = Q ∇L     ℓα + Q      e α nα   ℓβ ,
                        α        α         β̸=α                     α           α           β̸=α


                                                         38
valid on U , hence on Rn . Since ℓα ∤ Q, Q does not vanish identically on Hα (in affine coordinates
with ℓα = y1 , a polynomial vanishing identically on {y1 = 0} is divisible by y1 ); so generic
points of Hα — off the other Hβ and off {Q = 0} — exist, and restricting there yields kα = eα .
Subtracting, ∇Q = Q ∇L with ∇L =: v constant; if v =     ̸ 0 then deg(Qv) = deg Q > deg ∇Q —
impossible; so v = 0, ∇Q = 0, and Q is a nonzero constant.
                                         r
                                         X               X
Theorem 11B.6. (i) Balance:                   γα nα =        wα = 0; consequently r ≥ n + 1. (ii)
                                        α=1              α
kα := 1 − γα dα ∈ Z≥0 , and kα ̸=Q1 (else γα = 0); so for each α: either kα = 0, γα = 1/dα > 0,
or kα ≥ 2, γα < 0. (iii) P = c0 α ℓkαα identically, c0 > 0.

           P Lemma 11B.5 to (11B:C.2) (on a small ball in int K, where all ℓα > 0): the affine
Proof. Apply
exponent      γα ℓα − C must have zero gradient — this is (i) — andPthe exponents 1 − γα dα must
                        integers kα ,Pgiving (ii),(iii)                −C+ α γα dα > 0 (by (i) the affine
be the nonnegative
         P                                         P with c0 = e
function     γα ℓα is the constant     γα ℓα (0) =      γα dα ). kα ̸= 1 since kα = 1 would give γα dα = 0
with dα > 0, i.e. γα = 0, excluded. r ≥ n + 1: the nonzero wα span and satisfy the nontrivial
relation (i), which n linearly independent vectors cannot.


                                                              S
11B-D. K is a polytope Theorem 11B.7. ∂K ⊆                        α Hα and
                                              r
                                              \
                                       K=         {y : ℓα (y) ≥ 0};
                                              α=1

in particular K is a polytope, every facet hyperplane of K is one of the Hα , and every facet
hyperplane of K contains a point of 2K ∩ Zn .

Proof. ∇ϕ∗ : int K → Rn is a homeomorphism        (inverse of ∇ϕ), hence proper: yk → y ∗ ∈ ∂K ⇒
     ∗                ∗                                                                    ∇ϕ∗ (yk ) is
                                 S
|∇ϕ (yk )| → ∞. If y ∈ ∂K \ Hα , all S      log ℓα (yk ) stay bounded, so by (11B:B.1) T
bounded — contradiction. Hence ∂K ⊆ Hα . Each Hα supports K, so K ⊆ P := {ℓα ≥ 0}.
Conversely if z ∈ P \ K, the segment [0, z] (0 ∈ int K) exits K at some y ∗ ∈ ∂K strictly before z;
then y ∗ ∈ Hα0 for some α0 , and ℓα0 is affine with ℓα0 (0) > 0, ℓα0 (y ∗ ) = 0, hence ℓα0 (z) < 0, i.e.
z∈/ P — contradiction.
                  S      If a facet F of K, with hyperplane HF , had HF =     ̸ Hα for every α, then
relint F ⊂ ∂K ⊆ α Hα would be covered by the finitely many sets HF ∩Hα of dimension ≤ n−2
— impossible, since relint F has positive Hn−1 -measure while those sets are Hn−1 -null. So each
facet hyperplane equals some Hα , which contains a lattice point m ∈ 2K ∩ Zn by Theorem
11B.3.


11B-E. Relation  P classes: K is a product of simplex cells, and every Hα is a facet Let
R := {c ∈ Rr : α cα wα = 0}; dim R = r − n, and 1 ∈ R by balance. DefinePα ∼ α′ iff cα = cα′
for all c ∈ R; let C1 , . . . , Ck be the classes, Wj := span{wα : α ∈ Cj }, Vj := i̸=j Wi , Uj := Vj⊥
(annihilator), nj := dim Wj ≥ 1, rj := |Cj |.
TheoremL11B.8. (a) For every mL      ∈ Λ\0: α(m) ∼ α(−m) and m ∈ Uj(m) , where Cj(m) ∋ α(m).
      n                        n
(b) R = j Wj and   Pdually R = j Uj with dim Uj = nj and ⟨Wi , Uj ⟩ = 0 for i =      ̸ j. (c) Every
class is balanced:    α∈Cj w α  = 0; the only relations are class-constants, so rj = n j + 1, any nj
                                                                          P
of {wα }α∈Cj are linearly independent, and r = n + k. (d) Along y = j yj (yj ∈ Uj ), each ℓα
(α ∈ Cj ) depends only on yj ; hence K = kj=1 Kj with Kj ⊂ Uj cut out by the nj + 1 conditions
                                           Q
{ℓα ≥ 0}α∈Cj . (e) Within each class all γα have the same sign, each Kj is a nondegenerate
nj -simplex, every condition {ℓα ≥ 0} defines a facet of Kj , hence of K; i.e. every Hα is a
facet hyperplane of K.

                                                    39
                                                                                        P
Proof. (a) Pairing the pattern (11B:B.2) with a relation c ∈ R: 0 = α cα ⟨m, wα ⟩ = cα(−m) −
cα(m) ; hence α(m) ∼ α(−m), and then (11B:B.2) gives ⟨m, wβ ⟩ = 0 for all β ∈                           / Cj(m) , i.e.
m ∈ Uj(m) .
     (b) By (a) and Lemma 11A.8, Rn = span Λ ⊆ P                                    ⊥
                                                                P           T              T               P
                                                                   j Uj = ( j Vj ) , so      j Vj = 0. If    j xj = 0
with xj ∈ Wj and some          x j 0 ̸
                                     =   0,  then  x j 0  =     −          x
                                                                      j̸=j0 Lj ∈  V j 0 while  x j 0 ∈ W j0 ⊆  Vl for
                                                                               Wj = Rn (the sum is all of Rn
                          T
all l ≠ Pj0 , so xj0 ∈ Vl = 0 — contradiction. Hence
                                       n
since
P           j Wj ⊇ span{wα } = R by Corollary 11B.4); then dim Uj = n − dim Vj = nj and
P dim Uj = n. Independence of the Uj : note Wi ⊆ VjPfor i ̸= j, so ⟨Wi , Uj ⟩ = 0 for i ̸= j. If
   j uj = 0 withP uj ∈ Uj , then for any x ∈ W             0 = ⟨x, j uj ⟩ = ⟨x, uj0 ⟩; since also uj0 ⊥ Wi for
                                                      j0 : L
i≠ j0 and i Wi = Rn , uj0 = 0. Hence             R n =
                                                                j Uj , and the pairing Wj × Uj → R is perfect:
                                                           n , so x = 0; dimensions match.
                                            L
if x ∈ Wj has ⟨x,PUj ⟩ = 0, then x ⊥ P           U
                                               i i  =   R                P
     (c) Balance α wα = 0 splits as j sj = 0, sj := Cj wα ∈ Wj ; by (b), sj = 0. Every
relation is class-constant by definition of ∼; a relation supported in Cj is then t1Cj , admissible
since sj = 0. Hence relations = class-constants (dim = k, so r = n + k), and the only relation
among {wα }Cj is 1Cj : rj = nj + 1, any nj of them independent.
     (d) ℓα (y) = γα−1 (1 − kα ) + ⟨wα , y⟩ (from Theorem 11B.6(ii): γα ℓα = γα ⟨nα , y⟩ + γα dα =
⟨wα , y⟩ + 1 − kα )Qand ⟨wα , y⟩ = ⟨wα , yj ⟩ for α ∈ Cj , since wα ∈          LWj ⊥ Ui P     ̸ j). Theorem 11B.7
                                                                                           (i =
then gives K = Kj , meaning the internal direct sum K = j Kj = { j yj : yj ∈ Kj }.
     (e) K bounded ⇒ Kj bounded. The family {να }α∈Cj , να := sgn(γα )wα , positively spans Wj :
rewriting each constraint, Kj = {yj ∈ Uj : ⟨να , yj ⟩ ≥ c′α (α ∈ Cj )} with c′α := − sgn(γα )(1 − kα ).
If the closed convex cone generated by {να } were a proper subset of Wj , a separation in Wj (using
the perfect pairing Wj × Uj from (b)) would give v ∈ Uj \ {0} with ⟨να , v⟩ ≥ 0 for all α ∈ Cj ;
then Kj + R≥0 v ⊆ Kj , contradicting boundedness. A positively spanning finite family carries
                                                                                                           P (β)
a strictly positive relation: each −νβ (β ∈ Cj ) is a nonnegative combination −νβ = α sα να ;
                            P                                       P (β)
summing
P              over β gives α tα να = 0 with tα = 1 + β sα ≥ 1 > 0. Now a positive relation
    tα sgn(γα )wα = 0 must, by (c), have tα sgn(γα ) = c · 1 on Cj , forcing all signs in Cj equal.
So Kj is the intersection of the rj = nj + 1 (by (c)) half-spaces {⟨να , yj ⟩ ≥ c′α } in Uj , whose
normals
P           να are nj -wise independent (by (c), after sign flips) and carry a strictly positive relation
    µα να = 0, unique up to scale (relations among {wα }Cj areLR1Cj by (c)). Interior points are
strictly feasible: Kj has nonempty interior in Uj (else K =                      Ki would have empty interior);
if ⟨να , y ◦ ⟩ = c′α at an interior point y ◦ , moving in a direction u ∈ Uj with ⟨να , u⟩ < 0 (which
exists by the perfect pairing of (b)) stays inP          Kj for small steps    P and′ violates the constraint —
contradiction. Hence, at any interior y ◦ , 0 = µα ⟨να , y ◦ ⟩ > P               α µα cα . Vertex classification: no
point of Kj has all nj + 1 constraints active (that would give                     µα c′α = 0); every vertex of the
compact polyhedron Kj has at least nj linearly independent active constraints, hence active
set exactly Cj \ {α} for some α, and equals the unique point pα solving ⟨νβ , pα ⟩ = c′β (β =                   ̸ α).
                                     −1              ′        ′
                                         P
P ′pα satisfies ⟨να , pα ⟩ = −µα
Each                                        β̸=α µβ cβ > cα (computed from the relation; the inequality is
    µc < 0), so each pα is feasible, hence a vertex. Therefore Kj = conv{pα : α ∈ Cj } has exactly
nj + 1 vertices; full-dimensionality forces them affinely independent: Kj is a nondegenerate
nj -simplex. The face {⟨νβ , ·⟩ = c′β } ∩ Kj contains the nj affinelyL             independent vertices {pα }α̸=β ,
hence is a facet of Kj . Finally a facet F of Kj gives the facet F ⊕ i̸=j Ki of K, lying in Hβ .


11B-F. The facet sign law: γα > 0, kα = 0, all heights = −1 Lemma 11B.9 (normal
asymptotics). ϕ∗ is bounded on int K (by (11B:C.1)). If xk = tk ξˆ + O(1) with tk → ∞, |ξ|
                                                                                        ˆ = 1,
               ˆ → hK (ξ).
then ⟨∇ϕ(xk ), ξ⟩      ˆ

Proof. With yk = ∇ϕ(xk ), Legendre gives ⟨xk , yk ⟩ = ϕ(xk ) + ϕ∗ (yk ) ≥ hK (xk ) − osc ϕ∗ , using
ϕ(x) = supint K (⟨x, y⟩ − ϕ∗ ) ≥ hK (x) − sup ϕ∗ (hK (x) = supK̄ ⟨x, ·⟩ = supint K ⟨x, ·⟩). Writing
xk = tk ξˆ+ek , |ek | ≤ C, R := maxK |y|: on one side ⟨xk , yk ⟩ = tk ⟨ξ,
                                                                       ˆ yk ⟩+⟨ek , yk ⟩ ≤ tk ⟨ξ,
                                                                                               ˆ yk ⟩+CR;


                                                         40
on the other, hK (xk ) = hK (tk ξˆ + ek ) ≥ hK (tk ξ)
                                                   ˆ − hK (−ek ) ≥ tk hK (ξ)
                                                                          ˆ − CR (subadditivity and
                                    ˆ               ˆ               ∗
hK (w) ≤ |w|R). Combining, tk ⟨ξ, yk ⟩ ≥ tk hK (ξ) − 2CR − osc ϕ ; divide by tk → ∞. The upper
        ˆ yk ⟩ ≤ hK (ξ)
bound ⟨ξ,             ˆ is trivial.

Theorem 11B.10. For every α: γα > 0, hence kα = 0, γα = 1/dα , and

             γα ℓα (y) = 1 + ⟨wα , y⟩,       K = {y ∈ Rn : ⟨wα , y⟩ ≥ −1, α = 1, . . . , r},

and each Kj = {yj ∈ Uj : ⟨wα , yj ⟩ ≥ −1, α ∈ Cj }.

Proof. By Theorem 11B.8(e), Hα0 carries a facet F of K. Choose y 0 ∈ relint F not on any
other Hβ (possible: the sets Hβ ∩ Hα0 are ≤ (n − 2)-dimensional). Let yt = (1 − t)y 0 , t ∈ (0, 1];
then yt ∈ int K (segment from the interior point 0 to the boundary point y 0 ), and ℓα0 (yt ) =
(1 − t)ℓα0 (y 0 ) + t ℓα0 (0) = t dα0 ↓ 0 (affinity) while ℓβ (yt ) → ℓβ (y 0 ) > 0 for β =
                                                                                          ̸ α0 . By (11B:B.1),
                                         1
with the O(1) uniform for t ∈ (0, 2 ],

      xt := ∇ϕ∗ (yt ) = γα0 nα0 log(tdα0 ) + O(1) = t′ ξˆ + O(1),      t′ → ∞, ξˆ = − sgn(γα0 )n̂α0

(note log(tdα0 ) < 0 for small t). Applying Lemma 11B.9 along a sequence tk ↓ 0 and using
                       ˆ = hK (ξ).
ytk → y 0 gives ⟨y 0 , ξ⟩      ˆ If γα < 0, then ξˆ = +n̂α and y 0 would maximize ⟨n̂α , ·⟩ on K;
                                      0                    0                              0
but ℓα0 ≥ 0 on K with ℓα0 (y ) = 0 says y 0 minimizes it, and min < max since K has interior —
                               0

contradiction. So γα0 > 0; then kα0 = 1 − γα0 dα0 < 1 and kα0 ∈ Z≥0 force kα0 = 0, γα0 = 1/dα0 ,
and γℓ = 1 + ⟨w, ·⟩. Theorem 11B.7 finishes.

    (At this point ϕ∗ = ⟨κ̃, y⟩ + α ℓ̃α log ℓ̃α + const with ℓ̃α = 1 + ⟨wα , y⟩: an exact Guillemin
                                   P
potential with balanced data.)


11B-G. Lattice saturation and integrality of the cage
 n            n                                n   n
                                                     Lk Theorem 11B.11. (a) ZΛ(p) =
Z . (b) wα ∈ Z for all α. (c) With Lj := Uj ∩ Z : Z = j=1 Lj .

Proof. (a) L := ZΛ(p) has full rank (Lemma 11A.8; for integer vectors the rank of the generated
subgroup equals the dimension of the real span). If L ⊊ Zn , then the dual lattice satisfies
L∗ ⊋ Zn (duality of full-rank lattices), so there is θg ∈ 2πL∗ \ 2πZn , i.e. a nontrivial g =
[θg ] ∈ Tn with ⟨m, θg ⟩ ∈ 2πZ for all m ∈ Λ. By Theorem 11A.1 (pinning kills every nonzero
modeP   with cm = 0) and Theorem 11A.3 (finiteness), up is, on Rn × Tn , a finite Fourier sum
up = m∈Λ∪{0} ûm (x)ei⟨m,θ⟩ with frequencies in Λ(p) ∪ {0} (Fourier inversion for a continuous
function whose coefficients vanish off a finite set). Hence u(x, θ+θg ) = u(x, θ); so u (x0 , θ0 +θg ) =
                                                                                                      

u(p) = 0 with (x0 , θ0 + θg ) ̸= p on the torus — contradicting Theorem 11B.1.
     (b) By (11B:B.2), ⟨m, wα ⟩ ∈ {0, ±1} ⊂ Z for all m ∈ Λ; by (a) and Z-linearity, ⟨v, wα ⟩ ∈ Z
for all v ∈ Zn ; taking v = ei gives wα ∈ Zn .
                                                                                             n
P (c) Each L m ∈ Λ nlies in some Uj(m) (Theorem 11B.8(a)), hence in Lj(m) . So Z = ZΛ ⊆
   j Lj =    j Lj ⊆ Z .


                                                                                               (m + 1)m
11B-H. Exclusion of products: k = 1 Throughout this subsection set F (m) :=                             —
                                                                                                  m!
the conjectured sharp volume bound in dimension m, proved in Part I.
                                                                                                  P
Lemma
Q          11B.12 (strict superadditivity of F ). For k ≥ 2 and n1 , . . . , nk ≥ 1 with              nj = n:
  j F (nj ) < F (n).


                                                     41
                 Qm                          1 i
Proof. F (m) =     i=1 ei with ei := (1 + i ) , by telescoping. ei is strictly increasing (AM–GM on i
                                         1/(i+1)
copies of 1 + 1i and one 1: (1 + 1i )i                  1
                                       
                                                 < 1 + i+1 , strict as factors differ). Hence for a, b ≥ 1:
                             Pa+b                Pa
log F (a + b) − log F (b) = i=b+1 log ei > i=1 log ei = log F (a), i.e. F (a + b) > F (a)F (b);
induct on k.

Theorem 11B.13. k = 1; hence r = n + 1.

Proof. Suppose P  k ≥ 2. First,Prank Lj = nj and Uj = spanR Lj : by Theorem 11B.11(c),
n = rank Zn = j rank Lj ≤ j dim UjL= n, so equality holds termwise. Concatenating Z-
bases of the Lj gives a Z-basis of Zn =         Lj ; let Ψ ∈ GLn (Z) be the unimodular linear map
sending it to the standard basis arranged in coordinate blocks Rn1 × · · · × Rnk ; then | det Ψ|     Q = 1,
Ψ(Zn ) = Zn , Ψ(Uj ) = Rnj -block, Ψ(Lj ) = Znj -block. By Theorem 11B.8(d), ΨK = j Kj′ ,
Kj′ := ΨKj ⊂ Rnj , a convex body (product facts used below: the interior of a product is the
product of interiors; the centroid is computed factorwise by Fubini; volume is multiplicative).
    Each factor satisfies the Ehrhart hypotheses in dimension nj : (i) centroid: b(ΨK) = Ψb(K) =
0 and for a product body the centroid is the tuple of factor centroids (Fubini), so b(Kj′ ) = 0. (ii)
interior lattice point: if ξ ∈ int Kj′ ∩ Znj , then v := (0, . . . , ξ, . . . , 0) ∈ Zn and v ∈ int ΨK (the
other components 0 are interior since 0 ∈ int K), so v ∈ Ψ(int K ∩ Zn ) = {0}, i.e. ξ = 0.
    By the fully proved Ehrhart inequality (P1)–(P6) in dimension nj : vol(Kj′ ) ≤ F (nj ).
Hence, using | det Ψ| = 1 and Lemma 11B.12,
                                             Y               Y
                         F (n) = vol(K) =        vol(Kj′ ) ≤     F (nj ) < F (n),
                                               j              j

a contradiction. (No circularity: only the inequality — unconditionally proved in every dimension
— is used, never the equality classification.)


11B-I. The balanced integer cage and the conclusion Theorem 11B.14 (equality case
of Ehrhart’s conjecture). Let K ⊂ Rn be a convex body with b(K) = 0, int K ∩ Zn = P    {0} and
               n
vol(K) = (n+1) /n!. Then K = A(S) for some A ∈ GLn (Z), where S = {x : xj ≥ −1,          j xj ≤
1}. Consequently, for centroid in Zn as in the original statement, K is unimodularly equivalent
to S.

Proof. By Theorems 11B.8, 11B.10, 11B.11, 11B.13 there are w0 , w1 , . . . , wn ∈ Zn (r = n + 1,
relabeled) with:
                                   n
                                   X
            span{wi } = Rn ,             wi = 0,     K = {y : ⟨wi , y⟩ ≥ −1, i = 0, . . . , n}.
                                   i=0

We conclude directly: any n of the wi are linearly independent (Theorem 11B.8(c)); let B be the
integer matrix with rowsP w1 , . . . , wn , det B ∈ Z \ {0}. Under ξ = By, the constraints become
ξj ≥ −1 and ⟨w0 , y⟩ = − j ξj ≥ −1, i.e. BK = S. Then

                   (n + 1)n             vol(S)    (n + 1)n
                            = vol(K) =          =             =⇒ | det B| = 1,
                      n!               | det B|   n! | det B|

so B ∈ GLn (Z) and K = B −1 (S).

   Combined with (P1)–(P6), this completes Ehrhart’s conjecture: vol(K) ≤ (n + 1)n /n!,
with equality iff K is unimodularly equivalent to S.


                                                    42
11B-J. Examples
        ′′   −ϕ
                 R −ϕJ.1 (n = 1, fully explicit). K = [−1, 1], ϕ(x) = 2 log cosh(x/2) + log 2
solves ϕ = e , e = 2 = V , y = tanh(x/2). Modes: up = 1 − sech(x/2) cos θ at p = (0, 0);
Λ = {±1}; Λ1 = t(1 − y), Λ−1 = t′ (1 + y), (FE): ex = 1+y                              ∗
                                                          1−y ; rep (11B:B.1): ∇ϕ = log(1 +
y) − log(1 − y), so w± = ±1, κ = 0; balance; d± = 1, γ± = 1, k± = 0; polynomial identity
                   1     1       2                           2
(11B:C.2): M = 1+y    + 1−y = 1−y  2 , so P = det M · (1 − y ) = 2 = c0 , a positive constant.

Theorem 11B.1: unique zero at x = θ = 0; Hessian uxx = 14 = 12 ϕ′′ (0), uθθ = 1 = 2ϕ′′ (0), uxθ = 0;
law check at leading order: det H = 14 = e−2ϕ(0) , contribution 1!1 . Saturation: ZΛ = Z; cage
{y ≥ −1} ∩ {−y ≥ −1} = K; finale: B = (1), K = S.
J.2 (model, general n). K = S: ℓi = 1+⟨v             i ,y⟩
                                                  n+1 , vj = ej , v0 = −1. Direct computation
                                 
                        |⟨Z,P ⟩|2
(up = (n + 1) 1 − ∥P      ∥2 ∥Z∥2
                                    for p ↔ P (hermitian pairing)) gives Λ(p) = {±ei } ∪ {ei − ej }
                                                                    P 
— exactly the Demazure roots; e.g. ûej = exj /2 · − 1−n+1yk , so Hej = {⟨v0 , y⟩ = −1},
and Λej = ℓ0 ; each root m pairs −1 with vα(m) , +1 with vα(−m) , 0 otherwise — the pattern
                                                                                               1
(11B:B.2). (FE): exj = ℓj /ℓ0 , so (11B:B.1) holds with wi = vi (i.e. γi = n + 1, di = n+1         ,
                          ∗
         P                       P
ki P
   = 0),    wi = 0; ϕP= i ℓ̃i log ℓ̃i +const (exact Guillemin); the polynomial identity reads
cn i det(vî )2 ℓ̃i = cn i ℓ̃i = const (unimodular corner determinants). ZΛ = Zn (ei ∈ Λ); k = 1,
r = n + 1; am ∥ facet normals — so the argument specializes exactly to the model, and Theorem
                                                  |w|2
11B.1’s Hessian identity matches u = (n + 1) 1+|w|      2 , Hess = id in normal coordinates.


J.3 (the square). For [−1, 1]2 (P1 × P1 ), the exact Guillemin potential satisfies the conclusions
of §§11B-B–11B-G with k = 2 classes {±e1 }, {±e2 }, integer cage, d = 1 — and is eliminated
exactly at §11B-H: F (1)2 = 4 < 4.5 = F (2), matching vol = 4 < 92 . So the volume hypothesis,
and only it, separates products.


11B-K. Remarks
   1. One fixed p suffices for the entire argument (the all-p freedom, Propositions 11A.6/11A.7,
      and the variance identity are not needed ). Inputs: Theorems 11A.1, 11A.3 (finiteness —
      convenient, not essential), 11A.5 ((FE), supporting hyperplanes; Hm ̸= H−m re-derived
      in Theorem 11B.3), Lemma 11A.8, the exact law for all λ, u ∈ C ω , u ≥ 0, u(p) = 0,
      ∆u = n − u, the KE equation and Legendre duality, and the proved Ehrhart inequality in
      dimensions < n (§11B-H). Hypotheses enter: (i) b(K) = 0 via (P1)/(E1)–(E2) upstream
      and via factor centroids in §11B-H; (ii) int K ∩ Zn = {0} via the upstream machinery and
      factor lattice points in §11B-H; (iii) volume in §§11B-H–11B-I.

   2. There is no circularity: §11B-H uses only the unconditional inequality (P1)–(P6) in strictly
      smaller dimensions; the equality classification is never invoked before being proved. No
      induction on dimension is needed in the main line.

   3. The degenerate case span Λ ⊊ Rn is handled by Lemma 11A.8 (and independently by
      Theorem 11B.1).

   4. Some technical points warrant remark: the tube/Morse asymptotics in §11B-A (real-
      analyticity gives clean third-order control, and only lower bounds on sublevel mass are used,
      so possible “mass at infinity” is harmless); Fischer’s inequality and the block AM–GM with
      the KE calibration det D2 ϕ = e−ϕ ; the genericity choices on hyperplanes (finitely many
      distinct affine hyperplanes); and properness of ∇ϕ∗ (from the established diffeomorphism
      property).
                                              0
   5. Byproducts. det Hess up (p) = e−2ϕ(x ) with the split Hessian uxx = 12 D2 ϕ, uθθ = 2D2 ϕ,
      uxθ = 0 — the infinitesimal form of the model automorphism ray (∂Vp (p) = id, Vp the
      Euler field at p); polytopality and rationality of K are derived, not assumed; and every

                                                  43
      facet hyperplane of the extremal K carries a lattice point of 2K, quantizing heights exactly
      as in the Demazure picture.


12     Proof of the Main Theorem
Inequality. Part I (Sections 1–7): n! vol(K) ≤ (n + 1)n for every K satisfying (i), (ii).
Equality is attained by the simplices A(S) + b. Unimodular maps preserve the hypotheses
and the volume, and Lemma 8.1 shows S itself satisfies (i), (ii) with vol(S) = (n + 1)n /n!.
Equality forces K = A(S). Let K satisfy (i), (ii) with vol(K) = (n + 1)n /n!, i.e. τ = n + 1.
By Proposition 8.2, the saturation identities (E1), (E2) hold for every base point p ∈ T . Fix one
p. Theorem 9.6 gives the energy bound E0 (λ∗p ) ≤ n+2
                                                    n
                                                      ; Theorems 10.5, 10.7 and 10.14 upgrade it
to the eigenfunction package: a real-analytic up with up = λ∗p a.e., ∆up = n − up , 0 ≤ up ≤ n + 1,
up (p) = 0, the exact level-set law m({up < λ}) = λn /n!, and a holomorphic gradient field Vp .
Section 11A extracts the Laurent-mode structure of up : a finite active set Λ(p) ⊆ 2K ∩ Zn
carrying the functional equations (FE)/(ROW) with supporting hyperplanes of K at lattice
points, and spanning Rn (Lemma 11A.8). Section 11B then closes the argument: the unique
base-zero theorem (11B.1), the log-affine representation of ∇ϕ∗ and its Monge–Ampère rigidity
(11B.3–11B.7: balance, integer exponents, K a polytope cut out by its supporting hyperplanes),
the product decomposition and the facet sign law (11B.8, 11B.10: all facets at height −1),
lattice saturation and integrality of the normals (11B.11), the exclusion of products by strict
superadditivity of (n + 1)n /n! together with the already-proved inequality in lower dimensions
(11B.12–11B.13), and the final volume pinch (11B.14) give

                              K = A(S)       for some A ∈ GLn (Z).

Undoing the normalization. For the original body (before the translation x 7→ x − b(K))
the conclusion reads: K is unimodularly equivalent to S, i.e. K = A(S) + t with A ∈ GLn (Z),
t = b(K) ∈ Zn . ■


                                                44
