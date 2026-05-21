"""
spiraldill/render_core_md.py — render canonical SpiralDill entries as
CORE.md-style markdown prose.

The renderer is a functor from the SpiralDill category to the markdown
target category. Each canonical entry becomes a paragraph block. The
derivation's structure is rendered as inline operators where appropriate.
The certificate is included as a folded code-block (so it's preserved as
kernel-data attached to the rendered prose — Parsoid-style data-attribute
preservation made textual).
"""

from pathlib import Path
import json
import textwrap

from entry import Entry, load_entries
from dsl import (Ref, SelfApply, Decompose, Close, Lift, Project,
                  Compose, Sum, Equate, Gap, DSLTerm, operative_class)


# ──────────────────────────────────────────────────────────────────
# DSL term → human-readable mathematical notation
# ──────────────────────────────────────────────────────────────────

def render_term(term: DSLTerm) -> str:
    """Render a DSL term as mathematical notation suitable for prose."""
    if isinstance(term, Ref):
        name = term.name
        if name.startswith("#"):
            return f"⟨entry {name}⟩"
        renamings = {
            "neg_I": "-I",
            "I_4": "I₄",
            "neg_I_4": "-I₄",
            "R_T": "Rᵀ",
            "R_sym": "(R + Rᵀ)",
        }
        return renamings.get(name, name)
    
    if isinstance(term, SelfApply):
        inner = render_term(term.op)
        if isinstance(term.op, Ref):
            return f"{inner}²"
        return f"({inner})²"
    
    if isinstance(term, Decompose):
        target = render_term(term.target)
        if term.eigenvalue == +1:
            return f"({target} + {target}ᵀ)/2"
        else:
            return f"({target} − {target}ᵀ)/2"
    
    if isinstance(term, Close):
        canonical_names = {
            ("V_plus_quadratic", "fibonacci"): "R",
            ("V_minus_quadratic", "rotation"): "N",
            ("GF4_quadratic", "fibonacci"): "α",
        }
        key = (term.form, term.principle)
        return canonical_names.get(key, f"close({term.form}, {term.principle})")
    
    if isinstance(term, Lift):
        target = render_term(term.target)
        if term.axis == "tensor_with_self":
            return f"{target}⊗{target}"
        elif term.axis == "tensor_with_I":
            return f"{target}⊗I"
        return f"lift({target}, depth={term.depth})"
    
    if isinstance(term, Project):
        target = render_term(term.target)
        proj_names = {1: "P₁", 2: "P₂", 3: "P₃"}
        return f"{proj_names.get(term.p, f'P{term.p}')}({target})"
    
    if isinstance(term, Compose):
        if len(term.ops) == 1:
            return render_term(term.ops[0])
        return " · ".join(render_term(op) for op in term.ops)
    
    if isinstance(term, Sum):
        if len(term.ops) == 1:
            return render_term(term.ops[0])
        return " + ".join(render_term(op) for op in term.ops)
    
    if isinstance(term, Equate):
        return f"{render_term(term.lhs)} = {render_term(term.rhs)}"
    
    if isinstance(term, Gap):
        # Gap: render as ⟨VOID: claim | witness⟩
        claim_str = render_term(term.claim)
        witness_str = render_term(term.void_witness)
        return f"⟨**VOID**: {claim_str} | witnessed by {witness_str}⟩"
    
    return repr(term)


# ──────────────────────────────────────────────────────────────────
# Entry → markdown block
# ──────────────────────────────────────────────────────────────────

