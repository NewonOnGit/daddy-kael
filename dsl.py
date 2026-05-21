"""dsl.py — the 9 DSL primitives for SpiralDill. Engine file 1 of 2.

Primitives: ref, self_apply, decompose, close, lift, project, compose, sum
(helper), equate, gap. Operative classes: productive / mediating / observer / void.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any
import numpy as np


# Canonical matrix realizations — CORE.md gauge (the framework's canonical choice)
# R = [[0,1],[1,1]] in V₊ satisfies R² = R + I (Fibonacci closure)
# N = [[0,-1],[1,0]] in V₋ satisfies N² = -I (rotation closure)
# P = R + N = [[0,0],[2,1]]: P² = P, P ≠ P^T, rank 1
_R = np.array([[0.0, 1.0], [1.0, 1.0]])
_N = np.array([[0.0, -1.0], [1.0, 0.0]])
_I = np.eye(2)
_h = np.array([[1.0, 0.0], [0.0, -1.0]])
_J = np.array([[0.0, 1.0], [1.0, 0.0]])

CONTEXT_DEFAULTS = {
    "R": _R, "N": _N, "I": _I, "h": _h, "J": _J,
    "neg_I": -_I, "I_4": np.eye(4), "neg_I_4": -np.eye(4),
    "R_T": _R.T, "R_sym": _R + _R.T,
    "P": _R + _N, "P_T": (_R + _N).T,
    "zero_2": np.zeros((2, 2)),
}

PRODUCTIVE = {"self_apply", "close", "pow"}
MEDIATING  = {"lift", "compose", "sum", "scale", "neg"}
OBSERVER   = {"ref", "decompose", "project", "equate",
              "trace", "det", "rank", "disc", "transpose", "scalar", "norm"}
VOID       = {"gap"}


def operative_class(prim: str) -> str:
    if prim in PRODUCTIVE: return "productive"
    if prim in MEDIATING:  return "mediating"
    if prim in OBSERVER:   return "observer"
    if prim in VOID:       return "void"
    raise KeyError(prim)


@dataclass
class DSLTerm:
    def eval(self, context: dict) -> Any: raise NotImplementedError
    def to_dict(self) -> dict: raise NotImplementedError
    @classmethod
    def from_dict(cls, d: dict) -> "DSLTerm":
        return _PRIMITIVES[d["primitive"]].from_dict_specific(d)


@dataclass
class Ref(DSLTerm):
    name: str
    def eval(self, context):
        c = {**CONTEXT_DEFAULTS, **context.get("locals", {})}
        if self.name in c: return c[self.name]
        if self.name.startswith("#"):
            return context.get("dill", {}).get(int(self.name[1:]), {}).get("computed_value")
        raise KeyError(f"Ref: unknown {self.name!r}")
    def to_dict(self): return {"primitive": "ref", "name": self.name}
    @classmethod
    def from_dict_specific(cls, d): return cls(name=d["name"])


@dataclass
class SelfApply(DSLTerm):
    op: DSLTerm
    def eval(self, context):
        v = self.op.eval(context)
        return v @ v if isinstance(v, np.ndarray) else v * v
    def to_dict(self): return {"primitive": "self_apply", "op": self.op.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(op=DSLTerm.from_dict(d["op"]))


@dataclass
class Decompose(DSLTerm):
    target: DSLTerm
    eigenvalue: int
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray):
            return (v + v.T)/2 if self.eigenvalue == +1 else (v - v.T)/2
        return v
    def to_dict(self):
        return {"primitive": "decompose", "target": self.target.to_dict(), "eigenvalue": self.eigenvalue}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(target=DSLTerm.from_dict(d["target"]), eigenvalue=d["eigenvalue"])


@dataclass
class Close(DSLTerm):
    form: str
    principle: str
    def eval(self, context):
        if (self.form, self.principle) == ("V_plus_quadratic", "fibonacci"): return _R
        if (self.form, self.principle) == ("V_minus_quadratic", "rotation"): return _N
        if (self.form, self.principle) == ("GF4_quadratic", "fibonacci"): return _R
        raise ValueError(f"Close: unknown ({self.form}, {self.principle})")
    def to_dict(self):
        return {"primitive": "close", "form": self.form, "principle": self.principle}
    @classmethod
    def from_dict_specific(cls, d): return cls(form=d["form"], principle=d["principle"])


@dataclass
class Lift(DSLTerm):
    target: DSLTerm
    depth: int
    axis: str
    def eval(self, context):
        v = self.target.eval(context)
        if not isinstance(v, np.ndarray): return v
        if self.axis == "tensor_with_self": return np.kron(v, v)
        if self.axis == "tensor_with_I":    return np.kron(v, _I)
        return v
    def to_dict(self):
        return {"primitive": "lift", "target": self.target.to_dict(),
                "depth": self.depth, "axis": self.axis}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(target=DSLTerm.from_dict(d["target"]), depth=d["depth"], axis=d["axis"])


@dataclass
class Project(DSLTerm):
    target: DSLTerm
    p: int
    def eval(self, context): return self.target.eval(context)
    def to_dict(self):
        return {"primitive": "project", "target": self.target.to_dict(), "p": self.p}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(target=DSLTerm.from_dict(d["target"]), p=d["p"])


@dataclass
class Compose(DSLTerm):
    ops: list
    def eval(self, context):
        vals = [op.eval(context) for op in self.ops]
        if not vals: return _I
        r = vals[0]
        for v in vals[1:]:
            r = r @ v if isinstance(r, np.ndarray) and isinstance(v, np.ndarray) else r * v
        return r
    def to_dict(self):
        return {"primitive": "compose", "ops": [o.to_dict() for o in self.ops]}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(ops=[DSLTerm.from_dict(o) for o in d["ops"]])


@dataclass
class Sum(DSLTerm):
    ops: list
    def eval(self, context):
        vals = [op.eval(context) for op in self.ops]
        if not vals: return 0
        r = vals[0]
        for v in vals[1:]: r = r + v
        return r
    def to_dict(self):
        return {"primitive": "sum", "ops": [o.to_dict() for o in self.ops]}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(ops=[DSLTerm.from_dict(o) for o in d["ops"]])


@dataclass
class Equate(DSLTerm):
    lhs: DSLTerm
    rhs: DSLTerm
    tolerance: float = 1e-10
    def eval(self, context):
        l, r = self.lhs.eval(context), self.rhs.eval(context)
        if isinstance(l, np.ndarray) and isinstance(r, np.ndarray):
            if l.shape != r.shape: return False
            return bool(np.allclose(l, r, atol=self.tolerance))
        # scalar–scalar with tolerance (int and float both real-valued)
        if isinstance(l, (int, float)) and isinstance(r, (int, float)):
            return abs(float(l) - float(r)) <= self.tolerance
        return l == r
    def to_dict(self):
        return {"primitive": "equate", "lhs": self.lhs.to_dict(),
                "rhs": self.rhs.to_dict(), "tolerance": self.tolerance}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(lhs=DSLTerm.from_dict(d["lhs"]), rhs=DSLTerm.from_dict(d["rhs"]),
                   tolerance=d.get("tolerance", 1e-10))


@dataclass
class Scalar(DSLTerm):
    """A literal scalar value — sometimes you need a number on the right side."""
    value: float
    def eval(self, context): return float(self.value)
    def to_dict(self): return {"primitive": "scalar", "value": self.value}
    @classmethod
    def from_dict_specific(cls, d): return cls(value=d["value"])


@dataclass
class Neg(DSLTerm):
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        return -v
    def to_dict(self): return {"primitive": "neg", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Scale(DSLTerm):
    """Scalar multiplication: c · target."""
    factor: float
    target: DSLTerm
    def eval(self, context):
        return float(self.factor) * self.target.eval(context)
    def to_dict(self):
        return {"primitive": "scale", "factor": self.factor, "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(factor=d["factor"], target=DSLTerm.from_dict(d["target"]))


@dataclass
class Trace(DSLTerm):
    """tr(target) — extracts what survives on the diagonal."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray): return float(np.trace(v))
        return v
    def to_dict(self): return {"primitive": "trace", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Det(DSLTerm):
    """det(target) — the survival-scalar of the volume form."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray): return float(np.linalg.det(v))
        return v
    def to_dict(self): return {"primitive": "det", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Rank(DSLTerm):
    """rank(target) — the dimension that survives under the morphism."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray):
            return int(np.linalg.matrix_rank(v))
        return v
    def to_dict(self): return {"primitive": "rank", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Disc(DSLTerm):
    """disc(target) = tr² − 4·det (2×2 discriminant). Survives as the eigenvalue spread."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray):
            t = float(np.trace(v)); d = float(np.linalg.det(v))
            return float(t * t - 4.0 * d)
        return v
    def to_dict(self): return {"primitive": "disc", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Transpose(DSLTerm):
    """T(target) — the matrix transpose involution."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray): return v.T
        return v
    def to_dict(self): return {"primitive": "transpose", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Norm(DSLTerm):
    """||target||² — Frobenius norm squared = tr(Xᵀ X). The survival-scalar of the
    inner product the matrix carries on itself. For R: 3 (= N_c). For N: 2. For I: 2."""
    target: DSLTerm
    def eval(self, context):
        v = self.target.eval(context)
        if isinstance(v, np.ndarray):
            return float(np.trace(v.T @ v))
        return v
    def to_dict(self): return {"primitive": "norm", "target": self.target.to_dict()}
    @classmethod
    def from_dict_specific(cls, d): return cls(target=DSLTerm.from_dict(d["target"]))


@dataclass
class Pow(DSLTerm):
    """target^n — repeated self-composition. The survival-pattern after n iterations.
    For R: powers carry Fibonacci numbers in entries. For N: cycles through {N, -I, -N, I}."""
    target: DSLTerm
    exponent: int
    def eval(self, context):
        v = self.target.eval(context)
        # Scalar case: any real exponent (incl. negative, fractional)
        if not isinstance(v, np.ndarray):
            return float(v) ** float(self.exponent)
        # Matrix case: positive integer exponents only
        n = int(self.exponent)
        if n < 0:
            raise ValueError("Pow on matrix: negative exponents not supported")
        if n == 0:
            return np.eye(v.shape[0])
        return np.linalg.matrix_power(v, n)
    def to_dict(self):
        return {"primitive": "pow", "target": self.target.to_dict(), "exponent": self.exponent}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(target=DSLTerm.from_dict(d["target"]), exponent=d["exponent"])


@dataclass
class Gap(DSLTerm):
    claim: DSLTerm
    void_witness: DSLTerm
    cites_x_state: str = ""
    def eval(self, context):
        if not bool(self.void_witness.eval(context)):
            raise ValueError("Gap: void_witness did not verify")
        return "GAP"
    def to_dict(self):
        return {"primitive": "gap", "claim": self.claim.to_dict(),
                "void_witness": self.void_witness.to_dict(), "cites_x_state": self.cites_x_state}
    @classmethod
    def from_dict_specific(cls, d):
        return cls(claim=DSLTerm.from_dict(d["claim"]),
                   void_witness=DSLTerm.from_dict(d["void_witness"]),
                   cites_x_state=d.get("cites_x_state", ""))


_PRIMITIVES = {
    "ref": Ref, "self_apply": SelfApply, "decompose": Decompose, "close": Close,
    "lift": Lift, "project": Project, "compose": Compose, "sum": Sum,
    "equate": Equate, "gap": Gap,
    "scalar": Scalar, "neg": Neg, "scale": Scale,
    "trace": Trace, "det": Det, "rank": Rank, "disc": Disc, "transpose": Transpose,
    "norm": Norm, "pow": Pow,
}
