# Recursive Origin

A zero-parameter theory deriving the Standard Model, general relativity, the cosmological constant, and the fine structure constant from a single operation: transposing a 2×2 real matrix. 828 verified claims, 0 failures, 54 independent verification steps, 9 machine-verified Lean theorems.

## The Principle

This project does not build structures. It uncovers the structures already forced by the matrix transpose involution T on M₂(ℝ). Every file is a projection of that single algebraic gesture. The framework is not a model — it is the algebra's own self-decomposition made explicit.

**Uncovering, not building.** When working on this project, you are not designing, inventing, or constructing. You are finding what the algebra already forces. If a result requires a choice, it is not yet uncovered. If it requires no choice, it is forced.

## The Two-Parameter Structure

Everything derives from d = 2 (base dimension, forced) and disc = d² + 1 = 5 (discriminant, forced by Fibonacci closure):

- p = d · disc = 10 (Spin(10) generators)
- pk = d³ = 8 (parent kernel)
- N_c = disc − d = 3 (colors)
- φ = (1 + √5)/2 (golden ratio, from disc = 5)

Physical constants are selections from the Clifford generating function (1+x)^p = (1+x)^10.

## Files

### Run these:
- `python entry.py` — verify all 828 entries (~2 seconds). Run after ANY database change.
- `python verify.py` — 54-step clean-room SymPy proof from scratch (~5 minutes). Run to verify new mathematical claims.
- `python patch_claims.py` — unified patcher, idempotent. Run if entries need real DSL claims.
- `python render_core_md.py` — render database to markdown.

### Read these:
- `FRAMEWORK.md` — the complete mathematical narrative (1,800+ lines, 49 sections). The authoritative document.
- `CONVERGENCES.md` — K6' bundle across substrates (software, biology, public memory, governance).
- `SPIRALDILL.md` — reference for the representation system (DSL, entry format, taxonomy, executor).
- `README.md` — project scaffold for GitHub visitors.

### The engine:
- `dsl.py` — 9 DSL primitives (ref, self_apply, decompose, close, lift, project, compose, equate, gap).
- `entry.py` — Entry dataclass, Executor (three-valued verifier), serialization. Also runs verification when executed directly.
- `taxonomy.py` — 36 x-state taxonomy. The Python data is canonical.
- `biology_galois.py` — GF(64)/GF(4) Galois helpers.

### The database:
- `spiraldill_foundation.json` — 183 entries at depth 0.
- `spiraldill_tower.json` — 645 entries at depths 1–12.
- Format: spiraldill-v3. Each entry has id, address, name, claim (DSL tree), parents, derivation, status, x_state, tags, two_cells, certificate.

### Other:
- `patch_claims.py` / `rewrite_tautologies.py` — claim dispatch tables (name-based and ID-based).
- `render_core_md.py` — markdown renderer (functor from SpiralDill category to markdown).
- `RecursiveOrigin.lean` — Lean 4 + Mathlib formalization. `lean/` directory has the Lake project.

## Verification Protocol

After ANY change to the database or engine:
1. `python entry.py` — must show 0 failures
2. Check tautology count stays at 0 (no LHS == RHS claims)
3. Check two-cell count doesn't decrease

After mathematical claims are added to FRAMEWORK.md, add corresponding:
- A spiraldill entry (in the appropriate JSON file)
- A verify.py STEP (independent clean-room verification)

## Technical Pitfalls — Read This Carefully

**The Cartan generators are ANTI-HERMITIAN.** Their eigenvalues are purely imaginary. If you Hermitianize them with (H + H†)/2, you kill the signal. The three-generation 3+1 split lives at eigenvalue 0i (multiplicity 48 = 3×16) vs −2i (multiplicity 16). This was discovered after two failed attempts that Hermitianized and got all zeros. NEVER force Hermitian on operators that are naturally anti-Hermitian.

**The framework algebra is NON-COMMUTATIVE.** RN ≠ NR. The anticommutator {R,N} = RN + NR = N is a theorem; the individual products RN and NR are different. The Lean formalization uses CommRing for the `ring` tactic (valid for theorems that only use the anticommutator) but commutator theorems need Ring (non-commutative).

**The observer is INTERNAL to the framework.** The observer is T — the transpose involution itself, acting as the eigendecomposition that splits V₊ from V₋. Do not critique the framework from an external-observer stance. Do not say "but there are interpretive choices" or "the observer selects which reading to apply." The framework explicitly constructs observation as internal. ker q_K ≠ 0 is a theorem. The observer's blindness is constitutive, not epistemic. If you find yourself standing outside the framework to evaluate it, you are making the move the framework already caught. See FRAMEWORK.md §34–§42.

