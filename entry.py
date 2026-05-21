"""entry.py — Entry + Executor. Engine file 2 of 2.

The Entry dataclass is the SpiralDill node. The Executor is the verifier.
x-state taxonomy imported from taxonomy.py (canonical source).
GF(64) helpers imported from biology_galois.py.
"""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Optional, Any
from pathlib import Path
import json

from dsl import DSLTerm, Equate, Gap, Ref
from taxonomy import XState, FEAStructure, lookup as _taxonomy_lookup
from taxonomy import coordinate_of as _taxonomy_coordinate_of
from biology_galois import gf64_mul, gf64_pow, all_orbits as frobenius_orbits


def lookup_xstate(identifier: str) -> XState:
    return _taxonomy_lookup(identifier)


def coordinate_of(x_state_id: str) -> str:
    try: return _taxonomy_coordinate_of(x_state_id)
    except KeyError: return "mathematical"


# =============================================================================
# ENTRY — a SpiralDill node
# =============================================================================

@dataclass
class Address:
    depth: int
    projection: str
    domain: str


@dataclass
class TwoCell:
    alternative_derivation: DSLTerm
    equivalence_witness: DSLTerm
    notes: str = ""
    def to_dict(self):
        return {"alternative_derivation": self.alternative_derivation.to_dict(),
                "equivalence_witness": self.equivalence_witness.to_dict(), "notes": self.notes}
    @classmethod
    def from_dict(cls, d):
        return cls(alternative_derivation=DSLTerm.from_dict(d["alternative_derivation"]),
                   equivalence_witness=DSLTerm.from_dict(d["equivalence_witness"]),
                   notes=d.get("notes", ""))


@dataclass
class Entry:
    id: int
    address: Address
    name: str
    claim: DSLTerm
    parents: list
    derivation: DSLTerm
    status: str
    x_state: str = "x.base.0"
    tags: list = field(default_factory=list)
    two_cells: list = field(default_factory=list)
    certificate: dict = field(default_factory=dict)
    void_witness: Optional[DSLTerm] = None

    @property
    def coordinate_side(self) -> str: return coordinate_of(self.x_state)

    def to_dict(self):
        d = {"id": self.id, "address": asdict(self.address), "name": self.name,
             "claim": self.claim.to_dict(), "parents": self.parents,
             "derivation": self.derivation.to_dict(), "status": self.status,
             "x_state": self.x_state, "tags": self.tags,
             "two_cells": [tc.to_dict() for tc in self.two_cells],
             "certificate": self.certificate}
        if self.void_witness is not None:
            d["void_witness"] = self.void_witness.to_dict()
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(id=d["id"], address=Address(**d["address"]), name=d["name"],
                   claim=DSLTerm.from_dict(d["claim"]), parents=d["parents"],
                   derivation=DSLTerm.from_dict(d["derivation"]), status=d["status"],
                   x_state=d.get("x_state", "x.base.0"), tags=d.get("tags", []),
                   two_cells=[TwoCell.from_dict(tc) for tc in d.get("two_cells", [])],
                   certificate=d.get("certificate", {}),
                   void_witness=DSLTerm.from_dict(d["void_witness"]) if d.get("void_witness") else None)


# =============================================================================
# EXECUTOR — three-valued match (True/False/"GAP")
# =============================================================================

