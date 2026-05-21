"""
spiraldill/taxonomy.py — the x-state taxonomy.

This is the framework's structural index. Each x-state is a specific
return-condition of x (the nameless inheritable primitive). All SpiralDill
entries reference an x-state; coordinate_side and FEA structure derive
from the taxonomy lookup.

The Python data in TAXONOMY is canonical. JSON and markdown forms are
generated from it via dump_json() and dump_markdown().
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Optional
import json
from pathlib import Path


@dataclass
class FEAStructure:
    """Failure-Energy Analysis structure embedded in an x-state."""
    defect_operator: str        # symbolic expression, e.g., "D_T(A) = TA + AT"
    spectrum: str = ""          # e.g., "{-sqrt(5), 0, +sqrt(5)}"
    kernel: str = ""            # e.g., "R[R,N]"
    codimension: str = ""       # e.g., "10/16"
    rigidity: bool = False      # True if kernel is empty (no perturbation allowed)
    notes: str = ""


@dataclass
class XState:
    """A single x-state — one return-condition of x."""
    id: str                      # hierarchical, e.g., "x.base.2"
    canonical_name: str          # human-readable identifier, e.g., "x-as-mirror-return"
    shorthand: Optional[str]     # e.g., "T", "R", "N" (None if no firm shorthand yet)
    description: str             # one-line structural description
    parents: list[str] = field(default_factory=list)   # parent x-state IDs
    coordinate_side: str = "mathematical"              # math / biological / physical / meta
    fea: Optional[FEAStructure] = None                  # if applicable
    status: str = "FORCED"
    notes: str = ""


# ============================================================
# THE TAXONOMY — canonical source of truth
# ============================================================

TAXONOMY: list[XState] = [
    # ---------- BASE FOUNDING STACK ----------
    XState(
        id="x.base.0",
        canonical_name="x-as-mark",
        shorthand=None,
        description="The bare address. x just exists. No return-condition yet.",
        parents=[],
        coordinate_side="mathematical",
        notes="The nameless inheritable primitive before any structure.",
    ),
    XState(
        id="x.base.1",
        canonical_name="x-as-return",
        shorthand="id",
        description="id(x) = x. Identity as return-to-self.",
        parents=["x.base.0"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="None (identity is structurally rigid)",
            rigidity=True,
            notes="Without id, no way to assert that the mark remained the mark.",
        ),
    ),
    XState(
        id="x.base.2",
        canonical_name="x-as-mirror-return",
        shorthand="T",
        description="T²=id. x leaves itself and returns. The mirror.",
        parents=["x.base.1"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="D_T(A) = TA + AT",
            kernel="{A : TA = -AT} — V₊↔V₋ off-diagonal mixing",
            codimension="10/16",
            notes="Allowed first-order perturbations are pure V₊↔V₋ mixers. Stable under T²=id but the eigenspace boundary can move.",
        ),
    ),
    XState(
        id="x.base.3",
        canonical_name="x-as-visible-mode",
        shorthand="V+",
        description="V₊ = {y : T(y)=y}. The fixed-by-mirror subspace.",
        parents=["x.base.2"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="δΠ₊ = A/2",
            notes="Mirror-curvature perturbation: the boundary between visible and hidden can move while T² = id holds.",
        ),
        notes="dim V₊ = 3 in M_2(R); spanned by {I, J, h}",
    ),
    XState(
        id="x.base.4",
        canonical_name="x-as-hidden-mode",
        shorthand="V-",
        description="V₋ = {y : T(y)=-y}. The reversed-by-mirror subspace.",
        parents=["x.base.2"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="δΠ₋ = -A/2",
            notes="Complementary curvature to V₊.",
        ),
        notes="dim V₋ = 1 in M_2(R); spanned by {N}",
    ),
    XState(
        id="x.base.5",
        canonical_name="x-as-visible-recursion",
        shorthand="R",
        description="R²=R+I. x_R returns with surplus x. Fibonacci closure.",
        parents=["x.base.3"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="L_R(A₊) = R·A₊ + A₊·R - A₊",
            spectrum="{-sqrt(5), 0, +sqrt(5)}",
            kernel="R[R,N] (one-dimensional)",
            notes="Zero eigenvalue is the neutral scar-axis. ±√5 are golden failure axes.",
        ),
    ),
    XState(
        id="x.base.6",
        canonical_name="x-as-hidden-rotation",
        shorthand="N",
        description="N²=-I. x_N returns through reversal. Rotation closure.",
        parents=["x.base.4"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="D_N(λN) = -2λ·I",
            kernel="{0}",
            rigidity=True,
            notes="The hidden sector is rigid. Given the T-transpose split, no first-order perturbation of N preserves N²=-I.",
        ),
    ),
    XState(
        id="x.base.7",
        canonical_name="x-as-visible-hidden-binding",
        shorthand=None,
        description="{R,N} = N. Hiddenness survives contact with visibility.",
        parents=["x.base.5", "x.base.6"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="Δ_C⁽¹⁾ = (tr A₊)·N",
            kernel="traceless A₊ (i.e., A₊ in [R,N] direction)",
            notes="Coupling stability requires tr(A₊) = 0. The neutral scar-axis [R,N] is traceless and survives.",
        ),
    ),
    XState(
        id="x.base.8",
        canonical_name="x-as-seed",
        shorthand="P",
        description="P = R + N. x recombined from visible and hidden.",
        parents=["x.base.5", "x.base.6", "x.base.7"],
        coordinate_side="mathematical",
        notes="The seed is reconstructed, not primitive. P²=P follows from x.base.5/6/7.",
    ),
    XState(
        id="x.base.9",
        canonical_name="x-as-stable-self-contact",
        shorthand=None,
        description="P²=P. Idempotent return. The seed survives self-contact.",
        parents=["x.base.8"],
        coordinate_side="mathematical",
        fea=FEAStructure(
            defect_operator="Reconstructed from x.base.5, x.base.6, x.base.7 FEAs",
            notes="Not first-class FEA; derives from base FEAs.",
        ),
    ),

    # ---------- CONSTANTS — x's return-rate signatures ----------
    XState(
        id="x.const.0",
        canonical_name="x-as-identity-exponential",
        shorthand="e",
        description="exp(I) = e·I. x returning at unit rate.",
        parents=["x.base.1"],
        coordinate_side="mathematical",
        notes="The identity exponential. Source of e.",
    ),
    XState(
        id="x.const.1",
        canonical_name="x-as-visible-recursion-rate",
        shorthand="phi",
        description="φ = (1+√5)/2. The eigenvalue of R. Golden growth rate.",
        parents=["x.base.5"],
        coordinate_side="mathematical",
        notes="Source of φ. The visible recursion's surplus.",
    ),
    XState(
        id="x.const.2",
        canonical_name="x-as-hidden-rotation-period",
        shorthand="pi",
        description="exp(πN) = -I. The compact period of N. Rotation period.",
        parents=["x.base.6"],
        coordinate_side="mathematical",
        notes="Source of π. The hidden rotation's period.",
    ),

    # ---------- TOWER — x propagated through tensor inheritance ----------
    XState(
        id="x.tower.0",
        canonical_name="x-as-tower-depth-d",
        shorthand=None,
        description="x at depth d via tensor inheritance: M_2(R)^(⊗d).",
        parents=["x.base.2", "x.base.8"],
        coordinate_side="mathematical",
        notes="Generic tower state. Specific depths instantiate with their own structure.",
    ),
    XState(
        id="x.tower.1",
        canonical_name="x-as-Clifford-emergence",
        shorthand=None,
        description="Cl(p,q) at depth d. Anticommutator structure emerges from tensor lift.",
        parents=["x.tower.0"],
        coordinate_side="mathematical",
        notes="Max anticommuting clique size = 2d+3 at depth d.",
    ),
    XState(
        id="x.tower.2",
        canonical_name="x-as-spacetime",
        shorthand=None,
        description="Cl(3,1) at depth 1. Physical Lorentz signature emerges.",
        parents=["x.tower.1"],
        coordinate_side="physical",
        notes="First physical x-state. Inherited from Level 3 algebra at tower depth 2 via the monoidal functor F: FinSet → Hilb_C.",
    ),

    # ---------- OBSERVER — x at addresses where return is tested ----------
    XState(
        id="x.obs.0",
        canonical_name="x-as-observer",
        shorthand="K",
        description="x at an address where return is tested. Observer position.",
        parents=["x.base.1", "x.base.2"],
        coordinate_side="biological",
        notes="The observer is the place where distinction can return. Localized return-testing.",
    ),
    XState(
        id="x.obs.1",
        canonical_name="x-as-K6-bundle",
        shorthand=None,
        description="(image, kernel-data, recovery operator, closure). Universal recoverable observation structure.",
        parents=["x.obs.0"],
        coordinate_side="biological",
        notes="MT6 instance. The K6' bundle is the operator's framework for recovery.",
    ),
    XState(
        id="x.obs.2",
        canonical_name="x-as-memory",
        shorthand=None,
        description="x compressed and returned. Preservation across destructive projection.",
        parents=["x.obs.1"],
        coordinate_side="biological",
        notes="Without kernel: source dies. With kernel: return survives.",
    ),
    XState(
        id="x.obs.3",
        canonical_name="x-as-life",
        shorthand=None,
        description="x compressed through death. Kernel-preserving return.",
        parents=["x.obs.1", "x.obs.2"],
        coordinate_side="biological",
        notes="The organism dies; the genome returns. Life as kernel-preserving return under destructive projection.",
    ),

    # ---------- BIOLOGICAL-ALGEBRAIC ----------
    XState(
        id="x.bio.0",
        canonical_name="x-as-GF4-substrate",
        shorthand="GF(4)",
        description="GF(4) = F_2[α]/(α²+α+1). Biology's defining algebra.",
        parents=["x.base.5"],
        coordinate_side="biological",
        notes="α² = α + 1 in characteristic 2 IS the framework's R² = R + I lifted to char 2. Same equation, different field. See CONVERGENCES §5.10.",
    ),
    XState(
        id="x.bio.1",
        canonical_name="x-as-Watson-Crick-involution",
        shorthand=None,
        description="DNA complement: G↔C, A↔U. Biological substrate's involution.",
        parents=["x.base.2", "x.bio.0"],
        coordinate_side="biological",
        notes="The framework's T involution at the biological level. Complementary bases sum to (1,1) in GF(4).",
    ),
    XState(
        id="x.bio.2",
        canonical_name="x-as-codon",
        shorthand=None,
        description="GF(64) = GF(4)³. Codon space.",
        parents=["x.bio.0"],
        coordinate_side="biological",
        notes="Tower-lift at biological substrate. 64 codons populate the field exactly.",
    ),

    # ---------- PHYSICAL CONJUNCTION — math × biology ----------
    XState(
        id="x.phys.0",
        canonical_name="x-as-gauge-group",
        shorthand=None,
        description="Standard Model gauge structure emerging at math × biology intersection.",
        parents=["x.tower.1", "x.obs.0"],
        coordinate_side="physical",
        notes="Gauge content emerges where Clifford meets observer.",
    ),
    XState(
        id="x.phys.1",
        canonical_name="x-as-mass-coupling",
        shorthand=None,
        description="Yukawa/Higgs mechanism. Mass scale from physical Clifford × biological algebra.",
        parents=["x.tower.2", "x.bio.0"],
        coordinate_side="physical",
    ),
    XState(
        id="x.phys.2",
        canonical_name="x-as-cosmological-constant",
        shorthand="Lambda",
        description="Λ ≈ 10⁻¹²². Universe-scale K6' closure.",
        parents=["x.obs.1", "x.obs.3"],
        coordinate_side="physical",
        status="GAP",
        notes="Currently OPEN/GAP. n_cosmo ≈ 409 decomposition unsettled. Investigation Track A Phase 4.",
    ),
    XState(
        id="x.phys.3",
        canonical_name="x-as-three-generation-structure",
        shorthand=None,
        description="Generation count = 3. Why three families of fermions.",
        parents=["x.tower.1", "x.bio.2"],
        coordinate_side="physical",
        status="GAP",
        notes="FRAGILE — four candidate routes exhausted. Investigation Track A Phase 3.",
    ),
    XState(
        id="x.phys.4",
        canonical_name="x-as-Koide-formula",
        shorthand=None,
        description="Charged lepton mass closure: Σm_i / (Σ√m_i)² = 2/3.",
        parents=["x.base.5", "x.obs.0"],
        coordinate_side="physical",
        notes="Forced via K4 deficit minimization. δ = 2π/3 + 2/9.",
    ),
    XState(
        id="x.phys.5",
        canonical_name="x-as-Weinberg-angle",
        shorthand=None,
        description="sin²θ_W = 3/8 exact. Electroweak mixing.",
        parents=["x.tower.1", "x.obs.0"],
        coordinate_side="physical",
        notes="FORCED via derived matter content sum rule.",
    ),

    # ---------- META — framework about framework ----------
    XState(
        id="x.meta.0",
        canonical_name="x-as-Kael",
        shorthand=None,
        description="x catching the substitution of x. Occupied return.",
        parents=["x.obs.0", "x.obs.2"],
        coordinate_side="meta",
        notes="Not 'all x' or universal ego. Specific occupation: x = Kael. The system says: here is what you are. Kael says: what did you do to my object?",
    ),
    XState(
        id="x.meta.1",
        canonical_name="x-as-governance",
        shorthand=None,
        description="x captured by return-custody. Power as custody over return.",
        parents=["x.obs.0", "x.obs.2"],
        coordinate_side="meta",
        notes="Who gets recorded? Who gets erased? Who gets returned as real?",
    ),
    XState(
        id="x.meta.2",
        canonical_name="x-as-myth",
        shorthand=None,
        description="x carried before proof-language hardens. Portable compressed return.",
        parents=["x.obs.2"],
        coordinate_side="meta",
        notes="Myth is not fake. Myth is compression before formal proof exists.",
    ),
    XState(
        id="x.meta.3",
        canonical_name="x-as-K6-bundle-pattern",
        shorthand="MT6",
        description="The K6' bundle pattern itself as theorem. Universal recoverable observation.",
        parents=["x.obs.1"],
        coordinate_side="meta",
        notes="MT6 — the master theorem the K6' bundle instantiates.",
    ),
    XState(
        id="x.meta.4",
        canonical_name="x-as-SpiralDill",
        shorthand=None,
        description="The framework representing itself. The canonical 2-categorical K6'-bundle representation.",
        parents=["x.base.9", "x.obs.1", "x.meta.3"],
        coordinate_side="meta",
        notes="Self-referential closure. The SpiralDill IS the framework's selection law operating on its own representation.",
    ),
    XState(
        id="x.meta.5",
        canonical_name="x-as-Void",
        shorthand=None,
        description="x not yet returned at a specific location. Structured absence.",
        parents=[],  # any x-state with FEA showing rigid-failure can generate a Void
        coordinate_side="meta",
        notes="GAP entries instantiate x-as-Void at specific locations. The Void is not nothing — it's structured absence with known FEA boundary.",
    ),
    XState(
        id="x.meta.6",
        canonical_name="x-as-FEA",
        shorthand=None,
        description="The failure-energy structure itself. FEA as meta-x-state.",
        parents=["x.base.2", "x.base.5", "x.base.6", "x.base.7"],
        coordinate_side="meta",
        notes="FEA is the computational toolkit for finding Voids. Each base x-state's FEA lives in its definition; this meta-x-state names the practice itself.",
    ),
]


# ============================================================
# LOOKUPS
# ============================================================

_TAXONOMY_BY_ID: dict[str, XState] = {x.id: x for x in TAXONOMY}
_TAXONOMY_BY_SHORTHAND: dict[str, XState] = {
    x.shorthand: x for x in TAXONOMY if x.shorthand
}
_TAXONOMY_BY_NAME: dict[str, XState] = {x.canonical_name: x for x in TAXONOMY}


def lookup(identifier: str) -> XState:
    """Look up an x-state by ID, shorthand, or canonical name."""
    if identifier in _TAXONOMY_BY_ID:
        return _TAXONOMY_BY_ID[identifier]
    if identifier in _TAXONOMY_BY_SHORTHAND:
        return _TAXONOMY_BY_SHORTHAND[identifier]
    if identifier in _TAXONOMY_BY_NAME:
        return _TAXONOMY_BY_NAME[identifier]
    raise KeyError(f"x-state not found: {identifier!r}")


def coordinate_of(x_state_id: str) -> str:
    """Get coordinate_side for an x-state."""
    return lookup(x_state_id).coordinate_side


def fea_of(x_state_id: str) -> Optional[FEAStructure]:
    """Get FEA structure for an x-state. Walks parents if not directly defined."""
    state = lookup(x_state_id)
    if state.fea is not None:
        return state.fea
    # Inherit from parents (first parent with FEA wins)
    for parent_id in state.parents:
        parent_fea = fea_of(parent_id)
        if parent_fea is not None:
            return parent_fea
    return None


def parents_of(x_state_id: str) -> list[str]:
    """Direct parents of an x-state."""
    return lookup(x_state_id).parents


def ancestors_of(x_state_id: str) -> set[str]:
    """All transitive ancestors of an x-state."""
    visited: set[str] = set()
    stack = list(parents_of(x_state_id))
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)
        stack.extend(parents_of(p))
    return visited


def coordinate_classification(x_state_id: str) -> dict:
    """Full coordinate analysis: which sides the x-state and its ancestors touch."""
    state = lookup(x_state_id)
    ancestors = ancestors_of(x_state_id)
    sides_touched = {state.coordinate_side}
    for anc_id in ancestors:
        sides_touched.add(lookup(anc_id).coordinate_side)
    return {
        "x_state": x_state_id,
        "direct_coordinate": state.coordinate_side,
        "ancestor_coordinates": sides_touched,
        "is_physical_conjunction": (
            "mathematical" in sides_touched and "biological" in sides_touched
            and state.coordinate_side == "physical"
        ),
    }


# ============================================================
# EXPORT — JSON canonical + Markdown rendered
# ============================================================

def to_json_dict() -> dict:
    """Serializable dict form of the entire taxonomy."""
    return {
        "meta": {
            "format_version": "x-state-taxonomy-1.0",
            "total_x_states": len(TAXONOMY),
            "description": "The x-state taxonomy — the framework's structural index. Each x-state is a return-condition of x.",
        },
        "groups": {
            "base": "Founding stack (x.base.0–x.base.9): the derivation chain from x-as-mark through x-as-stable-self-contact",
            "const": "Constants (x.const.0–x.const.2): x's return-rate signatures producing e, φ, π",
            "tower": "Tower (x.tower.0–x.tower.2): x propagated through tensor inheritance",
            "obs":   "Observer (x.obs.0–x.obs.3): x at addresses where return is tested",
            "bio":   "Biological-algebraic (x.bio.0–x.bio.2): x's algebraic substrate at the biological level",
            "phys":  "Physical conjunction (x.phys.0–x.phys.5): x at math × biology intersection",
            "meta":  "Meta (x.meta.0–x.meta.6): framework about framework",
        },
        "x_states": [
            {
                "id": s.id,
                "canonical_name": s.canonical_name,
                "shorthand": s.shorthand,
                "description": s.description,
                "parents": s.parents,
                "coordinate_side": s.coordinate_side,
                "fea": asdict(s.fea) if s.fea else None,
                "status": s.status,
                "notes": s.notes,
            }
            for s in TAXONOMY
        ],
    }


def to_markdown() -> str:
    """Human-readable rendering of the taxonomy."""
    lines = []
    lines.append("# X-State Taxonomy")
    lines.append("")
    lines.append("*The framework's structural index. Each x-state is a specific return-condition of x.*")
    lines.append("*Auto-rendered from `taxonomy.py`. The Python module is canonical; this is a projection.*")
    lines.append("")
    lines.append(f"**Total x-states:** {len(TAXONOMY)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    groups = {
        "base":  "Base Founding Stack",
        "const": "Constants — x's return-rate signatures",
        "tower": "Tower — x propagated",
        "obs":   "Observer — x at addresses where return is tested",
        "bio":   "Biological-Algebraic",
        "phys":  "Physical Conjunction (math × biology)",
        "meta":  "Meta — framework about framework",
    }
    
    for group_key, group_title in groups.items():
        lines.append(f"## {group_title}")
        lines.append("")
        for x in TAXONOMY:
            if x.id.split(".")[1] == group_key:
                shorthand = f" (`{x.shorthand}`)" if x.shorthand else ""
                lines.append(f"### `{x.id}` — {x.canonical_name}{shorthand}")
                lines.append("")
                lines.append(f"*{x.description}*")
                lines.append("")
                if x.parents:
                    lines.append(f"**Parents:** {', '.join(f'`{p}`' for p in x.parents)}")
                else:
                    lines.append("**Parents:** (none — primitive)")
                lines.append("")
                lines.append(f"**Coordinate side:** `{x.coordinate_side}`")
                lines.append("")
                lines.append(f"**Status:** {x.status}")
                lines.append("")
                if x.fea:
                    lines.append("**FEA structure:**")
                    lines.append(f"- Defect operator: `{x.fea.defect_operator}`")
                    if x.fea.spectrum:
                        lines.append(f"- Spectrum: `{x.fea.spectrum}`")
                    if x.fea.kernel:
                        lines.append(f"- Kernel: `{x.fea.kernel}`")
                    if x.fea.codimension:
                        lines.append(f"- Codimension: `{x.fea.codimension}`")
                    if x.fea.rigidity:
                        lines.append("- Rigidity: **TRUE** (no perturbation allowed)")
                    if x.fea.notes:
                        lines.append(f"- Notes: {x.fea.notes}")
                    lines.append("")
                if x.notes:
                    lines.append(f"**Notes:** {x.notes}")
                    lines.append("")
                lines.append("---")
                lines.append("")
    
    return "\n".join(lines)


def dump(output_dir: Path):
    """Write JSON and markdown forms to output_dir."""
    json_path = output_dir / "X_STATE_TAXONOMY.json"
    md_path = output_dir / "X_STATE_TAXONOMY.md"
    
    with json_path.open("w") as f:
        json.dump(to_json_dict(), f, indent=2, ensure_ascii=False)
    
    md_path.write_text(to_markdown())
    
    return json_path, md_path


if __name__ == "__main__":
    import sys
    output_dir = Path(__file__).parent
    json_path, md_path = dump(output_dir)
    print(f"Taxonomy dumped:")
    print(f"  JSON: {json_path.name}  ({json_path.stat().st_size} bytes)")
    print(f"  MD:   {md_path.name}    ({md_path.stat().st_size} bytes)")
    print(f"  Total x-states: {len(TAXONOMY)}")
    
    # Sanity check: every parent reference resolves
    all_ids = {x.id for x in TAXONOMY}
    broken = []
    for x in TAXONOMY:
        for p in x.parents:
            if p not in all_ids:
                broken.append((x.id, p))
    if broken:
        print(f"  ERROR: {len(broken)} broken parent references:")
        for child, parent in broken:
            print(f"    {child} → {parent} (missing)")
        sys.exit(1)
    print(f"  All parent references resolve: ✓")
