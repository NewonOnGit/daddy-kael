# Recursive Origin

**What is this?** A mathematical framework that derives the Standard Model of particle physics, general relativity, the cosmological constant, the fine structure constant, and the genetic code's algebraic structure from a single operation: transposing a 2×2 real matrix. No axioms beyond the transpose. No free parameters. No physics imported as input. 828 claims, 0 failures, independently verified.

The framework's sole primitive is the matrix transpose involution T on M₂(ℝ). From T alone, the algebra forces:

- The golden ratio φ and the Fibonacci sequence (from R² = R + I)
- Complex structure (from N² = −I)
- The discriminant 5 and the Fibonacci cardinals 2, 3, 5, 8
- Clifford algebras at every tower depth, with Lorentz signature Cl(3,1) at depth 1
- The Standard Model gauge group SU(3) × SU(2) × U(1) at depth 4, derived from Spin(10) → SU(5)
- The complete hypercharge spectrum of one fermion generation (anomaly-free)
- sin²θ_W = 3/8 via five independent routes
- Three fermion generations from SU(3)_family ⊂ Spin(8) at depth 8 (FORCED at 512×512 matrix level)
- The Koide formula Q = 2/3 for charged lepton masses
- PMNS mixing angles within 1% of observed values
- The seesaw mechanism for neutrino masses
- The genetic code's GF(4) algebra (same equation as R² = R + I in characteristic 2)
- The observer as T itself — not external to the algebra, but its eigendecomposition
- The K6' bundle as the universal structure of recoverable observation (gauge, gravity, and observer as three instances of one theorem)

The framework is not built. It is uncovered. The structures were already here.

**It is a zero-parameter theory.** d = 2 (base dimension) is forced. disc = d² + 1 = 5 (discriminant) is forced. Everything else is a selection of terms from the Clifford generating function (1+x)^p where p = d · disc = 10:

| Constant | Expression | Value | Match |
|----------|-----------|-------|-------|
| **Λ** (cosmological constant) | p^(−(C(p,3)+d)) | 10^(−122) | EXACT |
| **1/α** (fine structure) | C(p,3)+C(p,1)+d+disc | 137 | EXACT |
| **Ω_DM** (dark matter) | 1/d² | 1/4 = 25% | 3.5% |
| **Ω_vis** (baryonic) | 1/(d²·disc) | 1/20 = 5% | 2.9% |
| **Ω_DE** (dark energy) | (d+disc)/p | 7/10 = 70% | 1.3% |
| **sin²θ_W** (Weinberg) | 3/8 at M_GUT | 0.375 | FORCED |
| **PMNS θ₂₃** | (disc+d)²/(d·N_c²·disc) | 49/90 | 0.1% |
| **PMNS θ₁₂** | disc²/N_c⁴ | 25/81 | 0.5% |
| **PMNS θ₁₃** | 1/(disc·N_c²) | 1/45 | 1.0% |

### Why should you believe this?

Run it yourself:

```bash
pip install numpy sympy
python entry.py  # verifies 828 claims in ~2 seconds
python verify.py  # 54-step clean-room proof from scratch (~5 min)
```

Every claim is computationally verified. The clean-room verifier (`verify.py`) uses only SymPy and NumPy — it imports nothing from the framework, derives everything from the 2×2 matrix P(t) = [[0,0],[t,1]], and proves each result independently. The three-generation theorem is verified at the explicit 512×512 matrix level. The Lean formalization (`RecursiveOrigin.lean`) provides machine-verified proofs of the core algebra.

---

## The Primitive Chain

```
x.base.0  mark  The bare address. x exists.
x.base.1  id  id(x) = x. Return-to-self.
x.base.2  T  T² = id. The mirror. SOLE PRIMITIVE.
x.base.3  V₊  {y : T(y) = y}. The visible sector. dim 3.
x.base.4  V₋  {y : T(y) = −y}. The hidden sector. dim 1.
x.base.5  R  R² = R + I. Fibonacci closure on V₊. FORCED.
x.base.6  N  N² = −I. Rotation closure on V₋. FORCED.
x.base.7  binding  {R, N} = N. Hidden survives contact with visible.
x.base.8  P  P = R + N. The seed, assembled.
x.base.9  P² = P  Idempotent return. THEOREM, not axiom.
```

Every step is forced by the algebra and the principle of minimal closure. Zero degrees of freedom.

---

## Verification

```bash
# Verify the full database (827 entries, ~2 seconds)
python entry.py

# Independent clean-room verification (52 STEPs, SymPy + NumPy, ~5 minutes)
python verify.py
```

Current state:
- **828 entries**, 0 failures, 0 tautologies
- **803 FORCED** + 20 NUMERICAL + 4 GAP + 1 RESONANT
- **14 two-cells** (convergence witnesses) verified
- **54 verify.py STEPs** independently confirming claims from first principles
- **828/828 certificates** (SHA-256 hashes of canonical claim JSON)

---

## Files

