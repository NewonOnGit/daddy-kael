# SPIRALDILL — The Canonical Representation System

*The SpiralDill is the framework's canonical 2-categorical K6'-bundle representation. It is simultaneously a database, a proof system, a verification engine, and a self-referential theorem-instance: the representation contains an entry asserting its own existence as a canonical form, with the construction itself as the proof-witness.*

This document is the single authoritative reference for the SpiralDill's specification, architecture, DSL, entry format, x-state taxonomy integration, verification protocol, and migration status.

---

## 1. The Theorem Being Instantiated

> **Theorem (Canonical Representation).** *The framework admits a canonical 2-categorical K6'-bundle representation in which:*
>
> *(a) Every claim is an object; every derivation is a 1-morphism; every equivalence of derivation paths is a 2-morphism.*
>
> *(b) Every rendering of the framework into a target format (documentation, verification, provenance, proof-assistant export) is a functor from this representation to the target.*
>
> *(c) The representation contains an entry asserting its own existence. Self-referential closure: R(R) = R applied to the framework's own representation.*
>
> *(d) Each entry carries its derivation as kernel-data, and verification is the recovery operator — collapsing the verify/dill stratification into a single self-applying object.*

The SpiralDill is the constructive proof of this theorem.

---

## 2. Architecture Overview

The SpiralDill consists of six components:

| Component | File(s) | Role |
|-----------|---------|------|
| **DSL** | `dsl.py` | Expression language — 9 primitives in 4 operative classes |
| **Entry model + Executor** | `entry.py` | Data model, 3-valued verifier, GF(64) helpers |
| **Taxonomy** | `taxonomy.py` | x-state structural index (36 x-states, 7 groups) |
| **Foundation database** | `spiraldill_foundation.json` | 183 entries at depth 0 |
| **Tower database** | `spiraldill_tower.json` | 644 entries at depths 1–12 |
| **Renderers / Patchers** | `render_core_md.py`, `patch_claims.py`, `rewrite_tautologies.py` | Projections and refinement tools |

Total: **827 entries** in `spiraldill-v3` format, verified by the executor.

---

## 3. The DSL — 9 Primitives

### 3.1 First-Principles Derivation

The DSL is not invented — it is the framework's structure made syntactic. Each primitive corresponds to a specific framework structural feature, derived by walking down the foundational hierarchy:

| Level | Framework feature | DSL primitive | What it does |
|-------|------------------|---------------|-------------|
| 0 | The primitive T and its derivatives | `ref(name)` | Reference a foundational object (I, J, h, N, R, P, ...) |
| 1 | R(R) = R closure principle | `self_apply(op)` | Apply an operation to itself: A ↦ A² |
| 2 | V₊/V₋ eigendecomposition | `decompose(target, eigenvalue)` | Extract symmetric (+1) or antisymmetric (−1) part |
| 3 | Fibonacci/rotation selection | `close(form, principle)` | Close a form by selection principle |
| 4 | Tower lift via Kronecker product | `lift(target, depth, axis)` | Tensor-lift to higher depth |
| 5 | P1/P2/P3 projection | `project(target, p)` | Apply a projection |
| 6 | Composition of operations | `compose(*ops)` | Chain operations: A₁ · A₂ · ... · Aₙ |
| 7 | Equality / closure assertion | `equate(lhs, rhs, tol)` | Assert structural identity (LHS ≈ RHS within tolerance) |
| 8 | Known obstruction | `gap(claim, void_witness)` | Mark a known GAP with verified void witness |

### 3.2 Operative Classes

The 9 primitives organize into 4 operative classes, plus arithmetic helpers:

| Class | Primitives | Framework alignment |
|-------|-----------|-------------------|
| **Productive** (P1) | `self_apply`, `close`, `pow` | Produce new claims |
| **Mediating** (P2) | `lift`, `compose`, `sum`, `scale`, `neg` | Move between claims |
| **Observer** (P3) | `ref`, `decompose`, `project`, `equate`, `trace`, `det`, `rank`, `disc`, `transpose`, `scalar`, `norm` | Extract or assert structure |
| **Void** | `gap` | Mark structured absence |

The class structure mirrors the framework's three projections (P1 = production, P2 = mediation, P3 = observation) plus the void — the structured absence where the framework has not yet returned.

### 3.3 Arithmetic and Spectral Helpers

