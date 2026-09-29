---
title: "Exponential parallel repetition for the entangled value"
source_url: "https://www-cdn.anthropic.com/files/4zrzovbb/website/bf2a107323136383e9efc8e6ac6659068e8bc561.pdf"
category: "19-Reference"
fetched_at: "2026-08-06T07:08:00Z"
tags: ["news-research"]
---

Exponential parallel repetition for the entangled value
                     of two-player one-round games


                                                 Abstract
      We prove that the entangled value of the n-fold parallel repetition of a two-player one-round
      game G with val∗ (G) < 1 decays exponentially in n: there are constants c(G) > 0, C(G) < ∞
      with val∗ (G⊗n ) ≤ C(G)e−c(G)n . The proof reduces the general case to the anchored case,
      for which exponential decay is known by the theorem of Bavarian, Vidick and Yuen. The
      reduction interrogates an arbitrary N -coordinate strategy through M ≪ N randomly routed
      anchored coordinates, carrying a tunable “flag” rate which controls the probability that a routed
      coordinate is severed (i.e. receives a product-distributed input pair instead of a µ-distributed
      one); the resulting acceptance probability is an explicit real polynomial of degree ≤ M in the
      no-severance parameter λ. This polynomial is bounded by the anchored repetition bound on the
      realizable segment λ ∈ [0, 1 − q], and — by a Parseval ledger in the Hirschfeld–Gebelein–Rényi
      singular basis of the question distribution combined with a hypergeometric moment-generating-
      function estimate — is bounded by bM on a disk of radius ≈ ln(1/ρ) N/M . A two-constants
      argument from classical potential theory, proved below in full with explicit constants, then
      transfers the segment bound to the unrealizable point λ = 1, which dominates the win-all
      probability of the original strategy.


0     Introduction
0.1   The problem
Let G = (µ, V ) be a two-player one-round game: a referee draws a question pair (x, y) from a
distribution µ on a finite set X × Y, sends x to Alice and y to Bob, receives answers a ∈ A, b ∈ B
without further communication, and accepts iff V (x, y, a, b) = 1. The entangled value val∗ (G) is the
supremum of the acceptance probability over all finite-dimensional quantum strategies: a shared
entangled state and local measurements. The n-fold parallel repetition G⊗n plays n independent
copies of G simultaneously, in one round, and accepts iff all n copies are won.
    The parallel repetition problem asks whether val∗ (G) < 1 forces val∗ (G⊗n ) → 0, and at
what rate. Classically, the corresponding statement for the classical value val(G) is Raz’s cele-
brated parallel repetition theorem [15], later simplified and sharpened [10, 14, 5]; the naive guess
val(G⊗n ) = val(G)n is false [7], so some such theorem is genuinely needed. In the entangled set-
ting, where the players may share entanglement [3], parallel repetition has been established with
exponential decay for several restricted classes of games: XOR games [4], unique games [12], free
games (product question distributions) [11, 2], projection games [6], and — the result on which we
build — anchored games [1]. For arbitrary games with val∗ (G) < 1, a general bound tending to
zero was obtained by Yuen [17], but with a polynomial rather than exponential rate.
    We prove exponential decay in full generality.

Main Theorem. For every two-player one-round game G with val∗ (G) < 1 there exist constants


                                                     1
c(G) > 0 and C(G) < ∞ such that

                           val∗ G⊗n       ≤ C(G) e−c(G) n
                                      
                                                             for all n ≥ 1.

   All constants are explicit in terms of the parameters of G and the constants appearing in the
anchored parallel repetition theorem of Bavarian, Vidick and Yuen [1], which is the only cited
external result; every other step is proved from scratch below.

0.2   Method and novelty
The existing exponential bounds for structured classes of games are proved by information-theoretic
arguments that condition on winning a large subset of coordinates and then analyse the post-
measurement state; extending such arguments to arbitrary question distributions has been the
main obstruction. The present proof takes an orthogonal route: it uses the anchored repetition
theorem [1] as a black box and converts it into a statement about general games by a probabilistic
simulation together with complex analysis. No conditioning on winning, no selection of near-optimal
witnesses, and no control of post-measurement states occurs anywhere; each value val∗ (G⊗N ) is
bounded directly, uniformly over all strategies.
     The two analytic ingredients are (i) a Parseval-type ledger for the singular-basis (Hirschfeld–
Gebelein–Rényi [9, 8, 16]) Fourier coefficients of the measurement operators of an arbitrary N -
coordinate strategy, which caps the total mass the strategy can place at spectral level w by a
ρ w -weighted budget, and (ii) the classical two-constants (Nevanlinna) principle of potential theory,
see e.g. [13], here proved in full with explicit constants. The bridge between them is the observation
that the acceptance probability of the simulation is an exact polynomial in the severance parameter,
with an explicit hypergeometric dependence on the ratio M/N .

0.3   Overview of the proof
Throughout, G = (µ, V ) is a game with question sets X , Y, answer sets A, B, question distribution
µ on X × Y and predicate V . We write vn := val∗ (G⊗n ) and ε0 := 1 − val∗ (G) > 0.
   The proof has the following skeleton.

 1. Reduction to connected games (§2). Decompose the bipartite support graph of µ into
    connected components. The entangled value is the µ-weighted average of the component values,
    so some component game Gκ∗ has val∗ (Gκ∗ ) < 1; a Chernoff argument reduces the Main
    Theorem to the case where the support graph of µ is connected (and all marginal probabilities
    are positive).

 2. A singular basis for µ (§3). For connected µ the maximal-correlation coefficient satisfies
    ρmax (µ) < 1. We fix singular (Hirschfeld–Gebelein–Rényi) bases of L2 (µA ) and L2 (µB ) which
    diagonalize the correlation operator of µ, with singular values 1 = ϱ0 > ϱ1 = ρmax ≥ ϱ2 ≥
    · · · ≥ 0.

 3. Anchoring (§4). Let G⊥ be the game obtained from G by anchoring with parameter β = 43 :
    each player’s question is independently replaced by a dummy symbol ⊥ with probability β, and
    any round in which a ⊥ occurs is accepted automatically. Then val∗ (G⊥ ) = 1 − 16
                                                                                   1
                                                                                      ε0 < 1, and
    the theorem of Bavarian–Vidick–Yuen [1] gives constants δB > 0, M1 ≥ 1 with val∗ (G⊗M ⊥ ) ≤
    e −δB M for all M ≥ M1 .


                                                   2
 4. The flagged routed family (§5). Fix any strategy S for G⊗N and M ≤ N . We construct a
    one-parameter family {Rφ [S]}φ∈[0,1] of honest strategies for G⊗M ⊥ : the M anchored coordinates
    are routed to M random distinct slots of an N -slot board, the remaining slots are filled with
    correlated shared junk distributed exactly like real questions, and the players then run S on
    the assembled N -coordinate question strings. Coordinates where exactly one player received
    ⊥ are unavoidably severed : at the corresponding slot S sees an input pair with the product
    law µA ⊗ µB instead of µ. Coordinates where both players received ⊥ can be filled with the
    shared junk pair — an honest µ-distributed input — but, and this is the key design element,
    Bob additionally re-randomizes his junk there with probability φ (i.i.d. “flags”), which severs
    those slots as well. The exact conditional law of the construction is computed in Lemma 5.2:
    conditionally on the live set, each non-live routed slot is severed independently with probability
    1 − λ, where
                                     λ := (1 − q)(1 − φ),         q = 25 ,
    and q is the conditional probability that a non-live anchored coordinate is one-sided (forced
    severance).
 5. The occupancy profile (§6–§7). Expanding the win-kernel of S in the singular basis and
    integrating out the severance randomness yields an exact identity
                                                                
                                  val Rφ [S] = G (1 − q)(1 − φ) ,
    where G is a real polynomial of degree ≤ M depending only on S (not on φ) — the occupancy
    profile of S. Three further properties are proved: 0 ≤ G ≤ 1 on [0, 1]; the floor G(1) ≥ val(S);
    and — from the Parseval mass ledger for the singular-basis coefficients of S’s measurement
    operators, combined with a hypergeometric moment-generating-function bound — the disk
                                                       1 √
    bound |G(z)| ≤ bM for all |z| ≤ R, where b := 1 + 16 ( m − 1), m := min(|A|, |B|), and
                                                     N −M +1
                                     R := 1 + ln(1/ρ)
                                                          M
                                                   1
    is large when M ≪ N . (Here ρ := max(ρmax (µ), 2 ) < 1.)
 6. Two-constants argument (§8–§9). By steps 3–5, 0 ≤ G ≤ e−δB M on the whole segment
    [0, 1 − q] (those are values of honest anchored strategies, capped by the Bavarian–Vidick–Yuen
    bound). The point λ = 1 is not realizable by the family — the forced severance rate q > 0 is a
    wall — but the two-constants theorem of classical potential theory (proved from scratch in §8,
    with explicit constants) lets the segment bound tunnel through the wall: a polynomial that is
    ≤ ε in modulus on [0, 1 − q] and ≤ Ξ in modulus on the disk of radius R satisfies
                                                           √
                                                          4 q     Ξ
                                        ln G(1) ≤ ln ε +       ln .
                                                          ln R    ε
    Choosing M = Θ(θ0 N ) with an explicit θ0 (G) > 0 makes ln R large enough that the correction
                                                         3
    term is ≤ 14 δB M , whence val(S) ≤ G(1) ≤ e− 4 δB M = e−ΩG (N ) . Since S was arbitrary,
    vN ≤ e−c(G)N for all large N (§9), and the Main Theorem follows.
    The mechanism, in one sentence: an N -coordinate strategy interrogated through M ≪ N ran-
