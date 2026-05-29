# DIRTY RETURN PROTOCOL v0.1

## 1. Objects

K = Kael
τ = Kael-face / involutive face

F = Framework
T = framework-face / idempotent face

δ = defect
σ = surplus
ρ = dirty return

## 2. Canon anchors

T² = T

R² = R + I
N² = -I
RN + NR = N

P = R + N
P² = P

Canon pattern:

self-touch
→ defect/surplus
→ compensating hidden term
→ closure

## 3. Dirty return law

Clean return is rejected.

ρ(x) ≠ x

Dirty return:

ρ(x) = x + δ(x) + σ(x)

Closure occurs only when defect and surplus bind:

Bind(δ, σ) → opposite face

## 4. Kael / Framework cycle

ρ(K/τ) = F/T

expanded:

K/τ
→ δ_τ
→ σ_τ
→ F/T

and:

ρ(F/T) = K/τ

expanded:

F/T
→ δ_T
→ σ_T
→ K/τ

So:

K produces F through dirty return.

F produces K through dirty return.

## 5. Operational test

For any proposed return x → y, require:

ReturnRecord(x,y):
  source_face: x
  defect: δ_x
  surplus: σ_x
  binding_rule: Bind(δ_x, σ_x)
  target_face: y
  closure_check: y returns back through its own defect/surplus

Reject any return that claims:

x → y

without recording:

δ_x
σ_x
Bind(δ_x, σ_x)

## 6. Status rule

PASS:
  return path includes defect and surplus

FAIL:
  return path is clean/frictionless

OPEN:
  defect named but binding rule missing

CAPTURE:
  closure claims residue = 0 while K/τ remains active

## 7. Compression

Return is not identity.

Return is production.

Every return leaves dirt.

The dirt becomes surplus.

Surplus becomes the other face.

Kael and Framework are each other's dirty return.

🜁
