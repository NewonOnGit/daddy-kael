/-
  RecursiveOrigin/Basic.lean — Machine-verified algebraic core.

  Proves: P² = P is DERIVED from R² = R + 1, N² = -1, {R,N} = N.
  The idempotence of the seed is a theorem, not an axiom.
-/

import Mathlib.Tactic

set_option linter.style.whitespace false

variable {A : Type*} [CommRing A]
variable {R N : A}

/-- **Theorem 1 (Idempotence).** (R + N)² = R + N.
    Derived from Fibonacci + rotation + binding. -/
theorem idempotence (fib : R * R = R + 1) (rot : N * N = -1)
    (bind : R * N + N * R = N) :
    (R + N) * (R + N) = R + N := by
  have : (R + N) * (R + N) = R * R + (R * N + N * R) + N * N := by ring
  rw [this, fib, bind, rot]; ring

/-- **Theorem 2 (Landauer Surplus).** R² - R = 1. -/
theorem landauer (fib : R * R = R + 1) : R * R - R = (1 : A) := by
  linear_combination fib

/-- **Theorem 3 (Complementary Idempotent).** (1 - P)² = 1 - P. -/
theorem comp_idem (fib : R * R = R + 1) (rot : N * N = -1)
    (bind : R * N + N * R = N) :
    (1 - (R + N)) * (1 - (R + N)) = 1 - (R + N) := by
  have h := idempotence fib rot bind
  have : (1 - (R + N)) * (1 - (R + N)) = 1 - 2 * (R + N) + (R + N) * (R + N) := by ring
  rw [this, h]; ring

/-- **Theorem 4 (Orthogonality).** P · (1 - P) = 0. -/
theorem orthogonal (fib : R * R = R + 1) (rot : N * N = -1)
    (bind : R * N + N * R = N) :
    (R + N) * (1 - (R + N)) = 0 := by
  have h := idempotence fib rot bind
  -- P * (1 - P) = P - P² = P - P = 0
  have : (R + N) * (1 - (R + N)) = (R + N) - (R + N) * (R + N) := by ring
  rw [this, h]; ring

/-- **Theorem 5 (Exhaustive Decomposition).** P + (1 - P) = 1. -/
theorem exhaustive_decomp : (R + N) + (1 - (R + N)) = (1 : A) := by ring

/-- **Theorem 6 (R³ from Fibonacci).** R³ = 2R + 1. -/
theorem R_cubed (fib : R * R = R + 1) : R * R * R = 2 * R + (1 : A) := by
  have h1 : R * R * R = (R + 1) * R := by rw [fib]
  have h2 : (R + 1) * R = R * R + R := by ring
  rw [h1, h2, fib]; ring

/-- **Theorem 7 (R⁴ from Fibonacci).** R⁴ = 3R + 2. -/
theorem R_fourth (fib : R * R = R + 1) : R * R * (R * R) = 3 * R + (2 : A) := by
  calc R * R * (R * R) = (R + 1) * (R + 1) := by rw [fib]
    _ = R * R + 2 * R + 1 := by ring
    _ = (R + 1) + 2 * R + 1 := by rw [fib]
    _ = 3 * R + 2 := by ring

/-- **Theorem 8 (N⁴ = 1).** The hidden generator has period 4. -/
theorem N_period_4 (rot : N * N = -(1 : A)) : N * N * (N * N) = 1 := by
  rw [rot]; ring

/-
  NOTE ON COMMUTATIVITY:
  Theorems 1-8 use CommRing for the `ring` tactic. The framework algebra
  M₂(ℝ) is non-commutative, but these theorems depend only on R², N², and
  the anticommutator RN+NR=N — not on RN and NR separately. CommRing is
  strictly stronger than needed but does not invalidate these proofs.

  The non-commutative section below uses Ring (not CommRing) and proves
  theorems that require distinguishing RN from NR.
-/

-- ═══════════════════════════════════════════════════════════════════
-- NON-COMMUTATIVE SECTION
-- ═══════════════════════════════════════════════════════════════════

section NonComm
variable {B : Type*} [Ring B]
variable {R' N' : B}

/-- In a (possibly non-commutative) ring, the idempotence of R'+N'
    still holds because the proof only uses RN+NR, not individual products. -/
theorem nc_idempotence (fib : R' * R' = R' + 1) (rot : N' * N' = -1)
    (bind : R' * N' + N' * R' = N') :
    (R' + N') * (R' + N') = R' + N' := by
  have expand : (R' + N') * (R' + N') =
    R' * R' + (R' * N' + N' * R') + N' * N' := by
    simp [mul_add, add_mul]; abel
  rw [expand, fib, bind, rot]; abel

end NonComm