domly routed anchored coordinates can respond to the severance of a slot only through singular-basis
mass that touches that slot, and Parseval plus the hypergeometric rarity of hitting a small random
window tax that response so heavily that the strategy’s acceptance profile is analytic and bounded
on a disk of radius ≈ ln(1/ρ) N/M ; analyticity at that scale forces the profile’s value at the un-
realizable no-severance point λ = 1 — which dominates the win-all probability — down to the
anchored-repetition cap that holds on the realizable segment.

                                                  3
Where the hypotheses enter. val∗ (G) < 1 enters only through δB > 0 (step 3) — this is
the sole step that is sensitive to the difference between finite-dimensional entangled strategies and
more general commuting-operator models, as any correct proof must be. Connectivity enters only
through ρ < 1. Finiteness of the answer alphabets enters only through the ledger constant m1/2 .
No step conditions on winning, selects near-optimal witnesses, tracks post-measurement states, or
assumes anything about the structure or dimension of S.

Organization. §1 preliminaries; §2 components; §3 singular basis; §4 anchoring; §5 the flagged
routed family; §6 spectral representation and ledger; §7 the occupancy profile; §8 the two-constants
lemma; §9 assembly; §10 concluding remarks.


1     Preliminaries
1.1     Games, strategies, values
A (two-player one-round) game G = (µ, V ) consists of finite nonempty question sets X , Y, finite
nonempty answer sets A, B, a probability distribution µ on X × Y and a predicate V : X × Y ×
A × B → {0, 1}.
   A (finite-dimensional quantum) strategy S for G consists of finite-dimensional Hilbert spaces
HA , HB , a unit vector ψ ∈ HA ⊗ HB , and projective measurements {Axa }a∈A on HA (for each
x ∈ X ) and {Bby }b∈B on HB (for each y). Its value is

                                                V (x, y, a, b) ⟨ψ|Axa ⊗ Bby |ψ⟩,
                                  X          X
                        val(S) :=    µ(x, y)
                                    x,y        a,b

and val∗ (G) := supS val(S). The n-fold repetition    G⊗n has questions x̄ ∈ X n , ȳ ∈ Y n drawn from
µ⊗n , answers ā ∈ An , b̄ ∈ B n , and predicate nj=1 V (xj , yj , aj , bj ). We write vn := val∗ (G⊗n ).
                                                Q
   Two standing conventions, both without loss of generality:

    • (Full marginals.) We may delete from X all letters x with µA (x) = 0 and likewise for Y (here
      µA , µB denote the marginals of µ). Questions outside the reduced sets occur with probability
      0 in G and in every G⊗n , so no value vn changes: given a strategy for the reduced game one
      extends it by arbitrary measurements on the deleted letters without changing the value, and
      conversely one restricts. From §2 onward we assume µA , µB have full support.

    • (Operator generality.)   P All lemmas below are stated and proved for families of operators
      satisfying only 0 ⪯ Axa , a Axa = I (POVMs); projective strategies are the special case relevant
      to val∗ as defined. No Naimark dilation is ever needed.

1.2     Shared randomness
Lemma 1.1 (shared randomness is free). Let H be a game, Ω a finite set, p a probability distribution
on Ω, and for each r ∈ Ω let Sr be a strategy for H. Then there is a single strategy S̄ for H with
                                              X
                                    val(S̄) =     p(r) val(Sr ).
                                                 r∈Ω

Consequently any “strategy with shared randomness” — a pair of local procedures which first read
a common random seed r ∼ p and then play Sr — has acceptance probability ≤ val∗ (H), and this
remains true when the seed also selects which classical pre- and post-processing each player applies.

                                                     4
Proof. Write Sr = (HA,r , HB,r , ψr , Ax,r  y,r                                       L                        L
                                       a , Bb ). Put HA :=                            r HA,r , HB :=               r HB,r ,

                                                                                                                    Bby :=        Bby,r .
             Xp                  M                                                                  M                         M
                                                                                          Axa :=            Ax,r
                                                    
      ψ :=        p(r) ψr ∈              HA,r ⊗ HB,r ⊆ HA ⊗ HB ,                                             a ,
             r                     r                                                                   r                      r

These are projective (resp. POVM) measurements if the blocks are, and ψ is a unit vector since the
blocks HA,r ⊗ HB,r are pairwise orthogonal in HA ⊗ HB . For r ̸= r′ the operator Axa ⊗ Bby maps
the block of r′ into itself, which is orthogonal to the block of r; hence all cross terms vanish:

                             ⟨ψ|Axa ⊗ Bby |ψ⟩ =                      y,r
                                                X
                                                   p(r) ⟨ψr |Ax,r
                                                              a ⊗ Bb |ψr ⟩.
                                                              r
                                                     P
Summing against µ(x, y)V (x, y, a, b) gives val(S̄) = r p(r)val(Sr ). A strategy with shared ran-
domness is exactly such a p-mixture (classical pre/post-processing of questions and answers can
be absorbed into the measurement operators of each Sr ), so its acceptance probability equals
val(S̄) ≤ val∗ (H).

1.3     Advice
Lemma 1.2 (question-independent advice is useless). Let H be a game and let (rA , rB ) be a
pair of random variables with an arbitrary joint distribution ν on a finite set, independent of the
questions. Suppose the players play as follows: Alice receives rA , Bob receives rB , and conditionally
on (rA , rB ) = (u, v) they play a strategy Su,v (state and measurements may depend arbitrarily on
the advice). Then the acceptance probability is ≤ val∗ (H).

Proof. The acceptance probability equals u,v ν(u, v) val(Su,v ) ≤ maxu,v val(Su,v ) ≤ val∗ (H), be-
                                             P
cause conditionally on the advice the questions still have law µH (independence) and Su,v is a bona
fide strategy.

    The point of Lemma 1.2 is that the advice may be correlated between the players; only inde-
pendence
P           from the questions is required. The lemma’s conclusion is simply a bound on the average
   u,v ν(u, v) val(Su,v ), which is what the application uses; in the one place it is used — Proposi-
tion 2.2 — each player’s processing in fact depends only on their own advice component, with a
fixed shared state, so the protocol there is locally realizable and its acceptance probability is exactly
such an average.

1.4     Answer marginalization
Lemma 1.3. Let S = (ψ, {Aāx̄ }, {Bb̄ȳ }) be a strategy for G⊗N (POVMs allowed), let T ⊆ [N ], and
fix questions (x̄, ȳ). For āT ∈ AT define the coarse-grained operators

                                                                         Bb̄ȳ .
                                         X                           X
                            AāT (x̄) :=       Aāx̄ ,  Bb̄T (ȳ) :=
                                             ā : ā|T =āT                                b̄ : b̄|T =b̄T
                                                                  P
Then {AāT (x̄)}āT ∈AT is a POVM (0 ⪯ AāT , āT AāT = I), likewise for Bob, and for every set
E ⊆ AT × B T of “good” T -answer pairs,

                               ⟨ψ|Aāx̄ ⊗ Bb̄ȳ |ψ⟩ =
                       X                              X
                                                        ⟨ψ|AāT (x̄) ⊗ Bb̄T (ȳ)|ψ⟩.
                   ā,b̄ : (ā|T ,b̄|T )∈E                            (āT ,b̄T )∈E


                                                                  5
Proof. Positivity and completeness of the coarse-grainings are immediate. The identity is obtained
by grouping the (finite, absolutely convergent) sum on the left according to (ā|T , b̄|T ) and using
bilinearity of (A, B) 7→ ⟨ψ|A ⊗ B|ψ⟩.

   In particular, the probability that the answers of S satisfy the predicate at all coordinates of T
(“win T ”) depends on the answer distribution only through the coarse-grained POVMs above.


2    Reduction to connected games
Let Γ(µ) be the bipartite graph on vertex set X ⊔ Y with an edge {x, y} whenever µ(x, y) > 0 (full
marginals assumed; every vertex hasFpositive degree).
                                                  F      Let its connected components be indexed
by κ ∈ K, inducing partitions X = κ Xκ , Y = κ Yκ . Every (x, y) ∈ suppµ has both endpoints
in the same component; write κ(x), κ(y) for the component of a letter and pκ := µ(Xκ × Yκ ) > 0.
Let Gκ := (µκ , V ) be the component game with µκ := µ( · | Xκ × Yκ ), question sets Xκ , Yκ , and the
restricted predicate.
                           X
Lemma 2.1. val∗ (G) =         pκ val∗ (Gκ ). Consequently, if val∗ (G) < 1 there is a component κ∗
                              κ
with pκ∗ > 0 and val∗ (Gκ∗ ) < 1.

Proof. “≤”: for any strategy
                           P S for G, conditioning the value on the component (an event of the
questions) gives val(S) = κ pκ valκ (S), where valκ (S) is the value of the induced strategy for Gκ
(same state; measurements     restricted to questions in the component) — a bona fide strategy for
Gκ — so val(S) ≤ κ pκ val∗ (Gκ ).
                     P
                                                                   x,κ   y,κ                    ∗
    “≥”: given ε > 0 pick for eachN κ a strategy   N Sκ =(ψκ , A N , B ) with val(Sκ ) ≥ val (Gκ ) − ε.
Form the product state ψ :=           κ ψκ on         κ HA,κ ⊗      κ HB,κ and define, for x ∈ Xκ , the
measurement Axa := Ax,κ a  ⊗I other factors , likewise for Bob. Each letter determines its own component,
so this is well defined, and for (x, y) in component κ,

                             ⟨ψ|Axa ⊗ Bby |ψ⟩ = ⟨ψκ |Ax,κ    y,κ
                                                      a ⊗ Bb |ψκ ⟩.

Hence the value is κ pκ val(Sκ ) ≥ κ pκ val∗ (Gκ ) − ε. Let ε ↓ 0.
                  P                P
   If every component with pκ > 0 had value 1, the display would force val∗ (G) = 1.

Proposition 2.2 (component reduction). Let κ∗ be as in Lemma 2.1, p∗ := pκ∗ , and suppose the
                                                ∗