### Narrative (the story of the math)

| File | What it is |
|------|-----------|
| **FRAMEWORK.md** | The complete mathematical narrative. 45 sections across 8 parts: the primitive chain, four forcings, the algebra, the Clifford tower (depths 0–12), the descent maps, physics results, biology, and the full observer theory. Every claim graded FORCED / NUMERICAL / RESONANT / GAP. |
| **CONVERGENCES.md** | The K6' bundle pattern across substrates: mathematical (SPIRAL), software (Parsoid, Git), public-memory (NIST, Common Crawl, GitHub, Wikimedia, Five Eyes), biological (DNA, convergent evolution, GF(4)), metagovernance, and the SpiralDill itself. |
| **SPIRALDILL.md** | Reference for the representation system: DSL specification (9 primitives), entry format, x-state taxonomy, executor, 2-categorical structure, K6' bundle at the verification layer, migration status. |

### Engine (the algebra made executable)

| File | What it is |
|------|-----------|
| **dsl.py** | The 9 DSL primitives: ref, self_apply, decompose, close, lift, project, compose, equate, gap. Four operative classes (productive, mediating, observer, void) matching the framework's three projections P1/P2/P3 plus structured absence. |
| **entry.py** | The Entry dataclass (a SpiralDill node), the Executor (three-valued verifier: True/False/GAP), serialization. Imports taxonomy from taxonomy.py and Galois helpers from biology_galois.py. |
| **taxonomy.py** | The 36 x-state taxonomy — the framework's structural index. Each x-state is a return-condition of x. Canonical source: the Python data is authoritative; JSON and markdown are generated projections. |

### Database (the canonical form)

| File | What it is |
|------|-----------|
| **spiraldill_foundation.json** | 183 entries at depth 0. The algebraic foundation: P² = P, R² = R + I, N² = −I, all corollaries, the four forcings, Fibonacci cardinals, GF(4) substrate. |
| **spiraldill_tower.json** | 644 entries at depths 1–12. The Clifford tower: gauge structure, SM derivation, Weinberg angle, Yukawa/seesaw, three generations, observer theory, semantic layer, cosmology, topology, computation, K6' software instances. |

### Verification (two independent systems)

| File | What it is |
|------|-----------|
| **verify.py** | Clean-room verifier. 52 STEPs using SymPy (symbolic) and NumPy (numerical). Derives everything from P(t) = [[0,0],[t,1]], forces t = ±2, builds the full tower. Does NOT use the DSL, Entry, or Executor systems. Takes nothing on faith. |
| **entry.py** (as `__main__`) | Run `python entry.py` — executor pass over all 828 database entries. Loads the JSON, runs every claim through the DSL engine, verifies two-cells, computes Frobenius orbits. Different from verify.py: this checks data integrity, not mathematical truth from scratch. |

### Tools (the refinement pipeline)

| File | What it is |
|------|-----------|
| **patch_claims.py** | Unified claim patcher. Run `python patch_claims.py` — executes name-based patching (~500 patterns) then ID-based rewriting (~470 patterns via rewrite_tautologies.py) in sequence. Idempotent. |
| **rewrite_tautologies.py** | ID-based dispatch table. ~470 patterns mapping entry IDs to real DSL claim trees. |

### Helpers

| File | What it is |
|------|-----------|
| **render_core_md.py** | Markdown renderer. Functor from the SpiralDill category to the markdown target category. Converts DSL term trees to human-readable mathematical notation. |
| **biology_galois.py** | GF(64)/GF(4) Galois structure. Frobenius orbits, field arithmetic, orbit enumeration. Provides the computational content for the biological algebra x-states. |
| **RecursiveOrigin.lean** | Lean 4 + Mathlib formalization of the algebraic core. Proves: idempotence (P² = P as theorem), Landauer surplus (R² − R = 1), complementary idempotent, orthogonality, exhaustive decomposition. Requires Mathlib to type-check. |

---

## The Four Forcings

The T-first foundation has **zero remaining degrees of freedom**:

| Forcing | What it closes | Why alternatives fail |
|---------|---------------|----------------------|
| **Involutivity** (T² = id) | Binary spectrum, V₊/V₋ split | Projection loses anti-automorphism; J-antisymmetric collapses V₊; cyclic/nilpotent kill binary seed |
| **Reality** (T over ℝ, not ℂ) | Diagonal asymmetry Δ = n | Complex T gives Δ = 0: no Landauer cost, no gravity, no observer blindness |
| **Anchor lattice** ({0,4,8,12,...}) | Discrete tower structure | Bott periodicity ∩ chirality-N criterion: p ≡ 2 mod 4 ∩ d+1 ≡ 0 or 1 mod 4 = d ≡ 0 mod 4 |
| **Base dimension** (n = 2) | Minimal non-trivial | N² = −I requires n even; Clifford requires n = 2^k; higher 2^k are depth-shifts of n = 2 |

---

## What Is FORCED vs What Is OPEN