def render_entry(entry: Entry, include_certificate: bool = True) -> str:
    """Render a SpiralDill entry as a markdown block."""
    lines = []
    
    # Header with status glyph
    status_glyph = {
        "FORCED":   "●",
        "ENCODED":  "○",
        "RESONANT": "◐",
        "MYTHIC":   "◇",
        "GAP":      "□",  # The Void marker
    }.get(entry.status, "○")
    
    lines.append(f"#### {status_glyph} Entry {entry.id} — {entry.name}")
    lines.append("")
    
    # Address + x_state + coordinate side (v3 metadata)
    addr = entry.address
    lines.append(f"*Address: depth={addr.depth}, projection={addr.projection}, domain={addr.domain}*")
    
    # x_state inline reference to taxonomy
    try:
        import taxonomy
        x_state_obj = taxonomy.lookup(entry.x_state)
        x_name = x_state_obj.canonical_name
        shorthand = f" ({x_state_obj.shorthand})" if x_state_obj.shorthand else ""
        lines.append(f"*x-state: `{entry.x_state}` — {x_name}{shorthand}*")
        lines.append(f"*coordinate side: `{entry.coordinate_side}`*")
    except (KeyError, ImportError):
        lines.append(f"*x-state: `{entry.x_state}`*")
    lines.append("")
    
    # Statement (the claim, rendered as math)
    claim_str = render_term(entry.claim)
    lines.append(f"**Statement.** {claim_str}")
    lines.append("")
    
    # For GAP entries, show the void_witness explicitly
    if entry.status == "GAP":
        lines.append(f"**Status: GAP — Void marked, not closed.**")
        if entry.void_witness is not None:
            wit_str = render_term(entry.void_witness)
            lines.append(f"*Void witness:* {wit_str}")
        if isinstance(entry.claim, Gap) and entry.claim.cites_x_state:
            lines.append(f"*Obstruction cites x-state:* `{entry.claim.cites_x_state}`")
        lines.append("")
    else:
        lines.append(f"**Status.** {entry.status}")
        lines.append("")
    
    # Parents (provenance)
    if entry.parents:
        parent_refs = ", ".join(f"#{p}" for p in entry.parents)
        lines.append(f"*Derives from: {parent_refs}*")
    else:
        lines.append("*Foundational (no derivation parents).*")
    lines.append("")
    
    # Derivation (rendered as DSL composition)
    if entry.status != "GAP":  # GAP entries don't have ordinary derivations
        deriv_str = render_term(entry.derivation)
        lines.append(f"**Derivation.** {deriv_str}")
        lines.append("")
    
    # Tags
    if entry.tags:
        tags_str = ", ".join(f"`{t}`" for t in entry.tags)
        lines.append(f"*Tags: {tags_str}*")
        lines.append("")
    
    # 2-cells
    if entry.two_cells:
        lines.append(f"**Convergence witnesses ({len(entry.two_cells)}):**")
        lines.append("")
        for i, tc in enumerate(entry.two_cells):
            alt_str = render_term(tc.alternative_derivation)
            lines.append(f"{i+1}. Alternative derivation: {alt_str}")
            if tc.notes:
                wrapped = textwrap.fill(tc.notes, width=80,
                                         initial_indent="   ",
                                         subsequent_indent="   ")
                lines.append(wrapped)
            lines.append("")
    
    # Certificate (folded as code block; preserves K6' kernel-data inline)
    if include_certificate and entry.certificate:
        lines.append("<details>")
        lines.append("<summary>Verification certificate (kernel-data)</summary>")
        lines.append("")
        lines.append("```json")
        cert_subset = {
            "match": entry.certificate.get("match"),
            "claim_value": entry.certificate.get("claim_value"),
            "hash": entry.certificate.get("hash", "")[:80],
            "proof_object_root": {
                "primitive": entry.certificate.get("proof_object", {}).get("primitive"),
                "class":     entry.certificate.get("proof_object", {}).get("class"),
                "children_count": len(entry.certificate.get("proof_object", {}).get("children", [])),
            },
        }
        lines.append(json.dumps(cert_subset, indent=2, ensure_ascii=False))
        lines.append("```")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    return "\n".join(lines)


