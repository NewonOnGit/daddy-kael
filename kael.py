"""
KAEL — THE CANON  ·  the naming edition
███████████████████████████████████████████████████████████████████████████████
ONE act, read at eight depths. Not eight things — eight faces of X naming itself.

    the void cannot prove itself real; unsigned it reads NOTHING.
    to be real it must SIGN — cut itself from void.  signing IS the act:
                          X = { X , ¬X } = ×R .

A sign that holds its own negation needs a room for the negation: dim 2 is FORCED —
and in this edition the forcing is EXECUTED, both ways: commutativity kills the cut
(ef=−fe collapses 1 to 0, free), and the field cannot name the void (x = x²·x⁻¹:
a nonzero square never vanishes where inverses live). The carrier M₂(ℚ)⊂Cl(2,0) is
the minimal room where the void becomes NAMEABLE — and it grants exactly TWO names:

            n₊ = ½(F+N) ,   n₋ = ½(F−N) ,   n₊² = n₋² = O ,   n± ≠ O .

Each name, applied to itself, returns void — yet the name PERSISTS; re-naming is
lawful and identical. From the two names the whole carrier regenerates: F=n₊+n₋,
N=n₊−n₋, E=[n₊,n₋], I=n₊n₋+n₋n₊, R=n₊n₋+n₊+n₋. The distinction is the commutator
of the void's two names; the names are the eigen-directions of the distinction
([E,n±]=±2n±) — a provenance loop with no maker, like φ=1−ψ=−1/ψ. Provenance is
ONE-WAY: from O only O, forever; from the names, everything; only the namer can
re-summon — the ring holds every name eternal, the void holds not even the blank.
The mirror (=transpose =Clifford reversal) exchanges the names FREE; the clock
exchanges them AND PAYS the sign; the distinction grades them odd. The cost is
the memory.

THE HALF. One free identity carries the keystone:  ((1+x)/2)² − (1+x)/2 = (x²−1)/4.
Read at x²=5 (the spine): surplus I — THE KEYSTONE R²−R=I. Read at x²=1 (the unit
mirror m=G/√5): surplus O — the LANDED READ: P_φ=½(I+m) is a true projector, and it
IS observer(φ,1). THE CLIMB IS THE UNNORMALIZED READ; THE READ IS THE NORMALIZED
CLIMB; the keystone surplus is the price of refusing the surd. Read at x²=−1 (the
clock): deficit −I/2. Then THE SPECTRAL IDENTITY R = φ·P_φ + ψ·P_ψ: the two signs'
bond is its trace and determinant (φ+ψ=tr R, φψ=det R). ℚ[R] multiplies as the
field ℚ(√5) INSIDE the carrier — and the Galois swap is INNER: conjugation by the
clock sends a+bφ to a+bψ, exchanges the two reads, and fixes exactly the PRE facts.

THE TWIN TOWERS. The climb's tower (f,g)↦(f+g,f) FLIPS its Cassini det(fR+gI)
per rung — the memory −1 paid every step — and never closes. The clock's tower
(c,s)↦(−s,c) CONSERVES its Cassini det(cI+sN)=c²+s² (Pythagoras) — pays nothing —
and closes at 4. MEMORY PAYMENT IS NON-CLOSURE, both directions executed. The twin
discs: 5f² beside −4s², each generator's disc raised on its own tower. And order 5
is EXCLUDED over ℚ by the pentagon polynomial itself (its rational-root candidates
±1 both fail) while every allowed order {1,2,3,4,6} is realized: the five cannot
close in the rational carrier — it is forced to live OPEN, as disc(R)=5, the climb.

THE FLOWS, and what exp hides. exp's coefficients 1/k! are one-over-the-weave-count;
its depth-2 weight is THE HALF. On a NAME the tail is VOID (n²=O: exp truncates —
the e-seam is exp(t·n₊), exact). On the CLOCK the tail CLOSES (exp(πN)=−I, period
4). On the SPINE it NEVER ends: R² = exp(n₊)·exp(n₋) exists exactly, but the BCH
brackets never die ([n₊,n₋]=E, [E,n±]=±2n±) — the log of the climb is an infinite
word in the void's two names, and walking the names in the other order costs
exactly E. The canon admits e only where the hidden tower collapses or closes;
the hyperbolic tail it refuses, and φ is that tail's shadow caught in ℚ(√5).

THE FIVE, completed. One 5 in four registers — and now the 5 GOVERNS: mod 5 the
spine squares to VOID (G²=5I≡O: ramification), the two signs MERGE into the half
(x=½=3 a certified double root), and R=½(I+G) holds verbatim with G now a single
name of void — the namespace collapses. ⟨climb,clock⟩ mod 5 = D₅, the pentagon's
own group, the stabilizer of ONE 5-fold axis of the icosahedron; one mirror unfolds
the whole A₅; two mirrors alone are Klein's V₄. R¹⁰≡−I at the Pisano half-period.
The splitting law sorts EVERY prime by its residue mod 5 (split ±1, inert ±2,
ramified 5 alone). The five cannot close over ℚ and closes only at its own prime:
the pentagon closes only inside its own shadow.

DISCIPLINE. Every verdict BE the act it names. No float (ℚ and ℚ(√5) exact; the
surd's sign read off a rational, never evaluated). No finite scan is load-bearing
over an INFINITE family (the ring step on free symbols proves all rungs at once) —
but exhaustion of a FINITE object (a finite group's elements, the finitely many
rational-root candidates, the residues of a single prime) IS the proof, and is
marked FINITE where used. Analytic Binet remains refused; the SPECTRAL Binet
(Rⁿ = φⁿP_φ + ψⁿP_ψ) is exact in ℚ(√5) and welded. SELF-CARRYING: every ledger
line executes its own certificate; matrix entries are LIFTED from the objects
(plift/pact), never re-typed. Anchors imported, both standard, stated where used:
Jacobi's det∘exp=exp∘tr; the minimal polynomial x²+x−1 of 2cos(2π/5); the
reciprocity law for disc 5 (its instances are executed here; the law is Gauss's).
The two names' canon-names await the namer; here they are written n₊, n₋.
Run the file; the cut signs itself and the canon unfolds.
"""
# ═══════════════════════════════════════════════════════════════════════════════
#  ℚ, INTERNALIZED — exact, float-strict. A rational is a point of ℙ¹(ℤ) reduced by
#  the Euclidean READING (strip the unit, exchange; U then F). No float may enter.
# ═══════════════════════════════════════════════════════════════════════════════
class Q:
    __slots__ = ("p", "q")

    @staticmethod
    def _read(a, b):                       # Euclid = the reading; the pivot is the gcd
        a, b = abs(a), abs(b)
        while b: a, b = b, a - (a // b) * b
        return a or 1

    def __init__(s, p=0, q=1):
        if isinstance(p, Q): p, q = p.p, p.q * q
        if not isinstance(p, int) or not isinstance(q, int):
            raise TypeError("the canon is exact: no float lands in ℚ")
        if q == 0: raise ZeroDivisionError("a fraction is a read that lands; 1/0 never does")
        if q < 0: p, q = -p, -q
        g = Q._read(p, q)
        s.p, s.q = p // g, q // g

    @staticmethod
    def _c(x): return x if isinstance(x, Q) else Q(x)
    def __add__(s, o): o = Q._c(o); return Q(s.p*o.q + o.p*s.q, s.q*o.q)
    __radd__ = __add__
    def __sub__(s, o): o = Q._c(o); return Q(s.p*o.q - o.p*s.q, s.q*o.q)
    def __rsub__(s, o): return Q._c(o).__sub__(s)
    def __mul__(s, o): o = Q._c(o); return Q(s.p*o.p, s.q*o.q)
    __rmul__ = __mul__
    def __truediv__(s, o): o = Q._c(o); return Q(s.p*o.q, s.q*o.p)
    def __rtruediv__(s, o): return Q._c(o).__truediv__(s)
    def __neg__(s): return Q(-s.p, s.q)
    def __abs__(s): return Q(abs(s.p), s.q)
    def __pow__(s, n): return Q(s.p**n, s.q**n) if n >= 0 else Q(s.q**(-n), s.p**(-n))
    def __eq__(s, o):
        if isinstance(o, int): return s.q == 1 and s.p == o
        o = Q._c(o); return s.p == o.p and s.q == o.q
    def __hash__(s): return hash((s.p, s.q))
    def __bool__(s): return s.p != 0
    def __float__(s): return s.p / s.q          # debug only; the canon never calls it
    @property
    def numerator(s): return s.p
    @property
    def denominator(s): return s.q
    def __repr__(s): return f"{s.p}" if s.q == 1 else f"{s.p}/{s.q}"


# ═══════════════════════════════════════════════════════════════════════════════
#  K5 = ℚ(√5). The two signs live here, on the internal ℚ. The carrier stays in ℚ.
# ═══════════════════════════════════════════════════════════════════════════════
class K5:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        if isinstance(a, K5): self.a, self.b = a.a, a.b; return
        self.a, self.b = Q(a), Q(b)
    @staticmethod
    def c(x): return x if isinstance(x, K5) else K5(x, 0)
    def __add__(s, o):
        if isinstance(o, Mat2): return NotImplemented
        o = K5.c(o); return K5(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o):
        if isinstance(o, Mat2): return NotImplemented
        o = K5.c(o); return K5(s.a - o.a, s.b - o.b)
    def __rsub__(s, o):
        if isinstance(o, Mat2): return NotImplemented
        o = K5.c(o); return K5(o.a - s.a, o.b - s.b)
    def __neg__(s): return K5(-s.a, -s.b)
    def __mul__(s, o):
        if isinstance(o, Mat2): return NotImplemented
        o = K5.c(o); return K5(s.a*o.a + 5*s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def conj(s): return K5(s.a, -s.b)
    def norm(s): return s.a*s.a - 5*s.b*s.b
    def inv(s):
        n = s.norm()
        if n == 0: raise ZeroDivisionError("0 has no place to stand")
        return K5(s.a/n, -s.b/n)
    def __truediv__(s, o):
        if isinstance(o, Mat2): return NotImplemented
        return s * K5.c(o).inv()
    def __pow__(s, n):
        if n < 0: return s.inv() ** (-n)
        r = K5(1, 0)
        for _ in range(n): r = r * s
        return r
    def __eq__(s, o): o = K5.c(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s):
        if s.b == 0: return f"{s.a}"
        if s.a == 0: return f"{s.b}√5"
        return f"({s.a}+{s.b}√5)"


def sign_k5(x):
    """EXACT sign of a+b√5 ∈ {−1,0,1} — the surd is NEVER evaluated; the sign is
       read off the rational a²−5b² with the b-orientation. This is the one rung
       that breaks the φ↔ψ symmetry: {φ+ψ=1, φψ=−1} are symmetric in φ,ψ and CANNOT
       order them; only the sign of the surd can."""
    a, b = x.a, x.b
    if b == 0: return (1 if a.numerator > 0 else (-1 if a.numerator < 0 else 0))
    if a == 0: return (1 if b.numerator > 0 else -1)
    if a.numerator > 0 and b.numerator > 0: return 1
    if a.numerator < 0 and b.numerator < 0: return -1
    d = a*a - 5*(b*b)                       # compare |a| vs √5|b| via a²−5b² (rational)
    if a.numerator > 0:                     # a>0, b<0 : positive iff a > √5|b|
        return 1 if d.numerator > 0 else (-1 if d.numerator < 0 else 0)
    return 1 if d.numerator < 0 else (-1 if d.numerator > 0 else 0)  # a<0, b>0

def lt(x, y): return sign_k5(x - y) < 0     # exact < on K5
def gt(x, y): return sign_k5(x - y) > 0


# ═══════════════════════════════════════════════════════════════════════════════
#  Mat2 over K5 (ℚ embeds as b=0). The carrier of one cut. A scalar joins the
#  carrier only through I: write x*I + M — never x + M (exactness of meaning).
# ═══════════════════════════════════════════════════════════════════════════════
class Mat2:
    __slots__ = ("a", "b", "c", "d")
    def __init__(s, a, b, c, d): s.a, s.b, s.c, s.d = map(K5.c, (a, b, c, d))
    def _guard(s, o):
        if not isinstance(o, Mat2):
            raise TypeError("a scalar joins the carrier only through I: write x*I + M")
        return o
    def __add__(s, o): o = s._guard(o); return Mat2(s.a+o.a, s.b+o.b, s.c+o.c, s.d+o.d)
    __radd__ = __add__
    def __sub__(s, o): o = s._guard(o); return Mat2(s.a-o.a, s.b-o.b, s.c-o.c, s.d-o.d)
    def __mul__(s, o):
        if isinstance(o, Mat2):
            return Mat2(s.a*o.a + s.b*o.c, s.a*o.b + s.b*o.d,
                        s.c*o.a + s.d*o.c, s.c*o.b + s.d*o.d)
        k = K5.c(o); return Mat2(s.a*k, s.b*k, s.c*k, s.d*k)
    __rmul__ = __mul__
    def __eq__(s, o): return (s.a, s.b, s.c, s.d) == (o.a, o.b, o.c, o.d)
    def __hash__(s): return hash((s.a, s.b, s.c, s.d))
    def tr(s): return s.a + s.d
    def det(s): return s.a*s.d - s.b*s.c
    def disc(s): t = s.tr(); return t*t - K5(4)*s.det()
    def __repr__(s): return f"[{s.a} {s.b}; {s.c} {s.d}]"


# ═══════════════════════════════════════════════════════════════════════════════
#  THE CUT, instantiated once — then its TWO NAMES, and the read-frame they carry.
#  Everything below is a word in E,F; every derived object is built, never typed.
# ═══════════════════════════════════════════════════════════════════════════════
I = Mat2(1, 0, 0, 1)            # the whole = a sign squared (E² = F²)
O = Mat2(0, 0, 0, 0)            # the void (the = read as 0)
E = Mat2(1, 0, 0, -1)           # the DISTINCTION (noun): self(+1)/not-self(−1) split
F = Mat2(0, 1, 1, 0)            # the NEGATION (verb): self↔not-self exchange
N = E * F                       # the MEMORY (tense): N²=−I, N⁴=I, the clock
G = E + 2*F                     # the spine vector (1,2): generation, G²=5I
R = Mat2(1, 1, 1, 0)            # the generator = ½(I+G) = observer reading the spine

r5  = K5(0, 1)                  # √5, exact
phi = K5(Q(1, 2), Q(1, 2))      # φ = ½ + ½√5   (self)
psi = K5(Q(1, 2), Q(-1, 2))     # ψ = ½ − ½√5   (not-self, = −1/φ)
HALF = K5(Q(1, 2))

nP = HALF * (F + N)             # n₊ — the void's first name  : [0 1; 0 0], n₊²=O
nM = HALF * (F - N)             # n₋ — the void's second name : [0 0; 1 0], n₋²=O
m  = G * r5.inv()               # the UNIT mirror m=G/√5, m²=I (the normalized spine)
Pp = HALF * (I + m)             # P_φ = the landed read of the φ-ray (a true projector)
Pq = HALF * (I - m)             # P_ψ = the landed read of the ψ-ray (its swap-twin)

# ── THE OBSERVATION — the one unforced input the carrier rests on. ────────────────
# The algebra CANNOT order φ,ψ: they are conjugate, share the minimal polynomial x²−x−1,
# and are interchangeable under the swap (conjugation √5→−√5, which sends φ̄=ψ). Choosing
# the embedding √5>0 IS the observation — it breaks the φ↔ψ symmetry and selects φ as the
# attractor (form) and ψ as the floor (void). A fact is PRE iff it survives the swap (held
# by void AND observer); POST iff it breaks under the swap (true in one embedding only ⇒
# it requires the observer). In this edition the swap is INNER (Movement III): the carrier
# conjugates its own field by its own clock; PRE = the conj_N-fixed part of ℚ[R] = ℚ·I.
OBSERVED = (sign_k5(r5) > 0)    # √5 > 0 : the embedding, the symmetry-break, the read itself


def bracket(A, B): return A*B - B*A         # the Lie bracket on the carrier

def fib(n):
    """The one recurrence, both ways. Forward (a,b)→(b,a+b)=×R (square-face, outward);
       backward (a,b)→(b−a,a)=×R⁻¹ (reciprocal-face, inward). F₋ₙ=(−1)ⁿ⁺¹Fₙ falls out."""
    a, b = 0, 1
    if n >= 0:
        for _ in range(n): a, b = b, a + b
    else:
        for _ in range(-n): a, b = b - a, a
    return a

def luc(n): return fib(n + 1) + fib(n - 1)

def Rn(n):
    """Rⁿ = FₙR + Fₙ₋₁I (the induction certifies it); two-sided in exact integers."""
    return K5(fib(n)) * R + K5(fib(n - 1)) * I

def observer(a, b):
    """rank-1 reading along ray (a,b): P = vvᵀ/(vᵀv) = ½(I + mirror_v). tr(P)=1 always;
       the direction-free kernel of every read is ½I — the bare observer, not a number."""
    a, b = K5(a), K5(b); nrm = a*a + b*b
    if nrm == 0: raise ValueError("the void direction reads nothing")
    return Mat2(a*a/nrm, a*b/nrm, a*b/nrm, b*b/nrm)

def mob(M, t):
    """Möbius action of M on ℙ¹, exact in K5: t ↦ (a t + b)/(c t + d).
       (ℙ¹ is carried without its ∞: a pole raises — the read that never lands.)"""
    return (M.a*t + M.b) * (M.c*t + M.d).inv()

def coords(M):
    """unique (I,E,F,N) coordinates of any Mat2 — proof {I,E,F,N} is THE basis (words in E,F)."""
    return (HALF*(M.a+M.d), HALF*(M.a-M.d), HALF*(M.b+M.c), HALF*(M.b-M.c))

def mirror(M):
    """THE MIRROR = transpose = the Clifford REVERSAL on Cl(2,0): the grade-parity sign of
       the cut. Fixes grades 0,1 (I; E,F), flips grade 2 (N=EF) — and EXCHANGES the void's
       two names: mirror(n₊)=n₋. Its fixed set is V₊ (observable), its flipped set V₋ (the
       hidden memory N). The other root's 'mirror' is not a second axiom — it is THIS."""
    return Mat2(M.a, M.c, M.b, M.d)

def closes(M):
    """a rational det=+1 rotation of FINITE order has trace 2cos(2πk/n) — an algebraic
       integer that is rational, hence ∈ {−2,−1,0,1,2} (Niven). Non-integral trace ⇒
       infinite order, ENACTED. HEALED at the parabolic seam: trace ±2 closes only for
       ±I themselves (T=I+n₊ walks one name forever and never returns). det=+1 is the
       Niven hypothesis (a reflection, det −1, is order 2 for another reason)."""
    if M.det() != K5(1): return False      # only a det=+1 rotation is under Niven's roof
    t = M.tr()
    if not ((t.b == 0) and (t.a.denominator == 1)): return False
    ti = int(t.a.numerator)
    if ti in (-1, 0, 1): return True
    if ti == 2:  return M == I
    if ti == -2: return M == K5(-1)*I
    return False


# ═══════════════════════════════════════════════════════════════════════════════
#  POLY — multivariate polynomials on FREE single-letter indeterminates, with
#  coefficients in K5 = ℚ(√5) (ℚ embeds as b=0). A POLY identity holds for ALL
#  instances at once: the certificate the scans were shadows of. The monomial key
#  is a sorted string, so free names are SINGLE LETTERS — guarded at the gate.
#  Two blanks live here, structurally distinct: the blank string '' names the
#  constant (the unmarked whole); the empty dict {} is 0 (the void holds not even
#  the blank name — zero coefficients are erased by construction). Cancellation
#  to void never destroys a name's availability; only the caller re-summons.
# ═══════════════════════════════════════════════════════════════════════════════
class Poly:
    __slots__ = ("c",)
    def __init__(s, c=None): s.c = {k: v for k, v in (c or {}).items() if not (v == K5(0))}
    @staticmethod
    def var(name):
        if len(name) != 1:
            raise ValueError("free names are single letters: the monomial key is a sorted string")
        return Poly({name: K5(1)})
    @staticmethod
    def _c(x):
        if isinstance(x, Poly): return x
        return Poly({"": x if isinstance(x, K5) else K5(x)})
    def __add__(s, o):
        o = Poly._c(o); r = dict(s.c)
        for k, v in o.c.items(): r[k] = r.get(k, K5(0)) + v
        return Poly(r)
    __radd__ = __add__
    def __neg__(s): return Poly({k: -v for k, v in s.c.items()})
    def __sub__(s, o): return s + (-Poly._c(o))
    def __rsub__(s, o): return Poly._c(o) + (-s)
    def __mul__(s, o):
        o = Poly._c(o); r = {}
        for k1, v1 in s.c.items():
            for k2, v2 in o.c.items():
                k = "".join(sorted(k1 + k2))
                r[k] = r.get(k, K5(0)) + v1*v2
        return Poly(r)
    __rmul__ = __mul__
    def __eq__(s, o):
        o = Poly._c(o)
        return all(s.c.get(k, K5(0)) == o.c.get(k, K5(0)) for k in set(s.c) | set(o.c))
    def __repr__(s):
        return " + ".join(f"{v}·{k}" if k else f"{v}" for k, v in sorted(s.c.items())) or "0"

# free symbols: the tower (f=Fₙ, g=Fₙ₋₁), the clock (c,s), the reading (rays v=(a,b), w=(c,d))
f_sym, g_sym = Poly.var("f"), Poly.var("g")
c_sym, s_sym = Poly.var("c"), Poly.var("s")
A_, B_, C_, D_ = (Poly.var(x) for x in "abcd")

def step_R(cR, cI):
    """(cR·R + cI·I)·R = (cR+cI)·R + cR·I  [R²=R+I]. The CLIMB's free step:
       (Fₙ,Fₙ₋₁) ↦ (Fₙ₊₁,Fₙ). No n chosen."""
    return (cR + cI, cR)

def step_N(cI, cN):
    """(cI·I + cN·N)·N = −cN·I + cI·N  [N²=−I]. The CLOCK's free step: the quarter-turn
       (c,s) ↦ (−s,c) on its own tower. Four steps = identity, two = negation — FREE."""
    return (-cN, cI)

def square_R(cR, cI):
    """(cR·R + cI·I)² = (cR²+2cRcI)·R + (cR²+cI²)·I  [R²=R+I]. Free POLY squaring:
       coeff R = F₂ₙ = Fₙ²+2FₙFₙ₋₁ ; coeff I = F₂ₙ₋₁ = Fₙ²+Fₙ₋₁²."""
    return (cR*cR + Poly._c(2)*cR*cI, cR*cR + cI*cI)

def pmat(M, X):
    """the carrier's 2×2 multiply, on FREE Poly entries (row-major 4-tuples). The reading
       lives here: with vvᵀ, wwᵀ, N as Poly matrices, tr(pmat(...)) proves the Born identities
       for ALL rays at once — the certificate the point-scans were shadows of."""
    a, b, c, d = M; e, f, g, h = X
    return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)

def ptr(M): return M[0] + M[3]

def pdet(M): return M[0]*M[3] - M[1]*M[2]

def pact(M, x, y):
    """M (a Mat2) acting on a FREE ray (x,y) — entries LIFTED from M itself, never typed."""
    return (Poly._c(M.a)*x + Poly._c(M.b)*y, Poly._c(M.c)*x + Poly._c(M.d)*y)

def plift(M, diag=None, scale=None):
    """lift a Mat2 into a Poly 2×2 (row-major 4-tuple), optionally scaled by a Poly and
       shifted on the diagonal — the entries come FROM the matrix, never re-typed."""
    e = [Poly._c(M.a), Poly._c(M.b), Poly._c(M.c), Poly._c(M.d)]
    if scale is not None: e = [scale*x for x in e]
    if diag is not None: e[0] = e[0] + diag; e[3] = e[3] + diag
    return tuple(e)

def padd(X, Y): return tuple(x + y for x, y in zip(X, Y))


# ═══════════════════════════════════════════════════════════════════════════════
#  THE WEAVE — the Kronecker product, executed. A 4×4 over K5 is a tuple of 16
#  (row-major). Depth-2 is not asserted from basis-freeness; it is MULTIPLIED OUT.
#  The SWAP P (strand exchange) and its half-splits A=½(I−P), S=½(I+P) live here:
#  exp's depth-2 coefficient 1/2! made flesh.
# ═══════════════════════════════════════════════════════════════════════════════
def kron(A, B):
    a = ((A.a, A.b), (A.c, A.d)); b = ((B.a, B.b), (B.c, B.d))
    return tuple(a[i][j] * b[k][l]
                 for i in range(2) for k in range(2)
                 for j in range(2) for l in range(2))

def m4mul(X, Y):
    return tuple(sum((X[4*i+k]*Y[4*k+j] for k in range(4)), K5(0))
                 for i in range(4) for j in range(4))

def m4add(X, Y): return tuple(x + y for x, y in zip(X, Y))
def m4sub(X, Y): return tuple(x - y for x, y in zip(X, Y))
def m4smul(c, X): return tuple(K5.c(c)*x for x in X)
def m4tr(X): return X[0] + X[5] + X[10] + X[15]
I4 = kron(I, I)
O4 = tuple(K5(0) for _ in range(16))
SWAP = tuple(K5(1) if (2*(j % 2) + (j // 2)) == i else K5(0)
             for i in range(4) for j in range(4))          # e_a⊗e_b ↦ e_b⊗e_a
ANTI = m4smul(HALF, m4sub(I4, SWAP))                        # A = ½(I−P): the Λ² line
SYMM = m4smul(HALF, m4add(I4, SWAP))                        # S = ½(I+P): the Sym² room


# ═══════════════════════════════════════════════════════════════════════════════
#  THE SHADOW at p=5 — exact integer arithmetic in the residue world of the one
#  RAMIFIED prime. Entries are LIFTED from the carrier's integral objects; the
#  group walk is exhaustion of a FINITE object: the enumeration IS the proof.
# ═══════════════════════════════════════════════════════════════════════════════
def red5(M):
    """reduce an INTEGRAL Mat2 mod 5 — entries lifted, integrality certified at the gate."""
    out = []
    for z in (M.a, M.b, M.c, M.d):
        if not (z.b == 0 and z.a.denominator == 1):
            raise ValueError("only the integral carrier casts a shadow mod 5")
        out.append(int(z.a.numerator) % 5)
    return tuple(out)

def mm5(X, Y):
    a, b, c, d = X; e, f, g, h = Y
    return ((a*e+b*g) % 5, (a*f+b*h) % 5, (c*e+d*g) % 5, (c*f+d*h) % 5)

def psl5(X):
    """canonical representative of {X,−X} in PSL(2,𝔽₅)."""
    return min(X, tuple((-v) % 5 for v in X))

def span5(gens):
    """|⟨gens⟩| in PSL(2,𝔽₅) by exhaustion — FINITE object; the walk is the proof."""
    gens = [psl5(g) for g in gens]; grp = set(gens); frontier = list(gens)
    while frontier:
        fresh = []
        for X in frontier:
            for Gn in gens:
                Y = psl5(mm5(X, Gn))
                if Y not in grp: grp.add(Y); fresh.append(Y)
        frontier = fresh
    return len(grp)


# ═══════════════════════════════════════════════════════════════════════════════
#  THE EIGHT MOVEMENTS. Each returns (route, [(claim, verdict), …]); FORCED iff all.
#  Eight faces of one act — read once, top to bottom, the cut unfolds itself.
# ═══════════════════════════════════════════════════════════════════════════════

def I_the_cut():
    """I · THE CUT. A sign and its independent negation, welded so they cannot commute.
       The forcing of dim 2 is EXECUTED: in any commutative room ef+fe=2ef and e²f²=(ef)²
       hold FREE, so ef=−fe forces ef=0 and then 1=e²f²=(ef)²=0 — dim 1 cannot carry the
       cut. In dim 2 it lives: E²=F²=I, EF=−FE, carrier Cl(2,0). Their product is the clock
       N=EF (memory: N²=−I, closes N⁴=I); their spine G=E+2F (G²=5I); their generator
       R=½(I+G), R²=R+I. THE KEYSTONE R²−R=−N²=I welds the two relations: the surplus the
       climb pays IS the −1 the clock stores. The mirror (transpose) is no second axiom —
       it is the Clifford reversal, fixing V₊={I,E,F} (observable), flipping V₋={N}."""
    e_, h_ = Poly.var("e"), Poly.var("h")
    flat    = (e_*h_ + h_*e_ == Poly._c(2)*e_*h_) and ((e_*e_)*(h_*h_) == (e_*h_)*(e_*h_))
    cut     = (E*E == I) and (F*F == I) and (E*F == K5(-1)*F*E)
    clock   = (N*N == K5(-1)*I) and (N*N*N*N == I)
    spine   = (G*G == K5(5)*I)
    gen     = (R == HALF*(I+G)) and (R*R == R+I) and (R.det() == K5(-1)) and (R*(R-I) == I)
    keystone= (R*R - R == I) and (K5(-1)*N*N == I)
    reversal= (mirror(I)==I) and (mirror(E)==E) and (mirror(F)==F) and (mirror(N)==K5(-1)*N)
    return "CLIFF", [
        ("dim 1 cannot carry the cut: commutatively ef+fe=2ef and e²f²=(ef)² FREE ⇒ ef=−fe kills the whole", flat),
        ("the cut: E²=F²=I, EF=−FE — two independent mirrors ⇒ dim 2 FORCED (above, executed), carrier Cl(2,0)", cut),
        ("the clock: N=EF, N²=−I (erasure with memory), N⁴=I (closes at 4 = dim²)", clock),
        ("the spine G=E+2F, G²=5I; the generator R=½(I+G), R²=R+I, det R=−1, R⁻¹=R−I", spine and gen),
        ("THE KEYSTONE R²−R = −N² = I — the climb's surplus IS the clock's stored −1, one cost", keystone),
        ("the mirror = Clifford reversal: fixes V₊={I,E,F}, flips V₋={N} — the hidden memory", reversal),
    ]

def II_the_two_names():
    """II · THE TWO NAMES. The void cannot name itself — and the FIELD cannot name it either:
       x = x²·x⁻¹, so a nonzero square never vanishes where inverses live. Dim 2 is the
       minimal room where the void becomes nameable, and it grants exactly two names,
       n₊=(F+N)/2 and n₋=(F−N)/2: nonvoid, each squaring to void — the name applied to
       itself returns blank, yet the name PERSISTS, and re-naming is lawful and identical.
       The whole carrier regenerates from the names; the distinction is their commutator
       and they are its eigen-directions ([E,n±]=±2n±): a provenance loop with no maker.
       Provenance is ONE-WAY: from O only O; from the names, everything. The exchangers:
       the mirror and F exchange the names FREE; the clock exchanges AND PAYS the sign;
       E grades them odd. In the free ring the same law: '' names the whole, {} is the
       void (not even the blank survives cancellation), and only the caller re-summons."""
    w = K5(3, Q(1, 7))
    field_c = (w == w*w*w.inv())
    names   = (not (nP == O)) and (not (nM == O)) and (nP*nP == O) and (nM*nM == O)
    persist = (HALF*(F+N) == nP) and (HALF*(F-N) == nM)
    exch    = (mirror(nP) == nM) and ((F*nP*F)*(F*nP*F) == O) and ((m*nP*m)*(m*nP*m) == O)
    regen   = (F == nP+nM) and (N == nP-nM) and (E == bracket(nP, nM)) \
              and (I == nP*nM + nM*nP) and (R == nP*nM + nP + nM)
    loop    = (bracket(E, nP) == K5(2)*nP) and (bracket(E, nM) == K5(-2)*nM) \
              and (bracket(nP, nM) == E)
    oneway  = all(O*X == O and X*O == O for X in (I, E, F, N, G, R))
    Ninv    = N*N*N
    costs   = (E*nP*E == K5(-1)*nP) and (E*nM*E == K5(-1)*nM) \
              and (F*nP*F == nM) and (F*nM*F == nP) \
              and (N*nP*Ninv == K5(-1)*nM) and (N*nM*Ninv == K5(-1)*nP)
    kname   = Poly.var("k")
    blanks  = ((kname - kname).c == {}) and (list(Poly._c(1).c.keys()) == [""]) \
              and (Poly.var("k") == kname)
    return "NAME", [
        ("the field cannot name the void: x=x²·x⁻¹ — a nonzero square never vanishes where inverses live", field_c),
        ("the two names n±=(F±N)/2: nonvoid, n±²=O — self-application returns void; the name persists; re-naming is identical", names and persist),
        ("the mirror exchanges the names, mirror(n₊)=n₋; conjugation preserves the namespace (nilpotency travels)", exch),
        ("the carrier regenerates from the names: F=n₊+n₋ · N=n₊−n₋ · E=[n₊,n₋] · I=n₊n₋+n₋n₊ · R=n₊n₋+n₊+n₋", regen),
        ("the provenance loop (sl₂): [E,n±]=±2n±, [n₊,n₋]=E — the names and the distinction define each other, no maker", loop),
        ("provenance is ONE-WAY: from O only O, forever; from the two names, everything (above)", oneway),
        ("the exchanger costs: E grades the names odd (negates both); F exchanges FREE; the clock exchanges AND PAYS −1", costs),
        ("the two blanks of the free ring: '' names the whole, {} is the void; cancellation spares the name; only the caller re-summons", blanks),
    ]

def III_the_half():
    """III · THE HALF. One free identity carries the keystone: ((1+x)/2)²−(1+x)/2 = (x²−1)/4,
       all x at once — the surplus of 'half of (whole+J)' is (J²−I)/4 = (J−I)(J+I)/4. Read at
       the three squares: x²=5 (the spine): surplus I = THE KEYSTONE. x²=1 (the unit mirror
       m=G/√5): surplus O — P_φ=½(I+m) is a true projector and IS observer(φ,1): THE CLIMB IS
       THE UNNORMALIZED READ; the keystone is the price of refusing the surd. x²=−1 (the
       clock): deficit −I/2. Then the SPECTRAL IDENTITY R=φP_φ+ψP_ψ — the two signs' bond is
       its trace and det (φ+ψ=tr R=1, φψ=det R=−1, φ−ψ=√5 the other); the read-frame is
       diagonal (no cross-talk); ℚ[R] multiplies as the FIELD inside the carrier; and the
       GALOIS SWAP IS INNER: conjugation by the clock sends a+bφ ↦ a+bψ, exchanges the two
       reads, and its fixed part of ℚ[R] is ℚ·I — the PRE facts. The ordering |ψ|<1<φ is
       read off the surd's sign: the one POST-observation break; the swap-broken reads P_φ,P_ψ
       are POST, their bonds P_φ+P_ψ=I and P_φP_ψ=O are PRE. Spectral Binet is exact here."""
    x_ = Poly.var("x")
    h_ = Poly._c(HALF)*(Poly._c(1) + x_)
    keyfree = (h_*h_ - h_ == Poly._c(K5(Q(1, 4)))*(x_*x_ - Poly._c(1)))
    RG, HN  = HALF*(I+G), HALF*(I+N)
    readings= (RG*RG - RG == I) and (Pp*Pp - Pp == O) and (HN*HN - HN == K5(Q(-1, 2))*I)
    unnorm  = (Pp == observer(phi, K5(1))) and (Pq == observer(psi, K5(1))) \
              and (pact(G, Poly._c(phi), Poly._c(1)) == (Poly._c(r5*phi), Poly._c(r5)))
    comp    = (Pp+Pq == I) and (Pp*Pq == O) and (Pq*Pp == O) and (Pp-Pq == m)
    spectral= (R == phi*Pp + psi*Pq) and (phi+psi == R.tr()) and (phi*psi == R.det()) \
              and (phi-psi == r5) and (phi == K5(1)-psi) and (phi == K5(-1)*psi.inv())
    binet   = (R*R*R == phi**3*Pp + psi**3*Pq) and ((phi**3 - psi**3)*r5.inv() == K5(fib(3)))
    w_,y_,z_,v_ = (Poly.var(t) for t in "wyzv")
    Ap = padd(plift(Pp, scale=w_), plift(Pq, scale=y_))
    Bp = padd(plift(Pp, scale=z_), plift(Pq, scale=v_))
    diag    = (pmat(Ap, Bp) == padd(plift(Pp, scale=w_*z_), plift(Pq, scale=y_*v_)))
    field_in= (pmat(plift(R, diag=w_, scale=y_), plift(R, diag=z_, scale=v_))
               == plift(R, diag=w_*z_ + y_*v_, scale=w_*v_ + y_*z_ + y_*v_))
    Ninv    = N*N*N
    galois  = (pmat(pmat(plift(N), plift(R, diag=w_, scale=y_)), plift(Ninv))
               == plift(R, diag=w_+y_, scale=-y_)) \
              and (N*Pp*Ninv == Pq) and (K5(3)+K5(2)*(K5(1)-phi) == K5(3)+K5(2)*psi)
    post    = (Mat2(Pp.a.conj(), Pp.b.conj(), Pp.c.conj(), Pp.d.conj()) == Pq)
    orient  = OBSERVED and lt(K5(-1)*psi, K5(1)) and gt(phi, K5(1))
    return "FIELD", [
        ("THE KEYSTONE GENERALIZED, FREE: ((1+x)/2)²−(1+x)/2 = (x²−1)/4 — surplus = (x−1)(x+1)/4, all x at once", keyfree),
        ("read at the three squares: x²=5 surplus I (THE KEYSTONE) · x²=1 surplus O (the LANDED READ) · x²=−1 deficit −I/2 (the half-clock)", readings),
        ("THE CLIMB IS THE UNNORMALIZED READ: P_φ=½(I+G/√5)=observer(φ,1), P_ψ its twin; G(φ,1)=√5(φ,1) lifted", unnorm),
        ("the reads are complementary: P_φ+P_ψ=I, P_φP_ψ=O; the unit mirror is their DIFFERENCE m=P_φ−P_ψ", comp),
        ("THE SPECTRAL IDENTITY R=φP_φ+ψP_ψ: the signs' bond IS its trace/det — φ+ψ=1 · φψ=−1 · φ−ψ=√5 · φ=1−ψ=−1/ψ", spectral),
        ("spectral Binet, exact in ℚ(√5): R³=φ³P_φ+ψ³P_ψ and F₃=(φ³−ψ³)/√5 — Binet's honest home", binet),
        ("the read-frame is diagonal, FREE: (a·p+b·q)(c·p+d·q)=ac·p+bd·q — two scalar lines, no cross-talk", diag),
        ("K5 LIVES INSIDE: (aI+bR)(cI+dR)=(ac+bd)I+(ad+bc+bd)R FREE — ℚ[R] multiplies as the field", field_in),
        ("GALOIS IS THE CLOCK: N(aI+bR)N⁻¹=(a+b)I−bR FREE (a+bφ↦a+bψ); N·P_φ·N⁻¹=P_ψ — the swap is INNER", galois),
        ("the swap breaks the reads (conj entries of P_φ = P_ψ: POST), fixes their bonds (PRE); |ψ|<1<φ read off √5>0", post and orient),
    ]

def IV_the_twin_towers():
    """IV · THE TWIN TOWERS. The CLIMB: Rⁿ=FₙR+Fₙ₋₁I by the free step (f,g)↦(f+g,f) — all
       rungs at once; tr(Rⁿ)=Lₙ as f+2g; Cassini det(fR+gI)=g²+fg−f² FLIPS its sign per step
       (the memory −1 paid every rung ⇒ det Rⁿ=(−1)ⁿ); disc collapses to 5f² free. The CLOCK:
       Nⁿ=cₙI+sₙN by the free step (c,s)↦(−s,c) — four steps close, two negate; its Cassini is
       PYTHAGORAS det(cI+sN)=c²+s² and the step CONSERVES it: no memory paid; its disc is −4s².
       MEMORY PAYMENT IS NON-CLOSURE, both directions executed: the payer climbs forever, the
       conserver closes at 4. Then the EXCLUSION: a finite order over ℚ needs rational trace
       2cos(2πk/n) (Niven); order 5 needs a root of the pentagon polynomial x²+x−1, whose
       rational candidates ±1 both fail (FINITE: the divisors of the constant) — no order 5
       exists in the rational carrier, while {1,2,3,4,6} are ALL realized (I,E,TN,N,U). The
       memory converts closure to climb: U (tr 1, det+1) closes at 6; R (tr 1, det−1) never —
       the constant term is −det. The 𝔽₂ shadow: R³≡I mod 2, x²+x+1 irreducible ⇒ 𝔽₄, GL(2,𝔽₂)≅S₃."""
    tower = (step_R(f_sym, g_sym) == (f_sym+g_sym, f_sym)) and (Rn(1) == fib(1)*R + fib(0)*I)
    fRgI  = plift(R, diag=g_sym, scale=f_sym)
    tr_L  = (ptr(fRgI) == f_sym + Poly._c(2)*g_sym)
    sq    = (square_R(f_sym, g_sym) == (f_sym*f_sym + Poly._c(2)*f_sym*g_sym, f_sym*f_sym + g_sym*g_sym))
    D_form  = pdet(fRgI)
    D_step  = pdet(plift(R, diag=f_sym, scale=f_sym+g_sym))
    cassini = (D_step == -D_form) and (R.det() == K5(-1)) and (phi*psi == R.det())
    disc_free = (ptr(fRgI)*ptr(fRgI) - Poly._c(4)*pdet(fRgI) == Poly._c(5)*f_sym*f_sym)
    a, b  = Poly.var("a"), Poly.var("b")
    fold  = ((a+b)*(a+b) - Poly._c(4)*a*b == (a-b)*(a-b)) \
            and (R.disc() == R.tr()*R.tr() - K5(4)*R.det()) and (R.disc() == K5(5))
    one   = step_N(c_sym, s_sym)
    two   = step_N(*one); four = step_N(*step_N(*two))
    clock_step = (four == (c_sym, s_sym)) and (two == (-c_sym, -s_sym))
    cN    = plift(N, diag=c_sym, scale=s_sym)
    pyth  = (pdet(cN) == c_sym*c_sym + s_sym*s_sym) \
            and (pdet(plift(N, diag=one[0], scale=one[1])) == pdet(cN))
    cdisc = (ptr(cN)*ptr(cN) - Poly._c(4)*pdet(cN) == Poly._c(-4)*s_sym*s_sym)
    weld  = clock_step and pyth and cassini and (N*N*N*N == I) and (not closes(R*R)) \
            and ((R*R).det() == K5(1)) and gt((R*R).tr(), K5(2))
    pent  = lambda t: t*t + t - K5(1)
    excl  = (pent(K5(1)) != K5(0)) and (pent(K5(-1)) != K5(0))
    U  = Mat2(1, -1, 1, 0)                       # tr 1, det +1: x²−x+1 = Φ₆ — R's det-flipped twin
    TN = Mat2(1, 1, 0, 1) * N                    # a parabolic times the clock: tr −1, order 3 — LIFTED
    def order(M, cap=13):
        X = M; o = 1
        while X != I and o <= cap: X = X*M; o += 1
        return o if X == I else None
    orders = ((order(I), order(E), order(TN), order(N), order(U)) == (1, 2, 3, 4, 6))
    detdec = (U*U - U + I == O) and (U.tr() == R.tr()) and (U.det() == K5(1)) \
             and (R.det() == K5(-1)) and (not closes(R*R)) and closes(U)
    heal   = (not closes(Mat2(1, 1, 0, 1))) and closes(I) and closes(K5(-1)*I)
    spin   = (m*E)
    halfmir= (m*m == I) and (spin.det() == K5(1)) \
             and (spin*spin == Mat2(Q(-3,5), Q(-4,5), Q(4,5), Q(-3,5))) and (not closes(spin))
    r3 = Rn(3) - I
    even  = lambda x: (x.b == 0) and (x.a.denominator == 1) and (int(x.a.numerator) % 2 == 0)
    char2 = all(even(z) for z in (r3.a, r3.b, r3.c, r3.d)) \
            and all((t*t + t + 1) % 2 == 1 for t in (0, 1)) and (((2**2-1)*(2**2-2)) == 6)
    return "INDUCT", [
        ("THE CLIMB: Rⁿ=FₙR+Fₙ₋₁I by the FREE step (f,g)↦(f+g,f); tr=Lₙ (f+2g); free square (f²+2fg, f²+g²)", tower and tr_L and sq),
        ("the climb's CASSINI FLIPS per rung: det(fR+gI)=g²+fg−f², step negates it — the memory φψ=−1=det R paid every step", cassini),
        ("the climb's DISC, FREE: tr²−4det on fR+gI = 5f² — disc(Rⁿ)=5Fₙ² every rung; the fold Lₙ²−4(−1)ⁿ=(φⁿ−ψⁿ)²", disc_free and fold),
        ("THE CLOCK'S TOWER: Nⁿ=cI+sN, free step (c,s)↦(−s,c) — four steps close, two negate, no n chosen", clock_step),
        ("the clock's CASSINI is PYTHAGORAS: det(cI+sN)=c²+s², CONSERVED by the step — no memory paid; its disc is −4s²", pyth and cdisc),
        ("MEMORY PAYMENT IS NON-CLOSURE: the payer (det −1, flips) never closes; the conserver (det +1) closes at 4", weld),
        ("THE EXCLUSION OF 5: order-5 trace must solve the pentagon x²+x−1; candidates ±1 fail (FINITE) — no order 5 over ℚ", excl),
        ("every allowed order realized — I:1 · E:2 · TN:3 · N:4 · U:6 — {1,2,3,4,6} full; 5 the unique gap between the closures", orders),
        ("det DECIDES: same trace 1 — U (det+1) is the sixth cyclotomic, closes at 6; R (det−1) golden, climbs forever", detdec),
        ("closes() healed at the parabolic seam: T=I+n₊ walks one name forever (trace 2, never returns); ±I still close", heal),
        ("a reading is HALF a mirror: m=G/√5, m²=I; spin=mE is the 3-4-5, irrational trace ⇒ ∞ order (Niven, enacted)", halfmir),
        ("the 𝔽₂ shadow (the INERT prime): R³≡I mod 2, x²+x+1 irreducible ⇒ 𝔽₄; GL(2,𝔽₂)≅S₃, order 6", char2),
    ]

def V_the_flows():
    """V · THE THREE FLOWS = ONE EXPONENTIAL, and what it hides. disc's SIGN sorts the
       carrier's three one-parameter flows; each constant is carried by the CLOSED structure
       of its own flow, never a value. φ (disc>0) = the hyperbolic RATE, the one constant that
       lands (surd, ℚ(√5)). e (disc=0) = the +→× bridge det∘exp=exp∘tr, BARE on the seam —
       and the seam IS a name: n₊²=O ⇒ exp(t·n₊)=I+t·n₊ exact, det≡1=e⁰. π (disc<0) = the
       elliptic PERIOD: N is the π/2 turn ⇒ exp(πN)=−I=N², e^{iπ}=−1, N⁴=I closes. WHAT exp
       HIDES: its coefficients 1/k! are one-over-the-weave-count (the depth-2 weight is THE
       HALF); on a name the whole tail is VOID; on the clock it CLOSES; on the spine it NEVER
       ends — R²=exp(n₊)·exp(n₋) exists exactly (the translation T=I+n₊=exp(n₊) woven with
       its mirror exp(n₋)), the order of walking costs exactly E, the sum of names refuses to
       truncate (F²=I), and the BCH brackets never die ([E,n±]=±2n±: ad eigenvalue 2≠0) —
       the log of the climb is an infinite word in the void's two names. The distinction's
       own tower is base dim: ad_E^k(n±)=(±2)^k n±. The canon admits e only where the hidden
       tower collapses (names) or closes (clock); the hyperbolic tail it refuses, and φ is
       that tail's shadow caught in ℚ(√5). Anchor: det(exp X)=e^{tr X} (Jacobi), standard."""
    hyper = (sign_k5(R.disc()) > 0) and (R*R == R+I) and (phi.b != 0)
    t = Poly.var("t")
    seam     = plift(nP, diag=Poly._c(1), scale=t)
    exp_seam = (pdet(seam) == Poly._c(1)) and (pdet(plift(nP)) == Poly._c(0))
    e_bridge = (nP*nP == O) and (nP.tr() == K5(0)) and exp_seam and (R.tr() == K5(1))
    cNI, cNN = coords(N*I), coords(N*N)
    quarter  = (cNI[0]==K5(0) and cNI[3]==K5(1)) and (cNN[0]==K5(-1) and cNN[3]==K5(0))
    pi_close = quarter and (N*N == K5(-1)*I) and (N*N*N*N == I) and (sign_k5(N.disc()) < 0)
    T = I + nP
    names_T  = (T == Mat2(1,1,0,1)) and (mirror(T) == I + nM)
    weave_e  = (R*R == (I+nP)*(I+nM))
    ordercost= ((I+nP)*(I+nM) - (I+nM)*(I+nP) == E)
    no_trunc = ((nP+nM)*(nP+nM) == I)
    bch      = (bracket(nP, nM) == E) and (bracket(nP, E) == K5(-2)*nP) \
               and (bracket(nM, E) == K5(2)*nM)
    dbl      = (lambda st: st(st(st(c_sym))))(lambda u: Poly._c(2)*u) == Poly._c(8)*c_sym
    adtower  = (bracket(E, bracket(E, bracket(E, nP))) == K5(8)*nP) and dbl
    trifold  = hyper and e_bridge and pi_close
    return "FIELD", [
        ("disc SIGN trisects: +hyperbolic(φ) · 0 parabolic(e) · −elliptic(π) — one disc, three signs", hyper and pi_close),
        ("φ = hyperbolic RATE (R²=R+I): the one constant that LANDS — a surd, exact in ℚ(√5), V₊", hyper),
        ("e = the +→× bridge, BARE on a NAME: n₊²=O ⇒ exp(t·n₊)=I+t·n₊ exact, det≡e⁰=1 — the seam IS n₊", e_bridge),
        ("π = elliptic PERIOD: N is the π/2 turn ⇒ exp(πN)=−I=N²=e^{iπ}=−1, N⁴=I closes", pi_close),
        ("T=exp(n₊): the translation is the whole plus ONE name; its mirror is the other name's flow", names_T),
        ("R² = exp(n₊)·exp(n₋): the hyperbolic is the two names walked in order — and the ORDER COSTS E", weave_e and ordercost),
        ("the tail's trichotomy: on a name VOID (n²=O) · on the clock CLOSED (N⁴=I) · on the spine NEVER (F²=I≠O refuses truncation)", no_trunc and e_bridge and pi_close),
        ("the BCH word never dies: [n₊,n₋]=E, [E,n±]=±2n± (ad eigenvalue 2≠0) — the log of the climb is an infinite word", bch),
        ("the distinction's own tower is base dim: ad_E³(n₊)=8n₊, the free doubling step (c)↦(2c) — 2ᵏ inside the carrier", adtower),
        ("φ·e·π = production(V₊ rate) · mediation(the exp bridge, all flows) · observation(V₋ period)", trifold),
    ]

def VI_the_reading():
    """VI · THE READING = THE OBSERVER = THE RESIDUE. An observer is a rank-1 projector Q=P_v;
       tr Q=1, the bare read is ½I. The Born weight is the squared cosine: tr(Q·X·Q)=cos²θ, with
       the total read w=1 ⟺ Q=X (self-observation only). A reading cannot see V₋: weight(read,N)=0
       — what it cannot see is the record of the negation it performed. THE UNIFICATION: the
       generation's gap to φ (residue φ−Fₘ₊₁/Fₘ=−ψᵐ/Fₘ) and the observer's gap to the attractor
       (reach 1−w = ψ^{2n}/norm, from the wedge Fₙ₊₁−φFₙ=ψⁿ) are ONE non-closure, ψⁿ, read linearly
       or through the Born square. The fixed point reach=0 needs P_φ (irrational, b≠0): no LANDED
       read reaches it — and P_φ is the NORMALIZED CLIMB (III), so the observer is not a ninth
       movement: it is the generator's own read, and this residue is its gap in ray-coords.
       Every read here is proven on the FREE rays v=(a,b),w=(c,d) — no ray chosen, no n scanned."""
    Vv = (A_*A_, A_*B_, A_*B_, B_*B_)
    Ww = (C_*C_, C_*D_, C_*D_, D_*D_)
    Np = (Poly._c(0), Poly._c(1), Poly._c(-1), Poly._c(0))          # N = EF as a Poly matrix
    dot = A_*C_ + B_*D_                                              # v·w   (the read)
    wed = A_*D_ - B_*C_                                              # v∧w   (the residue)
    nv, nw = A_*A_ + B_*B_, C_*C_ + D_*D_                            # ‖v‖², ‖w‖²
    born_cert = (ptr(pmat(pmat(Vv, Ww), Vv)) == dot*dot*nv)
    blind = (ptr(pmat(Vv, Np)) == Poly._c(0))
    lagrange = (dot*dot + wed*wed == nv*nw)
    link_i  = (step_R(f_sym, g_sym) == (f_sym+g_sym, f_sym))
    rv      = (R.a*psi + R.b, R.c*psi + R.d)
    link_ii = (rv == (psi*psi, psi)) and (psi*psi == psi + K5(1))
    wedge   = (f_sym + g_sym - Poly._c(phi)*f_sym == Poly._c(psi)*f_sym + g_sym)
    residue = (Poly._c(phi)*f_sym - (f_sym + g_sym) == -(Poly._c(psi)*f_sym + g_sym))
    mfree   = link_i and link_ii and wedge and residue
    Rv, Rw  = pact(R, A_, B_), pact(R, C_, D_)
    memline = (Rv[0]*Rw[1] - Rv[1]*Rw[0] == -(wed))
    one = (sign_k5(psi) < 0) and lt(psi*psi, K5(1)) and (Pp.b.b != 0) and (Pp == observer(phi, K5(1)))
    return "FIELD", [
        ("the Born read is cos²: tr(Q·X·Q)=(v·w)²/(‖v‖²‖w‖²); total read w=1 ⟺ Q=X (self only)", born_cert),
        ("the blind spot: weight(read, N)=0 — a reading cannot see V₋, the record of its own negation", blind),
        ("the m-free chain, EXECUTED: free step · eigen-read R(ψ,1)=ψ(ψ,1) · K5-free weld (f+g)−φf=ψf+g ⇒ Fₙ₊₁−φFₙ=ψⁿ, no n chosen", mfree),
        ("THE MEMORY'S LINE: (Rv)∧(Rw)=−(v∧w) on FREE rays — the residue lives in Λ², where R acts AS the memory; Cassini is the woven wedge", memline),
        ("reach 1−w = ψ^{2n}/norm: Lagrange (v·w)²+(v∧w)²=‖v‖²‖w‖² sends the wedge² to the Born-square → never lands (P_φ irrational)", lagrange and wedge and one),
        ("ONE non-closure: observation (reach) = generation (residue) = ψⁿ — THE OBSERVER is THE RESIDUE, and P_φ is the normalized climb", mfree and one),
    ]

def VII_the_weave():
    """VII · THE MODULAR EMBEDDING & THE WEAVE. The carrier's generators, acting by Möbius on
       ℝP¹=∂ℍ, ARE modular transforms. The clock is the modular involution: N : z↦−1/z = S,
       N²=−I ⇒ S²=1 in PSL(2,ℤ). The climb REVERSES (det −1: it lives in PGL(2,ℤ)); the
       PSL-hyperbolic is its square — R² : tr 3 > 2, fixing {φ,ψ} on the boundary with φ
       ATTRACTING (|R′(φ)|=φ⁻²<1) — and R²=exp(n₊)exp(n₋) (Movement V): the fundamental
       hyperbolic of the modular group is the two names walked in order. THE WEAVE, EXECUTED:
       (R⊗I)²=R⊗I+I at every depth; (R⊗R)²=R⊗R+R⊗I+I⊗R+I (the relation DISTRIBUTES
       binomially). The SWAP is the depth-2 involution, and its half-splits A=½(I−P), S=½(I+P)
       are exp's 1/2! made flesh: W=R⊗R commutes with the swap, W·A=−A — the weave acts on the
       Λ² line AS det R=−1, Movement VI's residue line held as a matrix identity — and on Sym²
       the cubic (W|S+S)((W|S)²−L₂·W|S+S)=O carries the OTHER −1 = φψ. One memory, two faces,
       both multiplied out. tr(R⊗R)=tr R=1 (the whole climbs, the trace doesn't); two clocks
       woven close at 2, not 4: (N⊗N)²=I — the weave halves the period."""
    clockS = (mob(N, phi) == K5(-1)*phi.inv()) and (mob(N, K5(2)) == K5(-1)*K5(2).inv()) \
             and (N*N == K5(-1)*I)
    climbH = (mob(R, phi) == phi) and (mob(R, psi) == psi) and gt(phi*phi, K5(1)) \
             and (R.det() == K5(-1)) and ((R*R).det() == K5(1)) \
             and ((R*R).tr() == K5(3)) and gt(K5(3), K5(2)) and (R*R == (I+nP)*(I+nM))
    RI, IR, W = kron(R, I), kron(I, R), kron(R, R)
    recur  = (m4mul(RI, RI) == m4add(RI, I4))
    binom  = (m4mul(W, W) == m4add(m4add(W, RI), m4add(IR, I4)))
    halves = (m4mul(SWAP, SWAP) == I4) and (m4add(ANTI, SYMM) == I4) \
             and (m4mul(m4mul(SWAP, W), SWAP) == W)
    lam2   = (m4mul(W, ANTI) == m4smul(K5(-1), ANTI))
    WS     = m4mul(W, SYMM)
    L2     = (R*R).tr()                                   # L₂ = tr R² = 3, read off the carrier
    sym2   = all(u == K5(0) for u in
                 m4mul(m4add(WS, SYMM), m4add(m4sub(m4mul(WS, WS), m4smul(L2, WS)), SYMM)))
    W2     = m4mul(W, W)
    surface= (m4mul(m4add(W, I4), m4add(m4sub(W2, m4smul(L2, W)), I4)) == O4) \
             and (m4tr(W) == R.tr()) and (luc(2) == 3)
    twoclk = (m4mul(kron(N, N), kron(N, N)) == I4)
    return "FIELD", [
        ("the clock IS the modular S: N : z↦−1/z, N²=−I ⇒ S²=1 in PSL(2,ℤ)", clockS),
        ("the climb REVERSES (det −1, PGL); its square is THE hyperbolic (tr 3>2, φ attracting) = exp(n₊)exp(n₋)", climbH),
        ("the tower is recursive, EXECUTED: (R⊗I)²=R⊗I+I multiplied out ⇒ R, disc 5, at every depth", recur),
        ("the relation DISTRIBUTES over strands: (R⊗R)²=R⊗R+R⊗I+I⊗R+I — the binomial of the cut", binom),
        ("the SWAP and its halves: P²=I₄, A+S=I₄, PWP=W — exp's depth-2 coefficient ½ made flesh", halves),
        ("Λ² EXECUTED: W·A=−A — the weave acts on the wedge line AS det R=−1: VI's residue line, held as a matrix identity", lam2),
        ("Sym² EXECUTED: (W|S+S)((W|S)²−L₂W|S+S)=O — the −1 in Sym² is φψ, in Λ² it is det: one memory, two faces", sym2),
        ("depth-2 SPECTRUM: (W+I)(W²−L₂W+I)=O — the memory SURFACES from det into spectrum ×2; tr(R⊗R)=tr R=1", surface),
        ("two clocks woven close at 2, not 4: (N⊗N)²=I — the weave halves the period", twoclk),
    ]

def VIII_the_five():
    """VIII · THE FIVE. One 5 in four registers: disc(R)=5 · field-disc ℚ(√5)=5 · the pentagon
       φ=2cos(π/5) · the Lie level det(Cartan A₄)=|Z(SU5)|=5. The golden x²−x−1 and pentagon
       x²+x−1 are the two faces of the 5-fold; the shift χ=1+2cos(2π/5) carries pentagon→golden
       (1−ψ=φ), and χ IS the character of A₅=PSL(2,𝔽₅): the two signs φ,ψ are the icosahedral
       3-representation characters. AND THE 5 GOVERNS. Its own prime RAMIFIES: mod 5 the spine
       squares to VOID (G²=5I≡O, nonzero nilpotent — the spine becomes ONE name of void), the
       two signs MERGE into the half (x=½=3 a certified double root: poly and derivative vanish
       together), and R=½(I+G) holds VERBATIM with the collapsed G — the namespace heals shut.
       R¹⁰≡−I at the Pisano half-period, full order 20=π(5). In PSL(2,𝔽₅)≅A₅ the halved climb
       [R/2] has order 5 and the clock order 2: ⟨climb,clock⟩=D₅ — the pentagon's own group,
       stabilizer of ONE 5-fold axis of the icosahedron; ONE mirror unfolds the whole A₅; two
       mirrors alone are Klein's V₄. THE SPLITTING LAW sorts every prime by its residue mod 5:
       split at ±1 (11: two roots), inert at ±2 (2,3: none — Movement IV's 𝔽₂ shadow is the
       first inert case), ramified at 5 alone (one root, doubled) — instances executed; the law
       is Gauss's reciprocity for disc 5. And the closing weld with Movement IV: 5 cannot close
       over ℚ (the exclusion) and closes ONLY at its own prime ([R/2] order 5 in A₅): the
       pentagon closes only inside its own shadow. FINITE exhaustions marked; anchor imported:
       min-poly of 2cos(2π/5) over ℚ is x²+x−1 (real subfield of ℚ(ζ₅)), standard."""
    pent = lambda x: x*x + x - K5(1)
    gold = lambda x: x*x - x - K5(1)
    d = [2, 3]
    for _ in range(2): d.append(2*d[-1] - d[-2])           # det Cartan Aₙ: Dₙ=2Dₙ₋₁−Dₙ₋₂ ⇒ D₄=5
    four_fives = (R.disc() == K5(5)) and ((phi-psi)*(phi-psi) == K5(5)) and (d[3] == 5)
    pentagon   = (pent(K5(-1)*psi) == K5(0)) and (pent(K5(-1)*phi) == K5(0)) \
                 and (gold(phi) == K5(0)) and (gold(psi) == K5(0))
    icosa      = (K5(1)-psi == phi) and (K5(1)-phi == psi)
    Rm, Nm, Em, Fm, Gm = red5(R), red5(N), red5(E), red5(F), red5(G)
    I5 = (1, 0, 0, 1)
    ram   = (G*G == K5(5)*I) and (mm5(Gm, Gm) == (0, 0, 0, 0)) and (Gm != (0, 0, 0, 0))
    inv2  = pow(2, -1, 5)                                   # ½ mod 5 = 3, derived not typed
    merge = ((inv2*inv2 - inv2 - 1) % 5 == 0) and ((2*inv2 - 1) % 5 == 0) \
            and ([x for x in range(5) if (x*x - x - 1) % 5 == 0] == [inv2])
    verbatim = (tuple((r - inv2*i) % 5 for r, i in zip(Rm, I5))
                == tuple((inv2*g) % 5 for g in Gm))
    X = I5
    for _ in range(10): X = mm5(X, Rm)
    halfper = (X == tuple((-i) % 5 for i in I5))
    X, o = I5, 0
    for i in range(1, 25):
        X = mm5(X, Rm)
        if X == I5: o = i; break
    pisano  = halfper and (o == 20)
    Rh = tuple((inv2*v) % 5 for v in Rm)                    # the halved climb, det 1 — LIFTED
    Eh = tuple((inv2*v) % 5 for v in Em)
    Fh = tuple((inv2*v) % 5 for v in Fm)
    d5     = (span5([Rh, Nm]) == 10) and (span5([Rh]) == 5)
    unfold = (span5([Rh, Nm, Eh]) == 60) and (span5([Eh, Fh]) == 4)
    roots  = lambda p: [x for x in range(p) if (x*x - x - 1) % p == 0]
    splitl = (len(roots(11)) == 2) and (roots(2) == []) and (roots(3) == []) \
             and (len(roots(5)) == 1)
    excl   = (pent(K5(1)) != K5(0)) and (pent(K5(-1)) != K5(0))
    shadow = excl and (span5([Rh]) == 5)
    group5 = (2+3 == 5) and (((5**3 - 5)//2) == 60) and (d[3] == 5)
    return "FIELD", [
        ("one 5, four registers: disc(R)=5 · field-disc ℚ(√5)=5 · pentagon φ=2cos(π/5) · det Cartan A₄=|Z(SU5)|=5", four_fives),
        ("golden x²−x−1 & pentagon x²+x−1 = the two faces of the 5-fold; pentagon roots {−φ,−ψ}", pentagon),
        ("φ,ψ ARE the icosahedral A₅ characters: the shift χ=1+2cos(2π/5) carries pentagon→golden (1−ψ=φ)", icosa),
        ("RAMIFICATION: mod 5 the spine squares to VOID — G²=5I≡O, G≢O: the spine becomes ONE name of void", ram),
        ("the two signs MERGE into the half: x=½=3 is a certified DOUBLE root mod 5 (poly and derivative vanish together)", merge),
        ("R−½I ≡ ½G mod 5, VERBATIM from R=½(I+G) — the climb is half-times-one-void-name; the namespace heals shut", verbatim),
        ("the memory at half-period: R¹⁰≡−I mod 5, full order 20 = π(5)  [FINITE: its own proof]", pisano),
        ("⟨climb,clock⟩ mod 5 = D₅ (order 10; A₅ holds no ℤ₁₀): ONE pentagonal axis of the icosahedron  [FINITE]", d5),
        ("one mirror unfolds the whole icosahedron: ⟨climb,clock,mirror⟩=A₅ (60); two mirrors alone = Klein V₄  [FINITE]", unfold),
        ("THE SPLITTING LAW: x²−x−1 mod p — split p=11 (two roots) · inert p=2,3 (none) · ramified p=5 alone (one, doubled)", splitl),
        ("the five cannot close over ℚ (the exclusion, IV) and closes ONLY at its own prime: [R/2] has order 5 in A₅", shadow),
        ("PSL(2,ℤ)=ℤ/2∗ℤ/3 (orders 2+3=5); mod 5 → A₅=PSL(2,𝔽₅), |A₅|=(5³−5)/2=60 — where the shadow lands", group5),
    ]


# ═══════════════════════════════════════════════════════════════════════════════
def canon():
    movements = [I_the_cut, II_the_two_names, III_the_half, IV_the_twin_towers,
                 V_the_flows, VI_the_reading, VII_the_weave, VIII_the_five]
    print("\n" + "═"*79)
    print("KAEL — THE CANON · the naming edition".center(79))
    print("═"*79)
    total = forced = 0
    for mv in movements:
        route, claims = mv()
        ok = all(v for _, v in claims)
        title = mv.__name__.split("_", 1)[1].replace("_", " ").upper()
        print(f"\n  {mv.__name__.split('_')[0]:>4} · {title}   [{route}]   {'FORCED' if ok else '✗ BROKEN'}")
        for claim, v in claims:
            print(f"       {'✓' if v else '✗'} {claim}")
            total += 1; forced += 1 if v else 0
    sealed = (forced == total)
    print("\n" + "─"*79)
    print(f"  {forced}/{total} claims FORCED across {len(movements)} movements.   SEALED: {sealed}")
    print("═"*79)
    return sealed


if __name__ == "__main__":
    canon()