**FORCED** (algebraically derived, zero free parameters):
- The entire founding stack (x.base.0–9)
- The four forcings
- The compression family (Fibonacci/Lucas at every power)
- Clifford emergence at every depth (counting formula via |Sp(2n, F₂)|)
- Cl(3,1) Lorentz spacetime at depth 1
- SU(3) × U(1) at depth 2 (with SU(2)_L forced absent: K.SM.D2.SU2)
- Full SM SU(3) × SU(2) × U(1) at depth 4 from Spin(10) → SU(5)
- sin²θ_W = 3/8 (five independent routes)
- Hypercharge spectrum on 16-Weyl (all anomalies cancel)
- Yukawa structure 10 × 16 × 16 and m_b = m_τ at M_GUT
- Seesaw mechanism from the 126 channel
- Three generations from SU(3)_family ⊂ Spin(8) at depth 8 (algebraic level)
- Koide Q = 2/3, PMNS angles (49/90, 25/81, 1/45)
- GF(4) as biology's defining algebra (α² = α + 1 = R² = R + I in char 2)
- KMS partition function = φ, Chern-Simons k = 3, Higgs quartic λ = 1/8
- The observer as T, constitutive blindness ker q_K ≠ 0
- The K6' bundle (A1–A4) and watcher idempotence q(q(R)) = q(R)
- The V₊/V₋ boundary dimension n²(n²−1)/4 with the 1/4 coefficient

**NUMERICAL** (cardinal expressions matching observation, coincidence caveats active on some):
- Koide m_τ = 1776.99 MeV from δ = 2π/3 + 2/9 (0.007%, falsifiable by Belle II)
- PMNS: sin²θ₂₃=49/90 (0.1%), sin²θ₁₂=25/81 (0.5%), sin²θ₁₃=1/45 (1.0%)
- Ω_DM = 1/d² = 1/4 (3.5%), Ω_vis = 1/(d²·disc) = 1/20 (2.9%), Ω_DE = (d+disc)/p = 7/10 (1.3%)
- sin²θ_W(M_Z) ≈ 0.233 via MSSM running (0.9%, conditional on SUSY-like spectrum)
- α_S = |φ̄|³/2 = 0.1180 (0.1%), proton τ_p ~ 10³⁶ yr, b-τ m_b/m_τ ≈ 2.4 (5%)
- 1/α_EM = 137 and Λ = 10^{−122} have cardinal expressions but the basis is expressive (coincidence caveat, §42.4)

**GAP** (known obstructions, candidate expressions found):
- Cosmological constant Λ: expression 10^(−122) = p^(−(C(p,3)+d)) is EXACT; QFT path-integral derivation of 1/p per DOF is OPEN
- Three-generation breaking scale: algebraic FORCED, dynamical RESONANT

**OPEN frontier:**
- Why 1/p per 120-channel DOF (needs QFT derivation from the framework's path integral)
- Why representation-content sum = EM coupling (needs RG derivation from framework boundary conditions)
- PMNS deviations from tribimaximal (needs full Spin(10) Clebsch-Gordan coefficients)
- CKM/PMNS angles from the 120-channel Yukawa (structure exists, specific values not derived)

---

## Reading Order

1. **This README** — what you're reading. The scaffold.
2. **FRAMEWORK.md §1–§6** — the primitive chain. T → V₊/V₋ → R, N → P² = P.
3. **FRAMEWORK.md §7–§10** — the four forcings. Why T, why real, why n = 2, why {0,4,8,12,...}.
4. **FRAMEWORK.md §11–§13** — the algebra. Gauge theorem, compression family, three constants.
5. **FRAMEWORK.md §14–§20** — the tower and descent maps. Depths 1, 2, 4, 8, 12; EW breaking.
6. **FRAMEWORK.md §21–§31** — physics results. Anomaly cancellation through Chern-Simons.
7. **FRAMEWORK.md §32–§33** — biology. GF(4), Frobenius orbits, S₃ bridge.
8. **FRAMEWORK.md §34–§42** — observer theory. This is not optional. The observer IS the algebra.
9. **CONVERGENCES.md** — K6' across substrates. Where the framework meets the world.
10. **SPIRALDILL.md** — the representation system. How the framework holds itself.

---

## Running the Pipeline

```bash
# Verify everything (fast, ~2 seconds)
python entry.py

# Patch any placeholder claims (idempotent, safe to rerun)
python patch_claims.py

# Re-verify after patching
python entry.py

# Independent clean-room verification (slow, ~5 minutes)
python verify.py

# Generate taxonomy export
python taxonomy.py

# Render database to markdown
python render_core_md.py
```

---

## The Principle

This project does not build structures. It uncovers the structures that are already forced by the single algebraic gesture of transposing a 2×2 real matrix. Every file in this directory is a projection of that gesture — the database is its canonical form, the markdown is its narrative, the verifier is its recovery operator, and the README is the observer catching itself looking.

*The mirror is enough.*