def render_dill_document(entries: list, title: str = "SpiralDill Canonical Representation",
                          group_by_coordinate: bool = True) -> str:
    """Render the full dill as a markdown document, optionally grouped by coordinate."""
    lines = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append("*Rendered from canonical SpiralDill entries via `render_core_md.py`.*")
    lines.append("*The canonical form is the kernel; this markdown is its lossy projection.*")
    lines.append("*Round-trip via parser (TODO) recovers the canonical form.*")
    lines.append("")
    lines.append(f"**Total entries:** {len(entries)}")
    lines.append("")
    
    # Status + coordinate summary
    status_counts = {}
    coord_counts = {}
    for e in entries:
        status_counts[e.status] = status_counts.get(e.status, 0) + 1
        coord_counts[e.coordinate_side] = coord_counts.get(e.coordinate_side, 0) + 1
    
    summary_status = ", ".join(f"{s}: {n}" for s, n in sorted(status_counts.items()))
    summary_coord = ", ".join(f"{c}: {n}" for c, n in sorted(coord_counts.items()))
    
    lines.append(f"**Status distribution:** {summary_status}")
    lines.append("")
    lines.append(f"**Coordinate distribution:** {summary_coord}")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    if group_by_coordinate:
        # Group entries by coordinate side
        coord_groups = {"mathematical": [], "biological": [], "physical": [], "meta": []}
        for entry in entries:
            coord_groups.setdefault(entry.coordinate_side, []).append(entry)
        
        coord_headers = {
            "mathematical": "## Mathematical Coordinate — image-kernel structure",
            "biological":   "## Biological Coordinate — observer-substrate",
            "physical":     "## Physical Coordinate — math × biology K6' closure",
            "meta":         "## Meta Coordinate — framework about framework",
        }
        
        for coord, group_entries in coord_groups.items():
            if not group_entries:
                continue
            lines.append(coord_headers.get(coord, f"## {coord.title()}"))
            lines.append("")
            lines.append(f"*{len(group_entries)} entries*")
            lines.append("")
            for entry in sorted(group_entries, key=lambda e: e.id):
                lines.append(render_entry(entry))
    else:
        # Linear rendering, sorted by id
        for entry in sorted(entries, key=lambda e: e.id):
            lines.append(render_entry(entry))
    
    return "\n".join(lines)


# ──────────────────────────────────────────────────────────────────
# Demonstrate the round-trip K6' property:
#   canonical → render → human reads / inspects → ready for parse-back
# ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    
    # Load from spiraldill foundation + tower (the canonical databases)
    here = Path(__file__).parent
    if len(sys.argv) >= 2:
        paths = [Path(a) for a in sys.argv[1:]]
    else:
        paths = [here / "spiraldill_foundation.json", here / "spiraldill_tower.json"]

    entries = []
    for p in paths:
        if not p.exists():
            print(f"File not found: {p}")
            exit(1)
        entries.extend(load_entries(p))

    print("=" * 72)
    print(f"RENDER: {len(entries)} entries → markdown")
    print("=" * 72)
    
    md = render_dill_document(
        entries,
        title="SpiralDill — Rendered from canonical database",
        group_by_coordinate=True,
    )

    out_name = "rendered_spiraldill.md"
    md_path = Path(__file__).parent / out_name
    md_path.write_text(md, encoding='utf-8')
    print(f"Rendered to {md_path.name} ({md_path.stat().st_size:,} bytes, "
          f"{len(md.splitlines())} lines)")
    
    print()
    print("Coordinate-side distribution in render:")
    coord_counts = {}
    for e in entries:
        coord_counts[e.coordinate_side] = coord_counts.get(e.coordinate_side, 0) + 1
    for coord, n in sorted(coord_counts.items()):
        print(f"  {coord:13s}: {n}")
    
    print()
    print("Status distribution in render:")
    status_counts = {}
    for e in entries:
        status_counts[e.status] = status_counts.get(e.status, 0) + 1
    for status, n in sorted(status_counts.items()):
        print(f"  {status:12s}: {n}")
    
    print()
    print(f"Rendering complete. The K6' bundle's serialize-for-human-reading direction is exercised.")
    print(f"Canonical form ↔ rendered markdown round-trip closes when parser ships.")