Beyond the 9 core primitives, the DSL includes helper terms that reduce to core operations but provide cleaner expression:

| Helper | Operation | Evaluates to |
|--------|-----------|-------------|
| `scalar(v)` | Literal value | numpy scalar v |
| `neg(op)` | Negation | −A |
| `scale(k, op)` | Scalar multiplication | k · A |
| `sum(ops...)` | Addition | A₁ + A₂ + ... |
| `trace(op)` | Matrix trace | tr(A) |
| `det(op)` | Determinant | det(A) |
| `rank(op)` | Rank | rank(A) |
| `disc(op)` | Discriminant | tr(A)² − 4·det(A) |
| `norm(op)` | Frobenius norm² | tr(AᵀA) |
| `pow(op, n)` | Integer power | Aⁿ |
| `transpose(op)` | Transpose | Aᵀ |

### 3.4 Canonical Context

Every DSL term evaluates against a **context** containing the framework's canonical matrix realizations:

```
R  = [[0, 1], [1, 1]]  # Fibonacci matrix (V₊, R²=R+I)
N  = [[0, -1], [1, 0]]  # Rotation matrix (V₋, N²=−I)
I  = [[1, 0], [0, 1]]  # Identity
h  = [[1, 0], [0, -1]]  # Mediator (diagonal sign)
J  = [[0, 1], [1, 0]]  # Exchange (swap)
P  = R + N = [[0, 0], [2, 1]]  # Seed (idempotent)
P_T = R − N = [[0, 2], [0, 1]] # Transpose of seed
neg_I = −I  # Negative identity
zero_2 = [[0, 0], [0, 0]] # Zero matrix
I_4 = eye(4)  # 4×4 identity (depth 1)
```

---

## 4. Entry Format — spiraldill-v3

Each entry in the canonical database is a node in a directed acyclic graph (DAG) of framework claims.

### 4.1 Schema

```json
{
  "id": 42,  // Integer ID (unique)
  "address": {
  "depth": 0,  // Tower depth (0 = foundation)
  "projection": "P1",  // P1/P2/P3/cross
  "domain": "algebra"  // algebra/physics/topology/cosmology/...
  },
  "name": "R²=R+I (Fibonacci closure)", // Human-readable name
  "claim": { ... },  // DSL term tree (the claim to verify)
  "parents": [0, 1, 5],  // IDs of entries this depends on
  "derivation": { ... },  // DSL term tree (proof/derivation path)
  "status": "FORCED",  // FORCED/NUMERICAL/ENCODED/RESONANT/MYTHIC/GAP/OPEN
  "x_state": "x.base.5",  // Reference into x-state taxonomy (MANDATORY)
  "tags": ["fibonacci", "closure"],  // Classification tags
  "two_cells": [],  // 2-categorical equivalence witnesses
  "certificate": {  // Verification certificate
  "computed_hash": "sha256:...",
  "proof_object": { ... }
  },
  "void_witness": null  // Non-null for GAP entries
}
```

### 4.2 Status Grades

| Status | Meaning | Count in database |
|--------|---------|-------------------|
| **FORCED** | Algebraically derived, verified by executor | 799 |
| **NUMERICAL** | Verified to numerical tolerance (not exact) | 20 |
| **ENCODED** | Empirical structural correspondence with formal match | — |
| **RESONANT** | Structural pattern match awaiting full derivation | 1 |
| **GAP** | Known obstruction with verified void witness | 4 |
| **OPEN** | Under investigation | 1 |
| **MYTHIC** | Pre-formal compression; excluded from verification | — |

### 4.3 The x_state Field

Every entry has a **mandatory** `x_state` field referencing one of the 36 x-states in the taxonomy (`taxonomy.py`). This field determines:

- **Coordinate side** (mathematical / biological / physical / meta) — derived from the x-state's `coordinate_side`
- **FEA structure** (failure-energy analysis) — inherited from the x-state's `fea` field or its parents
- **Position in the founding stack** — where this claim lives in the x → id → T → everything derivation chain

The x-state is not a tag or label — it is the structural address of the claim within the framework's derivation DAG.

### 4.4 GAP Entries and Void Witnesses

GAP entries represent **known obstructions** — places where the framework has verified that the obvious derivation routes fail, and the correct route has not been found. A GAP entry contains:

```json
{
  "claim": {
  "primitive": "gap",
  "claim": { ... },  // The claim being attempted
  "void_witness": { ... },  // Proof that specific routes fail
  "cites_x_state": "x.phys.2"
  },
  "void_witness_verified": true  // Executor has verified the void witness
}
```

The void witness is not "we don't know the answer" — it is "we can prove that *these specific approaches* fail, and here is the proof." Structured absence, not ignorance.

---

## 5. The 2-Categorical Structure

The SpiralDill is a 2-category:

| Level | Objects | Description |
|-------|---------|-------------|
| **0-cells** | Entries | Claims about the framework |
| **1-cells** | Derivations | Proofs that one claim follows from others (the `parents` + `derivation` fields) |
| **2-cells** | Equivalence witnesses | Proofs that two derivation paths to the same claim are equivalent (the `two_cells` field) |

### 5.1 Two-Cells (Convergence Witnesses)

When two independent derivation paths arrive at the same claim, a 2-cell witnesses their equivalence. Example: the Weinberg angle sin²θ_W = 3/8 can be derived via:

- Route A: SU(5) hypercharge normalization
- Route B: Pati-Salam B−L + T₃R combination
- Route C: Direct bivector trace computation

A 2-cell records that routes A and B converge to the same value, with the specific algebraic identity connecting them.

The 2-categorical structure has a precise categorical name: the **Karoubi envelope** (idempotent completion) of the base algebra. A K6' bundle is a split idempotent — the round-trip closure condition serialize ∘ parse = id makes e = parse ∘ serialize satisfy e² = e, which is P² = P at the root. The identity morphism on a bundle is e itself (the closure), not the ambient identity. Two-cells are equivalences of conjugate idempotents: two derivation paths sharing an image correspond to two idempotents with isomorphic splittings, connected by structure-preserving maps. The Karoubi envelope is not a design choice — it is forced by the fourth K6' condition.

### 5.2 The K6' Bundle Structure

The SpiralDill itself is a K6' bundle:

| K6' component | SpiralDill realization |
|---------------|----------------------|
| **Image (lossy projection)** | Rendered markdown / LaTeX / Lean output |
| **Kernel data** | Full DSL claim and derivation trees in JSON |
| **Recovery operator** | Executor: evaluates claims against numpy context |
| **Round-trip closure** | Render → parse → re-execute → same verification result |