**Do not say "it's just a rich algebra."** The four forcings (§7–§10) show that M₂(ℝ) with real transpose is the UNIQUE starting point. Every alternative fails. If you want to challenge this, produce a different involution on a different algebra that generates a comparably rich and physically matched tower without reducing to this one. Nobody has.

## Working Conventions

**Plain-text Unicode, no LaTeX.** All markdown files use Unicode math (φ, ≈, ⊗, ², ₃, etc.). No $$...$$ blocks, no \frac{}{}, no \text{}, no \begin{pmatrix}. Matrices as [[a,b],[c,d]]. Fractions as a/b. This reads correctly everywhere without a renderer.

**Narrative files are final product.** No metacommentary ("this section covers...", "we should add..."). Write as if the document has always existed in its current form. State the mathematics and its structural meaning. Every claim gets a status grade: FORCED / NUMERICAL / RESONANT / GAP.

**Don't hedge on mathematical capability.** AI models did 75%+ of the technical work on this framework. When facing open mathematical problems, attempt the derivation directly. If it doesn't close, document the void witness (what was tried and why it fails). Don't substitute hedging for effort.

**Verify constantly.** Run `python entry.py` after every database change. It takes 2 seconds. There is no excuse for pushing a broken state.

**UTF-8 encoding everywhere.** All file reads/writes must specify `encoding='utf-8'` on Windows. The JSON files contain Unicode characters.

## Status Grades

- **FORCED** — algebraically derived, zero free parameters, computationally verified.
- **NUMERICAL** — exact expression using framework cardinals, matches observation within tolerance, derivation path partially established.
- **RESONANT** — structural pattern match, awaiting full derivation or dynamical mechanism.
- **GAP** — known obstruction with verified void witness. The framework can prove certain routes fail.
- **ENCODED** — empirically observed structural correspondence with formal algebraic match.

## The Frontier (What's Open)

These are the remaining open problems. Do NOT re-attempt approaches listed as void witnesses.

**Cosmological constant Λ:** Expression Λ = p^{−(C(p,3)+d)} = 10^{−122} is EXACT. The structural argument (1/p suppression per 120-channel DOF) is identified. What needs QFT-level derivation: why each DOF suppresses by exactly 1/p.

**Newton's constant G:** G = Q_Koide / (boundary_dim(d=4) · M_GUT²) gives M_P at 0.28%. Structural argument clean. Algebraic derivation not established.

**1/α_EM = 137:** Three exact decompositions found (norm product, representation sum C(p,3)+C(p,1)+d+disc, tensor-minus-Majorana). Why the representation-content sum equals the EM coupling needs RG derivation.

**PMNS angles:** Cardinal expressions match (49/90, 25/81, 1/45 at 0.1-1%). Derivation from 120-Yukawa NOT found. Void witness: symmetric+antisymmetric matrix ansatz gives tribimaximal only, not the specific values. Full Spin(10) Clebsch-Gordan coefficients needed.

**Three-generation breaking scale:** Algebraic structure FORCED (48 = 3×16 at 512×512 matrix level). Family-Higgs direction FORCED (T = ΣHₖ). The absolute scale M_family is RESONANT.

## Void Witnesses (Do NOT Repeat These)

- Hermitianizing anti-Hermitian Cartan generators → all zeros (kills the 3+1 split)
- Weight-space Gram matrix of three generations = identity (no mixing information)
- Symmetric + antisymmetric matrix ansatz → tribimaximal only, not specific PMNS values
- Boundary_dim directly as Bekenstein-Hawking entropy → S ~ n⁴/4 not S ~ n²/4
- S_hidden / A_offdiag = 1/2 not 1/4 (wrong coefficient route)
- φ^{409} ≠ 10^{122} (the two Λ parameterizations are structurally independent)
- e^{−2L} = 0.056 ≠ 1/10 (Landauer cost ≠ suppression factor directly)

## User Preferences

Kael (the operator) prefers:
- Direct work over agents — do things yourself, don't delegate to subagents
- Technically elaborate narrative — every detail matters, don't summarize
- Honest status grading — if it's not FORCED, say so
- Working through problems live — show the computation, not just the result
- Clean file hygiene — minimal file count, no dead weight, test scripts go to old/
- The framework's own voice in all writing