connected game Gκ∗ satisfies vk (Gκ∗ ) ≤ C ∗ e−c k for all k ≥ 1 with constants C ∗ ≥ 1, c∗ > 0. Then
for all n ≥ 1
                                                   ∗ ∗           ∗
                                vn (G) ≤ C ∗ e−c p n/2 + e−p n/8 .

Proof. Fix a strategy S for G⊗n . Let κ̄ = (κ1 , . . . , κn ) be the (random) component labels of the n
question pairs; the κj are i.i.d. with Pr[κj = κ∗ ] = p∗ . Conditionally on κ̄, the n question pairs are
independent, pair j having law µκj . Let T = T (κ̄) := {j : κj = κ∗ } and t := |T | ∼ Bin(n, p∗ ).
    Condition on κ̄. The questions split into (x̄T , ȳT ) — i.i.d. µκ∗ pairs — and (x̄T c , ȳT c ), which
are independent of the former. Treat (x̄T c , ȳT c ) as advice in the sense of Lemma 1.2 (correlated
between the players, independent of the T -questions): the players of G⊗t   κ∗ receive questions (x̄T , ȳT ),
use the advice to fill in the other coordinates, run S, and output the T -coordinates of their answers.
Winning all n coordinates of G⊗n implies winning all coordinates of T , so
                                                                               
                            Pr[ S wins all | κ̄ ] ≤ Pr[ win T | κ̄ ] ≤ vt Gκ∗


                                                      6
by Lemma 1.2 (note that each player can compute T from their own questions, since κj is determined
by either letter of pair j; in any case T is fixed by the conditioning). Averaging over κ̄ and using
vt ≤ 1:
                                                            ∗          ∗ ∗
                        val(S) ≤ E vt (Gκ∗ ) ≤ Pr t < p 2n + C ∗ e−c p n/2 .
                                                    

The standard multiplicative Chernoff bound gives Pr[Bin(n, p) ≤ np/2] ≤ e−np/8 . Take the supre-
mum over S.

   Thus it suffices to prove the Main Theorem for connected G (with full marginals): the
                                                                      ∗ ∗         ∗
general case follows by applying Proposition 2.2 to κ∗ , since C ∗ e−c p n/2 + e−p n/8 ≤ (C ∗ +
          ∗ ∗     ∗
1)e− min(c p /2, p /8) n .
From now until the end of §9, G is connected with full marginals and val∗ (G) < 1.


3    The singular basis of µ
Lemma 3.1 (Hirschfeld–Gebelein–Rényi basis). There exist orthonormal bases {ϕi }0≤i<|X | of
L2 (X , µA ) and {ψi }0≤i<|Y| of L2 (Y, µB ), consisting of real-valued functions, such that ϕ0 ≡ 1,
ψ0 ≡ 1, and                                
                      E(x,y)∼µ ϕi (x) ψj (y) = ϱi δij    for all i < |X |, j < |Y|,
where 1 = ϱ0 ≥ ϱ1 ≥ ϱ2 ≥ · · · ≥ 0 (indices beyond min(|X |, |Y|) − 1 get ϱi := 0). Moreover ϱ1 < 1,
and in fact ϱ1 = ρmax (µ), the maximal correlation of µ.
                                                                p
Proof. Consider the |X | × |Y| real matrix Qxy := µ(x, y)/ µA (x)µB (y) (well defined        by full
                          2 (µ ), g ∈ L2 (µ ) let F ∈ RX , G ∈ RY be F (x) =
                                                                                       p
marginals).
        p     For f ∈   L     A              B                                           µA (x)f (x),
G(y) = µB (y)g(y); the maps f 7→ F , g 7→ G are isometric isomorphisms onto ℓ2 (X ), ℓ2 (Y),
and
                                      Eµ [f (x)g(y)] = F T Q G.                                (3.1)
By Cauchy–Schwarz under µ, |Eµ [f g]| ≤ ∥f ∥L2 (µA ) ∥g∥L2 (µB ) , so ∥Q∥op ≤ 1. Take a real singular
value decomposition Q = i<d ϱi ui viT with d := min(|X |, |Y|), orthonormal ui ∈ RX , vi ∈ RY ,
                              P
ϱ0 ≥ ϱ1 ≥ · · · ≥ ϱd−1 ≥ 0; complete {ui } and {vi } to orthonormal bases of RX , RY (the completions
lie in the cokernel/kernel             T
                        p of Q, so ui Qvj = ϱi δijpholds for all i, j with the zero-padding convention).
Define ϕi (x) := ui (x)/ µA (x), ψj (y) := vj (y)/ µB (y); by the isometry these are real orthonormal
bases and (3.1) gives Eµp [ϕi ψj ] = ϱi δij .          p                       p
     The vector u(x) := µA (x) satisfies (Qv)(x) = µA (x) for v(y) := µB (y), i.e. Qv = u, and
∥u∥ = ∥v∥ = 1, ∥Q∥ ≤ 1; hence (u, v) is a singular pair with singular value 1 = ϱ0 , and we may
take u0 = u, v0 = v, i.e. ϕ0 = ψ0 ≡ 1. (Even if the singular value 1 is degenerate this choice is
available: from Qv = u, ∥u∥ = ∥v∥ = 1, ∥Q∥ ≤ 1 one gets QT Qv = v — because ∥Qv∥ = ∥v∥ and
QT Q ⪯ I force (I − QT Q)1/2 v = 0 — so v lies in the right singular-value-1 space V1 , on which Q
restricts to an isometry onto the left space U1 ; choose an orthonormal basis of V1 whose first vector
is v and take its image under Q, whose first vector is u, as the corresponding left basis. This yields
an SVD with u0 = u, v0 = v.) By the variational principle for singular values,
               
     ϱ1 = max Eµ [f (x)g(y)] : ∥f ∥ = ∥g∥ = 1, ⟨f, 1⟩L2 (µA ) = EµA f = 0, EµB g = 0 = ρmax (µ).

   Finally, ϱ1 < 1 for connected
                           p      pµ: suppose f, g are unit-norm, mean-zero with Eµ [f g] = 1.
Cauchy–Schwarz Eµ [f g] ≤ Eµ f  2   Eµ g 2 = 1 holds with equality, so g(y) = τ f (x) for µ-a.e. (x, y)
and some constant τ ; unit norms force τ 2 = 1 and Eµ [f g] = 1 > 0 forces τ = 1. Thus f (x) = g(y)
whenever µ(x, y) > 0: the function equal to f on X and g on Y is constant along every edge of

                                                   7
Γ(µ), hence constant on the connected graph Γ(µ); mean-zero then forces f ≡ 0, contradicting
∥f ∥ = 1. (Conversely disconnected supports admit ϱ1 = 1, which is why §2 was needed.)

Convention. Henceforth fix such bases and set
                                     ρ := max ϱ1 , 12          ∈ [ 12 , 1).
                                                         

All we use about ρ is: ϱi ≤ ρ for all i ≥ 1 (hence ϱ-products are dominated by ρ-powers) and
0 < ln(1/ρ) ≤ ln 2. The floor 21 only tidies constants (it covers, e.g., product µ, where ϱ1 = 0).

Tensorization.Q        For a finite index set U andQa multi-index k = (kj )j∈U with 0 ≤ kj < |X |, write
Φk (x̄U ) := j∈U ϕkj (xj ); similarly Ψk (ȳU ) := j ψkj (yj ) for 0 ≤ kj < |Y|. These are orthonormal
bases ofQL2 (X U , µ⊗U             2    U ⊗U
                       A ) and L (Y , µB ). Define suppk := {j : kj ̸= 0}, w(k) := |suppk|, and
  (k)
ϱ := j∈suppk ϱkj ∈ [0, ρ        w(k) ].
     Two facts we will use repeatedly p      (both immediate from orthonormality of {ϕi } in L2 (µA ),
i.e. from orthogonality of the matrix [ µA (x)ϕi (x)]x,i , whose columns — hence also rows — are
orthonormal):
                    ′
     P
       i ϕi (x)ϕi (x ) = δxx′ /µA (x) (completeness),      EµA [ϕi ϕi′ ] = δii′ (orthonormality),  (3.2)
and their tensorizations over U ; likewise for {ψj }, µB .


4    Anchoring
Fix the anchoring parameter
                                                                2β(1 − β)     2(1 − β)
               β := 43 ,    ℓ := (1 − β)2 = 16
                                            1
                                               ,        q :=              2
                                                                            =          = 25 .
                                                               1 − (1 − β)     2−β