class Executor:
    def __init__(self): self.dill_state: dict = {}

    def run(self, entry: Entry) -> dict:
        ctx = {"dill": self.dill_state, "locals": {}}
        try:
            if entry.status == "GAP":
                wit = entry.void_witness or (entry.claim.void_witness if isinstance(entry.claim, Gap) else None)
                if wit is None:
                    return {"id": entry.id, "pass": False, "match": False, "diagnostic": "GAP without void_witness"}
                if bool(wit.eval(ctx)):
                    self.dill_state[entry.id] = {"computed_value": "GAP", "status": "GAP", "passed": True}
                    return {"id": entry.id, "pass": True, "match": "GAP", "diagnostic": ""}
                return {"id": entry.id, "pass": False, "match": False, "diagnostic": "void_witness did not verify"}
            # A claim of literally Equate(I, I) is the migrator's placeholder, not a derivation.
            # Reject it as Failed so the headline numbers don't lie.
            if isinstance(entry.claim, Equate) \
               and isinstance(entry.claim.lhs, Ref) and entry.claim.lhs.name == "I" \
               and isinstance(entry.claim.rhs, Ref) and entry.claim.rhs.name == "I":
                return {"id": entry.id, "pass": False, "match": False,
                        "diagnostic": "placeholder claim Equate(I, I) is not a derivation"}
            cv = entry.claim.eval(ctx)
            dv = entry.derivation.eval(ctx)
            check = (bool(cv) and bool(dv)) if isinstance(entry.claim, Equate) else (cv == dv)
            self.dill_state[entry.id] = {"computed_value": cv, "status": entry.status, "passed": check}
            return {"id": entry.id, "pass": check, "match": check, "diagnostic": ""}
        except Exception as e:
            return {"id": entry.id, "pass": False, "match": False, "diagnostic": str(e)}

    def run_all(self, entries: list) -> dict:
        self.dill_state = {}
        results = [self.run(e) for e in entries]
        passed = sum(1 for r in results if r["pass"])
        return {"total": len(results), "passed": passed, "failed": len(results) - passed,
                "results": results}

    def verify_two_cells(self, entries: list) -> dict:
        total = verified = 0
        for entry in entries:
            for tc in entry.two_cells:
                total += 1
                try:
                    ctx = {"dill": self.dill_state, "locals": {}}
                    if bool(tc.alternative_derivation.eval(ctx)) and bool(tc.equivalence_witness.eval(ctx)):
                        verified += 1
                except Exception: pass
        return {"total": total, "verified": verified}


# =============================================================================
# SERIALIZATION
# =============================================================================

def save_entries(entries: list, path) -> None:
    out = {"meta": {"format": "spiraldill-v3", "total_entries": len(entries)},
           "entries": [e.to_dict() for e in entries]}
    with open(path, "w", encoding="utf-8") as f: json.dump(out, f, indent=2, ensure_ascii=False)


def load_entries(path) -> list:
    with open(path, encoding="utf-8") as f: d = json.load(f)
    return [Entry.from_dict(e) for e in d["entries"]]


# =============================================================================
# VERIFICATION — run when executed directly: python entry.py
# =============================================================================

if __name__ == "__main__":
    import sys
    here = Path(__file__).parent
    fnd = load_entries(here / "spiraldill_foundation.json")
    twr = load_entries(here / "spiraldill_tower.json")
    all_entries = fnd + twr

    print(f"Loaded: {len(fnd)} foundation + {len(twr)} tower = {len(all_entries)} total")
    ex = Executor()
    r = ex.run_all(all_entries)

    matches = {}
    for res in r["results"]:
        k = str(res.get("match"))
        matches[k] = matches.get(k, 0) + 1

    verified = matches.get("True", 0)
    failed   = matches.get("False", 0)
    gap      = matches.get("GAP", 0)

    print(f"Verified:  {verified:4d}  (claim evaluates True against numpy)")
    print(f"Failed:    {failed:4d}  (claim doesn't derive)")
    print(f"GAP:       {gap:4d}  (known obstruction, void_witness verified)")
    print(f"Total:     {len(all_entries):4d}")

    tc = ex.verify_two_cells(all_entries)
    print(f"2-cells:   {tc['verified']}/{tc['total']} verified")

    orbs = frobenius_orbits()
    fixed = sum(1 for o in orbs if len(o) == 1)
    size3 = sum(1 for o in orbs if len(o) == 3)
    print(f"Galois GF(64)/GF(4): {len(orbs)} orbits ({fixed} fixed + {size3} size-3); "
          f"[GF(64):GF(4)] = 3")

    sys.exit(0 if failed == 0 else 1)