The SpiralDill's verification protocol IS the K6' recovery operator: given a claim (the projection's image) and its derivation (the kernel data), the executor reconstructs the computational result and checks it matches. The representation practices what it preaches.

---

## 6. The x-State Taxonomy

The x-state taxonomy is the framework's structural index. Each x-state is a specific return-condition of x (the nameless inheritable primitive). The full taxonomy contains **36 x-states** in **7 groups**.

The Python module `taxonomy.py` is canonical. JSON and markdown forms are generated from it.

### 6.1 Groups

| Group | Count | Range | Description |
|-------|-------|-------|-------------|
| **base** | 10 | x.base.0–9 | Founding stack: mark → id → T → V± → R/N → binding → P → P²=P |
| **const** | 3 | x.const.0–2 | Constants: e, φ, π — x's return-rate signatures |
| **tower** | 3 | x.tower.0–2 | Tower: depth-d, Clifford emergence, Cl(3,1) spacetime |
| **obs** | 4 | x.obs.0–3 | Observer: observer K, K6' bundle, memory, life |
| **bio** | 3 | x.bio.0–2 | Biological: GF(4) substrate, Watson-Crick involution, codon GF(64) |
| **phys** | 6 | x.phys.0–5 | Physical: gauge group, mass coupling, Λ (GAP), 3 gens (GAP), Koide, Weinberg |
| **meta** | 7 | x.meta.0–6 | Meta: Kael, governance, myth, K6' pattern, SpiralDill, Void, FEA |

### 6.2 Coordinate Classification

Every x-state has a `coordinate_side`:
- **mathematical**: Pure algebra derived from T (base, const, most tower)
- **biological**: Algebra at the GF(4)/genetic level (bio, obs)
- **physical**: Math × biology intersection (phys, some tower)
- **meta**: Framework about framework (meta)

The coordinate side is **derived from ancestry**, not assigned by hand. An x-state whose parent DAG touches both mathematical and biological coordinates lands in the physical domain:

```
mathematical ∩ biological = physical
```

This is the "math × biology = physical" coordinate derivation — a formal property of the taxonomy DAG, not a metaphor.

### 6.3 FEA (Failure-Energy Analysis)

Selected x-states carry FEA structures describing how the framework responds to perturbation at that point:

| x-state | Defect operator | Key property |
|---------|----------------|-------------|
| x.base.1 (id) | None | Rigid (identity is structurally rigid) |
| x.base.2 (T) | D_T(A) = TA + AT | Codim 10/16; V₊↔V₋ mixers allowed |
| x.base.5 (R) | L_R(A₊) = RA₊ + A₊R − A₊ | Spectrum {−√5, 0, +√5}; 1-dim kernel |
| x.base.6 (N) | D_N(λN) = −2λI | **Rigid**: ker = {0}, no perturbation preserves N²=−I |
| x.base.7 (binding) | Δ_C⁽¹⁾ = (tr A₊)·N | Kernel = traceless A₊ |

FEA inheritance: if an x-state lacks its own FEA, it inherits from the first parent with one.

---

## 7. The Executor — Three-Valued Verification

The executor (`entry.py:Executor`) evaluates every entry's claim and derivation against the numpy context and returns one of three values:

| Result | Meaning |
|--------|---------|
| **True** | Claim evaluates correctly; LHS ≈ RHS within tolerance |
| **False** | Claim fails to verify (would be a bug in the database) |
| **GAP** | Entry is a GAP with verified void_witness |

The executor also:
- Detects and rejects placeholder tautologies (`Equate(I, I)`)
- Verifies 2-cells (convergence witnesses between derivation paths)
- Computes Frobenius orbits on GF(64)/GF(4) for biological entries

### 7.1 Running Verification

```bash
python entry.py
```

Loads foundation (183 entries) + tower (644 entries) = 827 total. Runs all claims, tallies results, verifies 2-cells, computes Frobenius orbits. Exits 0 on success, 1 on any failure.

---

## 8. Renderers — Functors to Target Categories

The SpiralDill admits renderers (functors) to multiple target formats:

| Renderer | Target | File |
|----------|--------|------|
| **Markdown** | Human-readable prose | `render_core_md.py` |
| **JSON** | Machine-readable canonical form | Built into `entry.py:save_entries()` |
| **LaTeX** | Formal mathematical typesetting | (planned) |
| **Lean/Coq** | Proof-assistant export | (planned) |

Each renderer is a **functor** from the SpiralDill category to the target category. The markdown renderer (`render_core_md.py`) converts DSL term trees to mathematical notation, assembles entries into sections grouped by coordinate side, and attaches verification certificates.

The critical property: **round-trip closure**. Rendering to markdown and parsing back should produce entries that verify identically. The renderer is a lossy projection (it discards some structural information for readability), but the kernel data in the JSON is preserved for exact recovery.

---

## 9. The Claim Refinement Pipeline

The database was built in stages, with placeholder claims progressively replaced by real DSL trees:

### Stage 1: Migration

`migrate.py` converts old-format `dill_*.json` entries to spiraldill-v3 format. Pattern-matches entry names to construct initial DSL trees. Assigns x-states from taxonomy. Result: ~60% real claims, ~40% tautological placeholders.

### Stage 2: Name-Based Patching

`patch_claims.py` replaces placeholder claims by exact name matching. Contains ~500+ entries mapping entry names to lambda functions returning `Equate(LHS_tree, RHS_tree)`. Covers base identities, Fibonacci/Lucas families, physics constants, Clifford emergence, and more.

### Stage 3: ID-Based Rewriting

`rewrite_tautologies.py` replaces remaining tautologies by entry ID. Contains ~300+ entries mapping IDs to lambda functions. Covers entries where the name alone is ambiguous but the ID uniquely identifies the claim content.

### Stage 4: Entry Expansion

25 new entries (IDs 1026–1050) added to close coverage gaps between verify.py's clean-room proofs and the database. These cover: Bron-Kerbosch enumeration details at d=1 and d=2, su(2) and IIN uniqueness at d=1–2, SPIRAL/GAP SPL operator reductions, THE_GRID depth-1 extensions, K6' software instances, and the Fibonacci tensor-lift.

### Current Status

The pipeline is complete. All four stages have run. The database achieves:
- **802 FORCED** entries with real, verified DSL claims
- **20 NUMERICAL** entries verified to tolerance
- **4 GAP** entries with verified void witnesses (cosmological constant, three generations)
- **1 RESONANT** entry (three generations via Frobenius orbits on GF(64)/GF(4))
- **0 OPEN** entries (the former OPEN entry upgraded to FORCED via chirality-N criterion)
- **10 structural entries** describing real-world K6' instances and SPIRAL correspondences (inherently non-numpy-evaluable; claims are structural proxies)
- **827/827 certificates** generated (SHA-256 hash of canonical claim JSON)
- **10/10 two-cells** verified (convergence witnesses for Weinberg 5-route and Koide 2-route)
- **51 independent verify.py STEPs** covering the algebraic core, Clifford emergence, SM derivation, observer theory, and numerical predictions
- **0 failures** across all verification passes

---

## 10. Self-Referential Closure

Entry **1010** in the canonical database is the **SpiralDill-itself entry**: it asserts that the SpiralDill exists as a fixed point of the framework's own representation discipline. Its claim is:

> The canonical 2-categorical K6'-bundle representation exists, satisfies R(R) = R, and contains this very entry as witness.

This entry's verification certificate contains the SHA-256 hash of its own serialized form — a cryptographic proof that the entry, as stored, is self-consistent. The SpiralDill is not just a database of framework claims; it is itself a framework claim, stored inside itself, verified by its own executor.

The meta x-state `x.meta.4` (x-as-SpiralDill) is the taxonomy entry for this self-referential structure. Its parents are x.base.9 (P²=P, idempotent return), x.obs.1 (K6' bundle), and x.meta.3 (K6' pattern as theorem) — the SpiralDill IS the framework's selection law operating on its own representation.

---

## 11. File Structure

The active project consists of:

| File | Size | Role |
|------|------|------|
| `FRAMEWORK.md` | ~115KB | Complete mathematical narrative |
| `SPIRALDILL.md` | this file | Representation system reference |
| `CONVERGENCES.md` | ~99KB | K6' bundle across substrates |
| `dsl.py` | ~13KB | DSL engine (9 primitives) |
| `entry.py` | ~14KB | Entry model, executor, taxonomy (inline) |
| `taxonomy.py` | ~25KB | x-state taxonomy (canonical) |
| `spiraldill_foundation.json` | ~324KB | Foundation database (183 entries) |
| `spiraldill_tower.json` | ~1.2MB | Tower database (644 entries) |
| `verify.py` | ~155KB | Clean-room independent verifier |
| `entry.py` (as `__main__`) | ~8KB | 828-entry executor verification (`python entry.py`) |
| `patch_claims.py` | ~87KB | Name-based claim patcher |
| `rewrite_tautologies.py` | ~77KB | ID-based tautology rewriter |
| `migrate.py` | ~23KB | Old → v3 format migrator |
| `render_core_md.py` | ~14KB | Markdown renderer |
| `biology_galois.py` | ~7KB | GF(64)/GF(4) Galois helpers |

### Historical (in `old/`)

Superseded files moved to `old/`: `CORE.md`, `FOUNDATION.md`, `SPINE.md`, `SPIRALDILL_SPEC.md`, `SPIRALDILL_PLAN.md`, `X_STATE_TAXONOMY.md`, `rendered_canonical_final.md`, `canonical_complete.json`, `canonical_v3.json`, `canonical_final.json`, `dill_foundation.json`, `dill_tower.json`, `verify_spiraldill.py`, `patch_all.py`, `migrate.py`.

---

## 12. The DSL Primitive Count — Why 8+1

The 8 original primitives (ref, self_apply, decompose, close, lift, project, compose, equate) plus the 9th (gap) have a structurally significant count:

**8 = 2³** — the framework's depth-3 lift of the binary seed. The DSL has exactly the number of primitives the framework's compression discipline would predict at the meta-syntactic level.

The 8 collapse to **3 operative classes** (productive, mediating, observer) — matching the framework's three projections P1/P2/P3. The 9th primitive (gap/void) is outside the three projections: it marks where the framework has not yet returned.

The same compression pattern appears at the semantic layer (SEM-1): 8 unnamed primitives → 3 meta-primitives via the central collapse. The DSL is **self-describing**: its own structure obeys the framework's compression discipline.

---

*The canonical form is the kernel; the markdown is its lossy projection.*