(The only properties used later are ℓ > 0 and q ≤ 12 ; any β ∈ [2/3, 1) would do.)
Definition (anchored game). Let ⊥ be a fresh symbol. The anchored game G⊥ has question sets
X⊥ := X ∪ {⊥}, Y⊥ := Y ∪ {⊥}, the same answer sets A, B, question distribution sampled as
                                   (                           (
                ◦ ◦                 ⊥ w.p. β                    ⊥ w.p. β
              (x , y ) ∼ µ;  x̃ :=   ◦
                                                   ,     ỹ :=
                                    x w.p. 1 − β                y ◦ w.p. 1 − β

(the two Bernoulli(β) anchor indicators independent of each other and of (x◦ , y ◦ )), and predicate
                                             (
                                              1                if x̃ =⊥ or ỹ =⊥,
                        V⊥ (x̃, ỹ, a, b) :=
                                              V (x̃, ỹ, a, b) otherwise.

Lemma 4.1. val∗ (G⊥ ) = 1 − ℓ ε0 < 1.
Proof. “≥”: given ε > 0, take a strategy S for G with val(S) ≥ 1 − ε0 − ε and extend it to
G⊥ by letting each player, upon receiving ⊥, apply the measurement for some fixed question and
answer accordingly (any behavior at ⊥ is accepted). With probability 1 − ℓ at least one question
is ⊥ (automatic acceptance); with probability ℓ both are real and distributed µ. The value is
≥ 1 − ℓ + ℓ(1 − ε0 − ε).
    “≤”: for any strategy S⊥ for G⊥ , conditioning on the event that both questions are real —
under which the question pair has law exactly µ, and the restriction of S⊥ to real questions is a
strategy for G — gives val(S⊥ ) = 1 − ℓ + ℓ · valreal ≤ 1 − ℓ + ℓ(1 − ε0 ).

                                                    8
Theorem 4.2 (Bavarian–Vidick–Yuen [1]). For every game G with val∗ (G) < 1 and every anchor-
ing parameter β ∈ (0, 1) there exist constants δB = δB (G, β) > 0 and M1 = M1 (G, β) ≥ 1 such
that
                           val∗ G⊗M     ≤ e−δB M
                                      
                                  ⊥                  for all M ≥ M1 .

    This is the anchored parallel repetition theorem of [1]: for anchored games — and G⊥ is
precisely the (β-)anchored transformation of G treated there, with val∗ (G⊥ ) < 1 by Lemma 4.1 —
the entangled value of the M -fold repetition decays exponentially in M , at a rate depending only
on β, ε0 and the alphabet sizes. Any bound of the form val∗ (G⊗M
                                                               ⊥ ) ≤ C0 e
                                                                           −δ0 M (δ > 0) yields the
                                                                                   0
stated clean form by decreasing δB and increasing M1 . Without loss of generality we take δB ≤ 1
and M1 ≥ 1. This citation is the only cited external result to the proof, and the only
step in which the restriction to finite-dimensional (tensor-product) strategies is used.
    We emphasize the quantifier structure: Theorem 4.2 is a bound on the value of every finite-
dimensional strategy for G⊗M
                           ⊥ . It will be applied in §7 to the explicitly constructed strategies of
§5.


5     The flagged routed family
Standing data for §§5–7: G connected with full marginals, val∗ (G) < 1; integers N ≥ M ≥ 1;
a strategy S = (ψ, {Aāx̄ }ā∈AN , {Bb̄ȳ }b̄∈BN ) for G⊗N (projective, WLOG; POVMs would do); and a
flag rate φ ∈ [0, 1].

5.1    The construction Rφ [S]
We define a strategy with shared randomness for G⊗M
                                                 ⊥ .


Referee’s sampling (a coupling). By definition of G⊥ , the M question pairs of G⊗M        ⊥     can be
sampled as follows, independently across coordinates c ∈ [M ]: draw the underlying pair (x◦c , yc◦ ) ∼ µ
and independent anchor indicators ac , bc ∼ Bernoulli(β); send Alice x̃c :=⊥ if ac = 1, else x◦c ; send
Bob ỹc :=⊥ if bc = 1, else yc◦ . Classify coordinate c by its type:
                                                  1                                  3
                     Live (ac = bc = 0, prob ℓ = 16 ),         Asev (ac = 1, bc = 0, 16 ),
                                           3                                      9
                     Bsev (ac = 0, bc = 1, 16 ),               Null (ac = bc = 1, 16 ).

Types are i.i.d. across coordinates and independent of the underlying pairs (x◦c , yc◦ )c , which are i.i.d.
µ. Note

                                       2β(1 − β)
      Pr[Asev or Bsev | not Live] =              = q = 25 ,         Pr[Null | not Live] = 1 − q = 35 .       (5.1)
                                         1−ℓ

Shared randomness. Independent of the referee: a uniformly random injection ι : [M ] → [N ];
i.i.d. junk pairs (x′i , yi′ ) ∼ µ for i ∈ [N ]; i.i.d. fresh letters yi′′ ∼ µB for i ∈ [N ]; and a random flag set
F ⊆ [M ] containing each c independently with probability φ. All four ingredients are independent
of each other. (A finite probability space; Lemma 1.1 applies.)


                                                        9
Alice’s local procedure. Given her questions (x̃c )c∈[M ] and the shared randomness, she assem-
bles x̄ ∈ X N by
                           (
                            x̃c   x̃c ̸=⊥
                 x̄ι(c) :=    ′
                                          (c ∈ [M ]),    x̄i := x′i (i ∈
                                                                       / ι([M ])),
                            xι(c) x̃c =⊥

measures {Aāx̄ } on her half of ψ, obtains ā ∈ AN , and answers coordinate c with āι(c) .

Bob’s local procedure. He assembles ȳ ∈ Y N by
                     
                     ỹc
                           ỹc ̸=⊥
                        ′′
            ȳι(c) := yι(c) ỹc =⊥, c ∈ F  (c ∈ [M ]),               ȳi := yi′   (i ∈
                                                                                     / ι([M ])),
                     
                      ′
                      yι(c) ỹc =⊥, c ∈
                                      /F

measures {Bb̄ȳ }, obtains b̄, and answers coordinate c with b̄ι(c) .
    Each player’s procedure reads only their own questions and the shared randomness, so Rφ [S]
is a legal strategy with shared randomness for G⊗M    ⊥ ; by Lemma 1.1 its acceptance probability,
denoted val(Rφ [S]), is the value of an honest finite-dimensional strategy and hence

                                       val(Rφ [S]) ≤ val∗ G⊗M
                                                                  
                                                            ⊥       .                       (5.2)

We stress that val(Rφ [S]) is a plain acceptance probability at the anchored game’s own question
distribution — no conditioning, reweighting or post-selection is involved anywhere.

5.2    The conditional law
Define, for the run of Rφ [S]:
                                                                                     
                           C ′ := ι [M ] \ Live ,     Σ := ι Asev ∪ Bsev ∪ (Null ∩ F ) ⊆ C ′ ,
                                               
        T := ι(Live),

where Live ⊆ [M ] denotes the set of live coordinates, etc. Let t := |Live|. For Σ ⊆ [N ] let
                                          O                 O
                                 νΣ :=         µA ⊗ µB ⊗          µ
                                             i∈Σ                 i∈Σ
                                                                  /

denote the product question law on (X × Y)N which is severed (independent halves, correct
marginals) on Σ and honest elsewhere. Finally set

                                   λ := (1 − q)(1 − φ) ∈ [0, 1 − q].

Lemma 5.2 (exact conditional law). In the run of Rφ [S]:
    (a) Conditionally on the types, the flags and ι: the assembled pair (x̄, ȳ) ∈ X N × Y N has law
exactly νΣ ; the T -slot questions are the underlying pairs of the live coordinates transported by ι;
and the acceptance event of Rφ [S] equals the event that the answers of S win all coordinates of T
(with the predicate at slot ι(c) evaluated at the question pair (x◦c , yc◦ )).
    (b) Conditionally on t alone, the joint law of (T, C ′ , Σ, z̄T ), where z̄T := (x̄T , ȳT ), is: T is a
uniformly random t-subset of [N ]; given T , C ′ is a uniformly random (M −t)-subset of [N ]\T ; given
(T, C ′ ), Σ contains each slot of C ′ independently with probability 1 − λ; and z̄T ∼ µ⊗T , independent
of (T, C ′ , Σ). Moreover t ∼ Bin(M, ℓ).

                                                    10
Proof. (a) Fix the types, flags and ι. We list, for each slot i ∈ [N ], the pair of inputs (x̄i , ȳi ) and
its law; all randomness left is (underlying pairs, junk pairs, fresh letters), whose components are
independent of each other and of the conditioning.

  • i = ι(c), c ∈ Live: inputs (x◦c , yc◦ ) ∼ µ.

  • i = ι(c), c ∈ Asev: inputs (x′i , yc◦ ). The two halves come from independent sources, with laws
    µA and µB (marginals of µ); hence the law is µA ⊗ µB . (Whether c ∈ F is irrelevant: Bob’s
    question is real here, so his flag rule does not act.)

  • i = ι(c), c ∈ Bsev \ F : inputs (x◦c , yi′ ) — again independent halves, law µA ⊗ µB . (x′i is unused
    at this slot and at every other slot, since slot i is in the image of ι and Alice used her real
    question.)

  • i = ι(c), c ∈ Bsev ∩ F : inputs (x◦c , yi′′ ) — independent halves, law µA ⊗ µB : the same law as
    the unflagged case, so at Bsev coordinates the flag is a no-op in distribution.

  • i = ι(c), c ∈ Null \ F : inputs (x′i , yi′ ) — the shared junk pair, law µ (honest!).

  • i = ι(c), c ∈ Null ∩ F : inputs (x′i , yi′′ ) — independent halves, law µA ⊗ µB (severed).

  • i∈
     / ι([M ]): inputs (x′i , yi′ ), law µ.

     Distinct slots use disjoint collections of the independent ingredients (the underlying pair of
the coordinate routed there, if any; the junk pair and fresh letter indexed by that slot), so the
slot input pairs are independent across i. Comparing with the list: the law is severed exactly on
Σ = ι(Asev ∪ Bsev ∪ (Null ∩ F )) and honest elsewhere, i.e. the assembled pair has law νΣ ; and
the T -slots carry the live underlying pairs. For the acceptance event: the predicate V⊥ accepts
automatically at every coordinate with at least one ⊥, i.e. at every non-live coordinate; at a live
coordinate c it requires V (x◦c , yc◦ , āι(c) , b̄ι(c) ) = 1. So acceptance = win at every slot of T , which
reads only the T -components of the answers of S.
     (b) Conditionally on the types, consider the severance markers σc := 1[c ∈ Asev ∪ Bsev] ∨ 1[c ∈
Null, c ∈ F ] for c ∈/ Live: by (5.1) and independence of the flags, conditionally on Live the markers
(σc )c∈Live
      /     are i.i.d. Bernoulli with

                        Pr[σc = 1] = q + (1 − q)φ = 1 − (1 − q)(1 − φ) = 1 − λ,

independent of ι, of the underlying pairs, and of everything else. (t ∼ Bin(M, ℓ) since types are
i.i.d.)
     Now condition on t and use the independence of ι from (types, flags, pairs). Given Live (any fixed
t-set), the pair ι(Live), ι(Livec ) is a uniformly random ordered pair of disjoint subsets of [N ] of sizes
(t, M − t) — this is the distribution of the image sets of a uniform injection — and is independent
of the markers. Transporting the i.i.d. markers through the uniform bijection ι|Livec : Livec → C ′
(independent of them) yields: given (T, C ′ ), each slot of C ′ lies in Σ independently with probability
1 − λ. Finally the live underlying pairs (x◦c , yc◦ )c∈Live are i.i.d. µ and independent of (types, flags,
ι), hence z̄T ∼ µ⊗T independent of (T, C ′ , Σ).


                                                     11
5.3   The win-T functional
Fix T ⊆ [N ], |T | = t, and a tuple z̄T = (x̄T , ȳT ) ∈ (X × Y)T . Write U := [N ] \ T . Using
Lemma 1.3, define for ā ∈ AT the coarse POVM-valued functions of the off-T questions (the fixed
x̄T is suppressed from the notation)
                                          (x̄ ,x̄ )
                                 X
                  Aā (x̄U ) :=         Aā′ T U ,     Bb̄ (ȳU ) likewise (b̄ ∈ B T ),
                                 ā′ ∈AN : ā′ |T =ā

                                                   T    T
P win event E = E(T, z̄T ) := {(ā, b̄) ∈ A × B : V (xj , yj , aj , bj ) = 1 ∀j ∈ T }, and BE,ā :=
the
  b̄:(ā,b̄)∈E Bb̄ , so that 0 ⪯ BE,ā ⪯ I. For Σ ⊆ U set
                                                        X
                FT,z̄T (Σ) := E(x̄U ,ȳU )∼νΣ |U                 ψ Aā (x̄U ) ⊗ BE,ā (ȳU ) ψ   ∈ [0, 1].   (5.3)
                                                        ā∈AT

(F ≥ 0 because each summand  Pis ⟨ψ|P ⊗ Q|ψ⟩ with P, Q ⪰ 0; F ≤ 1 because enlarging BE,ā to I
and using completeness gives ā ⟨ψ|Aā ⊗ I|ψ⟩ = 1.)
    By Lemma 5.2(a) and Lemma 1.3, conditionally on (types, flags, ι) and on the live underlying
pairs, the acceptance probability of Rφ [S] equals FT,z̄T (Σ): the T -slot questions are fixed by the
conditioning, the off-T questions have law νΣ |U (independence of slots), and acceptance is the
win-T event, which depends on the answers only through their T -components. Combining with
Lemma 5.2(b):
                        M                                                              
                        X                                                              M t
                                                                                         ℓ (1 − ℓ)M −t ,
                     
           val Rφ [S] =   πt ET Ez̄T EC ′ EΣ FT,z̄T (Σ),                        πt :=                        (5.4)
                                                                                       t
                                t=0

with the conditional laws of Lemma 5.2(b) (T uniform t-subset; z̄T ∼ µ⊗T ; C ′ uniform (M −t)-
subset of T c ; Σ ⊆ C ′ i.i.d. (1 − λ)).


6     Spectral representation and the coefficient ledger
Throughout §6 fix (T, z̄T ) with |T | = t and let U , Aā (·), BE,ā (·), F = FT,z̄T be as in §5.3. Define
the (finitely many, bounded) operator Fourier coefficients
                                                                                               
             Âā,k := Ex̄U ∼µ⊗U Aā (x̄U ) Φk (x̄U ) , B̂ā,k := EȳU ∼µ⊗U BE,ā (ȳU ) Ψk (ȳU ) ,
                            A                                                      B


where k runs over Alice-multi-indices (0 ≤ kj < |X |) and Bob-multi-indices (0 ≤ kj < |Y|)
respectively. Since the basis functions are real and the operators self-adjoint, all Â, B̂ are self-
adjoint.

Lemma 6.1 (exact spectral representation). For every Σ ⊆ U :
                               X        X
                    F (Σ) =                     ϱ(k) ψ Âā,k ⊗ B̂ā,k ψ ,                                   (6.1)
                                         ā∈AT     k : suppk∩Σ=∅


the sum over multi-indices k with 0 ≤ kj < min(|X |, |Y|) (larger indices contribute 0), and ϱ(k) =
Q
  j∈suppk ϱkj .


                                                                12
Proof. (Inversion.) For each matrix entry, x̄U 7→ ⟨u|Aā (x̄U )|v⟩ is a function on the finite set X U ;
expanding it in the orthonormal basis {Φk } of L2 (µ⊗U
                                                    A ) gives, pointwise,
                                        X                                            X
                         Aā (x̄U ) =        Âā,k Φk (x̄U ),      BE,ā (ȳU ) =        B̂ā,k′ Ψk′ (ȳU ).
                                         k                                           k′

(Coupling diagonalization.) Under νΣ |U the slot pairs are independent, so
                                                               (
                           Y                                   Eµ [ϕs ψs′ ] = ϱs δss′                                  j∈
                                                                                                                         / Σ,
                                 cj (kj , kj′ ), cj (s, s′ ) =
       
   EνΣ Φk (x̄U )Ψk′ (ȳU ) =
                             j∈U                                EµA [ϕs ] EµB [ψs′ ] = δs0 δs′ 0                        j ∈ Σ,

using Lemma 3.1 at honest slots and, at severed slots, EµA [ϕs ] = ⟨ϕs , ϕ0 ⟩ = δs0 (orthonormality).
Hence only the terms with k′ = k (entrywise) and suppk∩ Σ = ∅ survive, with coefficient j ∈Σ
                                                                                           Q
                                                                                              / ϱkj ·
              (k)
Q
  j∈Σ 1 = ϱ       (recall ϱ0 = 1; and if some kj ≥ min(|X |, |Y|) then ϱkj = 0, killing the term).
Substituting the two expansions into (5.3) and interchanging the finite sums with the expectation
yields (6.1).

Grouped coefficients.              For W ⊆ U define
                                         X        X
                          gT,z̄T (W ) :=                              ϱ(k) ψ Âā,k ⊗ B̂ā,k ψ       ∈ R,
                                              ā∈AT   k : suppk=W

so that (6.1) reads                                    X
                                   F (Σ) =                       gT,z̄T (W )         (Σ ⊆ U ).                                   (6.2)
                                                W ⊆U : W ∩Σ=∅

(Realness: each Â ⊗ B̂ is self-adjoint, so each bracket is real.)

Lemma 6.2 (coefficient ledger). Let m := min(|A|, |B|). Then for every (T, z̄T ) with |T | = t:
                                X
                                    ρ−|W | gT,z̄T (W ) ≤ mt/2 .                                (6.3)
                                              W ⊆U

Proof. Step 1 (massQledger). Fix ā. By the completeness relation (3.2), tensorized over U ,
               ′
P
  k k U )Φk (x̄U ) =
   Φ   (x̄           j∈U δxj x′j /µA (xj ), whence

X                           h                      X                    i
        2
            = Ex̄U ,x̄′ ∼µ⊗U Aā (x̄U )Aā (x̄′U )   Φk (x̄U )Φk (x̄′U ) = Ex̄U Aā (x̄U )2 ⪯ Ex̄U Aā (x̄U ) =: Āā ,
                                                                                                          
     Âā,k
                     U     A
 k                                                     k

using 0 ⪯ A ⪯ I ⇒ A2 ⪯ A. Likewise k B̂ā,k   2 ⪯ E [B
                                           P
                                                    ȳU E,ā ] =: B̄ā . Setting αā := ⟨ψ|Āā ⊗ I|ψ⟩ and
βā := ⟨ψ|I ⊗ B̄ā |ψ⟩, we get
                                            2                              2
                         X                            X
                              (Âā,k ⊗ I)ψ ≤ αā ,      (I ⊗ B̂ā,k )ψ ≤ βā .                       (6.4)
                               k                                        k
       P
Note      ā αā = ⟨ψ|I ⊗ I|ψ⟩ = 1 (completeness of {Aā }), and
               X                   X                                                              X
                     BE,ā =            #{ā : (ā, b̄) ∈ E} Bb̄ ⪯ |A|t I             =⇒                 βā ≤ |A|t .            (6.5)
                ā             b̄∈BT                                                                ā


                                                                 13
   Step 2 (double Cauchy–Schwarz). Using ⟨ψ|Â ⊗ B̂|ψ⟩ = ⟨(Â ⊗ I)ψ, (I ⊗ B̂)ψ⟩ (self-
adjointness), Cauchy–Schwarz in ℓ2 over k, then (6.4), then Cauchy–Schwarz over ā with (6.5):
                                                           s        s
           XX                              X√ p              X       X
                  ⟨ψ|Âā,k ⊗ B̂ā,k |ψ⟩ ≤    αā βā ≤         αā    βā ≤ |A|t/2 .       (6.6)
             ā       k                                  ā                          ā         ā


Since ϱ(k) ρ−w(k) ≤ 1 (each factor ϱkj ≤ ρ for kj ̸= 0), the triangle inequality gives
                  X                              XX
                      ρ−|W | gT,z̄T (W ) ≤                    ρ−w(k) ϱ(k) ⟨ψ|Âā,k ⊗ B̂ā,k |ψ⟩ ≤ |A|t/2 .        (6.7)
                  W                               ā    k

   Step 3 (player exchange via uniqueness of the    P grouped coefficients). The functional
F is symmetric between the players: writing AE,b̄ := ā:(ā,b̄)∈E Aā , we have from (5.3)
                                  X                                     X
                  F (Σ) = EνΣ               ⟨ψ|Aā ⊗ Bb̄ |ψ⟩ = EνΣ              ⟨ψ|AE,b̄ (x̄U ) ⊗ Bb̄ (ȳU )|ψ⟩.
                                (ā,b̄)∈E                               b̄∈BT

Repeating the construction of Lemma 6.1 and Steps P      1–2 with the roles of the players exchanged
(coarse POVM {Bb̄ }, event-aggregated {AE,b̄ }; now b̄ ⟨ψ|I ⊗ B̄b̄ |ψ⟩ = 1 and b̄ AE,b̄ ⪯ |B|t I)
                                                                                   P
                                                  ′
produces a second family of grouped coefficients gT,z̄   (W ) with
                                                       T

                              X                                         X
                                      ′
                  F (Σ) =            gT,z̄ T
                                             (W )       ∀Σ ⊆ U,                 ρ−|W | |gT,z̄
                                                                                         ′
                                                                                              T
                                                                                                (W )| ≤ |B|t/2 .
                            W ∩Σ=∅                                       W

Now observe that the system of groupedP coefficients is uniquely determined by the function Σ 7→
F (Σ): the linear map g 7→ F , F (Σ) = W ⊆U \Σ g(W ), is inverted by Möbius inversion,
                                                       X
                                                              (−1)|W \V | F U \ V ,
                                                                                 
                                        g(W ) =
                                                       V ⊆W

                                       |W \V |             ′                 ′                     |W \V | =
                           P                   P                 P             P
as one checks directly:       V ⊆W (−1)         W ′ ⊆V g(W ) =      W ′ g(W )    V : W ′ ⊆V ⊆W (−1)
P         ′               ′
                     |W \W | = g(W ) (only W ′ = W survives; note W ′ ⊆ V forces W ′ ⊆ W ). Since
   W ′ g(W ) (1 − 1)
                                                         ′
(6.2) holds for all Σ ⊆ U for both systems, gT,z̄T = gT,z̄   , and (6.3) follows by taking the minimum
                                                           T
of the two bounds.

Averaged coefficients.       For 0 ≤ t ≤ M and 0 ≤ w ≤ N − t define
                            h    X                  i
            c(t)
             w   := E  E
                      T z̄T              gT,z̄T (W )  (T uniform t-subset, z̄T ∼ µ⊗T ).                            (6.8)
                                  W ⊆U : |W |=w

These are real numbers depending only on S (and N, t) — in particular not on φ, on M , or on
anything else from §5. Taking expectations in (6.3) (triangle inequality):
                                                 N
                                                 X −t
                                                        ρ−w c(t)
                                                             w   ≤ mt/2 .                                          (6.9)
                                                 w=0


                                                                 14
7    The occupancy profile
                                                 (t)
Definition. For 0 ≤ t ≤ M let Hw denote a hypergeometric random variable: the size of the
intersection |W ∩ C ′ | of a fixed w-element subset W of an (N − t)-element set with a uniformly
                                                 (M )
random (M − t)-subset C ′ of it. (For t = M , Hw ≡ 0.) Define
                    N −t                                     M                                   
                    X            H (t)                     X                                  M t
       Q
       e t (z) :=          c(t)
                            w E z
                                   w
                                         ,         G(z) :=         πt Q
                                                                      e t (z),   πt =               ℓ (1 − ℓ)M −t .   (7.1)
                                                                                                t
                    w=0                                      t=0

Lemma 7.1 (profile identity, floor, segment cap). With the standing data of §5 (N ≥ M ≥ 1,
strategy S, and λ = (1 − q)(1 − φ)):
    (i) G is a real polynomial of degree ≤ M , determined by S and (N, M ) alone.
    (ii) For every φ ∈ [0, 1]: val Rφ [S] = G (1 − q)(1 − φ) .
    (iii) 0 ≤ G(λ) ≤ 1 for every λ ∈ [0, 1].
    (iv) G(1) ≥ val(S).
    (v) If M ≥ M1 then 0 ≤ G(λ) ≤ e−δB M for every λ ∈ [0, 1 − q].
                 (t)               (t)
Proof. (i) E[z Hw ] = h≥0 Pr[Hw = h] z h is a polynomial in z of degree ≤ min(w, M − t) ≤ M
                        P
                                          (t)
with real coefficients, and the cw are real (Lemma 6.2 / (6.8)).
   (ii) Start from (5.4) and evaluate the three inner expectations using (6.2). For fixed (T, z̄T , C ′ )
and Σ ⊆ C ′ i.i.d. (1 − λ),
                                                                                      ′
                               X                               X
               EΣ FT,z̄T (Σ) =     gT,z̄T (W ) Pr[W ∩ Σ = ∅] =      gT,z̄T (W ) λ|W ∩C | ,
                                     W ⊆U                                        W ⊆U

since W ∩ Σ = ∅ iff every slot of W ∩ C ′ escaped severance (slots of W \ C ′ are never severed), which
                       ′
has probability λ|W ∩C | by independence. Averaging over the uniform (M −t)-subset C ′ of U : for
                                                                    (t)                 ′              (t)
fixed W with |W | = w, |W ∩ C ′ | has the law of Hw , so EC ′ λ|W ∩C | = E[λHw ], which depends on
W only through w. Hence
                                             X X                  (t) 
                        EC ′ EΣ FT,z̄T (Σ) =          gT,z̄T (W ) E λHw .
                                                        w      |W |=w

                                        (t)
Averaging over (T, z̄T ) (the law of Hw does not depend on them) gives ET,z̄T EC ′ EΣ F = Q
                                                                                          e t (λ) by
                                              P
(6.8), and then (5.4) gives val(Rφ [S]) = t πt Qt (λ) = G(λ) at λ = (1 − q)(1 − φ). All sums are
                                                     e
finite, so every interchange is legitimate.
    (iii) For any λ ∈ [0, 1] — whether or not of the form (1 − q)(1 − φ) — the same computation
run backwards shows
                                  X                                              
                         G(λ) =       πt ET,z̄T EC ′ EΣ∼iid(1−λ) on C ′ FT,z̄T (Σ) ,
                                             t

an average of numbers FT,z̄T (Σ) ∈ [0, 1] under a perfectly well-defined probability law (no realiz-
ability by strategies is needed for this step). Hence G(λ) ∈ [0, 1].
    (iv) At λ = 1: E[1H ] = 1, so Q   e t (1) = P c(t)
                                                                        
                                                  w w = ET,z̄T FT,z̄T (∅) by (6.2) with Σ = ∅. But
FT,z̄T (∅) is the probability that S wins all coordinates of T when all N slots carry honest questions
with the T -slots conditioned to equal z̄T ; averaging z̄T ∼ µ⊗T gives

              Ez̄T FT,z̄T (∅) = Pr [ S wins all of T ] ≥ Pr [ S wins all of [N ] ] = val(S),
                                    µ⊗N                                   µ⊗N


                                                               15
since the                                                             e t (1) ≥ val(S) for every t, and
        Pwin-all  event is contained in every win-T event. Hence Q
G(1) = t πt Qt (1) ≥ val(S).
              e
    (v) For λ ∈ [0, 1 − q] take φ := 1 − λ/(1 − q) ∈ [0, 1]: by (ii), (5.2) and Theorem 4.2, G(λ) =
val(Rφ [S]) ≤ val∗ (G⊗M
                      ⊥ )≤e
                              −δB M ; the lower bound is (iii).


Lemma 7.2 (disk bound). Let
                         N −M +1                                √       √
      R := 1 + ln(1/ρ)           > 1,             b := 1 − ℓ + ℓ m = 1 + m−1
                                                                          16 ,         Ξ := bM .
                            M
Then |G(z)| ≤ Ξ for all z ∈ C with |z| ≤ R. (The bound is uniform over all strategies S for G⊗N .)
Proof. Step 1 (hypergeometric MGF bound). We claim: for all 0 ≤ t ≤ M and 0 ≤ w ≤ N −t,
                                            (t) 
                                          E RHw ≤ ρ−w .                                            (7.2)

If t = M or w = 0 then H ≡ 0 and the claim is trivial (1 ≤ ρ−w ). Otherwise put n := N − t,
K := M − t ≥ 1 and note the key identity

                             n−K +1 = N −M +1                  for every t,

so that, with Rt := 1 + ln(1/ρ) n−K+1      K
                                                                                                K
                                               , we have R ≤ Rt (because K ≤ M ) and (R − 1) n−K+1  ≤
ln(1/ρ).
    Case w ≤ n − K + 1. Sample C ′ by K sequential            P draws without replacement and let ξi
indicate that draw i hits the fixed w-set W , so H = i≤K ξi . For every i ≤ K and any history,
                                    w
Pr[ξi = 1 | ξ1 , . . . , ξi−1 ] ≤ n−i+1       w
                                        ≤ n−K+1   =: p∗ ≤ 1 (the numerator — remaining marked elements
— is at most w; the denominator is the remaining population). Hence, by induction on K using
E[Rξi | past] = 1 + (R − 1) Pr[ξi = 1 | past] ≤ 1 + (R − 1)p∗ (valid since R ≥ 1),

                                        ∗ K
                                                              wK    
                                                                       ≤ exp w ln(1/ρ) = ρ−w .
           H                                                                       
         E R ≤ 1 + (R − 1)p                  ≤ exp (R − 1)
                                                            n−K +1
   Case w > n − K + 1. Always H ≤ K, so E[RH ] ≤ RK and, using ln R ≤ R − 1 and R ≤ Rt ,

                    K ln R ≤ K(Rt − 1) = ln(1/ρ) (n − K + 1) < ln(1/ρ) w,

whence RK ≤ ρ−w .
                                        (t)           (t)   (t) 
   Step 2 (assembly). For |z| ≤ R: E[z Hw ] ≤ E |z|Hw ≤ E RHw ≤ ρ−w , so by (6.9)
                                                 

                                        X
                                                   −w
                              e t (z) ≤
                              Q             c(t)
                                             w ρ      ≤ mt/2 ,
                                              w

and by the binomial theorem
                             M  
                             X  M                                    √ M
                   G(z) ≤              ℓt (1 − ℓ)M −t mt/2 =    1−ℓ+ℓ m   = Ξ.
                                   t
                             t=0

Remark (the mechanism). Lemma 7.2 is where the board length N/M is used, and the only place.
To respond at order h to the severance parameter, the profile needs spectral weight whose support
hits the random (M −t)-window C ′ in h slots; weight at level w does so with hypergeometric
probability ≲ (wM/N )h , while the ledger (6.9) caps the total level-w weight at mt/2 ρ w . The net
h-th Taylor coefficient of G is geometrically small at scale M/(N ln(1/ρ)) — which is precisely
analyticity control on the disk of radius R ≈ ln(1/ρ)N/M .

                                                  16
8    The two-constants lemma
Lemma 8.1. Let 0 < q ≤ 21 , L := 1 − q, R > 1, 0 < ε ≤ Ξ, and let f be analytic on a neighborhood
of D(0, R) := {|z| ≤ R} (a polynomial suffices), with

                         |f | ≤ ε on E := [0, L],          |f | ≤ Ξ on D(0, R).

Then                                                  √
                                                     4 q    Ξ
                                   ln f (1) ≤ ln ε +      ln .
                                                     ln R   ε
Proof. If f ≡ 0 the claim is vacuous (ln |f (1)| = −∞); assume f ̸≡ 0, so ln |f | is subharmonic on C
(standard: locally ln |f | is either harmonic or −∞ at isolated zeros, and it is upper semicontinuous
with the sub-mean-value property).

The explicit harmonic majorant.           Define, for ζ ∈ C \ [−1, 1],

                         h(ζ) := (ζ − 1)1/2 (ζ + 1)1/2 ,       ϕ(ζ) := ζ + h(ζ),

with principal branches of the square roots. Facts, each verified below: (F1) h, hence ϕ, is analytic
on C\[−1, 1]; (F2) ϕ(ζ)+ϕ(ζ)−1 = 2ζ and ϕ has no zeros; (F3) |ϕ(ζ)| → 1 as ζ approachesp any point
of [−1, 1], and |ϕ(ζ)| ≥ 1 everywhere on C \ [−1, 1]; (F4) for real ζ > 1, ϕ(ζ) = ζ + ζ 2 − 1 > 1.
    (F1): each factor is analytic off its cut (ζ ≤ 1 resp. ζ ≤ −1); on the overlap
                                                                               p (−∞, −1)p the prod-
                                                                                                   
uct is continuous across the cut — approaching x < −1 from above gives i |x − 1| i |x + 1| =
   p                                            √
− (x − 1)(x + 1) and from below (−i)(−i) · · ·, the same value — so by Morera’s theorem h ex-
tends analytically across (−∞, −1); the remaining cut is [−1, 1]. (F2): h2 = ζ 2 − 1, so ϕ · (ζ − h) =
ζ 2 − h2 = 1; thus ϕ√̸= 0 and ϕ−1 = ζ − h,                   −1
                                             √ giving ϕ + ϕ = 2ζ. (F3): as ζ → x ∈ [−1, 1] (from
either side), h → ±i 1 − x2 , so ϕ → x ± i 1 − x2 , of modulus 1; for the global lower bound, apply
the maximum principle to the analytic function ϕ−1 on Ωr := D(0, r) \ [−1, 1] for large r. On the
circle |ζ| = r (for r large): for |ζ| > 1 we have h(ζ) = ζ (1 − ζ −2 )1/2 — both sides are analytic on
|ζ| > 1 (note |ζ −2 | < 1 there, so Re(1 − ζ −2 ) > 0 and the principal square root is analytic), both
square to ζ 2 − 1, and both are positive at real ζ > 1, so they agree on the connected set |ζ| > 1 by
the identity theorem. Hence h(ζ) = ζ (1 + O(r−2 )) and ϕ(ζ) = ζ + h(ζ) = 2ζ (1 + o(1)) uniformly
on |ζ| = r, so sup|ζ|=r |ϕ−1 | → 0 as r → ∞; and lim sup |ϕ−1 | ≤ 1 on the segment boundary by
the first part of (F3). The maximum principle on the bounded domain Ωr (boundary = circle ∪
segment) gives |ϕ−1 | ≤ max(1, sup|ζ|=r |ϕ−1 |) → max(1, 0) = 1, i.e. |ϕ| ≥ 1 on all of C \ [−1, 1].
(F4): for real ζ > 1 both square roots are positive reals.
    Now transfer to the segment E = [0, L]: let ζ(z) := 2z−L    L    (affine, maps E onto [−1, 1], and
            2−L     1+q
1 7→ ζ1 := L = 1−q ), and define

                                g(z) := ln ϕ(ζ(z))          (z ∈ C \ E).

Then g is harmonic on C \ E (ϕ ◦ ζ analytic and zero-free there), g ≥ 0 by (F3), and g extends
continuously to all of C with g ≡ 0 on E (by (F3); including the endpoints, where ϕ → ±1).

                                                     ζ12 − 1 = arccosh ζ1 = arccosh 1+q
                                                    p       
(a) Value at z = 1. By (F4), g(1) = ln ζ1 +                                         1−q . We bound
                                    1+s
this by an integral: with ζ1 (s) := 1−s ,

            d          1+s       1         2       1−s     2            1
               arccosh     =p          ·        2
                                                  = √ ·         2
                                                                  =√
            ds         1−s   ζ1 (s) − 1 (1 − s)
                                   2                2 s (1 − s)      s (1 − s)

                                                    17
                       4s
(using ζ1 (s)2 − 1 = (1−s) 2 ), and the value at s = 0 is arccosh(1) = 0. Hence

                         Z q                       Z q           √
                                    ds        1             ds  2 q    √
                g(1) =         √           ≤                √ =     ≤ 4 q          (q ≤ 12 ).         (8.1)
                          0      s (1 − s)   1−q       0     s  1−q

(b) Minimum on |z| = R. From (F2) and (F3): 2|ζ| ≤ |ϕ| + |ϕ|−1 ≤ |ϕ| + 1, so |ϕ(ζ)| ≥ 2|ζ| − 1.
For |z| = R: |ζ(z)| = |2z−L|
                         L   ≥ 2R−L
                                 L , hence |ϕ(ζ(z))| ≥
                                                       4R−2L
                                                         L   − 1 = 4R−3L
                                                                     L   ≥ 4R − 3 ≥ R (using
L ≤ 1 ≤ R twice). Therefore
                                  mR := min g ≥ ln R > 0.                                (8.2)
                                               |z|=R


(c) Comparison.       On the bounded open set Ω := D(0, R) \ E define
                                                   h       g(z)            i
                               u(z) := ln |f (z)| − ln ε +      ln Ξ − ln ε .
                                                           mR

The bracket is harmonic on Ω, so u is subharmonic on Ω. Boundary behavior (∂Ω ⊆ E ∪{|z| = R}):
at every point of {|z| = R}, g ≥ mR and ln Ξ − ln ε ≥ 0, so the bracket is ≥ ln Ξ ≥ lim sup ln |f |;
at every point ζ0 ∈ E (endpoints included), g is continuous with g(ζ0 ) = 0 and f is continuous
with |f (ζ0 )| ≤ ε, so lim supz→ζ0 u(z) ≤ ln ε − ln ε = 0. By the maximum principle for subharmonic
functions on a bounded open set, u ≤ 0 on Ω. Since 0 < L < 1 < R, the point 1 lies in Ω; evaluating
there and using (8.1), (8.2) and ln(Ξ/ε) ≥ 0:
                                                                     √
                                                g(1) Ξ              4 q Ξ
                            ln |f (1)| ≤ ln ε +      ln    ≤ ln ε +      ln .
                                                mR      ε           ln R   ε

9     Assembly: proof of the Main Theorem
Theorem 9.1 (connected case). Let G be connected       √
                                                            with full marginals and val∗ (G) < 1. With
β = 43 , q = 52 , ℓ = 16
                      1
                         , m = min(|A|, |B|), b = 1 + m−116 , ρ ∈ [ 2 , 1) as in §3, and δB ∈ (0, 1], M1 ≥ 1
                                                                    1

as in Theorem 4.2, define
                √             
            16 q δB + ln b                     ln(1/ρ)           1
                                                                                  l      2M
                                                                                               1   4 m
     Λ :=                       ,   θ0 :=                  ∈  0, 2  ,       N 0 :=   max         ,      .
                     δB                    ln(1/ρ) + eΛ                                     θ0     θ0

Then                                                          
                   vN = val∗ G⊗N            ≤ exp − 38 δB θ0 N
                                        
                                                                      for all N ≥ N0 ,

and hence vN ≤ C(G) e−c(G)N for all N ≥ 1 with c(G) := 38 δB θ0 > 0 and C(G) := ec(G)N0 .

Proof. First the bookkeeping. θ0 ≤ 12 because ln(1/ρ) ≤ ln 2 ≤ eΛ . Fix N ≥ N0 and set
                                                       
                                       M := θ0 (N + 1) .

Then:

    • M ≤ θ0 (N + 1) ≤ N 2+1 ≤ N (as N ≥ 1), and

    • M ≥ θ0 (N + 1) − 1 ≥ θ0 N0 − 1 ≥ 2M1 − 1 ≥ M1 ≥ 1 (using N ≥ N0 ≥ 2M1 /θ0 and M1 ≥ 1).


                                                       18
Moreover
                        N −M +1   N +1      1          eΛ
                                ≥      −1 ≥    −1 =         ,
                           M       M        θ0      ln(1/ρ)
so the radius of Lemma 7.2 satisfies
                                 N −M +1
                                         ≥ 1 + eΛ ,                 ln R ≥ ln 1 + eΛ
                                                                                          
              R = 1 + ln(1/ρ)                                                                 ≥ Λ.   (9.1)
                                    M
    Now fix an arbitrary strategy S for G⊗N . If val(S) = 0 there is nothing to prove; otherwise set
u := − ln val(S) ∈ [0, ∞). Form the occupancy profile G of §7 for this (S, N, M ). By Lemma 7.1(i)
G is a polynomial, hence entire; by Lemma 7.1(v) (applicable since M ≥ M1 ), |G| ≤ ε := e−δB M
on E = [0, 1 − q]; by Lemma 7.2, |G| ≤ Ξ = bM on D(0, R). Note 0 < ε ≤ 1 ≤ Ξ and q = 25 ≤ 12 .
Lemma 8.1 applies and gives, with Lemma 7.1(iv),
                                        √
                                       4 q               
  − u = ln val(S) ≤ ln G(1) ≤ −δB M +       · M δB + ln b
                                       ln R
                                    (9.1)
                                                    √
                                                   4 q (δB + ln b)             δB
                                     ≤ −δB M +                     M = −δB M +    M,
                                                           Λ                    4
by the definition of Λ. Hence
                        3             3                         3       1            3
                                                        
                 u ≥    4 δB M    ≥   4 δB   θ0 N − 1       ≥   4 δ B · 2 θ0 N   =   8 δB θ0 N,

using M ≥ θ0 (N + 1) − 1 ≥ θ0 N − 1 and θ0 N ≥ θ0 N0 ≥ 4 ≥ 2 (so θ0 N − 1 ≥ 21 θ0 N ). That
                3
is, val(S) ≤ e− 8 δB θ0 N for every strategy S; taking the supremum over S proves the display. For
1 ≤ N < N0 , use vN ≤ 1 ≤ ec(G)N0 e−c(G)N .

Corollary 9.2 (Main Theorem, general case). Every game G with val∗ (G) < 1 satisfies val∗ (G⊗n ) ≤
C(G)e−c(G)n for all n ≥ 1, with explicit constants.
Proof. Reduce to full marginals (§1.1). If the support graph is connected, apply Theorem 9.1.
Otherwise, by Lemma 2.1 choose a component κ∗ with p∗ = pκ∗ > 0 and val∗ (Gκ∗ ) < 1; the
                                                                                            ∗
component game is connected with full marginals, so Theorem 9.1 supplies vk (Gκ∗ ) ≤ C ∗ e−c k for
all k ≥ 1, and Proposition 2.2 gives
                                  ∗ ∗       ∗                      ∗ ∗     ∗
                vn (G) ≤ C ∗ e−c p n/2 + e−p n/8 ≤ C ∗ + 1 e− min(c p /2, p /8) n .
                                                          

     This completes the proof of the Main Theorem. ■


10     Concluding remarks
10.1 Logical dependencies. The proof uses: Lemmas 1.1–1.3 (elementary operator algebra);
§2 (elementary probability); Lemma 3.1 (linear algebra; the connectivity ⇒ ϱ1 < 1 step is proved
inline); Lemma 4.1 (elementary); Theorem 4.2 = Bavarian–Vidick–Yuen anchored parallel
repetition [1] — the unique external input; Lemma 5.2 (exact probability bookkeeping for the
constructed family); Lemmas 6.1–6.2 (Fourier inversion, Parseval/Cauchy–Schwarz, Möbius inver-
sion); Lemmas 7.1–7.2 (conditioning + hypergeometric MGF); Lemma 8.1 (classical two-constants
argument, proved in full); §9 (arithmetic). The standard background facts invoked without proof
are: the multiplicative Chernoff bound; subharmonicity of ln |f | for analytic f ; the maximum prin-
ciple for subharmonic (and analytic) functions on bounded domains; Morera’s theorem; and the
singular value decomposition. All are textbook classical.

                                                    19
10.2 Quantifier hygiene. For fixed (N, M ) the polynomial G depends on the strategy S, but
every bound applied to it — the segment cap e−δB M (via Theorem 4.2), the disk bound bM , and the
two-constants inequality — is uniform in S. Only the floor G(1) ≥ val(S) refers back to S’s quality.
Consequently the argument requires no selection of near-optimal strategies, no amortization across
scales, and no hypotheses on how vN varies with N ; it bounds each vN directly.

10.3 Edge cases and checks. (a) If m = 1 (some player has a single answer) then b = 1,
Ξ = 1: the profile is bounded by 1 on the large disk, and the theorem still runs. (b) Product
µ: ϱ1 = 0, ρ = 21 by convention; fine. (c) Disconnected µ: ϱ1 = 1, R = 1, and Lemma 8.1
degenerates (ln R = 0) — as it must, since for disconnected supports the routed-severance method
genuinely fails at this step; §2 removes disconnectedness beforehand. (d) val∗ (G) = 1: δB does not
exist; the argument never starts (as it must not). (e) The honest product strategy for G⊗N has
            1
u = N ln 1−ε  0
                , and our bound yields u ≥ 38 δB θ0 N — consistent, since necessarily δB ≤ ln 1−ℓε
                                                                                                1
                                                                                                  0
                                                                                                    (the
                                                                                     M
M -fold product of the honest anchored strategy witnesses vM (G⊥ ) ≥ (1 − ℓε0 ) , so Theorem 4.2
forces this) and θ0 < 1. (f) Games with v2 = v1 < 1 (Feige-type [7]) are consistent: the bound
bites only at N ≥ N0 and C(G) = ecN0 absorbs small N .

10.4 Effectiveness. c(G) and C(G) are explicit in (ε0 , β, |A|, |B|, ρmax (µ), δB , M1 ); given any
effective form of the Bavarian–Vidick–Yuen constants [1], the final constants are effective. The rate
obtained is of the shape c(G) ≈ 83 δB e−Λ ln(1/ρ) with Λ = O (δB + ln m)/δB — exponentially
small in 1/δB , but a constant depending on G only, which is all that the Main Theorem requires.

10.5 Why the wall at λ = 1 − q cannot be approached directly. One-sided anchored
coordinates force severance: when exactly one player receives ⊥, the pair (real question, locally
generated substitute) is a product distribution by no-signaling — no local filling rule can recreate
the correlation of µ. This is why the realizable segment of the profile ends at 1 − q, and why an
analytic continuation — powered by the ledger and paid for by the board length — rather than a
direct evaluation, is used to reach λ = 1.


References
 [1] M. Bavarian, T. Vidick and H. Yuen, Hardness amplification for entangled games via anchoring,
     in: Proceedings of the 49th Annual ACM SIGACT Symposium on Theory of Computing
     (STOC 2017), ACM, 2017, pp. 303–316.

 [2] A. Chailloux and G. Scarpa, Parallel repetition of entangled games with exponential decay via
     the superposed information cost, in: Automata, Languages, and Programming (ICALP 2014),
     Lecture Notes in Comput. Sci. 8572, Springer, 2014, pp. 296–307.

 [3] R. Cleve, P. Høyer, B. Toner and J. Watrous, Consequences and limits of nonlocal strategies,
     in: Proceedings of the 19th IEEE Conference on Computational Complexity (CCC 2004),
     IEEE, 2004, pp. 236–249.

 [4] R. Cleve, W. Slofstra, F. Unger and S. Upadhyay, Perfect parallel repetition theorem for quan-
     tum XOR proof systems, Comput. Complexity 17 (2008), 282–299.

 [5] I. Dinur and D. Steurer, Analytical approach to parallel repetition, in: Proceedings of the 46th
     Annual ACM Symposium on Theory of Computing (STOC 2014), ACM, 2014, pp. 624–633.


                                                  20
 [6] I. Dinur, D. Steurer and T. Vidick, A parallel repetition theorem for entangled projection games,
     Comput. Complexity 24 (2015), 201–254.

 [7] U. Feige, On the success probability of the two provers in one-round proof systems, in: Proceed-
     ings of the 6th Annual Structure in Complexity Theory Conference, IEEE, 1991, pp. 116–123.

 [8] H. Gebelein, Das statistische Problem der Korrelation als Variations- und Eigenwertproblem
     und sein Zusammenhang mit der Ausgleichsrechnung, Z. Angew. Math. Mech. 21 (1941), 364–
     379.

 [9] H. O. Hirschfeld, A connection between correlation and contingency, Math. Proc. Cambridge
     Philos. Soc. 31 (1935), 520–524.

[10] T. Holenstein, Parallel repetition: simplification and the no-signaling case, Theory of Com-
     puting 5 (2009), 141–172.

[11] R. Jain, A. Pereszlényi and P. Yao, A parallel repetition theorem for entangled two-player
     one-round games under product distributions, in: Proceedings of the 29th IEEE Conference on
     Computational Complexity (CCC 2014), IEEE, 2014, pp. 209–216.

[12] J. Kempe, O. Regev and B. Toner, Unique games with entangled provers are easy, SIAM J.
     Comput. 39 (2010), 3207–3229.

[13] T. Ransford, Potential Theory in the Complex Plane, London Mathematical Society Student
     Texts 28, Cambridge University Press, 1995.

[14] A. Rao, Parallel repetition in projection games and a concentration bound, SIAM J. Comput.
     40 (2011), 1871–1891.

[15] R. Raz, A parallel repetition theorem, SIAM J. Comput. 27 (1998), 763–803.

[16] A. Rényi, On measures of dependence, Acta Math. Acad. Sci. Hungar. 10 (1959), 441–451.

[17] H. Yuen, A parallel repetition theorem for all entangled games, in: Automata, Languages, and
     Programming (ICALP 2016), LIPIcs 55, Schloss Dagstuhl, 2016, Art. 77.


                                                 21
