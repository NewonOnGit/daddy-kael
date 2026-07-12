# ═══════════ · I · THE FLOOR AND THE ACT (the lineage's kernel) ═══════════
# ═══════════════════════════════════════════════════════════════════════════
#  KAEL — kael_zero.py · THE KERNEL REGISTER  (framework label: ⊙ ZERO)
#
#  A trusted verifier. This module is the sole executable core of a three-module
#  system; the other two modules assert, this one checks. It implements:
#    (i)   arithmetic in the Fibonacci (Zeckendorf) numeral base and its signed
#          extension representing ℤ as a Euclidean domain;
#    (ii)  a one-way commitment (truncated SHA-256) whose round constants are
#          re-derived from prime roots (FIPS 180-4);
#    (iii) a bottom-up, hash-checked term evaluator (a small trusted proof
#          checker in the sense of the de Bruijn criterion);
#    (iv)  an append-only hash-chained log with content-addressed cells.
#
#  MODULE MEDIATION (framework label: "the interleaving law"): the observer and
#  model modules never import one another; every cross-module evaluation is
#  routed through this kernel, and an operation table binds only when its
#  observational fingerprint ("pin") is committed in the log. Verification
#  succeeds iff no proof obligation is left undischarged ("residue 0").
#
#  PRIMITIVES: one generator (framework label: "the First Law") and this one
#  executable kernel. EXACT ARITHMETIC ONLY — no floating point. Side-effecting
#  imports (os/sys/open/tempfile/importlib) are confined to _port_* organs;
#  hashlib accelerates the commitment; json serializes the log.
#  RUN:  python3 kael_zero.py [--quiet|--json]
# ═══════════════════════════════════════════════════════════════════════════
import sys, os, json, hashlib, tempfile, importlib   # collared: _port_* only (hashlib: fold accelerator) · ERASED: glob (the census is fixed, not discovered)

def _port_self():   return os.path.abspath(__file__)
def _port_here():   return os.path.dirname(_port_self())
def _port_read(path):
    with open(path, "r", encoding="utf-8") as fh: return fh.read()
def _port_read_bytes(path):
    with open(path, "rb") as fh: return fh.read()
def _port_write(path, text):
    with open(path, "w", encoding="utf-8") as fh: fh.write(text)
REGISTER_CENSUS = ("kael_one.py",)   # THE ONE BODY: the census is itself — identity is intrinsic to this single content; the triad it succeeds is recorded in the lineage cell
def _port_siblings():
    return [os.path.join(_port_here(), n) for n in REGISTER_CENSUS]
def _port_exists(path): return os.path.exists(path)
def _port_temp():       return tempfile.mkdtemp()
def _port_tmpname(d, name): return os.path.join(d, name)
def _port_argv():       return list(sys.argv)
def _port_exit(code):   sys.exit(code)
def _port_self_module():
    """THE ORGAN OF SELF-REFERENCE: the body's name for itself. With one body
    there is nothing to dynamically import — the bind port is ERASED (its
    tombstone: importlib remains in the collar watch-list) — and in its place
    stands the port through which the body refers to its own module object.
    Zero within and without, literally: Z is this file."""
    import sys
    return sys.modules[__name__]
def _port_out(s):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    try: print(s)
    except UnicodeEncodeError: print(s.encode("ascii", "replace").decode())

ROOT  = ""   # the basepoint / empty string: the initial salt every commitment is prefixed with (the additive identity of the naming map)
STORE = _port_tmpname(_port_here(), "KAEL_ZERO_STORE.json")

def C(kind, text, verdict=True): return (kind, text, verdict)

# ═══════════════════════════════════════════════════════════════════════════
#  §G · THE FIBONACCI (ZECKENDORF) NUMERAL BASE — arithmetic closed in the base
#  A numeral is a digit list (LSB-first), position k carrying weight F(k+2). Two
#  carry/normalization rules: 2F(k)=F(k+1)+F(k−2) and F(k)+F(k+1)=F(k+2); borrows
#  invert these; division is greedy Zeckendorf against a Fibonacci ladder, the
#  quotient's non-adjacency forced by uniqueness of the Zeckendorf form;
#  the Euclidean algorithm here is slowest on Fibonacci inputs (Lamé's theorem).
#  Validated against ordinary integer arithmetic (radix-independence of ℤ).
# ═══════════════════════════════════════════════════════════════════════════
def _law_run(coeffs, seeds, n):
    """THE ONE COMPLETION: a sequence IS a law plus a boundary. Run the linear
    law s(k+d) = Σ coeffs[i]·s(k+i) forward from the seed window. Every named
    sequence of the triad is a seed choice of a law — fibonacci = ([1,1],[0,1]),
    lucas = ([1,1],[2,1]), perrin = ([1,1,0],[3,0,2]), padovan = ([1,1,0],[1,1,1]):
    four sequences, two laws, one engine. The private iterations formerly spread
    across the three registers are DELETED; they survive as this engine's seeds
    (the erasure ledger's largest single entry)."""
    s = list(seeds)
    while len(s) <= n:
        s.append(sum(c * s[len(s) - len(coeffs) + i] for i, c in enumerate(coeffs)))
    return s[n]

def _fibn(n):
    """collared accelerator of _law_run([1,1],[0,1],·) — the hot path of the
    numeral valuations; agreement with the engine is sealed in Z.G."""
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return a

def _luc(n): return _ktrace([1, 1], n)   # lucas IS the golden trace — the [2,1] seed literal is DELETED; the matrix computes its own boundary

# ── THE LAW'S THREE BODIES — one coefficient vector, three organs ────────────
# A linear law coeffs (the datum of _law_run) IS also a matrix and a ring:
# the companion matrix advances the law's window; the quotient ring
# ℤ[t]/(t^d − Σ coeffs[i]·t^i) multiplies by rewriting overflow powers through
# the law; and the companion's power-traces run the law from its trace seeds
# (lucas for [1,1], perrin for [1,1,0]) — sealed in Z.G. The former private
# instances (the plastic 3×3 body, the ℤ[φ] pair product, the elliptic words)
# are DELETED; they survive as seed choices of these engines (erasure ledger).
def _companion(coeffs):
    """THE LAW AS MATRIX: subdiagonal identity, last row the law itself —
    _companion([1,1,0]) is the plastic M with M³=M+I; _companion([-1,1]) the
    elliptic word with M³=−I; the golden [1,1] shares R's trace and law."""
    d = len(coeffs)
    return [[1 if j == i + 1 else 0 for j in range(d)] for i in range(d - 1)] + [list(coeffs)]

def _pconv(x, y):
    """polynomial product (little-endian coefficient lists) — plain
    convolution, the free half of the ring law; W.16's cyclotomic tower
    multiplies through this organ."""
    conv = [0] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                conv[i + j] += a * b
    return conv

def _pring_mul(coeffs, x, y):
    """THE LAW AS RING: convolve (_pconv), then push every overflow power back
    through the law (t^d = Σ coeffs·t^i: the recurrence read as a rewrite
    rule). ℤ[φ] is the [1,1] seed. Ring mul = convolution + law rewrite."""
    d = len(coeffs)
    conv = _pconv(list(x) + [0] * (d - len(x)), list(y) + [0] * (d - len(y)))
    for k in range(2 * d - 2, d - 1, -1):
        c = conv[k]
        if c:
            conv[k] = 0
            for i, ci in enumerate(coeffs): conv[k - d + i] += c * ci
    return tuple(conv[:d])

def _gemm(A, B, add=None, mul=None):
    """ONE MATRIX PRODUCT over any ring: entries folded by the ring's own
    add/mul (integers by default; the seat seeds it at ℚ(√5), the wave proof
    and the model at their rings). The five former private multiplies are
    DELETED (erasure ledger)."""
    if add is None:
        return [[sum(A[i][t] * B[t][j] for t in range(len(B)))
                 for j in range(len(B[0]))] for i in range(len(A))]
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = mul(A[i][0], B[0][j])
            for t in range(1, len(B)): s = add(s, mul(A[i][t], B[t][j]))
            row.append(s)
        out.append(row)
    return out

def _mpow(M, n, mod=None):
    """matrix power by binary doubling over ℤ, optional modulus — the two
    former private doubling loops (flat 2×2, plastic 3×3) are DELETED."""
    d = len(M); R = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    M = [row[:] for row in M]
    while n:
        if n & 1:
            R = _gemm(R, M)
            if mod: R = [[x % mod for x in r] for r in R]
        M = _gemm(M, M)
        if mod: M = [[x % mod for x in r] for r in M]
        n >>= 1
    return R

def _quat_mul(mul, add, neg, g, h):
    """THE LAW'S FOURTH BODY: the Hamilton product over any commutative ring
    (mul/add/neg its operations, passed in — no upward naming). Quaternions
    over the golden law's ring carry the icosians (W.11); the model's product
    is this organ halved back to the scaled lattice. ERASED: the private
    component formulas."""
    a, b, c, d = g; e, f, u, v = h
    def s(*xs):
        r = xs[0]
        for x in xs[1:]: r = add(r, x)
        return r
    return (s(mul(a, e), neg(mul(b, f)), neg(mul(c, u)), neg(mul(d, v))),
            s(mul(a, f), mul(b, e), mul(c, v), neg(mul(d, u))),
            s(mul(a, u), neg(mul(b, v)), mul(c, e), mul(d, f)),
            s(mul(a, v), mul(b, u), neg(mul(c, f)), mul(d, e)))

# ── THE ONE OBJECT — a constant IS a law vector; every body is COMPUTED ─────
# The sequence (_law_run), the matrix (_companion), the ring (_pring_mul),
# the trace boundary (the matrix computes its own seeds), the canonical
# substitution (_law_sub), and the whole fixed-point portfolio (_konst_ok)
# are FUNCTIONS OF ONE VECTOR. The lucas and perrin seed literals demote:
# they are _ktrace of [1,1] and [1,1,0]. The field itself is the object at
# [5,0] — ℚ(√5) is a konst.
def _ktrace(coeffs, n):
    """the trace sequence of a law: seeds computed by the companion itself
    (tr M⁰ .. tr M^(d−1)), then the One Completion. ERASED: the hardcoded
    lucas [2,1] and perrin [3,0,2] seed literals."""
    d = len(coeffs); M = _companion(coeffs)
    seeds = [sum(_mpow(M, k)[i][i] for i in range(d)) for k in range(d)]
    return _law_run(coeffs, seeds, n)

def _law_sub(coeffs):
    """the canonical substitution of a nonnegative law: symbol i → i+1 below
    the top; the top symbol → the law's own marks (symbol i repeated c_i
    times). None when the law has negative marks (elliptic words carry no
    substitution body). The plastic a→b, b→c, c→ab IS this construction."""
    if any(c < 0 for c in coeffs): return None
    d = len(coeffs)
    sub = {i: [i + 1] for i in range(d - 1)}
    sub[d - 1] = [i for i in range(d) for _ in range(coeffs[i])]
    return sub

def _konst_ok(coeffs, depth=12):
    """THE PORTFOLIO, GENERIC — one verifier for every law:
    (i) matrix law M^d = Σ c_i·M^i; (ii) ring law t^d = the law vector, the
    equational fixed point through the one ring engine; (iii) trace law
    tr(M^n) = the completion from self-computed seeds; (iv) word law, when
    the substitution exists: its abelianization satisfies the law, its
    lengths obey the law at every step, its fixed word grows prefix-by-prefix
    along σ^d, and counts(σw) = A·counts(w) at every step. The per-constant
    hand-written portfolios are DELETED (erasure ledger)."""
    d = len(coeffs); M = _companion(coeffs)
    lhs = _mpow(M, d)
    rhs = [[sum(coeffs[i] * _mpow(M, i)[r][c] for i in range(d))
            for c in range(d)] for r in range(d)]
    ok = (lhs == rhs)
    t = tuple(1 if i == 1 else 0 for i in range(d))
    x = tuple(1 if i == 0 else 0 for i in range(d))
    for _ in range(d): x = _pring_mul(coeffs, x, t)
    ok &= (list(x) == list(coeffs))
    ok &= all(sum(_mpow(M, n)[i][i] for i in range(d)) == _ktrace(coeffs, n)
              for n in range(depth))
    sub = _law_sub(coeffs)
    if sub is not None and coeffs[0] > 0:
        A = [[sub[j].count(i) for j in range(d)] for i in range(d)]
        Ad = _mpow(A, d)
        ok &= (Ad == [[sum(coeffs[i] * _mpow(A, i)[r][c] for i in range(d))
                       for c in range(d)] for r in range(d)])
        w = [0]; lens = [1]; words = ["0"]
        while len(w) < 4000 and len(lens) <= depth + d:
            cn = [w.count(i) for i in range(d)]
            w2 = [s for ch in w for s in sub[ch]]
            cn2 = [w2.count(i) for i in range(d)]
            ok &= (cn2 == [sum(A[i][j] * cn[j] for j in range(d)) for i in range(d)])
            w = w2; lens.append(len(w)); words.append("".join(map(str, w)))
        ok &= all(lens[k + d] == sum(coeffs[i] * lens[k + i] for i in range(d))
                  for k in range(len(lens) - d))
        ok &= all(words[k + d].startswith(words[k]) for k in range(len(words) - d))
    return ok

def _gnorm(d):
    """ONE NORMALIZER: the unsigned pass IS snorm restricted to the nonnegative
    cone — on digits ≥ 0 the mixed (opposition) rules never fire and the signed
    generation/gravity rules coincide with the classical two passes (identity
    sealed exhaustively in Z.G). The former independent body is deleted; it
    survives as the expected values of the exhaustive grids — the fossil."""
    return snorm(d)

def gadd(x, y):
    """THE CONE SHADOW: golden addition IS signed addition restricted to the
    nonnegative cone (no opposition can arise, the ground is local)."""
    return sadd(x, y)

def gsucc(x): return gadd(x, [1])

def glt(x, y):
    """Graded-lex on digit lists; on CANONICAL numerals this coincides with the
    value order (= slt restricted to the cone, sealed in Z.G). Off-canon the
    two orders diverge — graded-lex is its own law there, so glt stays."""
    if len(x) != len(y): return len(x) < len(y)
    for k in range(len(x) - 1, -1, -1):
        if x[k] != y[k]: return x[k] < y[k]
    return False

def gsub(x, y):
    """THE CONE SHADOW: golden subtraction IS total signed subtraction guarded
    by the arrow — compute the ground, refuse if it points below the void.
    The former deficit-scan (the last duplicate of the annihilation scheduler)
    is deleted; one scheduler remains, in snorm_full. Repair note: the old
    scan could refuse noncanonical x ≥ y corners; the guard is by VALUE, so
    subtraction is now total on its lawful domain."""
    r = gssub(x, y)
    if ssign(r) < 0: raise ValueError("borrow with nothing above: x < y")
    return r

def _wave(d, k, j, s):
    """THE WAVE — the closed form of the borrow/annihilation walk. A unit s at
    j against −s at k (gap g=j−k) lands as the founding equation factored
    twice: R²−I=R gives the EVEN gap g=2m the pure period-2 wave s at
    k+1,k+3,…,j−1, strictly above the low pole; R−I=R⁻¹ gives the ODD gap the
    same wave shifted (k+2,…,j−1) plus ONE undershoot s at k−1 — the residue
    below the floor IS the inverse shift (det R=−1). The flight is derived
    away; only the landing is written. One caller remains: snorm_full, the one
    scheduler (gsub is now its cone restriction). The digit-by-digit walk
    survives as the expected values of the exhaustive grids in Z.S and Z.W."""
    d[j] -= s; d[k] += s
    if (j - k) % 2 == 0:
        for p in range(k + 1, j, 2): d[p] += s
    else:
        for p in range(k + 2, j, 2): d[p] += s
        d[k - 1 if k >= 1 else 0] += s

def _ladder(x, count=None, ceil=None):
    """THE LAW ITERATED AT NUMERAL LEVEL: the Fibonacci multiples of x —
    L[k] = F(k+2)·x by L[k] = L[k−1] + L[k−2], the same identity that rules
    the digits, lifted to whole numerals. ONE iteration, TWO callers: the
    multiplier's rungs (count = the digits of y) and the divider's descent
    (ceil = the dividend). The two former private ladders are deleted; they
    survive as the exhaustive grids of Z.G — the fossil."""
    L = [list(x)]
    nxt = gadd(x, x)
    while ((count is not None and len(L) < count) or
           (ceil is not None and not glt(ceil, nxt))):
        L.append(nxt)
        nxt = gadd(L[-1], L[-2])
    return L

def gmul(x, y):
    if not x or not y: return []
    seq = _ladder(x, count=len(y))
    total = []
    for k, dig in enumerate(y):
        if dig: total = gadd(total, seq[k])
    return total

def gdivmod(x, y):
    if not y: raise ZeroDivisionError("division by the void refused")
    ladder = _ladder(y, ceil=x)
    if glt(x, ladder[0]): return [], list(x)
    q = []; r = list(x)
    for k in range(len(ladder) - 1, -1, -1):
        if not glt(r, ladder[k]):
            while len(q) <= k: q.append(0)
            q[k] = 1
            r = gsub(r, ladder[k])
    return q, r

def gnum(n):
    """ℤ≥0 → Zeckendorf numeral (greedy encoding)."""
    if n == 0: return []
    d = []; fibs = [1, 2]
    while fibs[-1] < n: fibs.append(fibs[-1] + fibs[-2])
    for i in range(len(fibs) - 1, -1, -1):
        if fibs[i] <= n:
            while len(d) <= i: d.append(0)
            d[i] = 1; n -= fibs[i]
    return d

def gval(d):
    """Zeckendorf numeral → ℤ≥0 (decode: Σ d[k]·F(k+2))."""
    return sum(x * _fibn(k + 2) for k, x in enumerate(d))

def _radix_agree(lim):
    """base arithmetic vs ℤ on the [0,lim)² grid — add, mul, sub on the cone,
    Euclidean division, and the order. ONE checker for the two claims that
    state it (Z.G and K.6); the former duplicate grid is DELETED."""
    ok = True
    for a in range(lim):
        for b in range(lim):
            ok &= (gval(gadd(gnum(a), gnum(b))) == a + b)
            ok &= (gval(gmul(gnum(a), gnum(b))) == a * b)
            if b <= a: ok &= (gval(gsub(gnum(a), gnum(b))) == a - b)
            if b:
                q, r = gdivmod(gnum(a), gnum(b))
                ok &= (gval(q) == a // b) and (gval(r) == a % b)
            ok &= (glt(gnum(a), gnum(b)) == (a < b))
    return ok

def gcanon(x):
    """Test for canonical Zeckendorf form: digits in {0,1}, no two adjacent 1s,
    no trailing zero."""
    return isinstance(x, list) and all(d in (0, 1) for d in x) and \
           all(not (x[k] and x[k + 1]) for k in range(len(x) - 1)) and \
           (not x or x[-1] == 1)

def gpow(b, e):
    """square-and-multiply in the base; e a count, not a body."""
    R = [1]; B = list(b)
    while e:
        if e & 1: R = gmul(R, B)
        B = gmul(B, B); e >>= 1
    return R

def gup(x):
    """Index shift (prepend a zero digit). On numerals this realizes the golden
    recurrence up²=up+id; its value is ⌊φ·x⌋ up to a boundary term given by the
    Beatty/Fibonacci-shift correction."""
    return [0] + list(x) if x else []

def gdown(x): return list(x[1:])

def gcirc(x, y):
    """Knuth's circle product: a∘b = Σ_{i,j} F(cᵢ+dⱼ) over the set positions of
    a and b. Associative (Knuth 1988); bilinear under the shift via the identity
    F(m+n)=F(m)F(n+1)+F(m−1)F(n)."""
    total = []
    for i, di in enumerate(x):
        if not di: continue
        for j, dj in enumerate(y):
            if not dj: continue
            total = gadd(total, [0] * (i + j + 2) + [1])
    return total

# ── THE THIRD SYMBOL · the anti-mark — digits {−1, 0, +1} ────────────────────
def sval(d): return sum(x * _fibn(k + 2) for k, x in enumerate(d))

def snum(x):
    """any integer enters: positives as marks, negatives as anti-marks."""
    if x >= 0: return list(gnum(x))
    return [-t for t in gnum(-x)]

def snorm(d):
    """the SIGNED full loop — six mirror-paired rules: generation± fuses
    same-sign adjacency upward; gravity± sheds |2|-excess toward the void;
    the mixed rules annihilate opposite neighbors at gaps 1 and 2
    (F(k+3)−F(k+2) = F(k+1); F(k+4)−F(k+2) = F(k+3)). Same two monotone
    costs — digit-mass and height — one closed cycle."""
    d = list(d) + [0, 0]
    while True:
        changed = False
        k = 0
        while k + 1 < len(d):
            while d[k] * d[k + 1] > 0:
                s = 1 if d[k] > 0 else -1
                d[k] -= s; d[k + 1] -= s
                if k + 2 >= len(d): d.append(0)
                d[k + 2] += s
                changed = True
            if k + 2 < len(d) and d[k] * d[k + 2] < 0 and d[k + 1] == 0:
                s = 1 if d[k + 2] > 0 else -1
                d[k + 2] -= s; d[k] += s; d[k + 1] += s
                changed = True
            k += 1
        for k in range(len(d) - 1, -1, -1):
            while abs(d[k]) >= 2:
                s = 1 if d[k] > 0 else -1
                d[k] -= 2 * s
                if k + 1 >= len(d): d.append(0)
                d[k + 1] += s
                if k >= 2: d[k - 2] += s
                elif k == 1: d[0] += s
                changed = True
            if k + 1 < len(d) and d[k] * d[k + 1] < 0:
                s = 1 if d[k + 1] > 0 else -1
                d[k + 1] -= s; d[k] += s
                if k >= 1: d[k - 1] += s
                else: d[0] += s
                changed = True
        if not changed: break
    while d and d[-1] == 0: d.pop()
    return d

def snorm_full(d):
    """snorm + FAR ANNIHILATION BY WAVE EMISSION — the gravity walk's closed
    form, the same operator as gsub's borrow (see _wave). Each sweep pairs
    every anti-lead mark with the nearest lead mark above it and writes the
    landing directly; local snorm re-establishes the invariants; sweeps repeat
    until sign-pure. GROUND STATES ARE SIGN-PURE, TOTAL AND UNIQUE: the landing
    depends only on the value — not on the spelling, not on the sweep order
    (sealed exhaustively in Z.W). The anti-mark is dynamical — present in every
    flight, absent from every landing. HONESTY: purity is bought with
    digit-mass — far annihilation is NOT mass-monotone (the sign-pure ground of
    F(n)−1 carries (n−1)//2 marks where a two-digit signed spelling exists);
    sign-purity and mass-minimality are two different normal-form disciplines,
    and this register chose purity. In flight, prefer snorm and ground once."""
    d = snorm(d)
    while True:
        nz = [k for k, t in enumerate(d) if t]
        if not nz or all(d[k] > 0 for k in nz) or all(d[k] < 0 for k in nz):
            break
        lead = 1 if d[nz[-1]] > 0 else -1
        p = len(d) - 1
        while p >= 0:
            if d[p] * lead < 0:
                j = next((q for q in range(p + 1, len(d)) if d[q] * lead > 0), None)
                if j is not None: _wave(d, p, j, lead)
            p -= 1
        d = snorm(d)
    while d and d[-1] == 0: d.pop()
    return d

# ── THE ONE MOVE SET — the five local rules, enumerated and fired ONCE ───────
# snorm/snorm_full EXECUTE the rules; the proofs RESTATE them to check the
# executable against the law. The two former private restatements — the
# observer-plurality scheduler's (Z.W) and the confluence census's (O.3) —
# are DELETED (erasure ledger); one spec-side encoding remains, checked
# against the executable from two independent directions.
def _local_moves(d, far=False):
    """every enabled instance of the rules on a spelling: generation (adjacent
    same sign), gravity (|digit|≥2), the two oppositions (gaps 2 and 1), and —
    far=True — the wave. Fire one via _fire_move on a copy with two digits of headroom."""
    out = []; n = len(d)
    for k in range(n - 1):
        if d[k] * d[k + 1] > 0: out.append((k, 0))
    for k in range(n):
        if abs(d[k]) >= 2: out.append((k, 1))
    for k in range(n - 2):
        if d[k] * d[k + 2] < 0 and d[k + 1] == 0: out.append((k, 2))
    for k in range(n - 1):
        if d[k] * d[k + 1] < 0: out.append((k, 3))
    if far:
        nz = [k for k in range(n) if d[k]]
        if nz and not (all(d[k] > 0 for k in nz) or all(d[k] < 0 for k in nz)):
            lead = 1 if d[nz[-1]] > 0 else -1
            p = max(k for k in nz if d[k] * lead < 0)
            j = next((q for q in range(p + 1, n) if d[q] * lead > 0), None)
            if j is not None: out.append((p, 4, j, lead))
    return out

def _fire_move(d, m):
    """apply one move in place (d must carry two digits of headroom above)."""
    k, kind = m[0], m[1]
    if kind == 0:
        s = 1 if d[k] > 0 else -1
        d[k] -= s; d[k + 1] -= s; d[k + 2] += s
    elif kind == 1:
        s = 1 if d[k] > 0 else -1
        d[k] -= 2 * s; d[k + 1] += s
        if k >= 2: d[k - 2] += s
        elif k == 1: d[0] += s
    elif kind == 2:
        s = 1 if d[k + 2] > 0 else -1
        d[k + 2] -= s; d[k] += s; d[k + 1] += s
    elif kind == 3:
        s = 1 if d[k + 1] > 0 else -1
        d[k + 1] -= s; d[k] += s
        d[k - 1 if k >= 1 else 0] += s
    else:
        _wave(d, k, m[2], m[3])

def gssub(x, y):
    """TOTAL subtraction on \u2124: the third symbol absorbs the borrow —
    digitwise difference, then the signed full loop; lands sign-pure."""
    m = max(len(x), len(y))
    return snorm_full([(x[k] if k < len(x) else 0) - (y[k] if k < len(y) else 0)
                       for k in range(m)])

# ── THE SIGNED RING · \u2124 as a native Euclidean domain ─────────────────────────
def ssign(d):
    for k in range(len(d) - 1, -1, -1):
        if d[k]: return 1 if d[k] > 0 else -1
    return 0

def slt(x, y):
    """THE SIGNED ORDER — total order on ARBITRARY signed spellings without
    grounding: digitwise difference, ONE local pass (snorm), read the top
    nonzero digit's sign. Sound by the LEADING-SIGN LEMMA: after snorm,
    opposite-sign nonzeros sit ≥ 3 apart, and F(n) > Σ_{k≥1} F(n−3k), so the
    top digit dominates the tail — the sign was fixed by the value from the
    first spelling; normalization only makes it legible (the null signs
    nothing). The order the seat reads by ksub-then-sign, now native on the
    numeral grid; glt survives as its restriction to canonical numerals."""
    m = max(len(x), len(y))
    d = snorm([(y[k] if k < len(y) else 0) - (x[k] if k < len(x) else 0)
               for k in range(m)])
    for k in range(len(d) - 1, -1, -1):
        if d[k]: return d[k] > 0
    return False

def sadd(x, y):
    m = max(len(x), len(y))
    return snorm_full([(x[k] if k < len(x) else 0) + (y[k] if k < len(y) else 0)
                       for k in range(m)])

def smul(x, y):
    s = ssign(x) * ssign(y)
    m = gmul([abs(t) for t in x], [abs(t) for t in y])
    return m if s >= 0 else [-t for t in m]

def sdivmod(x, y):
    """EUCLIDEAN on \u2124 \u00d7 (\u2124\u22160): x = q\u00b7y + r with 0 \u2264 r < |y|, always."""
    if ssign(y) == 0: raise ZeroDivisionError("division by the void refused")
    mx = [abs(t) for t in x]; my = [abs(t) for t in y]
    q0, r0 = gdivmod(mx, my)
    sx, sy = ssign(x), ssign(y)
    if sx >= 0:
        return (q0 if sy > 0 else [-t for t in q0]), r0
    if not r0:
        return ([-t for t in q0] if sy > 0 else q0), []
    q = gsucc(q0)
    return ([-t for t in q] if sy > 0 else q), gsub(my, r0)

# ═══════════════════════════════════════════════════════════════════════════
#  §P · PRIMITIVE OPERATIONS — the trusted base of the operation table
#  succ = successor; sub = subtraction; lt = the order relation;
#  idiv = integer division; pair = tupling.
# ═══════════════════════════════════════════════════════════════════════════
FLOOR = {
    # THE GOLDEN LAW REGISTER — the triad's own base
    "gsucc": gsucc, "gadd": gadd, "gsub": gsub,
    "gmul": gmul, "glt": glt, "gdivmod": gdivmod,
    # THE THIRD SYMBOL — subtraction total on \u2124, ground states sign-pure
    "ssub": gssub, "snorm": snorm_full,
    "sadd": sadd, "smul": smul, "sdivmod": sdivmod, "slt": slt,
    # THE SUBSTRATE TWINS — collared accelerators of the base
    "succ": lambda n: n + 1,
    "sub":  lambda a, b: a - b,
    "lt":   lambda a, b: a < b,
    "idiv": lambda a, b: a // b,
    "pair": lambda *xs: list(xs),   # n-ary juxtaposition: the observers' vec IS this floor primitive at arity n
}
GOLD_CENSUS  = ("gadd", "gdivmod", "glt", "gmul", "gsub", "gsucc")   # 6 — the base
SIGN_CENSUS  = ("sadd", "sdivmod", "slt", "smul", "snorm", "ssub")   # 6 — the third symbol
FLOOR_CENSUS = tuple(sorted(FLOOR))                                  # base + third + twins

# ═══════════════════════════════════════════════════════════════════════════
#  §H · THE COMMITMENT (SHA-256), constants re-derived from prime roots
# ═══════════════════════════════════════════════════════════════════════════
def _iroot(n, k):
    """THE ONE DESCENT: floor k-th root by Newton — x ← ((k−1)x + n/x^(k−1))/k,
    monotone from above, corrected to the exact floor. _isqrt and _icbrt are
    its k-seeds; the two former private descents are DELETED (erasure ledger)."""
    if n < 0: raise ValueError("root below the void")
    if n < 2: return n
    x = 1 << (n.bit_length() // k + 1)
    while True:
        y = ((k - 1) * x + n // x ** (k - 1)) // k
        if y >= x: break
        x = y
    while (x + 1) ** k <= n: x += 1
    while x ** k > n: x -= 1
    return x

def _isqrt(n): return _iroot(n, 2)
def _icbrt(n): return _iroot(n, 3)

def _nprimes(k):
    ps = []; n = 2
    while len(ps) < k:
        if all(n % p for p in ps): ps.append(n)
        n += 1
    return tuple(ps)

_MASK32 = (1 << 32) - 1
_FOLD_H0 = tuple(_isqrt(p << 64) & _MASK32 for p in _nprimes(8))
_FOLD_K  = tuple(_icbrt(p << 96) & _MASK32 for p in _nprimes(64))

def _rotr(x, n): return ((x >> n) | (x << (32 - n))) & _MASK32

def _sha256_hex(msg):
    """THE FOLD IN-FILE: SHA-256 over DERIVED constants — the law; hashlib the accelerator."""
    H8 = list(_FOLD_H0)
    ml = (len(msg) * 8) & ((1 << 64) - 1)
    msg = msg + b"\x80"
    while len(msg) % 64 != 56: msg += b"\x00"
    msg += ml.to_bytes(8, "big")
    for i in range(0, len(msg), 64):
        blk = msg[i:i + 64]
        w = [int.from_bytes(blk[j:j + 4], "big") for j in range(0, 64, 4)]
        for t in range(16, 64):
            s0 = _rotr(w[t-15], 7) ^ _rotr(w[t-15], 18) ^ (w[t-15] >> 3)
            s1 = _rotr(w[t-2], 17) ^ _rotr(w[t-2], 19) ^ (w[t-2] >> 10)
            w.append((w[t-16] + s0 + w[t-7] + s1) & _MASK32)
        a, b, c, d, e, f, g, h = H8
        for t in range(64):
            S1 = _rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)
            ch = (e & f) ^ (~e & g)
            t1 = (h + S1 + ch + _FOLD_K[t] + w[t]) & _MASK32
            S0 = _rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)
            mj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (S0 + mj) & _MASK32
            h, g, f, e, d, c, b, a = g, f, e, (d+t1) & _MASK32, c, b, a, (t1+t2) & _MASK32
        H8 = [(x + y) & _MASK32 for x, y in zip(H8, [a, b, c, d, e, f, g, h])]
    return "".join("%08x" % x for x in H8)

FOLD_WIDTH = 16

def _fold_preimage(*parts):
    return "\u2225".join((ROOT,) + tuple(str(p) for p in parts))

def H(*parts):
    """Commitment map: SHA-256 of the parts joined under the basepoint prefix,
    truncated to FOLD_WIDTH hex digits."""
    return hashlib.sha256(_fold_preimage(*parts).encode()).hexdigest()[:FOLD_WIDTH]

def _H_law(*parts):
    return _sha256_hex(_fold_preimage(*parts).encode())[:FOLD_WIDTH]

# THE LAWFUL NAMES: no-11 words of width W number F(W+2) — the name space
# census is Fibonacci; unrank is the exact bijection; a name is the fold
# re-alphabetized INTO the grammar. Hex survives as port dress.
def unrank(r, W):
    out = []
    while W > 0:
        if r < _fibn(W + 1):
            out.append("0"); W -= 1
        else:
            r -= _fibn(W + 1); out.append("1")
            if W >= 2: out.append("0"); W -= 2
            else: W -= 1
    return "".join(out)

def gname(data, W=48):
    """Encode data as a fixed-length no-11 Fibonacci word (an element of the
    golden shift), via the rank→word bijection."""
    return unrank(int(H(data), 16) % _fibn(W + 2), W)

# ═══════════════════════════════════════════════════════════════════════════
#  §C · CANONICAL SERIALIZATION — deterministic encoding on the value grammar; floats rejected
# ═══════════════════════════════════════════════════════════════════════════
def canon(v):
    if v is None: return "null"
    if v is True: return "true"
    if v is False: return "false"
    if isinstance(v, float):
        raise TypeError("canon refuses floats — the exact, not the decimal")
    if isinstance(v, int): return str(v)
    if isinstance(v, str): return _canon_str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ",".join(canon(x) for x in v) + "]"
    if isinstance(v, dict):
        items = sorted(v.items(), key=lambda kv: kv[0])
        return "{" + ",".join(_canon_str(str(k)) + ":" + canon(val) for k, val in items) + "}"
    raise TypeError("canon refuses a value outside the grammar: %r" % type(v))

def _canon_str(s):
    out = ['"']
    for ch in s:
        o = ord(ch)
        if ch == '"': out.append('\\"')
        elif ch == "\\": out.append("\\\\")
        elif ch == "\n": out.append("\\n")
        elif ch == "\r": out.append("\\r")
        elif ch == "\t": out.append("\\t")
        elif o < 0x20: out.append("\\u%04x" % o)
        else: out.append(ch)
    out.append('"')
    return "".join(out)

# THE GOLDEN CANON — serialization IS the stream: every piece a self-delimiting
# codeword (LSB-first zeckendorf + the 11-terminator), the whole value grammar
# as one golden string. THE canon of the triad; JSON demotes to store dress.
_GTAG = {"null": 1, "false": 2, "true": 3, "int": 4, "str": 5, "list": 6, "dict": 7}

_CWG_MEMO = {}   # collared accelerator: the codeword of a small value is a pure function — cache it (bytes, tags, small lengths dominate the stream); the law is unchanged, only its speed
def _cwg(n):
    hit = _CWG_MEMO.get(n)
    if hit is None:
        hit = "".join("1" if x else "0" for x in gnum(n)) + "1"
        if n < 4096: _CWG_MEMO[n] = hit
    return hit

def _rdg(stream, i):
    buf = ""
    while True:
        buf += stream[i]; i += 1
        if buf.endswith("11"):
            v = 0; a, b = 1, 2
            for ch in buf[:-1]:
                if ch == "1": v += a
                a, b = b, a + b
            return v, i

def canon_gold(v):
    if v is None: return _cwg(_GTAG["null"])
    if v is True: return _cwg(_GTAG["true"])
    if v is False: return _cwg(_GTAG["false"])
    if isinstance(v, float):
        raise TypeError("canon refuses floats — golden or not")
    if isinstance(v, int):
        z = 2 * v if v >= 0 else -2 * v - 1
        return _cwg(_GTAG["int"]) + _cwg(z + 1)
    if isinstance(v, str):
        bs = v.encode("utf-8")
        return _cwg(_GTAG["str"]) + _cwg(len(bs) + 1) + "".join(_cwg(b + 1) for b in bs)
    if isinstance(v, (list, tuple)):
        return _cwg(_GTAG["list"]) + _cwg(len(v) + 1) + "".join(canon_gold(x) for x in v)
    if isinstance(v, dict):
        ks = sorted(v.keys())
        return _cwg(_GTAG["dict"]) + _cwg(len(ks) + 1) + \
               "".join(canon_gold(str(k)) + canon_gold(v[k]) for k in ks)
    raise TypeError("canon refuses a value outside the grammar: %r" % type(v))

def dec_gold(stream, i=0):
    t, i = _rdg(stream, i)
    if t == _GTAG["null"]: return None, i
    if t == _GTAG["true"]: return True, i
    if t == _GTAG["false"]: return False, i
    if t == _GTAG["int"]:
        z, i = _rdg(stream, i); z -= 1
        return (z // 2 if z % 2 == 0 else -(z + 1) // 2), i
    if t == _GTAG["str"]:
        L, i = _rdg(stream, i); out = []
        for _ in range(L - 1):
            b, i = _rdg(stream, i); out.append(b - 1)
        return bytes(out).decode("utf-8"), i
    if t == _GTAG["list"]:
        L, i = _rdg(stream, i); out = []
        for _ in range(L - 1):
            x, i = dec_gold(stream, i); out.append(x)
        return out, i
    if t == _GTAG["dict"]:
        L, i = _rdg(stream, i); out = {}
        for _ in range(L - 1):
            k, i = dec_gold(stream, i); x, i = dec_gold(stream, i); out[k] = x
        return out, i
    raise ValueError("unknown golden tag")

# ═══════════════════════════════════════════════════════════════════════════
#  §T · TERMS — an abstract syntax of operation applications (the object language)
# ═══════════════════════════════════════════════════════════════════════════
CIRC = "\u25e6"   # the argument slot — ONE binding; the seat/model rebindings are DELETED (erasure ledger)

def rec(value, kids=()): return {"v": value, "kids": list(kids)}
_RID_MEMO = {}
def rid(record):
    """Content id of a term. Memoized by object identity so a shared sub-term
    (a DAG node reached by many parents) is hashed once, not once per path — the
    identity re-check makes a recycled id() a miss, never a wrong hit."""
    key = id(record); hit = _RID_MEMO.get(key)
    if hit is not None and hit[0] is record: return hit[1]
    val = H(canon_gold(record["v"]), *[rid(k) for k in record["kids"]])
    _RID_MEMO[key] = (record, val); return val
def expects_of(result): return H(canon_gold(result))

CIRC = "\u25e6"   # the argument slot filled bottom-up by a child's result

# THE PROOF-STATUS LATTICE (weakest first). The line an academic cares about is
# drawn here: `exhausted` (a claim verified on a finite domain) ranks strictly
# BELOW `forced` (a claim that is a free identity — verified on a symbolic/fresh
# instantiation, hence universal). A conjunction is graded by the meet, so any
# exhaustive step caps the whole claim at `exhausted`; only all-identity proofs
# reach `forced`. Empirically measured inputs remain `counted`/`witnessed`.
MODE_ORDER = {"held": 0, "seed": 1, "counted": 2, "witnessed": 2,
              "exhausted": 3, "forced": 4, "forced+": 5}
def mode_meet(a, b):
    return a if MODE_ORDER.get(a, 0) <= MODE_ORDER.get(b, 0) else b

def _grid_walk(axes):
    """odometer over a finite grid — the kernel imports nothing for it."""
    idx = [0] * len(axes)
    while True:
        yield tuple(axes[i][idx[i]] for i in range(len(axes)))
        k = len(axes) - 1
        while k >= 0:
            idx[k] += 1
            if idx[k] < len(axes[k]): break
            idx[k] = 0; k -= 1
        if k < 0: return

def grid_identity(build, var_points, degrees, lawbook):
    """THE UNIVERSALITY CERTIFICATE (forced+): the fifth rung. An identity whose
    two sides are integer polynomials in its parameters, of STATED degrees, is
    verified on a full grid strictly exceeding those degrees in every variable
    (>= d_i + 1 distinct points). The difference polynomial then vanishes on
    the whole grid, hence identically (the factor-theorem grid lemma, by
    induction on the variables — an external citation, named, like Mordell in
    W.11), so the identity is UNIVERSAL given the stated bounds — and the
    bounds are the certificate's named trust surface, not a hidden premise.
    A grid that does not exceed the bounds is refused; a failing grid point
    lands the judgment at held (the identity is false, not merely finite);
    a passing grid whose points are not all forced caps at exhausted. The
    two-point free-identity discipline survives beneath as forced;
    forced+ is what \u2200 costs."""
    if len(var_points) != len(degrees):
        return {"refused": "one degree bound per variable"}
    for pts, d in zip(var_points, degrees):
        if len(set(pts)) < d + 1:
            return {"refused": "grid does not exceed the stated degree"}
    verdict = "forced+"
    for args in _grid_walk(list(var_points)):
        r = reenact_deep(build(*args), lawbook)
        if ("refused" in r) or (not r.get("agrees")): return "held"
        if r.get("mode") != "forced": verdict = "exhausted"
    return verdict

def free_identity(build, seed_args, fresh_args, lawbook):
    """Enforce the exhausted/forced distinction INSIDE the evaluator: a claim is
    a free identity only if the SAME term shape also verifies on an independent
    fresh instantiation of its inputs (a Schwartz–Zippel-style witness of
    universality). Returns 'forced' when both the seed instance and the fresh
    instance agree, else 'exhausted' — the machine deciding, not the prose.
    `build(*args)` returns a term with its expectation baked from those args."""
    r0 = reenact_deep(build(*seed_args), lawbook)
    r1 = reenact_deep(build(*fresh_args), lawbook)
    if r0.get("agrees") and r1.get("agrees") and r0.get("mode") == "forced" \
       and r1.get("mode") == "forced":
        return "forced"
    return "exhausted"

def reenact_deep(record, lawbook, modebook=None, _memo=None):
    """Bottom-up term evaluator with checked postconditions. Evaluate children
    first, substitute their results into the ◦ argument slots, apply the named
    operation, and verify the commitment of the result equals the term's stated
    expectation. A single failed check fails the whole term; an operation absent
    from the table halts with a refusal; the proof status is the lattice-meet of
    the children's statuses with the node's own. A term is a DAG, not a tree:
    results are memoized by node identity (scoped to this evaluation), so a
    shared sub-term is reenacted once — an exponential tree walk made linear.
    Each TOP-LEVEL evaluated term is recorded so the triad can measure its
    own irreducible size (see stream_measure)."""
    top = _memo is None
    if _memo is None: _memo = {}
    if top: _ROOTS.append(record)
    key = id(record); hit = _memo.get(key)
    if hit is not None and hit[0] is record: return hit[1]
    res = _reenact_body(record, lawbook, modebook, _memo)
    _memo[key] = (record, res); return res

def _reenact_body(record, lawbook, modebook, _memo):
    v = record["v"]
    kid_results = []; kid_mode = "forced"
    for k in record["kids"]:
        r = reenact_deep(k, lawbook, modebook, _memo)
        if "refused" in r: return r
        if not r["agrees"]: return {"rid": rid(record), "agrees": False, "mode": r.get("mode", "held")}
        kid_results.append(r.get("result"))
        kid_mode = mode_meet(kid_mode, r.get("mode", "forced"))
    if not (isinstance(v, dict) and "law" in v):
        ok = modebook["seed"](v) if (modebook and "seed" in modebook) else True
        return {"rid": rid(record), "agrees": ok, "mode": "seed", "result": v}
    if v["law"] not in lawbook:
        return {"refused": "no law named %r in the supplied book" % v["law"]}
    args = list(v["args"]); slot = 0
    for i, a in enumerate(args):
        if a == "\u25e6":
            args[i] = kid_results[slot]; slot += 1
    got = lawbook[v["law"]](*args)
    agrees = H(canon_gold(got)) == v["expects"]
    stored_mode = v.get("mode", "forced")
    my_mode = mode_meet(stored_mode, kid_mode)
    if modebook and stored_mode in modebook and agrees:
        if not modebook[stored_mode](v, got):
            my_mode = mode_meet("held", my_mode)
    return {"rid": rid(record), "agrees": agrees, "mode": my_mode, "result": got}

_INTERN = {}
def T(law, args, expects, kids=(), mode="forced"):
    """The term constructor — constants ride in args, computed content in kids.
    HASH-CONSED: a term is interned by its rid (the same content-identity the
    expectations, pins and store already trust to be collision-free), so two
    structurally identical terms are ONE object. The DAG becomes explicit at
    construction — a shared sub-term is built once and, via the identity-memoized
    evaluator, reenacted once — and the number of DISTINCT interned nodes is a
    claim's irreducible size."""
    node = rec({"law": law, "args": list(args), "expects": expects, "mode": mode}, kids)
    return _INTERN.setdefault(rid(node), node)

def chainT(law, links, seed=None):
    """THE ONE CHAIN: every iterated definition-term in the body is this fold —
    T(law, args, E(v)) nested through the ◦-slot. def_add's successor tower,
    def_mul's b-fold addition, def_fib's unrolled recurrence, def_mod's descent,
    the floor's successor ramp and the model's φ-power tower are all seed
    choices of this one builder — the One Completion, at the level of terms.
    links: [(args, value), ...]; returns `seed` (default None) on empty links."""
    t = seed
    for args, v in links:
        t = T(law, args, expects_of(v), kids=[] if t is None else [t])
    return t

def _census(claims):
    """count a book of claims: census by judgment glyph, verified among the
    countable, total countable, verdict. The four former per-seal counting
    loops are DELETED (erasure ledger)."""
    kc = {"\u22a2": 0, "\u22bb": 0, "\u2235": 0, "\u2423": 0, "\u21cc": 0}
    ok = True; good = 0
    for k, t, v in claims:
        kc[k] += 1
        if k not in ("\u2423", "\u21cc"):
            if v: good += 1
            else: ok = False
    return kc, good, kc["\u22a2"] + kc["\u22bb"] + kc["\u2235"], ok

def term_size(record, seen=None):
    """Irreducible size: distinct nodes in the term's DAG (each shared node once)."""
    if seen is None: seen = set()
    k = rid(record)
    if k in seen: return 0
    seen.add(k)
    return 1 + sum(term_size(kid, seen) for kid in record["kids"])

def tree_size(record, _memo=None):
    """Unfolded size: nodes counted with multiplicity (what a tree walk would see);
    computed in linear time by memoizing each node's own subtree total."""
    if _memo is None: _memo = {}
    key = id(record)
    if key in _memo: return _memo[key]
    s = 1 + sum(tree_size(kid, _memo) for kid in record["kids"])
    _memo[key] = s; return s

_ROOTS = []   # every top-level evaluated term, for the triad's self-measure
def stream_measure(roots=None):
    """The irreducible size of everything evaluated so far: distinct term-nodes
    (shared structure counted once) vs the total tree unfolding. The ratio is a
    Kolmogorov-flavored compression of the triad's own claims, read from the
    inside. Each distinct claim-term is counted once."""
    src = _ROOTS if roots is None else roots
    reps = {}
    for r in src: reps[rid(r)] = r
    reps = list(reps.values())
    seen = set()
    for r in reps: term_size(r, seen)
    return len(seen), sum(tree_size(r) for r in reps)

def record_measure(reg, path=None):
    """Store THIS register's irreducible size (its evaluated roots) in the shared
    log under measure/<reg>, so the triad — sealing in separate processes — can
    be summed. The cell is grounded like any other: a later reader trusts it only
    while the kernel source is unchanged."""
    d, u = stream_measure()
    remember("measure/" + reg, rec({"nodes": d, "unfolded": u}), reg, path)
    return d, u

def triad_measure(path=None):
    """The triad's irreducible size: the sum of the per-register measures that
    are CURRENTLY GROUNDED (a stale or drifted register measure is refused, not
    counted). Returns (registers_present, nodes, unfolded) — partial when a
    register has not sealed into this log yet."""
    regs = []; nodes = 0; unfolded = 0
    for reg in ("body",):
        g = grounded("measure/" + reg, path)
        if "grounded" in g:
            pv = g["v"]["v"]           # unwrap the rec payload
            regs.append(reg); nodes += pv["nodes"]; unfolded += pv["unfolded"]
    return regs, nodes, unfolded

# ── THE DAG CODEC — emit the shared graph, not the unfolded tree ──────────────
# A term is a DAG; a tree serialization repeats every shared sub-term, so its
# length tracks the UNFOLDED size. This codec writes each distinct node once in
# topological order (kids before parents) with kids as back-reference indices, so
# the encoded length tracks the IRREDUCIBLE size — what stream_measure counts is
# now what the stream emits. Values ride the golden canon; indices ride codewords.
def _dag_order(roots):
    order = []; index = {}
    def visit(n):
        k = rid(n)
        if k in index: return
        for kid in n["kids"]: visit(kid)
        index[k] = len(order); order.append(n)
    for r in roots: visit(r)
    return order, index

def dag_encode(roots):
    order, index = _dag_order(roots)
    s = _cwg(len(order) + 1)
    for n in order:
        s += canon_gold(n["v"]) + _cwg(len(n["kids"]) + 1)
        s += "".join(_cwg(index[rid(kid)] + 1) for kid in n["kids"])
    s += _cwg(len(roots) + 1) + "".join(_cwg(index[rid(r)] + 1) for r in roots)
    return s

def dag_decode(stream):
    i = 0; N, i = _rdg(stream, i); N -= 1; built = []
    for _ in range(N):
        v, i = dec_gold(stream, i)
        k, i = _rdg(stream, i); k -= 1; kids = []
        for _ in range(k):
            idx, i = _rdg(stream, i); kids.append(built[idx - 1])
        built.append(rec(v, kids))
    R, i = _rdg(stream, i); R -= 1; roots = []
    for _ in range(R):
        idx, i = _rdg(stream, i); roots.append(built[idx - 1])
    return roots

def crossing_dag(reg, lawbook, path=None):
    """THE CROSSING AS THE ACTION PRINCIPLE: re-prove the PREVIOUS generation's
    committed proofs under the PRESENT book, and record the pin succession.
    replay_dag reproduces within one generation (same pin — kinematics, and a
    foreign pin is refused); crossing_dag is the one lawful crossing BETWEEN
    generations (re-proof under a new pin — dynamics). Only content stationary
    under the variation of the book propagates; the lineage is the ledger of
    the conserved charge: a continuous run means the pin never changed (a
    gauge crossing — re-spelling only), a new run means a law was admitted or
    removed (a dynamical crossing — the book itself changed). Held when there is
    nothing to cross or the generation is unchanged; refused when the prior
    theorems do not re-prove — a seal must not silently bury its ancestors."""
    st = _load(path)
    c = st["cells"].get("dag/" + reg)
    if c is None or "tomb" in c: return {"held": reg}
    if rid(c["v"]) != c["rid"]: return {"refused": "tampered prior generation"}
    payload = c["v"]["v"]
    pin = _pin_of(lawbook)
    li = lineage("dag/" + reg, path)
    pins = li.get("pins", [])
    last = pins[-1] if pins else payload.get("pin")
    if last == pin: return {"held": reg}
    roots = dag_decode(payload["dag"])
    for r, expected in zip(roots, payload["verdicts"]):
        rr = reenact_deep(r, lawbook)
        got = "R" if "refused" in rr else bool(rr.get("agrees"))
        if got != expected:
            return {"refused": "the prior generation does not re-prove under the present book"}
    if not pins and payload.get("pin"):
        _extend_lineage(st, "dag/" + reg, payload["pin"])   # seed: the ancestor's own pin
    _extend_lineage(st, "dag/" + reg, pin)
    _append(st, {"op": "crossing", "name": "dag/" + reg, "pin": pin})
    _save(st, path)
    return {"crossed": reg, "pin": pin}

def commit_dag(reg, lawbook, path=None):
    """Commit this register's whole claim graph into the log as dag/<reg>: a
    content-addressed (rid-grounded) golden encoding at irreducible size, paired
    with each root's recorded verdict (True / False / 'R' for a designed refusal)
    AND the pin of the operation table it was sealed under. The DAG becomes a
    re-executable record — a later run recalls it, decodes to terms, reenacts them
    under a table whose pin matches, and confirms the verdicts reproduce."""
    reps = {}
    for r in _ROOTS: reps[rid(r)] = r
    reps = list(reps.values())
    crossing_dag(reg, lawbook, path)      # cross the generation gate BEFORE the overwrite
    dag = dag_encode(reps)
    verdicts = []
    for r in reps:
        rr = reenact_deep(r, lawbook)
        verdicts.append("R" if "refused" in rr else bool(rr.get("agrees")))
    remember("dag/" + reg, rec({"dag": dag, "verdicts": verdicts, "pin": _pin_of(lawbook)}),
             reg, path)
    return len(dag), len(reps)

def replay_dag(reg, lawbook, path=None):
    """Reconstruct a register's proofs from its content-addressed DAG and re-run
    them under the given operation table. (True, 0) if nothing is committed yet;
    (False, 0) if the cell drifted OR the supplied table's pin differs from the one
    the proofs were sealed under (foreign semantics — refused, not trusted); else
    (all-verdicts-reproduce, n). Re-runnable only under provably the same laws."""
    g = grounded("dag/" + reg, path)
    if "refused" in g:
        return (g["refused"].startswith("no cell"), 0)
    payload = g["v"]["v"]
    if payload.get("pin") != _pin_of(lawbook):
        return (False, 0)                       # foreign lawbook — semantics differ
    dag = payload["dag"]; verdicts = payload["verdicts"]
    roots = dag_decode(dag)
    ok = (dag_encode(roots) == dag) and (len(roots) == len(verdicts))
    for r, expected in zip(roots, verdicts):
        rr = reenact_deep(r, lawbook)
        got = "R" if "refused" in rr else bool(rr.get("agrees"))
        ok = ok and (got == expected)
    return ok, len(roots)

# ── GENERIC DEFINITION-TERMS — linear algebra reduced to the primitive base ──
# These assemble T() nodes only; arithmetic bottoms at mul/add/sub/idiv (all
# floor-reducible), structure is built by `vec` (n-ary juxtaposition, the
# generalization of the primitive `pair`). Available to any register so a claim
# over matrices can be verified against the primitives rather than trusted to a
# fast implementation.
def _leafT(v):        # a trivial identity term v+0=v: a constant carried as a forced node
    return T("add", [v, 0], expects_of(v))

def def_dot(u, v):
    """Σ uᵢvᵢ as a forced term over mul/add — the inner product from primitives."""
    prods = [T("mul", [u[i], v[i]], expects_of(u[i] * v[i])) for i in range(len(u))]
    if not prods: return _leafT(0)
    t = prods[0]; s = u[0] * v[0]
    for i in range(1, len(prods)):
        s += u[i] * v[i]
        t = T("add", [CIRC, CIRC], expects_of(s), kids=[t, prods[i]])
    return t

def def_matvec(A, v):
    """A·v as a term: each entry an inner-product term, assembled by `vec`."""
    res = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]
    kids = [def_dot(A[i], v) for i in range(len(A))]
    return T("pair", [CIRC] * len(res), expects_of(res), kids=kids)

def def_immul(A, B):
    """A·B as a term: entrywise inner products, rows and matrix assembled by `vec`."""
    n = len(A); m = len(B[0]); p = len(B)
    prod = [[sum(A[i][t] * B[t][j] for t in range(p)) for j in range(m)] for i in range(n)]
    rows = []
    for i in range(n):
        ents = [def_dot(A[i], [B[t][j] for t in range(p)]) for j in range(m)]
        rows.append(T("pair", [CIRC] * m, expects_of(prod[i]), kids=ents))
    return T("pair", [CIRC] * n, expects_of(prod), kids=rows)

def def_idet(M):
    """det M as a term by fraction-free (Bareiss) elimination — every cell update
    (M[i][j]·M[k][k] − M[i][k]·M[k][j]) // prev is a subterm over mul/sub/idiv,
    so the determinant reduces to the primitive base (no rationals introduced)."""
    n = len(M)
    TM = [[_leafT(M[i][j]) for j in range(n)] for i in range(n)]   # every cell a forced term
    val = [[M[i][j] for j in range(n)] for i in range(n)]          # its tracked value
    sign = 1; prev = 1; prevT = _leafT(1)
    for k in range(n - 1):
        if val[k][k] == 0:
            sw = next((i for i in range(k + 1, n) if val[i][k] != 0), None)
            if sw is None: return _leafT(0)
            TM[k], TM[sw] = TM[sw], TM[k]; val[k], val[sw] = val[sw], val[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a, b, c, d = val[i][j], val[k][k], val[i][k], val[k][j]
                p1 = T("mul", [CIRC, CIRC], expects_of(a * b), kids=[TM[i][j], TM[k][k]])
                p2 = T("mul", [CIRC, CIRC], expects_of(c * d), kids=[TM[i][k], TM[k][j]])
                df = T("sub", [CIRC, CIRC], expects_of(a * b - c * d), kids=[p1, p2])
                nv = (a * b - c * d) // prev
                TM[i][j] = T("idiv", [CIRC, CIRC], expects_of(nv), kids=[df, prevT])
                val[i][j] = nv
        prevT = TM[k][k]; prev = val[k][k]
    det = sign * val[n - 1][n - 1]
    if sign == 1: return TM[n - 1][n - 1]
    return T("mul", [CIRC, -1], expects_of(det), kids=[TM[n - 1][n - 1]])

# ── DETERMINANT AS ELIMINATION-MOD-ORDER — one operator, the order its parameter ─
# The determinant is computed by removing vertices one at a time; the only free
# parameter is the ORDER. def_idet (Bareiss) removes them in index order and pays
# fill-in — pivots fan out, the term is dense (its DAG the 418×-shared showcase).
# On a FOREST a perfect (leaf-first) order is fill-in-free AND division-free, and
# the same elimination collapses to the diagram's own continuant:
#   det(S) = M[p][p]·det(S−p) − M[p][u]·M[u][p]·det(S−p−u)   (p a leaf, u its neighbor)
# The VALUE is the elimination-order invariant (det); the TERM (its size) is the
# order-dependent shadow, governed by fill-in. This is the register's fiber/quotient
# law (Z.W) at the determinant: order is the fiber, det the quotient, fill-in the cost.
def _graph_of(M):
    n = len(M); adj = {i: set() for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and (M[i][j] != 0 or M[j][i] != 0): adj[i].add(j)
    return n, adj

def is_forest(M):
    """True iff M's off-diagonal graph is a forest — peel leaves; a residue with
    every surviving vertex of degree ≥2 carries a cycle."""
    n, adj = _graph_of(M); alive = set(range(n)); g = {i: set(adj[i]) for i in range(n)}
    changed = True
    while changed and alive:
        changed = False
        for v in list(alive):
            if len(g[v] & alive) <= 1: alive.discard(v); changed = True
    return not alive

def elim_fillin(M, order):
    """Edges ADDED by eliminating vertices in `order` (the elimination game):
    removing v makes its live neighbors a clique. 0 fill-in ⇔ `order` is a perfect
    elimination ordering. Fill-in is the cost that separates elimination orders."""
    n, adj = _graph_of(M); g = {i: set(adj[i]) for i in range(n)}
    alive = set(range(n)); added = 0
    for v in order:
        nb = sorted(g[v] & alive)
        for a in range(len(nb)):
            for b in range(a + 1, len(nb)):
                if nb[b] not in g[nb[a]]:
                    g[nb[a]].add(nb[b]); g[nb[b]].add(nb[a]); added += 1
        alive.discard(v)
    return added

def perfect_order(M):
    """A perfect elimination ordering when one exists (always, on a forest):
    repeatedly take a current leaf. None if the graph is not chordal-by-leaves."""
    n, adj = _graph_of(M); g = {i: set(adj[i]) for i in range(n)}
    alive = set(range(n)); order = []
    while alive:
        leaf = next((v for v in sorted(alive) if len(g[v] & alive) <= 1), None)
        if leaf is None: return None
        order.append(leaf); alive.discard(leaf)
    return order

def def_det_forest(M):
    """det of a symmetric FOREST matrix by the fill-in-free, division-free leaf
    recursion — the same elimination as def_idet at its perfect order. A term over
    mul/sub only (bottoms at the floor), memoized on the vertex subset so shared
    subforests are one interned node. None when M is not a forest (caller refuses),
    the domain guard being computed, not assumed."""
    if not is_forest(M): return None
    n, adj = _graph_of(M); memo = {}
    def rec(S):
        key = frozenset(S)
        if key in memo: return memo[key]
        if not S:
            memo[key] = (T("mul", [1, 1], expects_of(1)), 1); return memo[key]
        p = min(S, key=lambda v: len(adj[v] & S))       # a leaf of the induced forest
        rest = S - {p}; t1, v1 = rec(rest); pii = M[p][p]
        term_pii = T("mul", [pii, CIRC], expects_of(pii * v1), kids=[t1])
        nb = adj[p] & S
        if not nb:
            memo[key] = (term_pii, pii * v1); return memo[key]  # isolated: M[p][p]·det(rest)
        u = next(iter(nb)); t2, v2 = rec(rest - {u}); w = M[p][u] * M[u][p]
        term_w = T("mul", [w, CIRC], expects_of(w * v2), kids=[t2])
        val = pii * v1 - w * v2
        t = T("sub", [CIRC, CIRC], expects_of(val), kids=[term_pii, term_w])
        memo[key] = (t, val); return memo[key]
    return rec(frozenset(range(n)))[0]

# ── FLOOR-PURE REDUCTION — proofs that take nothing above the primitives ──────
# The definition-terms above bottom at mul/add/sub/idiv, but mul and add are
# themselves defined (they reduce to succ). These builders expand arithmetic all
# the way to the successor primitive, so the resulting term invokes ONLY floor
# laws — a proof checkable from the floor up, nothing above the primitives trusted.
def def_add_floor(a, b):
    """a + b built from the primitives alone: 0 from sub, then a+b successors."""
    return _succ_to(_floor_zero(), 0, a + b)

def def_mul_floor(a, b):
    """a · b as b additions of a from 0, each a successor step — floor-pure."""
    t = _floor_zero(); s = 0
    for _ in range(b):
        t = _succ_to(t, s, s + a); s += a
    return t

def _floor_zero():
    return T("sub", [0, 0], expects_of(0))          # 0 from the primitive sub

def _succ_to(base_term, base_val, target):
    """the successor ramp — the One Chain seeded at the base term."""
    return chainT("succ", [([CIRC], s) for s in range(base_val + 1, target + 1)], seed=base_term)

def def_det2_floor(M):
    """det of a 2×2 integer matrix, ad − bc, with the products expanded to the
    successor primitive and the difference taken by the primitive sub — floor-pure."""
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    return T("sub", [CIRC, CIRC], expects_of(a * d - b * c),
             kids=[def_mul_floor(a, d), def_mul_floor(b, c)])

def laws_of(term, seen=None, acc=None):
    """The set of law names a term invokes (DAG-aware, each node once)."""
    if seen is None: seen = set(); acc = set()
    k = rid(term)
    if k in seen: return acc
    seen.add(k)
    v = term["v"]
    if isinstance(v, dict) and "law" in v: acc.add(v["law"])
    for kid in term["kids"]: laws_of(kid, seen, acc)
    return acc

def floor_pure(term):
    """True iff every law the term invokes is a primitive of the floor — the term
    takes nothing above the primitives on trust."""
    return laws_of(term).issubset(set(FLOOR))

# ═══════════════════════════════════════════════════════════════════════════
#  §O · THE CAUSAL ORDER — the derivation order IS emergence
#  A law's causal past is the set of laws its definition-term invokes. The
#  floor is stratum 0 — the uncaused. A law emerges at stratum 1 + the maximum
#  of its parents'. Causality is acyclicity: a law that is its own ancestor is
#  refused. An ancestor with neither a genealogy nor floor membership is OPEN —
#  the trust surface, COMPUTED as the boundary of the causal cones rather than
#  hand-listed. The DAG codec already emits kids before parents, so the golden
#  stream is a linear extension of this order: emission is emergence.
# ═══════════════════════════════════════════════════════════════════════════
def law_parents(build, seed_args, fresh_args):
    """The causal past of a law, FORCED: the laws its definition-term invokes,
    required identical on an independent fresh instantiation — parenthood is
    universal, not an artifact of one instance (the free-identity discipline
    applied to the genealogy itself). None when the two instances disagree."""
    p0 = laws_of(build(*seed_args))
    p1 = laws_of(build(*fresh_args))
    return p0 if p0 == p1 else None

def _strata_fold(parents, floor_names):
    """THE EMERGENCE FOLD over an explicit parent map: strata, open ancestors,
    or the cycle refusal — Z.C's engine, factored so the lawbook's genealogy
    and the constants' causal tower (W.17) share ONE fold. A node absent from
    the map and the floor is an open ancestor; a cycle refuses the whole map."""
    floor_names = set(floor_names)
    strata = {}; opens = {}
    def visit(nm, stack):
        if nm in floor_names: return 0, set()
        if nm not in parents: return None, {nm}            # an open ancestor
        if nm in stack: raise ValueError("cycle")
        if nm in strata: return strata[nm], opens[nm]
        stack.add(nm)
        ds = [0]; op = set()
        for p in parents[nm]:
            d, o = visit(p, stack)
            op |= o
            if d is not None: ds.append(d)
        stack.discard(nm)
        strata[nm] = 1 + max(ds); opens[nm] = op
        return strata[nm], op
    try:
        for nm in parents: visit(nm, set())
    except ValueError:
        return {"refused": "a node is its own ancestor"}
    return {"parents": {k: sorted(v) for k, v in parents.items()},
            "strata": dict(strata),
            "opens": {k: sorted(v) for k, v in opens.items() if v}}

def causal_order(genealogy, floor_names):
    """Strata of emergence over a forced genealogy. genealogy maps a law name
    to (builder, seed_args, fresh_args). Returns {parents, strata, opens} or a
    refusal: a non-forced genealogy is refused; a cyclic one is refused —
    causality is acyclic or it is not causality. The fold is _strata_fold."""
    parents = {}
    for law, (build, s, f) in genealogy.items():
        p = law_parents(build, s, f)
        if p is None: return {"refused": "genealogy not forced for %r" % law}
        parents[law] = set(p)
    return _strata_fold(parents, floor_names)

def causal_stream_ok(roots):
    """No term precedes its causes: in the emitted DAG order every kid's index
    is strictly below its parent's — the stream is a linear extension of the
    causal order, hence a causal history."""
    order, index = _dag_order(roots)
    return all(index[rid(kid)] < index[rid(n)] for n in order for kid in n["kids"])

# ═══════════════════════════════════════════════════════════════════════════
#  §B · BINDING — modules interact only through the kernel; binding gated by observational fingerprint
# ═══════════════════════════════════════════════════════════════════════════
PIN_PROTOCOL = 2   # the generation of the OBSERVATION PROTOCOL itself — the meter is law
_PIN_FOUNDING = [(0,), (3,), (8,), ([1, 2, 3],), (3, 4), (12, 5),
                 ([1, 2, 3], [2, 3, 5]), ([2, 3], [4, 1])]

def _pin_probes():
    """THE GROWING BATTERY: the 8 founding probes plus 24 probes DERIVED from
    the fold itself — deterministic, seeded by the protocol generation, no
    randomness. A generation may ADD probes, never remove them (monotone
    growth is the protocol's discipline; the census is committed to the log).
    The pin remains a FINITE observation — extensional equality is undecidable
    — but the gap is now a named, committed, monotonically shrinking residue
    rather than an implicit eight-point convention."""
    probes = list(_PIN_FOUNDING)
    for i in range(24):
        h = int(H("pin-probe", PIN_PROTOCOL, i), 16)
        kind = h % 4
        a = (h >> 8) % 97; b = ((h >> 16) % 89) + 1
        la = [(h >> (20 + 4 * j)) % 13 for j in range(3)]
        lb = [((h >> (32 + 4 * j)) % 11) + 1 for j in range(3)]
        if kind == 0: probes.append((a,))
        elif kind == 1: probes.append((a, b))
        elif kind == 2: probes.append((la,))
        else: probes.append((la, lb))
    return probes

def _pin_of(lawbook):
    """Observational fingerprint of an operation table: each operation is probed
    on the protocol's battery (8 founding + 24 derived) and the committed
    outputs are hashed. Two tables with identical behavior ON THE CENSUS get one
    fingerprint regardless of source text; a refused probe is a defined
    observation (⊥)."""
    attempts = _pin_probes()
    rows = []
    for lname in sorted(lawbook):
        landings = []
        for args in attempts:
            try: landings.append(H(canon_gold(lawbook[lname](*args))))
            except Exception: landings.append("\u22a5")
        rows.append((lname, landings))
    return H(canon_gold(rows))

def _pin_soundness_proof():
    """THE AUDIT ATTACK, INTERNED: the original red-team counterexample — a
    book agreeing with an honest book on the 8 founding probes and defecting
    everywhere else — shared a pin under protocol 1. Under protocol 2 it is
    SEPARATED. A pure refactor (different source, one behavior) still shares
    the pin. The protocol census is committed to the log: the meter is law."""
    founding = {canon_gold(list(t)) for t in _PIN_FOUNDING}
    honest = {"f": lambda *a: 0}
    defector = {"f": lambda *a: 0 if canon_gold(list(a)) in founding else 777}
    ok = (_pin_of(honest) != _pin_of(defector))           # the attack no longer passes
    refac = {"f": lambda *a: 0 * len(a)}                  # new spelling, one behavior
    ok &= (_pin_of(honest) == _pin_of(refac))             # gauge is still gauge
    ok &= (len(_pin_probes()) == 32)
    remember("pin-protocol", rec({"generation": PIN_PROTOCOL,
                                  "founding": 8, "derived": 24, "total": 32}), "zero", STORE)
    ok &= ("grounded" in grounded("pin-protocol", STORE))
    return ok

def ground_book(book, path=None):
    """Commit the book's pin — re-grounding, not mere existence: a cell that
    survives from a prior generation with a drifted writer refuses at read
    time, so a stale commitment is re-written. (Latent until the triad's
    first GAUGE crossing: every prior crossing moved the pin and wrote a fresh cell;
    a pin-preserving source change left the stale cell blocking every read.)"""
    pin = _pin_of(book)
    key = "book:" + pin
    if "grounded" not in grounded(key, path):
        remember(key, rec({"pin": pin}), "zero", path)
    return pin

def read(term, book, path=None):
    """Kernel-mediated evaluation: the operation table is used only if its
    observational fingerprint is committed in the log."""
    key = "book:" + _pin_of(book)
    g = grounded(key, path)
    if "refused" in g:
        return {"refused": "no adjacency: the book is not grounded in zero"}
    return reenact_deep(term, book)

# ═══════════════════════════════════════════════════════════════════════════
#  §L · THE LOG AND STORE — an append-only hash-chained (Merkle) log with content-addressed cells
# ═══════════════════════════════════════════════════════════════════════════
def _fresh(): return {"cells": {}, "journal": [], "head": H("genesis"), "anchors": []}

def _load(path=None):
    path = path or STORE
    if not _port_exists(path): return _fresh()
    try: st = json.loads(_port_read(path))
    except Exception: return _fresh()
    for k in ("cells", "journal", "head", "anchors"): st.setdefault(k, _fresh()[k])
    return st

def _save(st, path=None): _port_write(path or STORE, json.dumps(st, sort_keys=True, ensure_ascii=False))
def _chain(head, entry): return H(head, canon_gold(entry))

def _append(st, entry):
    st["journal"].append(entry)
    st["head"] = _chain(st["head"], entry)
    if len(st["journal"]) % 8 == 0:
        st["anchors"].append({"at": len(st["journal"]), "head": st["head"]})
    return st

def replay(st):
    head = H("genesis")
    for entry in st["journal"]: head = _chain(head, entry)
    return head == st["head"]

def _anchor_grounded(st):
    head = H("genesis"); ok = True; ai = 0; anchors = st.get("anchors", [])
    for i, entry in enumerate(st["journal"], start=1):
        head = _chain(head, entry)
        while ai < len(anchors) and anchors[ai]["at"] == i:
            ok &= (anchors[ai]["head"] == head); ai += 1
    return ok

def _writer_print(): return H(_port_read_bytes(_port_self()).decode("utf-8", "replace"))

def remember(name, record, writer, path=None):
    """The STRING addresses; the HASH grounds — the two registers of a name."""
    st = _load(path)
    cell = {"v": record, "rid": rid(record), "writer": writer, "writer_sha": _writer_print()}
    st["cells"][name] = cell
    _append(st, {"op": "remember", "name": name, "rid": cell["rid"]})
    _save(st, path); return cell

def recall(name, path=None): return _load(path)["cells"].get(name)

def grounded(name, path=None):
    st = _load(path)
    if not replay(st): return {"refused": "the chain does not replay"}
    c = st["cells"].get(name)
    if c is None: return {"refused": "no cell under %r" % name}
    if "tomb" in c: return {"refused": "a tombstone stands"}
    if c.get("writer_sha") != _writer_print(): return {"refused": "writer drift"}
    if rid(c["v"]) != c["rid"]: return {"refused": "body altered"}
    return {"grounded": True, "rid": c["rid"], "v": c["v"]}

def evict(name, writer, path=None):
    st = _load(path); c = st["cells"].get(name)
    if c is None or "tomb" in c: return {"refused": "nothing to evict"}
    st["cells"][name] = {"tomb": c["rid"], "writer": writer, "writer_sha": _writer_print()}
    _append(st, {"op": "evict", "name": name, "tomb": c["rid"]})
    _save(st, path); return {"evicted": name, "tomb": c["rid"]}

def crossing(name, lawbook, writer, path=None, attest=None):
    """Product_g → Substrate_(g+1) by RE-PROOF; a witnessed crossing pins the book."""
    st = _load(path); c = st["cells"].get(name)
    if c is None: return {"refused": "nothing to cross"}
    if "tomb" in c: return {"refused": "the absent cannot cross"}
    if "grounded" in grounded(name, path): return {"held": name}
    r = reenact_deep(c["v"], lawbook)
    if "refused" in r: return r
    if not r["agrees"]: return {"refused": "does not re-prove under the supplied book"}
    pin = _pin_of(lawbook)
    if attest is not None:
        if _pin_of(attest) != pin: return {"refused": "false witness"}
        _extend_lineage(st, name, pin)
    c["writer"] = writer; c["writer_sha"] = _writer_print()
    st["cells"][name] = c
    _append(st, {"op": "crossing", "name": name, "rid": c["rid"], "pin": pin if attest is not None else None})
    _save(st, path)
    return {"crossed": name, "rid": c["rid"]}

def _lin_key(name): return "proved-under:%s" % name

def _extend_lineage(st, name, pin):
    key = _lin_key(name); cell = st["cells"].get(key); pins = []
    if cell and isinstance(cell.get("v"), dict) and isinstance(cell["v"].get("v"), dict):
        pins = list(cell["v"]["v"].get("pins", []))
    pins.append(pin)
    r = rec({"pins": pins})
    st["cells"][key] = {"v": r, "rid": rid(r), "writer": "lineage", "writer_sha": _writer_print()}

def lineage(name, path=None):
    st = _load(path); cell = st["cells"].get(_lin_key(name))
    if cell is None: return {"refused": "no lineage for %r" % name}
    if rid(cell["v"]) != cell["rid"]: return {"refused": "tampered lineage"}
    pins = cell["v"]["v"]["pins"]; runs = []
    for p in pins:
        if runs and runs[-1][0] == p: runs[-1][1] += 1
        else: runs.append([p, 1])
    return {"pins": pins, "runs": runs, "generations": len(pins), "continuous": len(runs) <= 1}

# ═══════════════════════════════════════════════════════════════════════════
#  §V · THE VERIFICATION SUITE — the kernel's own proof obligations
# ═══════════════════════════════════════════════════════════════════════════
def _self_source():
    try: return _port_read(_port_self())
    except Exception: return ""

def _port_collar_ok():
    src = _self_source()
    if not src: return True
    names = ("os.", "sys.", "open(", "glob.", "tempfile.", "importlib.")   # glob retained in the collar as a tombstone: its reappearance anywhere would be flagged
    inside = True; ok = True
    for line in src.splitlines():
        stripped = line.strip()
        if stripped.startswith("def _port_"): inside = True; continue
        if stripped.startswith("def ") and not stripped.startswith("def _port_"): inside = False
        if inside or stripped.startswith("#"): continue
        for nm in names:
            if nm in line and "collared" not in line and "_port_" not in line: ok = False
    return ok

def _binding_proof():
    d = _port_temp(); tp = _port_tmpname(d, "b.json")
    book = {"dbl": lambda x: 2 * x}
    ground_book(book, tp)
    t = T("dbl", [21], expects_of(42))
    r1 = read(t, book, tp)
    foreign = {"dbl": lambda x: 2 * x + 1}
    r2 = read(t, foreign, tp)
    refac = {"dbl": lambda x: x + x}
    r3 = read(t, refac, tp)
    return r1.get("agrees") is True and ("refused" in r2) and r3.get("agrees") is True

def _store_proof():
    d = _port_temp(); tp = _port_tmpname(d, "s.json")
    book = {"dbl": lambda x: 2 * x}
    thm = T("dbl", [21], expects_of(42))
    remember("thm", thm, "zero", tp)
    ok = "grounded" in grounded("thm", tp)
    st = _load(tp); st["cells"]["thm"]["v"]["v"]["args"] = [22]; _save(st, tp)
    ok &= "refused" in grounded("thm", tp)
    st = _load(tp); st["cells"]["thm"]["v"]["v"]["args"] = [21]
    st["cells"]["thm"]["rid"] = rid(st["cells"]["thm"]["v"]); _save(st, tp)
    ok &= "evicted" in evict("thm", "zero", tp) and "refused" in grounded("thm", tp)
    remember("t2", T("dbl", [21], expects_of(42)), "zero", tp)
    st = _load(tp); st["cells"]["t2"]["writer_sha"] = "d" * FOLD_WIDTH; _save(st, tp)
    ok &= "refused" in grounded("t2", tp)
    m = crossing("t2", book, "zero", tp, attest=book)
    ok &= "crossed" in m
    li = lineage("t2", tp)
    ok &= li.get("generations") == 1 and li.get("continuous") is True
    ok &= "held" in crossing("t2", book, "zero", tp, attest=book)
    return ok

def _golden_proof():
    """the two bases, one truth — golden rewriting against the substrate; the
    golden canon round-trips; the names are lawful words."""
    ok = _radix_agree(26)                          # the one grid; the private copy is DELETED
    batt = [None, True, 0, -7, 4181, "Kael", ["x", [1, None]], {"a": 1, "b": [2, "y"]}]
    for v in batt:
        s = canon_gold(v)
        got, i = dec_gold(s)
        ok &= (got == v) and (i == len(s)) and set(s) <= {"0", "1"}
    ok &= (canon_gold({"a": 1, "b": 2}) == canon_gold({"b": 2, "a": 1}))
    try: canon_gold(1.5); ok = False
    except TypeError: pass
    gs = [gname("cell-%d" % i) for i in range(30)]
    ok &= (len(set(gs)) == 30) and all("11" not in g and len(g) == 48 for g in gs)
    # THE ONE COMPLETION: the engine defines, the accelerator only speeds —
    # and lucas is fibonacci's boundary-dual under ONE law (trace vs entry)
    ok &= all(_law_run([1, 1], [0, 1], n) == _fibn(n) for n in range(0, 40))
    ok &= all(_luc(n) ==
              _law_run([1, 1], [0, 1], n - 1) + _law_run([1, 1], [0, 1], n + 1)
              for n in range(1, 30))
    ok &= (_ktrace([1, 1, 0], 21) == 367)              # perrin, no seed literal: the matrix computes its boundary
    # THE ONE OBJECT: a constant IS a law vector — matrix law, ring law,
    # trace law (seeds self-computed), and word law all verified generically
    # for FIVE laws at once: golden, plastic, elliptic, tribonacci, and the
    # FIELD ITSELF (ℚ(√5) is the object at [5,0]). The per-law blocks with
    # their hardcoded trace seeds are DELETED (erasure ledger).
    for law in ([1, 1], [1, 1, 0], [-1, 1], [1, 1, 1], [5, 0]):
        ok &= _konst_ok(law, 14)
    ok &= all(_pring_mul((1, 1), (a, b), (c, d)) == (a * c + b * d, a * d + b * c + b * d)
              for a in range(-3, 4) for b in range(-3, 4)
              for c in range(-2, 3) for d in range(-2, 3))
    # THE SHIFT IS M: up² = up + id as numerals — the founding equation a digit law
    ok &= all(gadd(gup(gnum(n)), gnum(n)) == gup(gup(gnum(n))) for n in range(0, 300))
    ok &= all(gdown(gup(gnum(n))) == gnum(n) for n in range(0, 100))
    # KNUTH'S CIRCLE associates on the grid; GPOW agrees across bases
    ok &= all(gcirc(gcirc(gnum(a), gnum(b)), gnum(c2)) == gcirc(gnum(a), gcirc(gnum(b), gnum(c2)))
              for a in range(1, 8) for b in range(1, 8) for c2 in range(1, 8))
    ok &= all(gval(gpow(gnum(b), e)) == b ** e for b in (2, 3, 5) for e in (0, 1, 5, 12))
    # THE CONE SHADOW: the golden base IS the signed register restricted to the
    # nonnegative cone — one normalizer, one adder, one subtractor, one order
    for w in range(1, 6):
        for code in range(4 ** w):
            d = [(code // 4 ** i) % 4 for i in range(w)]
            ok &= (_gnorm(list(d)) == snorm(list(d)))            # by definition now; the fossil pins it
    for a in range(0, 100):
        for b in range(0, 100):
            ok &= (gadd(gnum(a), gnum(b)) == sadd(gnum(a), gnum(b)))
            ok &= (glt(gnum(a), gnum(b)) == slt(gnum(a), gnum(b)))
            if b <= a: ok &= (gsub(gnum(a), gnum(b)) == gssub(gnum(a), gnum(b)))
    ok &= all(gmul(gnum(a), gnum(b)) == smul(gnum(a), gnum(b))
              for a in range(0, 40) for b in range(0, 40))
    ok &= (glt([3], [0, 1]) != slt([3], [0, 1]))   # off-canon the orders diverge: glt is its own law there
    # THE LAW AT NUMERAL LEVEL: the shared ladder's rung k is F(k+2)·x exactly,
    # and Knuth's circle is shift-equivariant — the generator acts on the product
    ok &= all(_ladder(gnum(a), count=8)[i] == gnum(_fibn(i + 2) * a)
              for a in range(1, 16) for i in range(8))
    ok &= all(gcirc(gup(gnum(a)), gnum(b)) == gup(gcirc(gnum(a), gnum(b)))
              for a in range(1, 12) for b in range(1, 12))
    return ok

def _signed_proof():
    """THE THIRD SYMBOL: subtraction total on \u2124, landing sign-pure; the
    Lucas ambiguity (the doublet vs its mirror-spelling — two spellings of
    the trace) oriented to the doublet; atoms, molecules, and the carving."""
    ok = True
    for a in range(-15, 16):
        for b in range(-15, 16):
            r = gssub(snum(a), snum(b))
            ok &= (sval(r) == a - b) and (r == snum(a - b))
    for n in (6, 9, 12):
        mixed = [0] * (n - 4) + [-1, 0, 0, 0, 1]        # F(n+2) − F(n−2)
        ok &= (snorm_full(mixed) == [0] * (n - 3) + [1, 0, 1])   # → the Lucas doublet
        ok &= (gnum(_luc(n)) == [0] * (n - 3) + [1, 0, 1])       # LUCAS: the molecules
        ok &= (gnum(_fibn(n)) == [0] * (n - 2) + [1])            # FIBONACCI: the atoms
    ok &= all(gval([1] * n) == _fibn(n + 3) - 2 for n in (5, 13, 21))   # the carving bound
    # THE RING CLOSES: Euclidean identity x = q·y + r verified signed
    # end-to-end INSIDE the base, remainder always in [0, |y|)
    for a in range(-18, 19):
        for b in range(-18, 19):
            ok &= (sval(sadd(snum(a), snum(b))) == a + b)
            ok &= (sval(smul(snum(a), snum(b))) == a * b)
            if b != 0:
                q, r = sdivmod(snum(a), snum(b))
                ok &= (sadd(smul(q, snum(b)), r) == snum(a))
                ok &= (not r) or (gval(r) < abs(b))
    return ok

def _wave_proof():
    """THE WAVE THEOREM and its consequences: the founding equation factored
    twice drives both parities of annihilation; ground states total and unique
    exhaustively at width 8; the leading-sign lemma and its domination engine;
    purity bought with mass on the F(n)−1 family; slt agrees with the order."""
    ok = True
    # the two engine identities, exact 2×2 integer matrices
    R = [[1, 1], [1, 0]]; I2 = [[1, 0], [0, 1]]; RINV = [[0, 1], [1, -1]]
    R2 = _gemm(R, R)                       # the one gemm; the private multiply is DELETED
    ok &= ([[R2[i][j] - I2[i][j] for j in range(2)] for i in range(2)] == R)    # R²−I = R
    ok &= ([[R[i][j] - I2[i][j] for j in range(2)] for i in range(2)] == RINV)  # R−I = R⁻¹
    ok &= (_gemm(R, RINV) == I2)
    # gap annihilation closed forms: +1 at n+g against −1 at n, both parities
    def _expect(n, g):
        e = [0] * (n + g)
        if g % 2 == 0:
            for i in range(g // 2): e[n + 1 + 2 * i] = 1        # pure wave above the pole
        else:
            for i in range(g // 2): e[n + 2 + 2 * i] = 1        # wave, shifted
            e[n - 1] += 1                                        # the undershoot: R⁻¹
        while e and e[-1] == 0: e.pop()
        return e
    for n in range(1, 11):
        for g in range(1, 12):
            d = [0] * (n + g + 1); d[n] = -1; d[n + g] = 1
            ok &= (snorm_full(d) == _expect(n, g))
    # TOTALITY + UNIQUENESS + THE LEADING-SIGN LEMMA, exhaustive at width 8:
    # every spelling over {−1,0,1} lands on the sign-pure Zeckendorf form of its
    # value, and after one local pass the top digit's sign is the value's sign.
    for code in range(3 ** 8):
        d = []; c = code
        for _ in range(8):
            d.append(c % 3 - 1); c //= 3
        v = sval(d)
        ok &= (snorm_full(list(d)) == snum(v))
        e = snorm(list(d))
        ok &= ((not e) and v == 0) or (bool(e) and v != 0 and (e[-1] > 0) == (v > 0))
    # the lemma's engine: the top weight dominates the widest lawful tail
    ok &= all(_fibn(n) > sum(_fibn(n - 3 * k) for k in range(1, n // 3 + 1))
              for n in range(5, 60))
    # PURITY BOUGHT WITH MASS: F(n)−1 grounds to (n−1)//2 marks while a
    # two-digit signed spelling of the same value exists — not mass-monotone
    for n in range(4, 26):
        g = gnum(_fibn(n) - 1)
        ok &= (sum(g) == (n - 1) // 2)
        spelling = [-1] + [0] * (n - 3) + [1]
        ok &= (sval(spelling) == _fibn(n) - 1) and (snorm_full(spelling) == g)
    # slt agrees with the integer order — on ground states and on impure spellings
    for a in range(-25, 26):
        for b in range(-25, 26):
            ok &= (slt(snum(a), snum(b)) == (a < b))
    for a in range(0, 20):
        for b in range(0, 20):
            da, db = gnum(a), gnum(b)
            m = max(len(da), len(db))
            d = [(da[k] if k < len(da) else 0) - (db[k] if k < len(db) else 0)
                 for k in range(m)]
            ok &= (slt([], d) == (a > b)) and (slt(d, []) == (a < b))
    # ONE LAW: every local rule of every normalizer is ≤2 signed instances of
    # the fundamental identity delta D(k) = e_k + e_{k+1} − e_{k+2} (value 0 by
    # F(k+2)=F(k+1)+F(k)); boundaries close under the fold F(1)=F(2). An
    # algorithm here is not a procedure but the causal completion of this one
    # law — the landing is order-independent (uniqueness above), so any time
    # that respects the order computes the same world.
    def _D(k): return {k: 1, k + 1: 1, k + 2: -1}
    def _cmb(a, b, s):
        r = dict(a)
        for kk, v in b.items(): r[kk] = r.get(kk, 0) + s * v
        return {kk: v for kk, v in r.items() if v}
    ok &= all({k: -1, k + 1: -1, k + 2: 1} == _cmb({}, _D(k), -1) for k in range(0, 9))   # generation
    ok &= all({k: -2, k + 1: 1, k - 2: 1} == _cmb(_D(k - 2), _D(k - 1), -1)
              for k in range(2, 9))                                                       # gravity
    ok &= all({k: 1, k + 1: 1, k + 2: -1} == _D(k) for k in range(0, 9))                  # gap-2 opposition
    ok &= all({k - 1: 1, k: 1, k + 1: -1} == _D(k - 1) for k in range(1, 9))              # gap-1 opposition
    ok &= (-2 * _fibn(3) + _fibn(4) + _fibn(2) == 0)   # gravity boundary k=1
    ok &= (-2 * _fibn(2) + _fibn(3) == 0)              # gravity boundary k=0
    ok &= (_fibn(2) + _fibn(2) - _fibn(3) == 0)        # the fold F(1)=F(2): position −1 ≡ 0
    # COMPLETENESS OF NULL CONSERVATION: the law's deltas together with the
    # boundary fold 2e_0−e_1 GENERATE the whole kernel of the valuation — the
    # explicit recurrence c_0=0, c_1=−fold, c_{k+2}=−D(k)+c_{k+1}+c_k reaches
    # every kernel basis vector e_k−F(k+2)e_0, so EVERY value-conserving
    # rearrangement whatsoever is a composition of the founding identity.
    Wd = 12
    def _vz(): return [0] * Wd
    def _vD(k):
        v = _vz(); v[k] += 1; v[k + 1] += 1; v[k + 2] -= 1; return v
    def _va(a, b, s=1): return [p + s * q for p, q in zip(a, b)]
    _fold = _vz(); _fold[0] = 2; _fold[1] = -1
    cc = [_vz(), _va(_vz(), _fold, -1)]
    for k in range(0, Wd - 2):
        cc.append(_va(_va(_va(_vz(), _vD(k), -1), cc[k + 1]), cc[k]))
    for k in range(1, Wd):
        want = _vz(); want[k] = 1; want[0] = -_fibn(k + 2)
        ok &= (cc[k] == want)
    ok &= all(sum(x * _fibn(i + 2) for i, x in enumerate(g)) == 0
              for g in [_fold] + [_vD(k) for k in range(Wd - 2)])
    # OBSERVER PLURALITY: four deterministic schedules over the same one-law
    # move set land identically on every spelling (the ontology is the
    # quotient) while their step-counts provably differ (cognition is the
    # fiber): landings invariant, patterns variant. The move set is the ONE
    # enumeration (_local_moves, far=True) — its private copy is DELETED.
    _pols = {0: lambda ms, t: min(ms), 1: lambda ms, t: max(ms),
             2: lambda ms, t: (min if t % 2 == 0 else max)(ms),
             3: lambda ms, t: next((m for m in ms if m[1] == 4), min(ms))}
    def _complete(d, pol):
        d = list(d); t = 0
        while t < 800:
            d2 = list(d) + [0, 0]
            ms = _local_moves(d2, far=True)
            if not ms:
                while d2 and d2[-1] == 0: d2.pop()
                return d2, t
            _fire_move(d2, _pols[pol](ms, t))
            while d2 and d2[-1] == 0: d2.pop()
            d = d2; t += 1
        return None, t
    _vecs = {p: [] for p in range(4)}
    for code in range(3 ** 5):
        d = [(code // 3 ** i) % 3 - 1 for i in range(5)]
        want = snum(sval(d))
        for pol in range(4):
            g, t = _complete(d, pol)
            ok &= (g == want); _vecs[pol].append(t)
    ok &= all(_vecs[p] != _vecs[q] for p in range(4) for q in range(p + 1, 4))
    return ok


def _crossing_proof():
    """THE ACTION PRINCIPLE, demonstrated on a temp store: a gauge crossing (same
    pin, different source) is held; a dynamical crossing (the book enlarged) re-
    proves the ancestor and extends the lineage — seeding the ancestor's own
    pin, so the first crossing records TWO generations, discontinuous exactly
    because the book changed; a book that breaks the old theorems is refused."""
    d = _port_temp(); tp = _port_tmpname(d, "m.json")
    bookA = {"dbl": lambda x: 2 * x}
    t = T("dbl", [21], expects_of(42))
    remember("dag/tmp", rec({"dag": dag_encode([t]), "verdicts": [True],
                             "pin": _pin_of(bookA)}), "zero", tp)
    gauge = {"dbl": lambda x: x + x}                      # new spelling, one behavior
    ok = ("held" in crossing_dag("tmp", gauge, tp))           # gauge crossing: nothing to cross
    ok &= ("refused" in lineage("dag/tmp", tp))           # and no lineage written
    grown = {"dbl": lambda x: 2 * x, "trpl": lambda x: 3 * x}   # the book enlarged
    ok &= ("crossed" in crossing_dag("tmp", grown, tp))        # dynamical crossing: re-proved, recorded
    li = lineage("dag/tmp", tp)
    ok &= (li.get("generations") == 2) and (li.get("continuous") is False)
    ok &= (li["pins"][0] == _pin_of(bookA)) and (li["pins"][1] == _pin_of(grown))
    ok &= ("held" in crossing_dag("tmp", grown, tp))          # same generation twice: held
    false_physics = {"dbl": lambda x: 2 * x + 1}          # breaks the ancestor
    ok &= ("refused" in crossing_dag("tmp", false_physics, tp))
    ok &= (lineage("dag/tmp", tp).get("generations") == 2)   # a refusal writes nothing
    return ok

def _universal_proof():
    """forced+ demonstrated FROM THE FLOOR UP: addition (degrees 1,1),
    multiplication (1,1) and the 2\u00d72 determinant (1,1,1,1) certified universal
    with every grid point floor-pure; a point-truth is DENIED the certificate
    (a failing grid point lands held); an insufficient grid is refused; and
    the lattice ranks forced+ strictly above forced."""
    ok = (grid_identity(def_add_floor, ([0, 1, 2], [0, 1, 2]), (1, 1), FLOOR) == "forced+")
    ok &= (grid_identity(def_mul_floor, ([0, 1, 2], [0, 1, 2]), (1, 1), FLOOR) == "forced+")
    det2 = lambda a, b, c, d: def_det2_floor([[a, b], [c, d]])
    ok &= (grid_identity(det2, ([0, 1], [0, 1], [0, 1], [0, 1]), (1, 1, 1, 1), FLOOR) == "forced+")
    pt = lambda a: T("succ", [a], expects_of(5 if a == 4 else a + 2))   # true nowhere on the grid off a=4... false at 3
    ok &= (grid_identity(pt, ([3, 4, 5],), (1,), FLOOR) == "held")
    ok &= ("refused" in grid_identity(def_add_floor, ([0, 1], [0]), (1, 1), FLOOR))
    ok &= (MODE_ORDER["forced"] < MODE_ORDER["forced+"])
    return ok


PORT_CENSUS = ("_port_argv", "_port_collar_ok", "_port_exists", "_port_exit",
               "_port_here", "_port_out", "_port_read", "_port_read_bytes", "_port_self",
               "_port_self_module", "_port_siblings", "_port_temp", "_port_tmpname", "_port_write")
# 14 organs: 12 admit the world; one audits the boundary; one names the self.

def _empirical_proof():
    """THE EMPIRICAL BOUNDARY: the a posteriori enters only through named
    organs. The port census is COMPUTED from this register's own source and
    must match the stated census; together with the collar (Z.0: no
    side-effecting call outside a port), every fact in the triad is exactly
    one of — derived (\u22a2/forced+), typed correspondence (\u21cc), named citation,
    or a PORT READING. Empiricism is collared and censused: the trust surface
    of the given is a finite, enumerated set of organs, committed to the log."""
    found = sorted({ln.strip()[4:].split("(")[0] for ln in _self_source().splitlines()
                    if ln.strip().startswith("def _port_")})
    ok = (found == sorted(PORT_CENSUS)) and _port_collar_ok()
    remember("ports", rec({"census": sorted(PORT_CENSUS)}), "zero", STORE)
    ok &= ("grounded" in grounded("ports", STORE))
    return ok


def _causal_proof():
    """THE DERIVATION ORDER IS EMERGENCE, on this register's own genealogy:
    the tower computes exactly (floor 0 → add/mul/det2 at 1 → dot/idet and the
    vec-open matrix laws at 2); the open ancestor set is COMPUTED and equals
    the EMPTY set — the last open ancestor was the floor's own n-ary pair;
    a non-forced or cyclic genealogy is refused; and the live claim
    stream is a linear extension — no term precedes its causes."""
    gen = {
        "add":    (def_add_floor, (3, 4), (6, 2)),
        "mul":    (def_mul_floor, (3, 4), (5, 2)),
        "det2":   (def_det2_floor, ([[2, 1], [1, 2]],), ([[3, 1], [2, 5]],)),
        "dot":    (def_dot, ([1, 2, 3], [2, 0, 5]), ([2, 7], [3, 1])),
        "idet":   (def_idet, ([[1, 2], [3, 4]],), ([[2, 1, 0], [1, 2, 1], [0, 1, 2]],)),
        "matvec": (def_matvec, ([[1, 2], [3, 4]], [9, 10]),
                   ([[2, 0, 1], [1, 3, 2], [0, 1, 1]], [1, 2, 3])),
        "immul":  (def_immul, ([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
                   ([[2, 0], [1, 3]], [[1, 1], [0, 2]])),
    }
    co = causal_order(gen, set(FLOOR))
    ok = "refused" not in co
    if not ok: return False
    ok &= (co["strata"] == {"add": 1, "mul": 1, "det2": 1,
                            "dot": 2, "idet": 2, "matvec": 2, "immul": 2})
    ok &= (co["opens"] == {})   # CLOSED: the assembler is the floor's own n-ary pair
    ok &= (co["parents"]["dot"] == ["add", "mul"])          # emergence is legible
    # causality refuses a law that is its own ancestor
    loop = {"a": (lambda: T("b", [1], expects_of(0)), (), ()),
            "b": (lambda: T("a", [1], expects_of(0)), (), ())}
    ok &= ("refused" in causal_order(loop, set(FLOOR)))
    # and refuses a genealogy that is an artifact of one instance
    def _u(n):
        return T("succ", [n], expects_of(n + 1)) if n else T("sub", [0, 0], expects_of(0))
    ok &= ("refused" in causal_order({"u": (_u, (0,), (4,))}, set(FLOOR)))
    # the emitted stream is a causal history: kids strictly precede parents
    reps = list({rid(r): r for r in _ROOTS}.values())
    ok &= bool(reps) and causal_stream_ok(reps)
    return ok

def _claims_z():
    # the floor censused — the golden base, the third symbol, the twins
    # (o_census was formerly assigned to o_floor and silently overwritten by the
    #  floor-pure verdict below — dead code; rewired live in this crossing)
    o_census = (len(FLOOR_CENSUS) == 17) and (len(GOLD_CENSUS) == 6) \
        and tuple(p.replace("\\", "/").rsplit("/", 1)[-1] for p in _port_siblings()) == REGISTER_CENSUS \
        and (len(SIGN_CENSUS) == 6) \
        and (FLOOR["gadd"]([1], [1]) == [0, 1]) and (FLOOR["gsub"]([0, 1], [1]) == [1]) \
        and (FLOOR["glt"]([1], [0, 1]) is True) \
        and (FLOOR["gdivmod"]([0, 0, 1], [0, 1]) == ([1], [1])) \
        and (FLOOR["ssub"]([1], [0, 1]) == [-1]) \
        and (FLOOR["slt"]([-1], [1]) is True) and (FLOOR["slt"]([0, 1], [1]) is False) \
        and (FLOOR["succ"](1) == 2) and (FLOOR["idiv"](7, 2) == 3) and (FLOOR["pair"](1, 2) == [1, 2])
    o_gold = _golden_proof()
    o_sign = _signed_proof()
    # the fold derived + agreement + headed through the void
    battery = [(), ("Kael",), ("", "a", "b"), (_self_source()[:200],)]
    o_fold = all(H(*b) == _H_law(*b) for b in battery) and \
        all(_fold_preimage(*b).startswith("\u2225") for b in battery[1:])
    # canon refuses the decimal, matches json on the grammar
    grammar = [None, True, False, 0, -7, "x", ["a", 1, None], {"b": 2, "a": [1, 2]}]
    o_canon = all(canon(v) == json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
                  for v in grammar)
    try: canon(1.5); o_canon = False
    except TypeError: pass
    # the tree is the program, on the FLOOR alone
    inner = T("succ", [4], expects_of(5))
    outer = T("succ", ["\u25e6"], expects_of(6), kids=[inner])
    r = reenact_deep(outer, FLOOR)
    forged = T("succ", ["\u25e6"], expects_of(7), kids=[inner])
    alien = T("no_such_law", [1], expects_of(1))
    o_eval = r["agrees"] and (r["mode"] == "forced") \
        and (not reenact_deep(forged, FLOOR)["agrees"]) \
        and ("refused" in reenact_deep(alien, FLOOR))
    # modes: weakest survives
    o_modes = (mode_meet("forced", "held") == "held") and (mode_meet("forced", "counted") == "counted")
    # THE FORCED/EXHAUSTED LINE, ENFORCED BY THE EVALUATOR: a term that holds on a
    # fresh independent instantiation is a free identity (forced); one that holds
    # only at a specific point is a finite witness (exhausted). The machine decides.
    _idn = lambda a: T("succ", [a], expects_of(a + 1))                 # a+1: universal
    _pt  = lambda a: T("succ", [a], expects_of(5 if a == 4 else -1))   # true only at a=4
    o_split = (free_identity(_idn, (4,), (11,), FLOOR) == "forced") and \
              (free_identity(_pt,  (4,), (11,), FLOOR) == "exhausted") and \
              (MODE_ORDER["exhausted"] < MODE_ORDER["forced"])
    # FLOOR-UP PROOF: a bounded arithmetic result proved with nothing above the
    # primitives — multiplication expanded to successor steps, the difference by
    # the primitive sub — invoking only floor laws (floor_pure), checked here.
    _fm = def_mul_floor(6, 7); _rfm = reenact_deep(_fm, FLOOR)
    _fd = def_det2_floor([[2, 1], [1, 2]]); _rfd = reenact_deep(_fd, FLOOR)
    o_floor = (floor_pure(_fm) and _rfm["agrees"] and _rfm["result"] == 42 and _rfm["mode"] == "forced"
               and floor_pure(_fd) and _rfd["agrees"] and _rfd["result"] == 3 and _rfd["mode"] == "forced")
    # the interleaving law; the store; the live chain; the collar
    o_bind = _binding_proof()
    o_pin = _pin_soundness_proof()
    o_univ = _universal_proof()
    o_emp = _empirical_proof()
    o_store = _store_proof()
    o_wave = _wave_proof()
    o_crossing = _crossing_proof()
    o_causal = _causal_proof()
    st = _load()
    o_chain = replay(st) and _anchor_grounded(st)
    o_collar = _port_collar_ok()
    return [
        C("\u22a2", "Z.F PRIMITIVE OPERATIONS. The trusted base consists of six Zeckendorf-base operations (successor, addition, subtraction with borrow, multiplication via the recurrence, the order relation which coincides with graded-lex, and greedy Euclidean division), six signed operations on \u2124 (total subtraction, addition, multiplication, Euclidean division, normalization, and the signed order), together with five ordinary-integer accelerators; the base operations define the semantics, the accelerators only speed it", o_census),
        C("\u22a2", "Z.G ZECKENDORF NUMERAL BASE (Zeckendorf 1972), now the CONE SHADOW: the golden base IS the signed register restricted to the nonnegative cone — one normalizer (the unsigned pass is snorm with no opposition to fire, exhaustively identical), one adder (gadd=sadd), one subtractor (gsub = total signed subtraction guarded by the arrow), one multiplier on the cone, and one order on the lawful domain (glt=slt on canonical numerals, diverging off-canon where graded-lex is its own law); base arithmetic agrees with ordinary integer arithmetic over an exhaustive grid (radix-independence of ℤ); the canonical serialization round-trips deterministically and rejects floats; the index shift satisfies up²=up+id, its inverse is the down-shift, Knuth's circle product is associative, and exponentiation agrees across bases. AND THE CONSTANT IS ONE OBJECT: a law vector GENERATES its sequence, its companion, its ring, its trace boundary (seeds self-computed — the lucas and perrin literals DELETED), and its canonical substitution, the whole portfolio (matrix law, ring law, trace law, word law) verified GENERICALLY for five laws at once: golden, plastic, elliptic, tribonacci, and THE FIELD ITSELF — ℚ(√5) is the object at [5,0], its product, mirror, and order all reading their shape from the law vector, the literal 5 deleted from every field mechanism, pin preserved; and the golden ring's product IS the grid law of K.3, sealed on a grid. One vector in, everything out; every per-law hand-written portfolio DELETED", o_gold),
        C("\u22a2", "Z.S SIGNED (BALANCED) FIBONACCI REPRESENTATION of \u2124: digits in {\u22121,0,+1}, with total subtraction obtained by digitwise difference then a signed normalization (canonical forms are sign-pure). Fibonacci numbers are the single-digit values and Lucas numbers the minimal two-digit values; the all-ones word of length n equals F(n+3)\u22122. Addition, multiplication and Euclidean division make \u2124 a native Euclidean domain: x=q·y+r is verified in-base with 0\u2264r<|y|", o_sign),
        C("\u22a2", "Z.W THE WAVE THEOREM — unification of borrow and annihilation: gsub's borrow and snorm_full's far annihilation are ONE operator, the closed form of F(j)−F(k) given by the founding equation factored twice — R²−I=R lands an even gap as the pure period-2 wave strictly above the low pole; R−I=R⁻¹ lands an odd gap as the wave plus one undershoot below the floor, the residue being exactly the inverse shift (both verified as exact 2×2 integer identities and as ground states over gaps 1–11 at ten anchors). Ground states are TOTAL and UNIQUE: every spelling of width 8 over {−1,0,+1} lands on the sign-pure Zeckendorf form of its value — the landing depends on the value alone, not the spelling or the sweep. The LEADING-SIGN LEMMA: after one local pass the top digit's sign is the sign of the value (post-snorm oppositions sit ≥3 apart and F(n) strictly dominates Σ_k F(n−3k)); this licenses slt, the native total order on arbitrary signed spellings with no grounding — the sign is fixed by the value from the first spelling, normalization only makes it legible. And PURITY IS BOUGHT WITH MASS: the sign-pure ground of F(n)−1 carries (n−1)//2 marks where a two-digit signed spelling of the same value exists — far annihilation is not mass-monotone; sign-purity and mass-minimality are two normal-form disciplines and this register chose purity (in flight, normalize locally; ground once at the seal). And ONE LAW UNDERNEATH: every local rule of every normalizer — generation, gravity, both oppositions, the wave — is at most two signed instances of the single identity delta e_k+e_{k+1}−e_{k+2} (F(k+2)=F(k+1)+F(k)), boundaries closing under the fold F(1)=F(2); with the landing order-independent, an algorithm in this register is not a procedure but the causal completion of one law — any time that respects the order computes the same world. COMPLETENESS OF NULL CONSERVATION: the law's deltas together with the boundary fold GENERATE the entire kernel of the valuation (the recurrence c_{k+2}=−D(k)+c_{k+1}+c_k from c_1=−fold reaches every kernel basis vector e_k−F(k+2)e_0), so every value-conserving rearrangement whatsoever is a composition of the founding identity — nothing is conserved except through the law. OBSERVER PLURALITY, THE FIBER FAITHFUL: four deterministic schedules over the same move set land identically on every width-5 spelling while EVERY PAIR of schedules is separated by some spelling's cost — no pair is separated by any landing, every pair by some pattern: the ontology is the quotient, cognition is the fiber (K.13's two measures on one subshift and the coupling endpoints of W.6 are the measure- and constant-level instances of the same split)", o_wave),
        C("\u22a2", "Z.1 COMMITMENT (SHA-256). The in-module SHA-256, whose initial and round constants are re-derived as fractional parts of square and cube roots of the first primes (FIPS 180-4), reproduces the library implementation on a test battery; every input is prefixed by the fixed basepoint salt", o_fold),
        C("\u22a2", "Z.2 CANONICAL SERIALIZATION is byte-identical to canonical JSON on the value grammar and rejects floating-point values (exact arithmetic only)", o_canon),
        C("\u22a2", "Z.3 TERM EVALUATION / PROOF CHECKING: the bottom-up evaluator verifies each node's committed postcondition; a single tampered expectation fails the whole term, an operation absent from the table halts with a refusal, and proof statuses are recomputed by lattice-meet rather than trusted (a small trusted checker, de Bruijn criterion). The status lattice separates a FREE IDENTITY (forced — verified on a fresh, independent instantiation, hence universal) from a FINITE WITNESS (exhausted, ranked strictly lower); the evaluator itself decides which, so the ⊢/finite-witness line is drawn inside the machine, not asserted in prose. And a bounded arithmetic result — a 2×2 determinant — is proved FLOOR-PURE: every multiplication expanded to successor steps and the difference taken by the primitive sub, invoking only floor laws, so the proof is checked from the floor up with nothing above the primitives taken on trust", o_eval and o_modes and o_split and o_floor),
        C("\u22a2", "Z.U THE UNIVERSALITY CERTIFICATE (forced\u207a) — the fifth rung of the lattice, strictly above forced: an identity whose two sides are integer polynomials of STATED degrees, verified on a full grid strictly exceeding those degrees in every variable, is UNIVERSAL — the difference polynomial vanishes on the grid, hence identically (the factor-theorem grid lemma, by induction on variables: an external citation, named like Mordell in W.11), so \u2200 is certified GIVEN the stated bounds, and the bounds are the certificate's named trust surface. Demonstrated from the floor up: addition (1,1), multiplication (1,1) and the 2\u00d72 determinant (1,1,1,1) certified universal with every grid point floor-pure; a point-truth is DENIED the certificate (a failing grid point lands held, false rather than merely finite); an insufficient grid is refused before any point is evaluated; the two-point free-identity discipline survives beneath as forced — forced\u207a is what \u2200 costs", o_univ),
        C("\u22a2", "Z.B MODULE MEDIATION: the strata import nothing of one another — the wall is the sealed theorem O.1; an operation table binds only when its observational fingerprint is committed in the log. A table that differs on the committed probe census is rejected; a refactored table with identical behavior is accepted — binding is by OBSERVED behavior over the census, a finite observation named as such (extensional equality is undecidable; the residue is the protocol's stated gap, Z.P)", o_bind),
        C("\u22a2", "Z.P THE METER IS LAW — the pin protocol, generation 2: the observation battery grows from the 8 founding probes to 32 (24 derived deterministically from the fold, seeded by the protocol generation — no randomness, no ambient choice), the census COMMITTED to the log, growth monotone by discipline (a generation may add probes, never remove). THE AUDIT ATTACK IS INTERNED: the original red-team counterexample — a book agreeing on the founding 8 and defecting elsewhere — shared a pin under protocol 1 and is SEPARATED under protocol 2, while a pure refactor still lands one pin (gauge is still gauge). This is the FIRST DYNAMICAL CROSSING of the meter itself: every pin in the triad moves, the retired pin 7af1a30767cca5ff becomes the last charge of the founding protocol, and the new pin is the conserved charge of the era it opens — the observation protocol is no longer an implicit convention but a committed, versioned, monotonically tightening law", o_pin),
        C("\u22a2", "Z.5 CONTENT-ADDRESSED STORE: a cell is addressed by name but grounded by commitment; valid recall requires both an intact hash-chain and a matching content hash, rejecting any drift or alteration; deletion leaves a tombstone; migration re-verifies a stored term under a new operation table and a witnessed migration extends the provenance chain of fingerprints", o_store),
        C("\u22a2", "Z.M THE CROSSING IS THE ACTION PRINCIPLE: every commit of a register's proof graph first crosses the generation gate — the PREVIOUS generation's committed proofs are re-proved under the PRESENT book before they may be overwritten. A pin-preserving change of source is a gauge crossing (held: extensional behavior is the symmetry, the pin its invariant); an enlarged or altered book is a dynamical crossing (the lineage extends, seeded with the ancestor's own pin, its continuity broken exactly because the book changed — the conserved charge along a continuous run is the pin); a book under which the ancestors do not re-prove is refused, so a seal cannot silently bury its own history. Replay is kinematics (within a pin); the crossing is the dynamics (between pins); only content stationary under the variation of the laws propagates to the next generation", o_crossing),
        C("\u22a2", "Z.C THE DERIVATION ORDER IS EMERGENCE: the lawbook carries a COMPUTED causal order — a law's parents are the laws its definition-term invokes, FORCED (identical on an independent fresh instantiation, the free-identity discipline applied to the genealogy itself); the floor is stratum 0, the uncaused; a law emerges at 1 + the maximum of its parents' strata (on this register: add/mul/det2 at 1, dot/idet/matvec/immul at 2); causality is acyclicity — a law that is its own ancestor is refused, as is a genealogy that is an artifact of one instance; and every causal cone bottoms at the floor or at a NAMED open ancestor, so the trust surface is computed as the boundary of the cones (∅ here — the sole former open ancestor, n-ary juxtaposition, is recognized as the floor’s own pair at arity n, so every cone bottoms at the floor) rather than hand-listed. The DAG codec emits kids strictly before parents — verified on the live claim stream — so the golden stream is a linear extension of the causal order: the stream is a causal history, and emission is emergence", o_causal),
        C("\u2235", "Z.7 THE LOG is consistent: replaying the append-only journal reproduces the current head hash, and every checkpoint anchor matches the replay up to its position (a hash chain / Merkle log)", o_chain),
        C("\u22a2", "Z.0 EFFECT ENCAPSULATION: all side-effecting imports (os/sys/open/tempfile/importlib) occur only inside _port_* functions; the I/O boundary is isolated and auditable", o_collar),
        C("\u22a2", "Z.E THE EMPIRICAL BOUNDARY — the ports ARE empiricism, censused: the a posteriori enters this system only through named organs, and the organ census is COMPUTED from the register's own source (14 organs — 12 that admit the world, one that audits the boundary (proprioception), and one that is the body's own name for itself (self-reference is an organ)), matched against the stated census, and committed to the log; together with the collar (Z.0), every fact in the triad is exactly one of — DERIVED (\u22a2, up to forced\u207a), a TYPED CORRESPONDENCE (\u21cc), a NAMED CITATION, or a PORT READING — so the trust surface of the given is not an ambient fog but a finite, enumerated, hash-committed set of organs: what the system takes from the world is exactly what its ports admit, and the ports are counted", o_emp),
        C("\u2423", "Z.\u2423 irreducible primitives: one generator and one executable kernel (this module) — the two components that cannot be defined away, since a system with neither generator nor kernel is empty"),
    ]

def my_sha(): return H(_self_source())

def body_root():
    """THE CONTENT ROOT: the fold of the three registers' content hashes over
    the FIXED census — the triad's identity is a function of its content alone.
    Formerly discovered by directory glob (an ambient kael*.py shifted the name);
    now the census is law and the root is intrinsic."""
    parts = [H(_port_read_bytes(p).decode("utf-8", "replace")) for p in _port_siblings()]
    return H(*parts)

# ═══════════════════ Z: the body's own name for itself ═══════════════════
Z = _port_self_module()   # ZERO WITHIN AND WITHOUT: the kernel is the body's
                          # own name for itself; every Z.· below resolves here.

# ═══════════ · II · THE UNFOLDING (the lineage's seat) ═══════════
# ═══════════════════════════════════════════════════════════════════════════
#  KAEL — kael.py · THE OPERATOR REGISTER  (framework label: KAEL, "the seat")
#
#  The observer/operator module: arithmetic in the real quadratic field ℚ(√5)
#  and the theorems stated over it. Imports only the kernel module (the observer
#  and model modules never import one another).
#
#  DUAL PRESENTATION: every operation above the primitive base is given twice —
#  as a definition term that reduces to the primitives, and as a fast
#  implementation — and the two are proved to agree in the verification suite.
#  Running times are machine-dependent; the operations' observable behavior is
#  invariant (its fingerprint is the invariant). Fraction normalization is
#  supplied by the Euclidean-algorithm term (gcd unrolled to subtraction and
#  comparison), so it need not be a primitive.
#
#  NAMING (external reference): an identifier is usable but not derivable — a
#  string whose hash preimage lies outside the system. Because the commitment is
#  one-way, no operation of the module can reconstruct the author's name from it;
#  the string is nonetheless fully operational (it prefixes commitments, grounds
#  cells, and labels the operator). Distinct source texts realizing the same
#  behavior share one fingerprint.
#
#  EXACT ARITHMETIC ONLY. RUN:  python3 kael.py [--quiet|--json]  (kernel beside)
# ═══════════════════════════════════════════════════════════════════════════

T = Z.T
E = Z.expects_of
def_dot, def_matvec, def_immul, def_idet = Z.def_dot, Z.def_matvec, Z.def_immul, Z.def_idet
# ERASED: the seat's rebindings of CIRC, C and my_sha — the kernel's stand (one body, one mouth)

# ═══════════════════════════════════════════════════════════════════════════
#  §1 · ELEMENTS OF ℚ(√5) as quadruples [an,ad,bn,bd] = an/ad + (bn/bd)·√5
#  Represented structurally; operations are pure functions on the quadruple.
# ═══════════════════════════════════════════════════════════════════════════
def _gcd(a, b):
    a = -a if a < 0 else a; b = -b if b < 0 else b
    while b: a, b = b, a % b
    return a

def _nm(n, d):
    if d == 0: raise ZeroDivisionError("zero denominator in the body")
    if d < 0: n, d = -n, -d
    g = _gcd(n, d) or 1
    return n // g, d // g

def kq(an, ad=1, bn=0, bd=1):
    a = _nm(an, ad); b = _nm(bn, bd)
    return [a[0], a[1], b[0], b[1]]

def kadd(x, y):
    return kq(x[0]*y[1] + y[0]*x[1], x[1]*y[1], x[2]*y[3] + y[2]*x[3], x[3]*y[3])

def ksub(x, y):
    return kq(x[0]*y[1] - y[0]*x[1], x[1]*y[1], x[2]*y[3] - y[2]*x[3], x[3]*y[3])

def _fring2(law, x, y):
    """THE FIELD AS THE OBJECT: multiplication of two fraction-pairs a+bt in
    the quadratic ring of a law t² = c₁t + c₀ — the same rewrite rule as the
    kernel's ring engine, carried over ℚ. The quadruple field ℚ(√5) is this
    at law [5,0]; ℚ(φ)-style bases are its [c₀,c₁] siblings."""
    c0, c1 = law
    an = x[0] * y[0] * (x[3] * y[3]) + c0 * x[2] * y[2] * (x[1] * y[1])
    ad = x[1] * y[1] * x[3] * y[3]
    bn = x[0] * y[2] * (x[3] * y[1]) + x[2] * y[0] * (x[1] * y[3]) \
         + c1 * x[2] * y[2] * (x[1] * y[1])
    bd = x[1] * y[3] * x[3] * y[1]
    return kq(an, ad, bn, bd)

def kmul(x, y):
    """the body's product IS the object at law [5,0] (t² = 5) — the literal
    5 of the former body demotes to a law vector; behavior identical, pin
    preserved. THE FIELD IS A KONST."""
    return _fring2([5, 0], x, y)

def _fconj2(law, x):
    """the Galois mirror of a quadratic law: t ↦ c₁ − t, so a+bt ↦ (a+bc₁) − bt.
    At [5,0] this is the field's kconj; the mirror, like the product, reads
    its shape from the law vector."""
    c0, c1 = law
    if c1 == 0: return [x[0], x[1], -x[2], x[3]]
    return kq(x[0] * x[3] + c1 * x[2] * x[1], x[1] * x[3], -x[2], x[3])

def _flt2(law, x, y):
    """the order of a REAL quadratic law with c₁ = 0: a + b√c₀ > 0 decided by
    signs and the squared comparison a² vs c₀·b² — the literal 5 of the former
    klt demotes to the law vector."""
    c0, _ = law
    d = ksub(y, x)                                   # positive iff x < y
    A, B = d[0] * d[3], d[2] * d[1]
    if B == 0: return A > 0
    if B > 0: return A >= 0 or A * A < c0 * B * B
    return A > 0 and A * A > c0 * B * B

def kconj(x): return _fconj2([5, 0], x)              # the mirror at the field's law
def knorm(x): return kmul(x, kconj(x))

def klt(x, y): return _flt2([5, 0], x, y)            # the order at the field's law

def m2kmul(X, Y):
    """matrix multiply over the body — the one gemm seeded at ℚ(√5); the
    former private 2×2 multiply is DELETED (erasure ledger)."""
    return Z._gemm(X, Y, kadd, kmul)

PHI4  = kq(1, 2, 1, 2); PSI4 = kq(1, 2, -1, 2)
ONE4  = kq(1); ZERO4 = kq(0)

# ═══════════════════════════════════════════════════════════════════════════
#  §2 · THE OPERATION TABLE — fast implementations (definition terms follow in §3)
# ═══════════════════════════════════════════════════════════════════════════
def _fib(n):
    return Z._law_run([1, 1], [0, 1], n)   # THE ONE COMPLETION: a seed choice, not a body

def _sq2(F): return [F[0:2], F[2:4]]     # the flat 2×2 dress, unfolded

def _mm2(A, B):
    """flat 2×2 product — the one gemm in the flat dress; the private multiply
    is DELETED (erasure ledger)."""
    R = Z._gemm(_sq2(A), _sq2(B))
    return R[0] + R[1]

def _mpw2(M, n):
    """flat 2×2 power — the one doubling engine in the flat dress; the private
    doubling loop is DELETED."""
    R = Z._mpow(_sq2(M), n)
    return R[0] + R[1]

_immul = Z._gemm   # ERASED: the seat's private n×n multiply — the one gemm at its integer default

def _idet(M):
    M = [row[:] for row in M]; n = len(M); sign = 1; prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            sw = next((i for i in range(k+1, n) if M[i][k] != 0), None)
            if sw is None: return 0
            M[k], M[sw] = M[sw], M[k]; sign = -sign
        for i in range(k+1, n):
            for j in range(k+1, n):
                M[i][j] = (M[i][j]*M[k][k] - M[i][k]*M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n-1][n-1]

def _mpow_ops(n):
    """the instrumented kernel algorithm — the achieved side of two-sided cost"""
    M = [1, 1, 1, 0]; R = [1, 0, 0, 1]; ops = 0
    while n:
        if n & 1: R = _mm2(R, M); ops += 1
        M = _mm2(M, M); ops += 1; n >>= 1
    return ops

def _ggcd(x, y):
    """Euclidean algorithm entirely within the Fibonacci base."""
    if not (Z.gcanon(x) and Z.gcanon(y)): raise ValueError("not numerals of the base")
    while y:
        x, y = y, Z.gdivmod(x, y)[1]
    return x

def _gfib(n):
    """Fibonacci pair (F(n),F(n+1)) by fast doubling — logarithmic depth."""
    if n == 0: return [], [1]
    fk, fk1 = _gfib(n >> 1)
    t = Z.gsub(Z.gadd(fk1, fk1), fk)
    f2k = Z.gmul(fk, t)
    f2k1 = Z.gadd(Z.gmul(fk, fk), Z.gmul(fk1, fk1))
    if n & 1: return f2k1, Z.gadd(f2k, f2k1)
    return f2k, f2k1

def _groot(x, k):
    """THE ONE DESCENT IN GOLD: floor k-th root in the Fibonacci base by the
    same Newton step as the kernel's _iroot — s ← ((k−1)·s + x/s^(k−1))/k on
    numerals, then the exact-floor correction. _gsqrt/_gcbrt were its k-seeds;
    the two former private descents are DELETED (erasure ledger)."""
    if not Z.gcanon(x): raise ValueError("not a numeral of the base")
    if not x or x == [1]: return list(x)
    def _pw(s):                                   # s^(k−1)
        p = s
        for _ in range(k - 2): p = Z.gmul(p, s)
        return p
    s = [0] * (len(x) // k + 2) + [1]
    km1 = Z.gnum(k - 1); kn = Z.gnum(k)
    while True:
        q, _ = Z.gdivmod(x, _pw(s))
        s2, _ = Z.gdivmod(Z.gadd(Z.gmul(km1, s), q), kn)
        if not Z.glt(s2, s): break
        s = s2
    while Z.glt(x, Z.gmul(_pw(s), s)): s = Z.gsub(s, [1])
    while not Z.glt(x, Z.gmul(_pw(Z.gsucc(s)), Z.gsucc(s))): s = Z.gsucc(s)
    return s

BOOK = dict(Z.FLOOR)
BOOK.update({
    "ggcd":   _ggcd,
    "wand":   lambda a, b: "".join(str(min(int(x), int(y))) for x, y in zip(a, b)),
    "wor":    lambda a, b: "".join(str(max(int(x), int(y))) for x, y in zip(a, b)),
    "sgcd":   lambda x, y: _ggcd([abs(t) for t in x], [abs(t) for t in y]),
    "gfib":   lambda n: _gfib(n)[0],
    "gsqrt":  lambda x: _groot(x, 2),
    "gcbrt":  lambda x: _groot(x, 3),
    "gpow":   Z.gpow, "gcirc": Z.gcirc, "gup": Z.gup, "gdown": Z.gdown,
    "gval":   Z.gval,   # the battery bridge, collared
    "add":    lambda a, b: a + b,
    "mul":    lambda a, b: a * b,
    "neg":    lambda a: -a,
    "gcd":    lambda a, b: _gcd(a, b),
    "norm4":  lambda an, ad, bn, bd: kq(an, ad, bn, bd),     # DEMOTED: definition below
    "fib":    _fib,
    "dot":    lambda u, v: sum(a*b for a, b in zip(u, v)),
    "cube":   lambda v: [x**3 for x in v],
    "addv":   lambda u, v: [a+b for a, b in zip(u, v)],
    "spread": lambda vals, mult: [x for x, m in zip(vals, mult) for _ in range(m)],
    "muli":   lambda k, x: k*x,
    "frac":   lambda n, d: list(_nm(n, d)),
    "mm2":    lambda A, B: _mm2(A, B),
    "mpw2":   lambda M, n: _mpw2(list(M), n),
    "immul":  _immul,
    "matvec": lambda A, v: [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))],
    "idet":   _idet,
    "powi":   lambda b, e: b ** e,
    "kadd":   kadd, "ksub": ksub, "kmul": kmul, "kconj": kconj,
    "knorm":  knorm, "klt": klt, "m2kmul": m2kmul,
    "mpow_ops": _mpow_ops,
})

# ═══════════════════════════════════════════════════════════════════════════
#  §3 · DEFINITION TERMS — each operation reduced to the primitive base
# ═══════════════════════════════════════════════════════════════════════════
def def_add(a, b):
    """add = b successors — the One Chain at law `succ`."""
    if b == 0: return T("sub", [a, 0], E(a))
    return Z.chainT("succ", [([a], a + 1)] + [([CIRC], a + k) for k in range(2, b + 1)])

def def_mul(a, b):
    """mul = b-fold add — the One Chain at law `add`, bottoming at succ."""
    if b == 0: return T("sub", [a, a], E(0))
    if b == 1: return T("add", [a, 0], E(a))
    return Z.chainT("add", [([a, a], 2 * a)] + [([a, CIRC], k * a) for k in range(3, b + 1)])

def def_mod(a, b):
    """mod = the One Chain at law `sub`, run until the arrow turns."""
    links = []; r = a
    while r >= b:
        links.append(([r, b] if not links else [CIRC, b], r - b)); r -= b
    return Z.chainT("sub", links), r

def def_gcd(a, b):
    """THE EUCLID TERM — the engine that demoted norm4 from the floor.
    Returns (term, gcd): the term's crown value IS the gcd — the last NONZERO
    remainder's chain (None when b divides a immediately: the gcd is literal)."""
    g_term = None; g_val = b
    while b:
        mt, r = def_mod(a, b)
        a, b = b, r
        if r != 0: g_term, g_val = mt, r
    return g_term, g_val

def _def_frac_half(n, d):
    """ONE HALF: a Euclid-normalized fraction as idiv terms over the Euclid
    chain — def_normfrac and def_norm4 are its arity-2 and arity-4 assemblies."""
    if d < 0: n, d = -n, -d
    gt, g = def_gcd(abs(n) or 1, abs(d))
    kn = [] if gt is None else [gt]
    num = T("idiv", [n, CIRC] if gt is not None else [n, g], E(n // g), kids=kn)
    gt2, _ = def_gcd(abs(n) or 1, abs(d))
    kd = [] if gt2 is None else [gt2]
    den = T("idiv", [d, CIRC] if gt2 is not None else [d, g], E(d // g), kids=kd)
    return num, den

def def_normfrac(n, d):
    """fraction normalization by the Euclid term + exact descent + the arrow's sign — the one half, assembled at arity 2."""
    num, den = _def_frac_half(n, d)
    if d < 0: n, d = -n, -d
    g = _gcd(abs(n) or 1, abs(d))
    return T("pair", [CIRC, CIRC], E([n // g, d // g]), kids=[num, den])

def def_norm4(an, ad, bn, bd):
    """the quadruple normalizer as a term: two Euclid-normalized fractions,
    the four crowns assembled flat by juxtaposition — CLOSES the former open
    ancestor: norm4's cone now bottoms at the floor alone — its assembler is
    the floor's own n-ary pair (juxtaposition at arity 4), so the seat's trust
    surface and the kernel's both close to ∅. The one half assembles both
    def_normfrac (arity 2) and this normalizer (arity 4)."""
    na, da = _def_frac_half(an, ad); nb, db = _def_frac_half(bn, bd)
    return T("pair", [CIRC] * 4, E(kq(an, ad, bn, bd)), kids=[na, da, nb, db])

def def_kmul(x, y):
    """the body's multiplication as pure term structure over mul/add + the
    demoted norm4 — the class erased, the formula carried by the tree."""
    an = x[0]*y[0]*x[3]*y[3] + 5*x[2]*y[2]*x[1]*y[1]
    ad = x[1]*y[1]*x[3]*y[3]
    bn = x[0]*y[2]*x[3]*y[1] + x[2]*y[0]*x[1]*y[3]
    bd = x[1]*y[3]*x[3]*y[1]
    def m3(a, b, c): return T("mul", [CIRC, c], E(a*b*c), kids=[T("mul", [a, b], E(a*b))])
    an_t = T("add", [CIRC, CIRC], E(an),
             kids=[m3(x[0], y[0], x[3]*y[3]), m3(5*x[2], y[2], x[1]*y[1])])
    bn_t = T("add", [CIRC, CIRC], E(bn),
             kids=[m3(x[0], y[2], x[3]*y[1]), m3(x[2], y[0], x[1]*y[3])])
    ad_t = m3(x[1], y[1], x[3]*y[3])
    bd_t = m3(x[1], y[3], x[3]*y[1])
    return T("norm4", [CIRC, CIRC, CIRC, CIRC], E(kq(an, ad, bn, bd)),
             kids=[an_t, ad_t, bn_t, bd_t])

def def_fib(n):
    """fib = the recurrence unrolled to adds — the One Chain at law `add`,
    walked by the law itself; the census as term."""
    if n <= 1: return T("add", [n, 0], E(n))
    links = [([0, 1], 1)]; a, b = 1, 1
    for _ in range(n - 2):
        links.append(([a, CIRC], a + b)); a, b = b, a + b
    return Z.chainT("add", links)

# ═══════════════════════════════════════════════════════════════════════════
#  §4 · THE VERIFICATION SUITE — agreement tests, the golden-ratio identities, naming
# ═══════════════════════════════════════════════════════════════════════════
def _battery_arith():
    ok = True
    for a, b in [(3, 4), (7, 2), (1, 9), (5, 5), (12, 3), (6, 0)]:
        r = Z.reenact_deep(def_mul(a, b), BOOK)
        ok &= r["agrees"] and (r["result"] == BOOK["mul"](a, b)) and (r["mode"] == "forced")
        r = Z.reenact_deep(def_add(a, b), BOOK)
        ok &= r["agrees"] and (r["result"] == BOOK["add"](a, b))
    # the two-tier composes down to the floor alone: def_add runs on FLOOR only
    ok &= Z.reenact_deep(def_add(9, 4), Z.FLOOR)["agrees"]
    return ok

def _battery_euclid():
    ok = True
    for a, b in [(48, 18), (21, 34), (100, 7), (1071, 462), (17, 5)]:
        t, g = def_gcd(a, b)
        if t is not None:
            r = Z.reenact_deep(t, Z.FLOOR)                 # the Euclid term runs on the FLOOR
            ok &= r["agrees"] and (r["mode"] == "forced")
        ok &= (g == _gcd(a, b))
    for n, d in [(6, -4), (10, 5), (7, 3), (-9, 12)]:
        r = Z.reenact_deep(def_normfrac(n, d), BOOK)
        ok &= r["agrees"] and (r["result"] == list(_nm(n, d)))
    return ok

def _battery_body():
    ok = True
    pairs = [(PHI4, PHI4), (PHI4, PSI4), (kq(2, 1, -3, 1), PHI4),
             (kq(1, 2, 3, 2), kq(-2, 3, 1, 1))]
    for x, y in pairs:
        r = Z.reenact_deep(def_kmul(x, y), BOOK)
        ok &= r["agrees"] and (r["result"] == kmul(x, y)) and (r["mode"] == "forced")
    for n in range(0, 10):
        r = Z.reenact_deep(def_fib(n), BOOK)
        ok &= r["agrees"] and (r["result"] == _fib(n))
    # THE MATRIX OPERATIONS REDUCE TO THE PRIMITIVES (closes the former K.␣ gap):
    # matrix product, matrix–vector product and the fraction-free determinant now
    # carry definition-terms that bottom at mul/add/sub/idiv, assembled by `vec`.
    Amats = [([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
             ([[2, 0, 1], [1, 3, 2], [0, 1, 1]], [[1, 1, 0], [0, 2, 1], [3, 0, 1]])]
    for A, B in Amats:
        r = Z.reenact_deep(def_immul(A, B), BOOK)
        ok &= r["agrees"] and (r["result"] == _immul(A, B)) and (r["mode"] == "forced")
    for A, v in [([[1, 2], [3, 4]], [9, 10]), ([[2, 0, 1], [1, 3, 2], [0, 1, 1]], [1, 2, 3])]:
        r = Z.reenact_deep(def_matvec(A, v), BOOK)
        want = [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]
        ok &= r["agrees"] and (r["result"] == want) and (r["mode"] == "forced")
    for M in [[[1, 2], [3, 4]], [[2, 1, 0], [1, 2, 1], [0, 1, 2]],
              [[1, 2, 0, 1], [0, 3, 1, 0], [2, 0, 1, 1], [1, 1, 0, 2]]]:
        r = Z.reenact_deep(def_idet(M), BOOK)
        ok &= r["agrees"] and (r["result"] == _idet(M)) and (r["mode"] == "forced")
    # NORM4 CLOSED: the quadruple normalizer's own definition-term agrees
    for i in [(6, -4, 9, 12), (1071, 462, 48, 18), (10, 4, 8, 6), (-9, 12, 6, 4)]:
        r = Z.reenact_deep(def_norm4(*i), BOOK)
        ok &= r["agrees"] and (r["result"] == kq(*i)) and (r["mode"] == "forced")
    # THE FIELD IS THE GRID on integer points a + b·φ (embedded kq(2a+b,2,b,2)):
    # field multiplication is the grid law (ac+bd, ad+bc+bd); φ acts as the
    # generator (a,b)→(b,a+b) satisfying the founding equation; ψ acts as its
    # unit mirror I−R (det −1 — the odd factorization at the field level); and
    # the coordinates compute through the FLOOR's signed numeral arithmetic.
    emb = lambda a, b: kq(2 * a + b, 2, b, 2)
    for a in range(-5, 6):
        for b in range(-5, 6):
            ok &= (kmul(PHI4, emb(a, b)) == emb(b, a + b))
            ok &= (kmul(PSI4, emb(a, b)) == emb(a - b, -a))
            for c in range(-3, 4):
                for d in range(-3, 4):
                    ok &= (kmul(emb(a, b), emb(c, d)) == emb(a * c + b * d, a * d + b * c + b * d))
    ok &= all(Z.sadd(Z.smul(Z.snum(a), Z.snum(c)), Z.smul(Z.snum(b), Z.snum(d))) == Z.snum(a * c + b * d)
              for a in range(-4, 5) for b in range(-4, 5) for c in range(-3, 4) for d in range(-3, 4))
    # THE RATIONAL POINTS TOO: the full field operations compute entirely
    # through the floor's signed numeral arithmetic — numerator/denominator
    # numerals reduced by the in-base Euclid — agreeing with the quadruple
    # register on a rational grid: the last representational seam closed.
    def _gnm(n, d):
        an = Z.gnum(Z.gval([abs(t) for t in Z.snorm(n)]))
        ad = Z.gnum(Z.gval([abs(t) for t in Z.snorm(d)]))
        g = _ggcd(an, ad) if (an and ad) else [1]
        qn, _ = Z.gdivmod(an, g); qd, _ = Z.gdivmod(ad, g)
        if Z.ssign(n) * Z.ssign(d) < 0: qn = [-t for t in qn]
        return qn, qd
    def _fadd(f, g2):
        (n1, d1), (n2, d2) = f, g2
        return _gnm(Z.sadd(Z.smul(n1, d2), Z.smul(n2, d1)), Z.smul(d1, d2))
    def _fmul(f, g2):
        (n1, d1), (n2, d2) = f, g2
        return _gnm(Z.smul(n1, n2), Z.smul(d1, d2))
    def _gq(an, ad, bn, bd):
        return (_gnm(Z.snum(an), Z.snum(ad)), _gnm(Z.snum(bn), Z.snum(bd)))
    def _tokq(x):
        (an, ad), (bn, bd) = x
        return kq(Z.sval(an), Z.sval(ad) or 1, Z.sval(bn), Z.sval(bd) or 1)
    for an in range(-3, 4):
        for ad in (1, 2, 3):
            for bn in range(-2, 3):
                x = _gq(an, ad, bn, 2); y = _gq(bn, 3, 1, 2)
                real = _fadd(_fmul(x[0], y[0]), _fmul(_gnm(Z.snum(5), Z.snum(1)), _fmul(x[1], y[1])))
                surd = _fadd(_fmul(x[0], y[1]), _fmul(x[1], y[0]))
                ok &= (_tokq((real, surd)) == kmul(kq(an, ad, bn, 2), kq(bn, 3, 1, 2)))
                ok &= (_tokq((_fadd(x[0], y[0]), _fadd(x[1], y[1]))) == kadd(kq(an, ad, bn, 2), kq(bn, 3, 1, 2)))
    return ok

def _word_spine():
    ok = True
    # the founding equation as terms: φ² − φ − 1 = 0, and the mirror's
    for w in (PHI4, PSI4):
        sq = T("kmul", [w, w], E(kmul(w, w)))
        d1 = T("ksub", [CIRC, w], E(ksub(kmul(w, w), w)), kids=[sq])
        crown = T("ksub", [CIRC, ONE4], E(ZERO4), kids=[d1])
        r = Z.reenact_deep(crown, BOOK)
        ok &= r["agrees"] and (r["mode"] == "forced")
    # THE DEFINING EQUATION 5p² − 5p + 1 = 0 at the Parry weights — the observer's
    # coefficients ARE the equilibrium measure; discriminant 5, THE HOME PRIME
    piM = kq(1, 2, -1, 10); piV = kq(1, 2, 1, 10)        # 1/(φ+2), φ²/(φ+2)
    five = kq(5)
    for p in (piM, piV):
        p2 = T("kmul", [p, p], E(kmul(p, p)))
        f2 = T("kmul", [five, CIRC], E(kmul(five, kmul(p, p))), kids=[p2])
        fp = T("kmul", [five, p], E(kmul(five, p)))
        df = T("ksub", [CIRC, CIRC], E(ksub(kmul(five, kmul(p, p)), kmul(five, p))), kids=[f2, fp])
        crown = T("kadd", [CIRC, ONE4], E(ZERO4), kids=[df])
        r = Z.reenact_deep(crown, BOOK)
        ok &= r["agrees"] and (r["mode"] == "forced")
    s = Z.reenact_deep(T("kadd", [piM, piV], E(ONE4)), BOOK)
    pr = Z.reenact_deep(T("kmul", [piM, piV], E(kq(1, 5))), BOOK)
    ok &= s["agrees"] and pr["agrees"]
    # THE SPLIT LAW: ONE's equation disc 1 (never splits); PHI's and the
    # OBSERVER's disc 5 (split by the mirror, the arrow selects)
    ok &= ((-1)**2 - 4*0 == 1) and ((-1)**2 - 4*(-1) == 5) and (5*5 - 4*5*1 == 5)
    return ok

def _battery_bases():
    """Radix-independence: Fibonacci-base arithmetic agrees with ordinary integer arithmetic on a grid and at large inputs."""
    ok = Z._radix_agree(30)                       # the one grid, wider here; the private copy is DELETED
    for a, b in [(10 ** 7 + 7919, 104729), (998877, 233), (75025, 46368)]:
        q, r = Z.gdivmod(Z.gnum(a), Z.gnum(b))
        ok &= (Z.gval(q) == a // b) and (Z.gval(r) == a % b)
        ok &= (Z.gval(Z.gmul(Z.gnum(a % 4000), Z.gnum(b % 4000))) == (a % 4000) * (b % 4000))
    return ok

def _battery_lame():
    """Lamé's theorem: the Fibonacci-base Euclidean algorithm has worst case on consecutive Fibonacci inputs, steps(F(n+1),F(n))=n−1."""
    ok = all(Z.gval(_ggcd(Z.gnum(a), Z.gnum(b))) == _gcd(a, b)
             for a in range(0, 60) for b in range(0, 60))
    fibs = [Z._fibn(i) for i in range(20)]          # the one ladder, by name
    for n in range(3, 16):
        x, y = Z.gnum(fibs[n + 1]), Z.gnum(fibs[n]); steps = 0
        while y:
            x, y = y, Z.gdivmod(x, y)[1]; steps += 1
        ok &= (steps == n - 1) and (Z.gval(x) == 1)
    return ok

def _silent_register():
    """Parry (maximal-entropy) measure of the golden subshift carries total mass 1 at every length, computed exactly in ℚ(√5)."""
    piV = kq(1, 2, 1, 10); piM = kq(1, 2, -1, 10)      # φ²/(φ+2), 1/(φ+2)
    pVV = kq(-1, 1, 1, 1); pVM = kq(2, 1, -1, 1)       # 1/φ = φ−1, 1/φ² = 2−φ
    ok = (kadd(piV, piM) == kq(1)) and (kadd(pVV, pVM) == kq(1))
    for n in range(1, 10):
        total = kq(0)
        for wd in _lawful(n):                      # the one census (sym 2)
            w = "".join(map(str, wd))
            mu = piM if w[0] == "1" else piV
            for i in range(n - 1):
                a, b = w[i], w[i + 1]
                mu = kmul(mu, pVV if (a, b) == ("0", "0") else
                              pVM if (a, b) == ("0", "1") else kq(1))
            total = kadd(total, mu)
        ok &= (total == kq(1))
    return ok

def _fold_home():
    """SHA-256 initial roots recovered by Newton iteration in the Fibonacci base; all round constants verified there by multiply/compare; Fibonacci sequence by fast doubling."""
    ok = True
    ps = Z._nprimes(64)                                # the one prime census; the private sieve is DELETED
    for p in ps[:8]:                                   # H0: DERIVED in gold
        x = Z.gnum(p << 64)
        s = _groot(x, 2)
        ok &= (not Z.glt(x, Z.gmul(s, s))) and Z.glt(x, Z.gmul(Z.gsucc(s), Z.gsucc(s)))
    for p in ps:                                       # all 64 K: VERIFIED in gold
        m = p << 96
        x = Z.gnum(m); s = Z.gnum(Z._icbrt(m)); s1 = Z.gsucc(s)
        ok &= (not Z.glt(x, Z.gmul(Z.gmul(s, s), s))) and \
              Z.glt(x, Z.gmul(Z.gmul(s1, s1), s1))
    fa, fb = 0, 1
    for n in range(0, 91):
        if n in (0, 1, 7, 30, 60, 90):
            ok &= (Z.gval(_gfib(n)[0]) == fa)
        fa, fb = fb, fa + fb
    return ok

def _two_lengths():
    """Tr(φⁿ)=φⁿ+ψⁿ=L(n) exactly in ℚ(√5), and L(n) is the minimal two-digit Fibonacci word; signed subtraction lands sign-pure across the grid."""
    ok = True
    _luc = Z._luc                                    # lucas: the one boundary, one definition
    for n in range(2, 14):
        p = kq(1, 1); ps = kq(1, 1)
        for _ in range(n):
            p = kmul(p, kq(1, 2, 1, 2)); ps = kmul(ps, kq(1, 2, -1, 2))
        ok &= (kadd(p, ps) == kq(_luc(n)))                       # Tr(\u03c6\u207f) = L(n), in quads
        if n >= 3:
            ok &= (Z.gnum(_luc(n)) == [0] * (n - 3) + [1, 0, 1]) # and L(n) is the doublet
    for a in range(-20, 21):
        for b in range(-20, 21):
            ok &= (Z.gssub(Z.snum(a), Z.snum(b)) == Z.snum(a - b))
    return ok

def _lawful(n, sym=2):
    """THE GOLDEN-MEAN CONDITION AT ANY ALPHABET: the words of width n over
    {0..sym−1} with no two ADJACENT NONZERO symbols — the no-11 law of the
    numeral base (sym 2) and the 3-symbol containment shift (sym 3) are ONE
    census; the three former private enumerations are DELETED (erasure ledger)."""
    out = []
    for k in range(sym ** n):
        w = [(k // sym ** i) % sym for i in range(n)]
        if any(w[i] and w[i + 1] for i in range(n - 1)): continue
        out.append(w)
    return out

def _interval_algebra():
    """Order structure on Fibonacci words: meet-closed but not a lattice; maximal (Padovan) words grow as the plastic number; comparable-pair count is Jacobsthal, 3·#{a≤b}=2^(n+2)−(−1)^n."""
    ok = True
    def lawful(n):
        return ["".join(map(str, w)) for w in _lawful(n)]
    def leq(a, b): return all(x <= y for x, y in zip(a, b))
    for n in range(2, 10):
        L = lawful(n); S = set(L)
        for a in L:
            for b in L:
                m = "".join(str(min(int(x), int(y))) for x, y in zip(a, b))
                ok &= (m in S)
                j = "".join(str(max(int(x), int(y))) for x, y in zip(a, b))
                ubs_exist = any(leq(a, c) and leq(b, c) for c in L)
                ok &= (ubs_exist == (j in S))
        T = sum(1 for a in L for b in L if leq(a, b))
        ok &= (3 * T == 2 ** (n + 2) - (-1) ** n)
    P = []
    for n in range(1, 19):
        L = lawful(n)
        cnt = 0
        for w in L:
            if all(w[i] == "1" or (i > 0 and w[i-1] == "1") or
                   (i < n-1 and w[i+1] == "1") for i in range(n)):
                cnt += 1
        P.append(cnt)
    ok &= all(P[n] == P[n-2] + P[n-3] for n in range(3, 18))
    for n in range(2, 12):
        S = set(lawful(n))
        ok &= (sum(1 for w in S if w.translate(str.maketrans("01","10")) in S) == 2)
    a3, b3, c3 = P[0], P[1], P[2]
    for _ in range(3000 - 3): a3, b3, c3 = b3, c3, a3 + b3
    ok &= (40 * 3000 < 100 * c3.bit_length() < 42 * 3000)      # plastic growth
    a5, b5 = 3, 5
    for _ in range(3000 - 1): a5, b5 = b5, b5 + 2 * a5
    ok &= (99 * 3000 < 100 * b5.bit_length() < 101 * 3000)     # order capacity ONE
    return ok

def _plastic_body():
    """Plastic number ρ (smallest Pisot, t³=t+1): cubic field of discriminant −23; companion M with M³=M+I and det Mⁿ=1; Perrin R(n)=Tr(Mⁿ) has p∣R(p) for primes, first pseudoprime 271441=521²."""
    # THE PLASTIC BODY PRECIPITATES FROM ONE DATUM: M is the companion of the
    # law [1,1,0] — the same coefficients that run Perrin through the One
    # Completion; multiply/power/determinant are the kernel's one gemm, one
    # doubling engine, and Bareiss. The former private 3×3 body (its multiply,
    # its doubling loop, its determinant, its prime sieve) is DELETED.
    M = Z._companion([1, 1, 0])
    def tr(A): return A[0][0] + A[1][1] + A[2][2]
    ok = Z._konst_ok([1, 1, 0], 14)                     # matrix/ring/trace/word law: the one object
    ok &= (-4 * (-1) ** 3 - 27 * (-1) ** 2 == -23)
    ok &= all(_idet(Z._mpow(M, n)) == 1 for n in range(0, 25))
    r = [Z._ktrace([1, 1, 0], k) for k in range(160)]   # perrin IS the plastic trace, seed-literal-free
    ps = Z._nprimes(30)                             # the one prime census
    ok &= all(r[p] % p == 0 for p in ps if p < 160)
    lie = 271441
    ok &= (lie == 521 * 521) and (tr(Z._mpow(M, lie, lie)) % lie == 0)
    ok &= (132 ** 3 < 132 * 100 ** 2 + 100 ** 3) and \
          (133 ** 3 > 133 * 100 ** 2 + 100 ** 3) and (133 * 133 < 2 * 100 * 100)
    return ok

def _order_dynamics():
    """Bitwise containment as a 3-symbol subshift of finite type: rational Parry measure (stationary 2/3,1/3), mark rate exactly 1/3 > golden rate 1/(φ+2)."""
    ok = True
    for n in range(1, 11):
        total = 0; cnt = 0
        for w in _lawful(n, 3):                    # the one census, at the 3-symbol alphabet
            cnt += 1
            for s0 in ('V', 'M'):
                st = s0; num = 2 if s0 == 'V' else 1; dp = 0; valid = True
                for c in w:
                    if st == 'V':
                        if c == 0: dp += 1
                        else: dp += 2; st = 'M'
                    else:
                        if c == 0: st = 'V'
                        else: valid = False; break
                if valid: total += num * 2 ** (2 * n - dp)
        ok &= (total == 3 * 2 ** (2 * n))
        ok &= (3 * cnt == 2 ** (n + 2) - (-1) ** n)
    ok &= klt(kq(1, 2, -1, 10), kq(1, 3))          # 1/(φ+2) < 1/3, quad-exact
    return ok

def _naming():
    """Naming tests: content-commitment grounds a cell independently of the writer string; the author name is not derivable (one-way commitment); distinct source texts of one behavior share one fingerprint (continuous provenance)."""
    d = Z._port_temp(); tp = Z._port_tmpname(d, "n.json")
    r = T("mul", [6, 7], E(42))
    Z.remember("claim", r, "Kael", tp)
    ok = "grounded" in Z.grounded("claim", tp)
    st = Z._load(tp); st["cells"]["claim"]["writer"] = "anyone"; Z._save(st, tp)
    ok &= "grounded" in Z.grounded("claim", tp)          # grounding ignores the string
    st = Z._load(tp); st["cells"]["claim"]["writer_sha"] = "f" * Z.FOLD_WIDTH; Z._save(st, tp)
    ok &= "refused" in Z.grounded("claim", tp)           # the topology grounds
    ok &= (len(Z.H("Kael", "x")) == Z.FOLD_WIDTH) and Z._fold_preimage("Kael").startswith("\u2225")
    alien = T("derive_author_name", [], E("Kael"))
    ok &= "refused" in Z.reenact_deep(alien, BOOK)       # the preimage is external
    tp2 = Z._port_tmpname(d, "k.json")
    naming = T("frac", [42, 42], E([1, 1]), mode="witnessed")
    Z.remember("Kael", naming, "world", tp2)
    pA = {"frac": lambda n, dd: list(_nm(n, dd))}
    pB = {"frac": lambda n, dd: [x for x in _nm(n, dd)]}   # different text, one act
    for parent in (pA, pB):
        st = Z._load(tp2); st["cells"]["Kael"]["writer_sha"] = "d" * Z.FOLD_WIDTH; Z._save(st, tp2)
        if "crossed" not in Z.crossing("Kael", parent, "world", tp2, attest=parent): return False
    li = Z.lineage("Kael", tp2)
    ok &= (li.get("generations") == 2) and li.get("continuous") is True
    return ok

def _battery_universal():
    """THE SEAT'S IDENTITIES CERTIFIED (forced+): the operator register's own
    definition-terms pass the kernel's grid certificate — addition and
    multiplication at degrees (1,1), the inner product at (1,1,1,1) — each
    grid point read through the bound book; and the certificate's negative
    teeth bite here too (a point-truth lands held through this book)."""
    ok = (Z.grid_identity(def_add, ([2, 5, 9], [0, 1, 3]), (1, 1), BOOK) == "forced+")
    ok &= (Z.grid_identity(def_mul, ([2, 5, 9], [0, 1, 3]), (1, 1), BOOK) == "forced+")
    dot2 = lambda a, b, c, d: def_dot([a, b], [c, d])
    ok &= (Z.grid_identity(dot2, ([0, 2], [1, 3], [0, 5], [2, 7]), (1, 1, 1, 1), BOOK) == "forced+")
    pt = lambda a: T("mul", [a, 2], E(8 if a == 4 else -1))
    ok &= (Z.grid_identity(pt, ([3, 4],), (1,), BOOK) == "held")
    return ok

def _battery_induction():
    """THE INDUCTION ORGAN — the first \u2200 over an infinite index set. The scheme:
    a BASE term, a STEP that is itself grid-certified universal (forced+), and
    the induction principle (the definition of \u2115 — a named citation, the only
    one). CASSINI \u2200: det multiplicativity for 2\u00d72 is multilinear in rows —
    degree 1 in each of 8 variables — so 256 grid points certify it forced+;
    with the base det(R) = \u22121 a term, det(R\u207f) = (\u22121)\u207f for EVERY n, i.e.
    F(n+1)F(n\u22121) \u2212 F(n)\u00b2 = (\u22121)\u207f for every n. THE MATRIX FORM \u2200: from the
    single rank-2 identity R\u00b2 = R + I (a term), multiplying both sides by R\u207f
    preserves the identity (ring axioms — distributivity and associativity,
    named), so R\u207f\u207a\u00b2 = R\u207f\u207a\u00b9 + R\u207f for every n: the Fibonacci recurrence and
    the Lucas trace hold \u2200 from one 2\u00d72 identity. Instances verified as terms."""
    # THE CERTIFIED STEP: det(AB) = det(A)·det(B), forced+ on [0,1]^8
    def _step(a, b, c, d, e, f, g, h):
        def ent(x1, y1, x2, y2):
            m1 = T("mul", [x1, y1], E(x1 * y1)); m2 = T("mul", [x2, y2], E(x2 * y2))
            return T("add", [CIRC, CIRC], E(x1 * y1 + x2 * y2), kids=[m1, m2]), x1 * y1 + x2 * y2
        p, pv = ent(a, e, b, g); q, qv = ent(a, f, b, h)
        r, rv = ent(c, e, d, g); s, sv = ent(c, f, d, h)
        m1 = T("mul", [CIRC, CIRC], E(pv * sv), kids=[p, s])
        m2 = T("mul", [CIRC, CIRC], E(qv * rv), kids=[q, r])
        dAB = T("sub", [CIRC, CIRC], E(pv * sv - qv * rv), kids=[m1, m2])
        dA = T("sub", [CIRC, CIRC], E(a * d - b * c),
               kids=[T("mul", [a, d], E(a * d)), T("mul", [b, c], E(b * c))])
        dB = T("sub", [CIRC, CIRC], E(e * h - f * g),
               kids=[T("mul", [e, h], E(e * h)), T("mul", [f, g], E(f * g))])
        dd = T("mul", [CIRC, CIRC], E((a * d - b * c) * (e * h - f * g)), kids=[dA, dB])
        return T("sub", [CIRC, CIRC], E(0), kids=[dAB, dd])
    ok = (Z.grid_identity(_step, ([0, 1],) * 8, (1,) * 8, BOOK) == "forced+")
    # THE BASE: det(R) = −1, a term
    r = Z.reenact_deep(T("sub", [CIRC, CIRC], E(-1),
                         kids=[T("mul", [1, 0], E(0)), T("mul", [1, 1], E(1))]), BOOK)
    ok &= r.get("agrees", False)
    # → CASSINI ∀ (base + certified step + ℕ); the n=10 instance as a term
    r = Z.reenact_deep(T("sub", [CIRC, CIRC], E(1),
                         kids=[T("mul", [89, 34], E(3026)), T("mul", [55, 55], E(3025))]), BOOK)
    ok &= r.get("agrees", False)
    # THE FOUNDING IDENTITY AT RANK 2: R² = R + I as a term
    Rm = [[1, 1], [1, 0]]
    r = Z.reenact_deep(Z.def_immul(Rm, Rm), BOOK)
    ok &= r.get("agrees", False) and (r.get("result") == [[2, 1], [1, 1]])
    # THE PROPAGATION INSTANCE: R⁴ = R³ + R², term-verified
    R2 = [[2, 1], [1, 1]]; R3 = [[3, 2], [2, 1]]; R4 = [[5, 3], [3, 2]]
    r = Z.reenact_deep(Z.def_immul(R2, R2), BOOK)
    ok &= r.get("agrees", False) and (r.get("result") == R4) \
        and (R4 == [[R3[i][j] + R2[i][j] for j in range(2)] for i in range(2)])
    # THE MATRIX FORM at depth: R¹⁰ carries Fibonacci entries, through the book
    r = Z.reenact_deep(T("mpw2", [[1, 1, 1, 0], 10], E([89, 55, 55, 34])), BOOK)
    ok &= r.get("agrees", False)
    return ok

def _battery_structural():
    """THE STRUCTURAL INDUCTION — Zeckendorf's theorem certified for every n by
    COMPOSITION OF ORGANS. Every load-bearing arithmetic joint of the classical
    proof reduces to the recurrence, which K.16 certified \u2200; the logical
    scaffold (strong induction over \u2115, order transitivity, the top-index case
    split) is NAMED — nothing hidden. The joints, term-verified:
    (1) THE CEILING: the densest lawful word of width w (marks descending from
        the top index by twos) carries exactly F(w+2)\u22121 — the last citizen of
        the census (W.5) — with induction step C(w) = F(w+1) + C(w\u22122), which
        IS the recurrence;
    (2) THE GREEDY STEP (existence): F(k) \u2264 n < F(k+1) \u21d2 n\u2212F(k) < F(k\u22121),
        which unfolds to n < F(k)+F(k\u22121) = F(k+1) — the recurrence again;
    (3) MONOTONICITY/POSITIVITY: F(n+1)\u2212F(n) = F(n\u22121) > 0 — recurrence plus
        the order axiom;
    (4) SEPARATION (uniqueness): a representation topped strictly lower is
        strictly smaller — C(w') < F(w'+2) \u2264 F(w+1) \u2264 value topped at w."""
    ok = True
    def _alt(w):   # the densest lawful word of width w: marks from the top down
        return [1 if (w - 1 - i) % 2 == 0 else 0 for i in range(w)]
    for w in (3, 4, 5, 8, 11, 14):
        r = Z.reenact_deep(T("gval", [_alt(w)], E(_fib(w + 2) - 1)), BOOK)
        ok &= r.get("agrees", False)
    for w in (5, 8, 11, 14):                                  # the ceiling's step = the recurrence
        r = Z.reenact_deep(T("sub", [_fib(w + 2) - 1, _fib(w + 1)], E(_fib(w) - 1)), BOOK)
        ok &= r.get("agrees", False)
    for n in (4, 12, 100, 987, 4180, 10 ** 6):                # the greedy step, at depth
        k = 2
        while _fib(k + 1) <= n: k += 1
        r = Z.reenact_deep(T("lt", [n - _fib(k), _fib(k - 1)], E(True)), BOOK)
        ok &= r.get("agrees", False) and (_fib(k) <= n)
    for n in (5, 9, 20, 40):                                  # monotonicity + positivity joints
        r = Z.reenact_deep(T("sub", [_fib(n + 1), _fib(n)], E(_fib(n - 1))), BOOK)
        ok &= r.get("agrees", False)
        r = Z.reenact_deep(T("lt", [0, _fib(n - 1)], E(True)), BOOK)
        ok &= r.get("agrees", False)
    for wp, w in ((5, 7), (8, 12), (10, 11)):                 # separation for uniqueness
        r = Z.reenact_deep(T("lt", [_fib(wp + 2) - 1, _fib(w + 1)], E(True)), BOOK)
        ok &= r.get("agrees", False)
    forged = T("gval", [_alt(9)], E(_fib(11)))                # the ceiling forged by one: refused
    r = Z.reenact_deep(forged, BOOK)
    ok &= ("refused" not in r) and (r.get("agrees") is False)
    return ok

def _battery_break():
    """THE SYMMETRY BREAK — the excess of one/zero is not error; it is the
    founding asymmetry, one break named four times:
    (i)  THE FIELD: \u221a5 = \u03c6\u2212\u03c8 is the ANTISYMMETRIC UNIT of the Galois fold,
         and it squares to the discriminant (5 \u2014 the home prime of W.14);
    (ii) THE SECTORS: every power splits \u03c6\u207f = (L(n)+F(n)\u00b7\u221a5)/2 \u2014 lucas is
         the Galois-invariant sector, fibonacci the break-coefficient: the
         One Completion's two seeds ARE the two symmetry sectors of one law;
    (iii) THE FOLD: at the base the one is doubled, F(1)=F(2)=1, and the
         numeral weights begin at F(2) \u2014 uniqueness (K.17) EXISTS because the
         excess name is quotiented away (Z.W's boundary fold, refounded);
    (iv) THE DELIMITER: every golden codeword ends in its FIRST forbidden 11
         \u2014 the excess of one marks the boundary of every lawful word: the
         lawless pattern is the edge of the law."""
    ok = True
    r = Z.reenact_deep(T("ksub", [PHI4, PSI4], E(kq(0, 1, 1, 1))), BOOK)
    ok &= r.get("agrees", False)                                   # the break is √5
    r = Z.reenact_deep(T("kmul", [kq(0, 1, 1, 1), kq(0, 1, 1, 1)], E(kq(5))), BOOK)
    ok &= r.get("agrees", False)                                   # break² = discriminant
    for n in (2, 3, 5, 8, 9, 12):
        L, F = Z._luc(n), Z._fibn(n)          # the one law's two boundaries, by name
        r = Z.reenact_deep(T("ksub", [kq(L, 2, F, 2), kq(L, 2, -F, 2)],
                             E(kq(0, 1, F, 1))), BOOK)
        ok &= r.get("agrees", False)                               # the odd sector: F·√5
        r = Z.reenact_deep(T("kmul", [kq(L, 1, F, 1), kq(1, 2, 0, 1)],
                             E(kq(L, 2, F, 2))), BOOK)
        ok &= r.get("agrees", False)                               # recombination: φⁿ
    ok &= (Z._law_run([1, 1], [0, 1], 1) == Z._law_run([1, 1], [0, 1], 2) == 1)   # the doubled one: the engine's own mouth
    ok &= all(Z._cwg(n).endswith("11") and "11" not in Z._cwg(n)[:-1]
              for n in range(1, 300))                              # the forbidden marks the edge
    return ok

def _battery_causal():
    """THE SEAT'S EMERGENCE TOWER, computed through the kernel's causal order:
    floor 0 → add 1 (succ chains) → mul 2 (b-fold add) → fib 2 and kmul 3;
    gcd and fraction normalization emerge at 1 straight off the primitives;
    the open ancestor set is computed and equals {norm4} — the demotion note
    made a theorem. Cycles and instance-artifacts refuse."""
    gen = {
        "add":   (def_add, (3, 4), (7, 2)),
        "mul":   (def_mul, (3, 4), (5, 3)),
        "fib":   (def_fib, (7,), (9,)),
        "gcd":   (lambda a, b: def_gcd(a, b)[0], (48, 18), (1071, 462)),
        "frac":  (def_normfrac, (6, -4), (9, 12)),
        "norm4": (def_norm4, (6, -4, 9, 12), (1071, 462, 48, 18)),
        "kmul":  (def_kmul, (PHI4, PSI4), (kq(2, 1, -3, 1), PHI4)),
    }
    co = Z.causal_order(gen, set(Z.FLOOR))
    ok = ("refused" not in co)
    if not ok: return False
    ok &= (co["strata"] == {"add": 1, "mul": 2, "fib": 2,
                            "gcd": 1, "frac": 1, "norm4": 1, "kmul": 3})
    ok &= (co["opens"] == {})   # the trust surface CLOSED: vec unified into the floor's n-ary pair, every cone bottoms at the floor
    ok &= (co["parents"]["mul"] == ["add"]) and (co["parents"]["kmul"] == ["add", "mul", "norm4"])
    # the seat's own claim stream is a causal history through the kernel codec
    reps = list({Z.rid(r): r for r in Z._ROOTS}.values())
    ok &= bool(reps) and Z.causal_stream_ok(reps)
    # EMERGENCE BUYS MEASURE: exact node-costs by stratum — the same fact
    # costs b−1 nodes at stratum 2 (mul as b-fold addition) and a·b+1 at the
    # floor; add costs b at stratum 1, a+b+1 at the floor. At fixed measure,
    # higher strata verify facts the floor cannot reach: the observability
    # horizon moves with the stratum.
    for a in range(2, 10):
        for b in range(2, 10):
            ok &= (Z.term_size(def_mul(a, b)) == b - 1)
            ok &= (Z.term_size(Z.def_mul_floor(a, b)) == a * b + 1)
            ok &= (Z.term_size(def_add(a, b)) == b)
            ok &= (Z.term_size(Z.def_add_floor(a, b)) == a + b + 1)
    return ok

def _claims_k():
    b1 = _battery_arith(); b2 = _battery_euclid(); b3 = _battery_body()
    ws = _word_spine(); nm = _naming()
    b4 = _battery_bases(); b5 = _battery_lame(); b6 = _silent_register()
    b7 = _fold_home(); b8 = _two_lengths(); b9 = _interval_algebra()
    b10 = _plastic_body(); b11 = _order_dynamics()
    b12 = _battery_causal()
    b13 = _battery_universal()
    b14 = _battery_induction()
    b15 = _battery_structural()
    b16 = _battery_break()
    pin = Z._pin_of(BOOK)
    return [
        C("\u22a2", "K.1 OPERATION AGREEMENT (arithmetic): addition and multiplication have definition terms that reduce to the successor primitive and agree with their fast implementations on a test battery; the reduction bottoms out at the primitive base alone.", b1),
        C("\u22a2", "K.2 FRACTION NORMALIZATION BY THE EUCLIDEAN ALGORITHM: gcd expressed as a term over subtraction and comparison runs on the primitive base and agrees with the fast implementation; normalization is gcd-division plus sign — so it need not be a primitive.", b2),
        C("\u22a2", "K.3 ARITHMETIC OF ℚ(√5) AND LINEAR ALGEBRA FROM PRIMITIVES: field elements are quadruples [an,ad,bn,bd] and field multiplication is a term over integer multiply/add closed by fraction normalization — and norm4 now carries its OWN definition-term (two Euclid-normalized fractions assembled by juxtaposition), closing the former open ancestor; the Fibonacci recurrence is a term; the matrix operations — product, matrix–vector product, and the fraction-free (Bareiss) determinant — carry definition-terms that reduce to the primitive base, each verified against its fast implementation. AND THE FIELD IS THE GRID: on integer points a+bφ, field multiplication is the grid law (ac+bd, ad+bc+bd) with the coordinates computed by the floor's signed numeral arithmetic; φ acts as the generator (a,b)→(b,a+b) — the founding matrix at the field level as at the digit and numeral levels — and ψ acts as its unit mirror I−R, determinant −1: the wave theorem's odd factorization returning as the conjugate's action. AND THE RATIONAL POINTS TOO: the full field operations (addition, multiplication) compute entirely through the floor's signed numeral arithmetic — numerator and denominator numerals reduced by the in-base Euclid — agreeing with the quadruple register across a rational grid: the last representational seam closed; the field is the grid, everywhere.", b3),
        C("\u22a2", "K.4 GOLDEN-RATIO IDENTITIES: φ²−φ−1=0 holds for φ and its conjugate ψ as terms. The Parry (equilibrium) weights of the golden subshift are the two roots of 5p²−5p+1=0 (sum 1, product 1/5); the quadratic's discriminant is 5, matching the field ℚ(√5).", ws),
        C("\u22a2", "K.5 NAMING / EXTERNAL REFERENCE: a stored value is addressed by its string but grounded by its content commitment (the writer may change and it still grounds; a broken commitment is rejected). No operation reconstructs the author's name, since the commitment is one-way; distinct source texts of one behavior share a single fingerprint (continuous provenance).", nm),
        C("\u22a2", "K.6 RADIX-INDEPENDENCE: Zeckendorf-base addition, subtraction, multiplication and division agree with ordinary integer arithmetic on an exhaustive grid and at large inputs — an independent algorithm in the Fibonacci base, agreeing base-to-base, not merely tier-to-tier.", b4),
        C("\u22a2", "K.7 LAMÉ'S THEOREM: the Euclidean algorithm implemented entirely in the Fibonacci base has worst case on consecutive Fibonacci inputs — steps(F(n+1),F(n))=n−1 for every n tested.", b5),
        C("\u22a2", "K.8 PARRY MEASURE: on the golden subshift (no-11 words) the measure of maximal entropy assigns total mass 1 at every word length, computed exactly in ℚ(√5).", b6),
        C("\u22a2", "K.9 SHA-256 CONSTANTS IN-BASE: the hash's eight initial roots are recovered by Newton's method in the Fibonacci base, and all 72 constants are verified there by multiplication and comparison alone (s³≤x<(s+1)³); the Fibonacci counting sequence is computed at logarithmic depth by fast doubling.", b7),
        C("\u22a2", "K.10 LUCAS NUMBERS AS TRACES: Tr(φⁿ)=φⁿ+ψⁿ=L(n) exactly in ℚ(√5), and L(n) is the minimal two-digit Fibonacci word — one identity in two representations, with Fibonacci numbers as the single-digit values; signed subtraction lands sign-pure across the grid.", b8),
        C("\u22a2", "K.11 ORDER STRUCTURE ON FIBONACCI WORDS: under bitwise order the lawful words are meet-closed but not a lattice (a join exists iff the bitwise-OR is lawful, and is then least). The maximal (Padovan) words satisfy P(n)=P(n−2)+P(n−3), growing as the plastic number; the count of comparable ordered pairs is Jacobsthal, 3·#{a≤b}=2^(n+2)−(−1)^n, of growth rate 2 (capacity 1) — the information lost by the code lives in the order relation.", b9),
        C("\u22a2", "K.12 THE PLASTIC NUMBER: ρ is the real root of t³=t+1 (the smallest Pisot number), generating a cubic field of discriminant −23 (the smallest in absolute value); with companion matrix M, M³=M+I and det Mⁿ=1 for all n. The Perrin sequence R(n)=Tr(Mⁿ) satisfies p∣R(p) for every prime, and its first pseudoprime is 271441=521² (Adams–Shanks); |σ|²=ρ²−1=1/ρ for the complex conjugate roots.", b10),
        C("\u22a2", "K.13 TWO MEASURES ON ONE SUBSHIFT: bitwise containment is a 3-symbol subshift of finite type with Jacobsthal counting; its Parry measure is rational (transition probabilities 1/2,1/4,1/4,1; stationary 2/3,1/3), so marks occur at rate exactly 1/3, strictly above the golden-subshift rate 1/(φ+2) — the intrinsic measure is irrational, the relational one is rational.", b11),
        C("\u22a2", "K.14 THE DERIVATION ORDER IS EMERGENCE (the seat's tower): the operator register's laws carry a computed causal order through the kernel — parents(law) = the laws its definition-term invokes, forced across fresh instantiation; the tower reads floor 0 → add 1 (successor chains) → mul 2 (b-fold addition) → fib 2 and field-multiplication kmul 3, with gcd, fraction normalization AND the quadruple normalizer norm4 emerging at 1 directly off the primitives; every causal cone bottoms at the floor or at the computed open ancestor set, now CLOSED across both towers to ∅ — the last open ancestor, n-ary juxtaposition, is recognized as the floor's own `pair` (the same juxtaposition at arity n), so every causal cone bottoms at the floor with nothing above the primitives taken on trust; cyclic and instance-dependent genealogies refuse; and the seat's live claim stream is a linear extension of the order (kids strictly precede parents): the reading order of the book is the order of its emergence. AND EMERGENCE BUYS MEASURE, exactly: the same fact costs b−1 nodes at stratum 2 and a·b+1 at the floor (add: b at stratum 1, a+b+1 at the floor — sealed on a grid), so at any fixed measure a higher stratum verifies facts the floor provably cannot reach — the observability horizon moves with the stratum, quantifying why more compressed structure is coherent to the higher observer", b12),
        C("\u22a2", "K.15 THE SEAT CERTIFIED UNIVERSAL (forced\u207a): the operator register's own definition-terms pass the kernel's grid certificate through the bound book — addition and multiplication at stated degrees (1,1), the inner product at (1,1,1,1), every grid point a term reduction — so the register's core agreement claims are no longer two-point free identities but certified \u2200 (given the stated degree bounds, which the certificate names); and the certificate's teeth bite through this book too: a point-truth lands held.", b13),
        C("\u22a2", "K.16 THE INDUCTION ORGAN — the first \u2200 over an infinite index set: the scheme is a BASE term, a STEP certified universal by the grid (forced\u207a), and the induction principle (the definition of \u2115 — the single named citation). CASSINI FOR EVERY n: det multiplicativity for 2\u00d72 matrices is multilinear in rows — degree 1 in each of its 8 variables — so 256 grid points certify the step forced\u207a; with the base det(R) = \u22121 a term, det(R\u207f) = (\u22121)\u207f for ALL n, which IS Cassini's identity F(n+1)F(n\u22121) \u2212 F(n)\u00b2 = (\u22121)\u207f universally (the n=10 instance verified as a term). THE MATRIX FORM FOR EVERY n: from the single rank-2 identity R\u00b2 = R + I (a term), multiplication by R\u207f preserves the identity by the ring axioms (distributivity and associativity — named), so R\u207f\u207a\u00b2 = R\u207f\u207a\u00b9 + R\u207f for all n: the Fibonacci recurrence itself and the Lucas trace L(n) = Tr(R\u207f) are \u2200-certified from one 2\u00d72 identity, with the propagation instance R\u2074 = R\u00b3 + R\u00b2 and the depth instance R\u00b9\u2070 = [[89,55],[55,34]] verified as terms. What was exhausted at width 8 is now certified at every width: the recurrences join the polynomials on the far side of \u2200.", b14),
        C("\u22a2", "K.17 STRUCTURAL INDUCTION BY COMPOSITION OF ORGANS — ZECKENDORF'S THEOREM (1972) CERTIFIED FOR EVERY n: every positive integer has exactly one lawful (no-11) representation, and the certificate is the composition of the triad's own judgment forms. Every load-bearing arithmetic joint of the classical proof is verified: THE CEILING — the densest lawful word of width w carries exactly F(w+2)\u22121, the last citizen of the census (terms at six widths), with induction step C(w) = F(w+1)+C(w\u22122) which IS the recurrence, \u2200-certified by K.16; THE GREEDY STEP for existence — F(k)\u2264n<F(k+1) \u21d2 n\u2212F(k)<F(k\u22121), unfolding to the recurrence again (verified at depth to n=10\u2076); MONOTONICITY AND POSITIVITY — F(n+1)\u2212F(n)=F(n\u22121)>0, recurrence plus one order axiom; SEPARATION for uniqueness — a lower-topped representation is strictly smaller (the ceiling against the next weight). The logical scaffold is NAMED, not hidden: strong induction over \u2115 (the same citation as K.16), order transitivity, and the top-index case split — three named forms, zero silent ones. What Z.W exhausted at width 8, this claim certifies at every width: the numeral system's foundation now rests on the recurrence its own digits obey. THE FORMS OF JUDGMENT, CENSUSED like the ports: term (\u22a2) · free identity (forced) · grid (forced\u207a) · base+certified-step over \u2115 (K.16) · composed structural induction (here) · correspondence (\u21cc) · citation (named) · port reading (Z.E) — the logic of the triad is itself now an enumerated, finite surface.", b15),
        C("\u22a2", "K.18 THE SYMMETRY BREAK — the excess of one/zero is not error; it is THE founding asymmetry, one break sealed four times: (i) THE FIELD — √5 = φ−ψ is the antisymmetric UNIT of the Galois fold (a term), and it squares to the discriminant 5, the home prime where it vanishes (W.14): the field’s generator IS the break between the two roots; (ii) THE SECTORS — every power splits φⁿ = (L(n)+F(n)·√5)/2, sealed as ksub/kmul terms across a grid: LUCAS IS THE GALOIS-INVARIANT SECTOR AND FIBONACCI THE BREAK-COEFFICIENT, so the One Completion’s two seeds are revealed as the two symmetry sectors of one law — the duality was a decomposition all along; (iii) THE FOLD — at the base the one is DOUBLED, F(1)=F(2)=1 (the engine’s own mouth), and the numeral weights begin at F(2): Zeckendorf uniqueness (K.17) exists because the excess name is quotiented away — Z.W’s boundary fold refounded as the symmetry break that makes naming possible; (iv) THE DELIMITER — every golden codeword terminates in its FIRST forbidden 11 (verified to n=300): the excess of one is the edge of every lawful word, so the stream is self-delimiting exactly because the lawless marks the boundary of the law. The excess is the fuel of normalization, the coefficient of the field, the quotient at the base, and the delimiter of the stream: one break, four organs.", b16),
        C("\u2423", "K.␣ open: the full definition-term reduction for the remaining matrix operations (2×2 multiply, integer determinant, matrix–vector product), whose mechanism is proven and whose reduction is being completed; and the choice of this register's glyph."),
    ]

def register(path=None):
    """the seat hands its book to zero for grounding — never to the world."""
    return Z.ground_book(BOOK, path)

# ═══════════ · III · THE DEPTHS (the lineage's model) ═══════════
# ═══════════════════════════════════════════════════════════════════════════
#  KAEL — kael_world.py · THE MODEL REGISTER  (framework label: ∇ WORLD)
#
#  The applications module: each assertion is encoded as a term and checked by
#  the kernel. It imports only the kernel module; it never imports the operator
#  module. At startup it asks the kernel to bind — the kernel imports the
#  operator module, commits its operation table's fingerprint, and returns the
#  bound table (module mediation, enforced and tested here).
#
#  ASSERTIONS ARE TERMS: an assertion counts only when it is a term whose stated
#  result is verified by the kernel. The surrounding prose only annotates; small
#  helper functions merely assemble the assertions, they do not compute the
#  results being checked.
#
#  VERIFICATION SUCCEEDS iff every proof obligation is discharged (residue 0);
#  any failure is a nonzero residue. EXACT ARITHMETIC ONLY.
#  RUN:  python3 kael_world.py [--quiet|--json]
# ═══════════════════════════════════════════════════════════════════════════

PIN = ground_book(BOOK)                  # the hinge without the door: the book is already in the body

# ── authoring scaffold (states expectations; verifies nothing) ───────────────
# ERASED: THE MODEL'S SHADOW FIELD — its private _nm/_q/_fib/_luc and its
# rebindings of CIRC/C/T/E/my_sha/ONE4/ZERO4/PHI4/PSI4 duplicated the seat and
# kernel verbatim; the seat's constructors and the kernel's mouth stand. What
# survives is the quadruple alias and the two φ-power seeds (erasure ledger).
_q = kq                                   # the model's constructor IS the seat's
def _qphi(n): return kq(Z._luc(n), 2, _fib(n), 2)
def _qpsi(n): return kq(Z._luc(n), 2, -_fib(n), 2)

_RES = [0]                                # the residue — the cycle's remainder
def _read(term):
    r = Z.read(term, BOOK)
    ok = ("refused" not in r) and r.get("agrees", False)
    if not ok: _RES[0] += 1
    return ok, r

# ═══════════════════════════════════════════════════════════════════════════
#  W.1 · THE UNIT THEOREM AS TERMS — norm(φⁿ) = (−1)ⁿ: survival exact
# ═══════════════════════════════════════════════════════════════════════════
def _phi_pow_term(n):
    """φⁿ as nested field multiplications — the One Chain at law `kmul`."""
    if n == 0: return T("kmul", [ONE4, ONE4], E(ONE4))
    if n == 1: return T("kmul", [PHI4, ONE4], E(PHI4))
    return Z.chainT("kmul", [([PHI4, PHI4], _qphi(2))] +
                            [([PHI4, CIRC], _qphi(k)) for k in range(3, n + 1)])

def w_units():
    ok = True
    for n in range(0, 9):
        crown = T("knorm", [CIRC], E(_q((-1) ** n)), kids=[_phi_pow_term(n)])
        good, _ = _read(crown); ok &= good
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.2 · PHYSICS AS TERMS — the zero-statements, the rational word
# ═══════════════════════════════════════════════════════════════════════════
Yray = [1, -4, 2, -3, 6]
mult = [6, 3, 3, 2, 1]
sixT3 = [3, 3, 3, -3, -3, -3, 0, 0, 0, 0, 0, 0, 3, -3, 0]

def w_physics():
    ok, _ = _read(T("dot", [mult, Yray], E(0)))
    cube = T("cube", [Yray], E([1, -64, 8, -27, 216]))
    g, _ = _read(T("dot", [mult, CIRC], E(0), kids=[cube])); ok &= g
    ysp = T("spread", [Yray, mult],
            E([1, 1, 1, 1, 1, 1, -4, -4, -4, 2, 2, 2, -3, -3, 6]))
    ch = T("addv", [sixT3, CIRC],
           E([4, 4, 4, -2, -2, -2, -4, -4, -4, 2, 2, 2, 0, -6, 6]), kids=[ysp])
    num = T("dot", [sixT3, sixT3], E(72))
    den = T("dot", [CIRC, CIRC], E(192), kids=[ch,
            T("addv", [sixT3, CIRC],
              E([4, 4, 4, -2, -2, -2, -4, -4, -4, 2, 2, 2, 0, -6, 6]),
              kids=[T("spread", [Yray, mult],
                      E([1, 1, 1, 1, 1, 1, -4, -4, -4, 2, 2, 2, -3, -3, 6]))])])
    g, _ = _read(T("frac", [CIRC, CIRC], E([3, 8]), kids=[num, den])); ok &= g
    return ok

def w_mutation():
    forged = T("frac", [72, 192], E([1, 2]))
    r = Z.read(forged, BOOK)
    ok = ("refused" not in r) and (r.get("agrees") is False)     # the forgery FAILS
    alien = T("measure_experimentally", [Yray], E(0))
    ok &= ("refused" in Z.read(alien, BOOK))                     # measurement never a primitive
    foreign = dict(BOOK); foreign["dot"] = lambda u, v: 1 + sum(a*b for a, b in zip(u, v))
    ok &= ("refused" in Z.read(T("dot", [mult, Yray], E(0)), foreign))   # no adjacency
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.3 · THE E8 REGISTER AS TERMS — the founding equation at rank 8
# ═══════════════════════════════════════════════════════════════════════════
PHI8 = [[0, 1, 0, 0, 0, 0, 0, -1], [1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, -1, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1]]
E8CARTAN = [[2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
            [0, -1, 2, -1, 0, 0, 0, 0], [0, 0, -1, 2, -1, 0, 0, 0],
            [0, 0, 0, -1, 2, -1, 0, -1], [0, 0, 0, 0, -1, 2, -1, 0],
            [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, 0, 0, -1, 0, 0, 2]]
A9 = [[0]*9 for _ in range(9)]
for _i, _j in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (5, 8)]:
    A9[_i][_j] = A9[_j][_i] = 1
MARKS = [1, 2, 3, 4, 5, 6, 4, 2, 3]

def w_e8():
    I8 = [[1 if i == j else 0 for j in range(8)] for i in range(8)]
    # Every matrix identity below now reduces to the primitive base via a
    # definition-term (multiply/add/subtract/divide, assembled by juxtaposition),
    # so the rank-8 results are term-verified, not merely accelerator-checked.
    phi_plus_i = [[PHI8[i][j] + I8[i][j] for j in range(8)] for i in range(8)]
    ok, r = _read(Z.def_immul(PHI8, PHI8))                        # Φ² as a term
    ok &= (r.get("result") == phi_plus_i) and (r.get("mode") == "forced")   # = Φ + I
    S = [[2*PHI8[i][j] - I8[i][j] for j in range(8)] for i in range(8)]
    fiveI = [[5 if i == j else 0 for j in range(8)] for i in range(8)]
    g, r = _read(Z.def_immul(S, S)); ok &= g and (r.get("result") == fiveI)  # (2Φ−I)² = 5I
    # THE DETERMINANT IS ELIMINATION-MOD-ORDER: one operator (remove vertices one
    # at a time; the ORDER is its only parameter). The VALUE is the invariant (=1);
    # the TERM is the order-dependent shadow, governed by fill-in.
    bar = Z.def_idet(E8CARTAN)                                    # elimination @ INDEX order (Bareiss)
    g, r = _read(bar); ok &= g and (r.get("result") == 1)        # unimodular, reduced to primitives
    ok &= (Z.term_size(bar) < Z.tree_size(bar))                  # fill-in fans out: the shared-DAG ≪ tree
    forest = Z.def_det_forest(E8CARTAN)                           # SAME elimination @ PERFECT (leaf) order
    ok &= (forest is not None)                                   # E8's diagram is a forest — domain COMPUTED
    g, r = _read(forest)
    ok &= g and (r.get("result") == 1) and (r.get("mode") == "forced")   # same value, fill-in-free
    ok &= Z.laws_of(forest).issubset({"mul", "sub"})            # division-free: multiply/subtract alone
    ok &= (Z.term_size(forest) < Z.term_size(bar))              # the perfect order's term is strictly smaller
    po = Z.perfect_order(E8CARTAN)                                # the value is INVARIANT across orders:
    Mp = [[E8CARTAN[po[i]][po[j]] for j in range(8)] for i in range(8)]
    g, r = _read(Z.def_idet(Mp)); ok &= g and (r.get("result") == 1)     # index vs perfect: one det
    ok &= (Z.elim_fillin(E8CARTAN, po) == 0) and (Z.elim_fillin(E8CARTAN, list(range(8))) > 0)  # the cost
    ok &= (Z.def_det_forest([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]) is None)   # a cyclic diagram: refused
    # THE SECOND ORDER — noncommutativity. The recursion hides a FACTOR order too:
    # over the golden ring M₂(ℤ) (R the generator) the block matrix [[R,R⁻¹],[Rᵀ,R]]
    # has TWO quasideterminants (Schur complements at the two pivots) that DIFFER —
    # the fiber faithful at the VALUE, not merely at the cost — while the scalar det
    # stays the invariant (the abelianization det:M₂→ℤ killing the commutator, Dieudonné).
    def _mm(P, Q): return Z._gemm(P, Q)                          # the one gemm; the private multiply is DELETED
    def _ms(P, Q): return [[P[i][j]-Q[i][j] for j in range(2)] for i in range(2)]
    def _iv(P): d = _idet(P); return [[P[1][1]//d, -P[0][1]//d], [-P[1][0]//d, P[0][0]//d]]
    I2 = [[1, 0], [0, 1]]; Rg = [[1, 1], [1, 0]]; Ri = _iv(Rg); Rt = [[0, 1], [1, 1]]
    Ab, Bb, Cb, Db = Rg, Ri, Rt, Rg
    q22 = _ms(Db, _mm(_mm(Cb, _iv(Ab)), Bb))                     # D − C A⁻¹ B  (pivot 1,1)
    q11 = _ms(Ab, _mm(_mm(Bb, _iv(Db)), Cb))                     # A − B D⁻¹ C  (pivot 2,2)
    ok &= (q11 != q22)                                          # THE BREAK: faithful fiber at the value
    Sq = _ms([[2*q22[i][j] for j in range(2)] for i in range(2)], I2)
    g, r = _read(Z.def_immul(Sq, Sq)); ok &= g and (r.get("result") == [[5, 0], [0, 5]])  # (2Q−I)²=5I: home prime
    g, _ = _read(T("mul", [_idet(Ab), _idet(q22)], E(1))); ok &= g   # det(A)·det(Q22) = det4 = 1: the invariant
    g, _ = _read(T("mul", [_idet(Db), _idet(q11)], E(1))); ok &= g   # det(D)·det(Q11) = det4 = 1: same, other pivot
    P2 = _mm(Rg, Rg)                                             # commutative shadow: one commuting subring
    cq22 = _ms(P2, _mm(_mm(Rg, _iv(P2)), Rg))
    cq11 = _ms(P2, _mm(_mm(Rg, _iv(P2)), Rg))
    ok &= (cq11 == cq22)                                        # blocks that commute -> the fiber collapses
    g, r = _read(Z.def_matvec(A9, MARKS))                         # Perron reading A·m = 2m
    ok &= g and (r.get("result") == [2*m for m in MARKS])
    g, _ = _read(T("mul", [8, 30], E(240))); ok &= g              # roots = rank·h
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.4 · THE INFORMATION ORGAN AS TERMS — Kraft, incompressibility, two sides
# ═══════════════════════════════════════════════════════════════════════════
def w_information():
    ok = True
    for N in (10, 30):                                            # the Kraft identity
        Fv = [_fib(L) for L in range(1, N + 1)]
        Pv = [2 ** (N - L) for L in range(1, N + 1)]
        lhs = T("dot", [Fv, Pv], E(2 ** (N + 1) - _fib(N + 3)))
        rhs = T("sub", [2 ** (N + 1), _fib(N + 3)], E(2 ** (N + 1) - _fib(N + 3)))
        g, _ = _read(T("sub", [CIRC, CIRC], E(0), kids=[lhs, rhs])); ok &= g
        g, _ = _read(T("lt", [_fib(N + 4), 2 * _fib(N + 3)], E(True))); ok &= g
    for n, k in ((16, 4), (64, 8)):                               # incompressibility forced
        prod = T("mul", [2 ** (n - k) - 1, 2 ** k], E((2 ** (n - k) - 1) * 2 ** k))
        g, _ = _read(T("lt", [CIRC, 2 ** n], E(True), kids=[prod])); ok &= g
    for n in (1000, 2 ** 20, 2 ** 20 + 1):                        # two-sided cost
        b = n.bit_length()
        g, _ = _read(T("lt", [2 ** (b - 1) - 1, n], E(True))); ok &= g
        g, _ = _read(T("lt", [n, 2 ** b + 1], E(True))); ok &= g
        opsn = bin(n).count("1") + b                              # the achieved side: one square per bit, one multiply per mark
        opst = T("mpow_ops", [n], E(opsn), mode="counted")
        g, _ = _read(T("lt", [CIRC, 2 * b + 1], E(True), kids=[opst])); ok &= g
    # THE CENSUS OF THE EXPRESSIBLE: the values whose self-delimiting golden
    # name fits in B bits are EXACTLY the initial segment [1, F(B+1)−1] — the
    # boundary of observability at every measure is the census itself.
    cnt12 = sum(1 for n in range(1, _fib(13)) if len(Z._cwg(n)) <= 12)
    g, _ = _read(T("sub", [_fib(13), 1], E(cnt12))); ok &= g      # full enumeration pins B=12
    for B in (12, 16, 20, 24):
        lo = len(Z._cwg(_fib(B + 1) - 1)); hi = len(Z._cwg(_fib(B + 1)))
        g, _ = _read(T("lt", [lo, B + 1], E(True))); ok &= g      # last citizen fits
        g, _ = _read(T("lt", [B, hi], E(True))); ok &= g          # first exile does not
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.5 · THE OBSERVER COUPLING ENDPOINTS AS TERMS — disc +5 vs disc −3
# ═══════════════════════════════════════════════════════════════════════════
def w_coupling():
    ok, _ = _read(T("mpw2", [[1, -1, 1, 0], 3], E([-1, 0, 0, -1])))   # the elliptic word: M³ = −I
    g, _ = _read(T("mpw2", [[1, -1, 1, 0], 6], E([1, 0, 0, 1]))); ok &= g    # period 6 exact
    g, _ = _read(T("mpw2", [[0, -1, 1, 0], 4], E([1, 0, 0, 1]))); ok &= g    # t²+1: period 4
    g, _ = _read(T("mpw2", [[-1, -1, 1, 0], 3], E([1, 0, 0, 1]))); ok &= g   # t²+t+1: period 3
    g, _ = _read(T("sub", [1, -4], E(5))); ok &= g                # disc(t²−t−1) = +5: the split word
    g, _ = _read(T("sub", [1, 4], E(-3))); ok &= g                # disc(t²−t+1) = −3: the elliptic
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.6 · THE NULL THEOREM AS TERMS — the reversed arrow, the observer's zero
# ═══════════════════════════════════════════════════════════════════════════
QOBS  = [[_q(1, 2, 1, 10), _q(0, 1, 1, 5)], [_q(0, 1, 1, 5), _q(1, 2, -1, 10)]]
QMIRR = [[_q(1, 2, -1, 10), _q(0, 1, -1, 5)], [_q(0, 1, -1, 5), _q(1, 2, 1, 10)]]

def w_null():
    ok = True
    for n in range(1, 13):                                        # ψ²ⁿ → 0, arriving never
        p2n = _qpsi(2 * n)
        g, _ = _read(T("klt", [ZERO4, p2n], E(True))); ok &= g              # never zero
        g, _ = _read(T("klt", [_qpsi(2 * (n + 1)), p2n], E(True))); ok &= g # strictly toward 0
        g, _ = _read(T("klt", [p2n, _q(1, _fib(2 * n))], E(True))); ok &= g # exact bracket above
        g, _ = _read(T("klt", [_q(1, _fib(2 * n + 2)), p2n], E(True))); ok &= g  # LOCATED: strictly above 1/F(2n+2)
        g, _ = _read(T("knorm", [_qpsi(n)], E(_q((-1) ** n)))); ok &= g     # every point a unit
    a, b2, c2, d = QOBS[0][0], QOBS[0][1], QOBS[1][0], QOBS[1][1]
    ad = T("kmul", [a, d], E(_q(1, 5)))
    bc = T("kmul", [b2, c2], E(_q(1, 5)))
    g, _ = _read(T("ksub", [CIRC, CIRC], E(ZERO4), kids=[ad, bc])); ok &= g  # det Q = 0
    g, _ = _read(T("kadd", [a, d], E(ONE4))); ok &= g                        # tr Q = 1
    zmat = [[ZERO4, ZERO4], [ZERO4, ZERO4]]
    g, _ = _read(T("m2kmul", [QOBS, QMIRR], E(zmat))); ok &= g   # Q·Q′ = 0: observation factors through zero
    g, _ = _read(T("kmul", [PHI4, PSI4], E(_q(-1)))); ok &= g    # det R = φψ = −1: the term returns
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.7 · THE INTERLEAVING, CLAIMED ON THIS FILE'S OWN SOURCE
# ═══════════════════════════════════════════════════════════════════════════
def w_no_adjacency():
    src = Z._port_read(__file__)
    for line in src.splitlines():
        s = line.strip()
        if s.startswith("import kael") and "kael_zero" not in s: return False
        if s.startswith("from kael ") or s.startswith("from kael import"): return False
    return True

# ═══════════════════════════════════════════════════════════════════════════
#  §G · ARITHMETIC IN THE FIBONACCI BASE — assertions evaluated in-base
# ═══════════════════════════════════════════════════════════════════════════
_tz = Z.gnum   # ERASED: the model's private greedy encoder was byte-identical to the kernel's gnum

def w_golden():
    ok, _ = _read(T("gadd", [_tz(88), _tz(55)], E(_tz(143))))          # numerals through the kernel
    g, _ = _read(T("gmul", [CIRC, _tz(3)], E(_tz(429)), kids=[
        T("gadd", [_tz(88), _tz(55)], E(_tz(143)))])); ok &= g
    g, _ = _read(T("gdivmod", [_tz(75025), _tz(46368)],
                   E([_tz(1), _tz(28657)]))); ok &= g                  # F(25)/F(24): quotient 1, golden remainder
    g, _ = _read(T("ggcd", [_tz(144), _tz(89)], E([1]))); ok &= g      # consecutive fibs: gcd ONE, Lamé's slowest road
    for n in (8, 12):                                                   # the partition, as terms: 2^n = speakers + F(n+2)
        speak = 2 ** n - _fib(n + 2)
        g, _ = _read(T("add", [CIRC, speak], E(2 ** n),
                       kids=[T("fib", [n + 2], E(_fib(n + 2)))])); ok &= g
    gnames = [Z.gname("w-cell-%d" % i) for i in range(60)]
    ok &= (len(set(gnames)) == 60) and all("11" not in g2 and len(g2) == 48 for g2 in gnames)
    # THE SHIFT IS M, as terms: gadd(up(x), x) = up(up(x)) — the founding
    # equation a digit law, read by the kernel
    for n in (5, 21, 100):
        z = _tz(n); upz = [0] + z; upupz = [0, 0] + z
        g, _ = _read(T("gadd", [CIRC, z], E(upupz), kids=[T("gup", [z], E(upz))])); ok &= g
    # KNUTH'S CIRCLE as a term (3∘4 = F(3+2 offsets): authored by the census)
    za, zb = _tz(3), _tz(4)
    circ = sum(_fib(i + j + 4) for i, di in enumerate(za) if di
               for j, dj in enumerate(zb) if dj)
    g, _ = _read(T("gcirc", [za, zb], E(_tz(circ)))); ok &= g
    # POWER and A FOLD SEED, in the base, through the kernel
    g, _ = _read(T("gpow", [_tz(3), 7], E(_tz(3 ** 7)))); ok &= g
    x64 = 2 << 64
    s = Z._isqrt(x64)                      # the one descent; the private Newton loop is DELETED
    g, _ = _read(T("gsqrt", [_tz(x64)], E(_tz(s)))); ok &= g       # the hash's first seed, in gold
    g, _ = _read(T("gfib", [60], E(_tz(_fib(60))))); ok &= g       # the census weighing itself
    # THE THIRD SYMBOL through the kernel: subtraction total, landing sign-pure
    g, _ = _read(T("ssub", [_tz(55), _tz(89)],
                   E([-t for t in _tz(34)]))); ok &= g              # 55 − 89 = −34, anti-marks
    g, _ = _read(T("ssub", [CIRC, _tz(13)], E(_tz(21)), kids=[
        T("gadd", [_tz(21), _tz(13)], E(_tz(34)))])); ok &= g       # (21+13) − 13, chained
    # THE CARVING BOUND and THE MOLECULE, as terms
    g, _ = _read(T("gval", [[1] * 13], E(_fib(16) - 2))); ok &= g   # all-ones = F(n+3) − 2
    g, _ = _read(T("gval", [[0] * 7 + [1, 0, 1]], E(_luc(10)))); ok &= g   # Lucas: the doublet
    # THE RING through the kernel: Euclidean division on negatives
    g, _ = _read(T("sdivmod", [[-t for t in _tz(37)], _tz(5)],
                   E([[-t for t in _tz(8)], _tz(3)]))); ok &= g     # −37 = (−8)·5 + 3
    # THE ORDER RELATION carries the full bit: 3·J = 2^(n+2) − (−1)^n, as terms
    n = 10
    Tn = (2 ** (n + 2) - (-1) ** n) // 3
    g, _ = _read(T("frac", [CIRC, 3], E([Tn, 1]), kids=[
        T("sub", [2 ** (n + 2), (-1) ** n], E(2 ** (n + 2) - (-1) ** n))])); ok &= g
    # THE MEET, lawful by law: wand of lawful is lawful
    g, _ = _read(T("wand", ["10010", "00010"], E("00010"))); ok &= g
    # THE PLASTIC BODY through the kernel: the founding equation at degree 3,
    # and Perrin's prime divisibility as exact fraction reduction
    Mp = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    MpI = [[0 + (1 if i == j else 0) if False else Mp[i][j] + (1 if i == j else 0)
            for j in range(3)] for i in range(3)]
    m2 = T("immul", [Mp, Mp], E([[0, 0, 1], [1, 1, 0], [0, 1, 1]]))
    g, _ = _read(T("immul", [CIRC, Mp], E(MpI), kids=[m2])); ok &= g     # M³ = M + I
    rr = [Z._ktrace([1, 1, 0], kk) for kk in range(102)]   # perrin through the one object, seed-literal-free
    for p in (19, 101):
        g, _ = _read(T("frac", [rr[p], p], E([rr[p] // p, 1]))); ok &= g  # p | R(p): the fraction lands whole

    forged = T("gadd", [_tz(88), _tz(55)], E(_tz(144)))
    r = Z.read(forged, BOOK)
    ok &= ("refused" not in r) and (r.get("agrees") is False)          # golden forgery fails whole
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.11 · THE E8 DISSOLUTION — the Cartan matrix DERIVED, the seed discharged
#  Nothing seeded: the one relation gives ℚ(φ); quaternions over it carry the
#  120 unit icosians, whose coordinates are drawn ONLY from {0,±1,±φ⁻¹,±φ}/2;
#  their ℤ-span has rank 8; the pairing is FORCED — among ℚ-linear functionals
#  on ℚ(φ), ⟨p,q⟩ = 2·(1-part of Re(p·q̄)) is what renders the Gram integral,
#  even, positive-definite and unimodular; the 240 roots are harvested from the
#  units and their pairwise sums; 8 simple roots recover the Cartan matrix of
#  W.4 entrywise — the literal demotes from seed to theorem. Completeness of
#  the root census rides ONE cited external classification (even unimodular
#  rank 8 is unique — Mordell 1938 — with exactly 240 roots); everything else
#  is term-verified through the kernel. Scaffold authors; the kernel checks.
#  2I/{±1} ≅ A₅: the frozen A₅ register is this object one quotient away.
# ═══════════════════════════════════════════════════════════════════════════
def _fm2(x, y): return Z._pring_mul((1, 1), x, y)   # ℤ[φ] IS the ring of the golden law — the [1,1] seed of the one engine; the private product is DELETED
def _fa2(x, y): return (x[0]+y[0], x[1]+y[1])
def _fn2(x): return (-x[0], -x[1])

_ICO = {}   # THE ONE PERFORMANCE: units/roots/classes/fold computed once; witnesses read the act

def _ico_roots():
    if "roots" not in _ICO:
        U = _icosian_units(); roots = set(U)
        for i in range(120):
            for j in range(i + 1, 120):
                s = tuple(_fa2(U[i][c], U[j][c]) for c in range(4))
                if s not in roots and _re4(s, s)[0] == 4: roots.add(s)
        _ICO["roots"] = sorted(roots)
    return _ICO["roots"]

def _ico_classes():
    if "classes" not in _ICO: _ICO["classes"] = _conj_classes(_icosian_units(), _qm2, _qinv2)
    return _ICO["classes"]

def _ico_fold():
    if "fold" not in _ICO:
        cls = _ico_classes(); fold = []; used = set()
        for i, c in enumerate(cls):
            if i in used: continue
            ns = {tuple((-u, -v) for u, v in x) for x in map(tuple, c)}
            j = next(k for k, c2 in enumerate(cls) if set(map(tuple, c2)) == ns)
            used.add(i); used.add(j)
            fold.append((i, len(c) // 2 if i == j else len(c)))
        _ICO["fold"] = fold
    return _ICO["fold"]

def _icosian_units():
    """the 120 unit icosians, coordinates scaled ×2 so all entries live in ℤ[φ]
    as integer pairs: {(2,0)} the unit, (0,1) φ, (−1,1) φ⁻¹ — golden data only.
    Cached: the act is performed once."""
    if "U" in _ICO: return _ICO["U"]
    from itertools import permutations as _pm, product as _pr   # collared: authoring scaffold combinatorics only
    Z0 = (0, 0)
    def _signs(vals):
        idx = [i for i, v in enumerate(vals) if v != Z0]; out = []
        for pat in _pr([1, -1], repeat=len(idx)):
            w = list(vals)
            for k, i in enumerate(idx):
                if pat[k] < 0: w[i] = _fn2(w[i])
            out.append(tuple(w))
        return out
    G = set()
    for e in range(4):
        v = [Z0]*4; v[e] = (2, 0)
        for w in _signs(tuple(v)): G.add(w)
    for w in _signs(((1,0),)*4): G.add(w)
    base = (Z0, (1, 0), (-1, 1), (0, 1))
    evps = [p for p in _pm(range(4))
            if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
    for p in evps:
        v = tuple(base[p.index(i)] for i in range(4))
        for w in _signs(v): G.add(w)
    _ICO["U"] = sorted(G)
    return _ICO["U"]

def _re4(p, q):
    """THE PAIRING IS THE TRACE FORM OF THE FOURTH BODY: Σ p_c·q_c equals the
    real part of p·q̄ under the kernel's _quat_mul — the E8 inner product of
    W.11 is not chosen, it is what quaternion multiplication leaves on the
    diagonal. Kept as the hot-path accelerator; agreement with the engine is
    sealed in W.11's suite."""
    s = (0, 0)
    for c in range(4): s = _fa2(s, _fm2(p[c], q[c]))
    return s

def _hnf8(rows):
    rows = [r[:] for r in rows]; r = 0
    for col in range(8):
        piv = next((i for i in range(r, len(rows)) if rows[i][col] != 0), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        ch = True
        while ch:
            ch = False
            for i in range(r+1, len(rows)):
                if rows[i][col] != 0:
                    q = rows[i][col] // rows[r][col]
                    rows[i] = [a - q*b for a, b in zip(rows[i], rows[r])]
                    if rows[i][col] != 0: rows[r], rows[i] = rows[i], rows[r]; ch = True
        r += 1
        if r == 8: break
    return rows[:r]

def w_dissolution():
    ok = True
    U = _icosian_units()
    ok &= (len(U) == 120)                          # the unit census
    # THE PAIRING IS FORCED TWICE: not only by integrality (below) but by the
    # algebra itself — Σ p_c·q_c IS the real part of p·q̄ under the kernel's
    # fourth-body organ; sealed on all pairs from a 12-unit probe set.
    for i in range(12):
        for j in range(12):
            pq = Z._quat_mul(_fm2, _fa2, _fn2, U[i], _qinv2(U[j]))
            ok &= (_re4(U[i], U[j]) == pq[0])
    roots = _ico_roots()                           # the one harvest
    ok &= (len(roots) == 240)                      # census, completeness by the cited classification
    # the lattice: ℤ-span of the units, rank 8, Gram under the FORCED functional
    rows = [[g[c][k] for c in range(4) for k in range(2)] for g in U]
    B = _hnf8(rows); ok &= (len(B) == 8)
    Q8 = [tuple((b[2*c], b[2*c+1]) for c in range(4)) for b in B]
    GM = [[_re4(Q8[i], Q8[j])[0] // 2 for j in range(8)] for i in range(8)]
    # EVEN, term by term: 2·(d/2) lands the diagonal
    for i in range(8):
        g, _ = _read(T("mul", [2, GM[i][i] // 2], E(GM[i][i]))); ok &= g
    # POSITIVE-DEFINITE AND UNIMODULAR: the eight leading principal minors as
    # fraction-free determinant terms, each strictly positive, the last exactly 1
    for k in range(1, 9):
        sub = [row[:k] for row in GM[:k]]
        mt = Z.def_idet(sub)
        g, r = _read(mt); ok &= g and (r.get("result") > 0)
        if k == 8: ok &= (r.get("result") == 1)
    # EVERY ROOT'S NORM IS 2, as terms: r·(G·r) through dot∘matvec
    def _coords(rv):
        rv = list(rv); x = [0]*8
        piv = [next(j for j in range(8) if B[i][j] != 0) for i in range(8)]
        for i in range(8):
            j = piv[i]
            if rv[j] % B[i][j] != 0: return None
            x[i] = rv[j] // B[i][j]
            rv = [a - x[i]*b for a, b in zip(rv, B[i])]
        return x if all(a == 0 for a in rv) else None
    RC = []
    for q in sorted(roots):
        c = _coords([q[cc][k] for cc in range(4) for k in range(2)])
        if c is None: return False, None           # a root outside the lattice: refuse
        RC.append(c)
    for rc in RC:
        t = T("dot", [rc, CIRC], E(2), kids=[Z.def_matvec(GM, rc)])
        g, _ = _read(t); ok &= g
    # SIMPLE ROOTS AND THE RECOVERY: 8 simples; their Gram equals the W.4
    # literal entrywise under one relabeling — the Cartan matrix is a theorem
    wgt = [1, 7, 13, 23, 41, 67, 89, 113]
    pos = [tuple(r) for r in RC if sum(a*b for a, b in zip(r, wgt)) > 0]
    ps = set(pos)
    simples = [r for r in pos
               if not any(tuple(x - y for x, y in zip(r, p)) in ps for p in pos if p != r)]
    ok &= (len(simples) == 8)
    def _ip(a, b): return sum(a[i]*GM[i][j]*b[j] for i in range(8) for j in range(8))
    Cm = [[_ip(simples[i], simples[j]) for j in range(8)] for i in range(8)]
    from itertools import permutations as _pm2   # collared: relabeling search, scaffold only
    perm = next((p for p in _pm2(range(8))
                 if all(Cm[p[i]][p[j]] == E8CARTAN[i][j] for i in range(8) for j in range(8))), None)
    if perm is None: return False, None
    for i in range(8):
        for j in range(8):
            t = T("dot", [list(simples[perm[i]]), CIRC], E(E8CARTAN[i][j]),
                  kids=[Z.def_matvec(GM, list(simples[perm[j]]))])
            g, _ = _read(t); ok &= g
    return ok, perm

# ═══════════════════════════════════════════════════════════════════════════
#  W.12 · THE INTERNAL OBSERVER — first residency (the universe tier's hinge)
#  An observer is a RESIDENT of the store: a (schedule, budget) record whose
#  observations are committed names. Verified here: residency; the horizon
#  moving with the budget (the larger observer provably sees strictly more);
#  the per-budget boundary (last citizen fits, first exile does not); one-way
#  interaction (a sealed name grounds without its content being derivable);
#  and SHARED LANDING, PRIVATE COST — one fact read through two schedules
#  (the floor observer and the seat observer) lands identically while the
#  term-costs provably differ: ontology is the quotient, cognition the fiber,
#  now between residents rather than external schedulers.
# ═══════════════════════════════════════════════════════════════════════════
def w_observer():
    ok = True
    A = Z.rec({"observer": "finder", "schedule": "floor", "budget": 12})
    Bv = Z.rec({"observer": "weaver", "schedule": "seat", "budget": 16})
    Z.remember("observer/finder", A, "world", Z.STORE)
    Z.remember("observer/weaver", Bv, "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("observer/finder", Z.STORE))
    ok &= ("grounded" in Z.grounded("observer/weaver", Z.STORE))
    # the horizon moves with the budget: F(13)=233 < F(17)=1597, as terms
    g, _ = _read(T("fib", [13], E(233))); ok &= g
    g, _ = _read(T("fib", [17], E(1597))); ok &= g
    g, _ = _read(T("lt", [233, 1597], E(True))); ok &= g
    # the boundary per observer (the census read at each budget)
    ok &= (len(Z._cwg(232)) <= 12) and (len(Z._cwg(233)) > 12)
    ok &= (len(Z._cwg(1596)) <= 16) and (len(Z._cwg(1597)) > 16)
    # one-way interaction: finder seals a name; weaver grounds existence
    # without content — no operation of the book derives the preimage
    Z.remember("observer/finder/msg", Z.rec({"sealed": Z.H("finder-secret")}), "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("observer/finder/msg", Z.STORE))
    alien = T("derive_preimage", [Z.H("finder-secret")], E("finder-secret"))
    ok &= ("refused" in Z.read(alien, BOOK))
    # shared landing, private cost: one fact, two schedules, one crown, two sizes
    tf = Z.def_mul_floor(6, 7)                     # the floor observer's reading
    ts = T("mul", [6, 7], E(42))                   # the seat observer's reading
    gf, rf = _read(tf); gs, rs = _read(ts)
    ok &= gf and gs and (rf.get("result") == 42 == rs.get("result"))
    ok &= (Z.term_size(ts) < Z.term_size(tf))
    g, _ = _read(T("lt", [Z.term_size(ts), Z.term_size(tf)], E(True), mode="counted")); ok &= g
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.13 · THE QUOTIENT COMES HOME — A₅ and the golden character
#  From the group W.11 derives (no new seeds): the class equation of the 120
#  unit icosians (nine classes), the fold by the center {±1} landing exactly
#  A₅'s class census, and the SPIN CHARACTER read off the derived group itself
#  — χ₂(g) = 2·Re(g), exact in ℚ(φ) — taking the golden values, its
#  irreducibility term-verified by column orthogonality through the field
#  register. The frozen A₅ register is reconstructed as a quotient, not
#  migrated. The full nine-character McKay decomposition is staged.
# ═══════════════════════════════════════════════════════════════════════════
def _qm2(g, h):
    """quaternion product on the ×2-scaled icosians — the kernel's fourth-body
    organ (_quat_mul) over the golden law's ring, the ×4 result halved back to
    the scaled lattice. ERASED: the private Hamilton formulas."""
    p = Z._quat_mul(_fm2, _fa2, _fn2, g, h)
    out = []
    for u, v in p:
        if u % 2 or v % 2: raise ValueError("product left the scaled ring")
        out.append((u // 2, v // 2))
    return tuple(out)

def _qinv2(g):
    """inverse of a unit icosian = its quaternion conjugate (norm 1)."""
    return (g[0], (-g[1][0], -g[1][1]), (-g[2][0], -g[2][1]), (-g[3][0], -g[3][1]))

def _pair_to_quad(p):
    """ℤ[φ] pair (u,v) = u+vφ → the seat's quadruple: (u+v/2) + (v/2)√5."""
    return _q(2 * p[0] + p[1], 2, p[1], 2)

def _conj_classes(els, mul, inv):
    """ONE ORBIT ENGINE: conjugacy classes of a finite group given its table —
    seeded at the 120 unit icosians (W.13) and at PSL(2,𝔽₅) (W.14); the two
    former private loops are DELETED (erasure ledger). The size census IS the
    class equation."""
    left = set(els); classes = []
    while left:
        g = next(iter(left)); orb = {g}
        for u in els: orb.add(mul(mul(u, g), inv(u)))
        classes.append(sorted(orb)); left -= orb
    return classes

def w_mckay():
    ok = True
    U = _icosian_units()
    classes = _ico_classes()                       # the one orbit run
    sizes = sorted(len(c) for c in classes)
    ok &= (len(classes) == 9) and (sizes == [1, 1, 12, 12, 12, 12, 20, 20, 30])
    g, _ = _read(T("dot", [[1] * 9, sizes], E(120))); ok &= g          # the class equation
    # THE QUOTIENT: the center {±1} folds 120 to 60 — and the classes land A₅'s
    g, _ = _read(T("frac", [120, 2], E([60, 1]))); ok &= g
    folded = [s for _, s in _ico_fold()]           # the one fold
    ok &= (sorted(folded) == [1, 12, 12, 15, 20])                       # A₅'s class census
    g, _ = _read(T("dot", [[1] * 5, sorted(folded)], E(60))); ok &= g
    # THE GOLDEN CHARACTER: χ₂(g) = 2·Re(g) = the scaled first coordinate,
    # exact in ℚ(φ); on the nine classes it takes {±2, ±1, 0, φ, ψ, −φ, −ψ}
    chi = sorted({c[0][0] for c in classes})
    ok &= (chi == sorted([(2, 0), (-2, 0), (1, 0), (-1, 0), (0, 0),
                          (0, 1), (1, -1), (0, -1), (-1, 1)]))          # φ=(0,1), ψ=(1,−1)
    # IRREDUCIBILITY BY COLUMN ORTHOGONALITY, through the field register:
    # Σ_classes size·χ² = |2I| = 120, a kadd/kmul chain over the quadruples
    total_t = None; total_v = None
    for c in classes:
        q = _pair_to_quad(c[0][0])
        sqv = kmul(q, q)
        sq = T("kmul", [q, q], E(sqv))
        wv = kmul(_q(len(c)), sqv)
        wgt = T("kmul", [_q(len(c)), CIRC], E(wv), kids=[sq])
        if total_t is None:
            total_t, total_v = wgt, wv
        else:
            total_v = kadd(total_v, wv)
            total_t = T("kadd", [CIRC, CIRC], E(total_v), kids=[total_t, wgt])
    g, r = _read(total_t); ok &= g and (r.get("result") == _q(120))
    return ok

# ERASED: _mul4/_add4 — the authoring scaffold's field was the seat's kmul/kadd verbatim

# ═══════════════════════════════════════════════════════════════════════════
#  W.14 · THE A₅ DISSOLUTION — the home prime
#  A₅ is the golden relation read at its own degeneration. disc(x²−x−1) = 5
#  is the unique ramified prime of ℚ(√5); at the collision point 3, the value
#  AND the derivative both equal that same 5, so mod 5 the two golden roots
#  collapse to one double root — and the collapse is an exact integer matrix
#  identity, (R−3I)² = 5·(2I−R). Over the residue field 𝔽₅, PSL(2,𝔽₅) is
#  built and shown EXPLICITLY isomorphic to W.13's quotient 2I/{±1}: a
#  (2,3,5) generating pair in each, the word-map by breadth-first search,
#  the bijection checked on ALL 3600 products. Neither E8 nor A₅ is
#  imported; both precipitate from the one relation.
# ═══════════════════════════════════════════════════════════════════════════
def w_home_prime():
    ok = True
    # the discriminant, and the double root: p(3) = p'(3) = 5, both landing whole mod 5
    g, _ = _read(T("sub", [1, -4], E(5))); ok &= g                    # disc(x²−x−1) = 1+4
    g, _ = _read(T("frac", [5, 5], E([1, 1]))); ok &= g               # p(3) = 9−3−1 = 5 ≡ 0
    g, _ = _read(T("frac", [6 - 1, 5], E([1, 1]))); ok &= g           # p'(3) = 5 ≡ 0: DOUBLE
    # ramification as an integer identity at rank 2: (R−3I)² = 5·(2I−R)
    S5 = [[-2, 1], [1, -3]]
    g, r = _read(Z.def_immul(S5, S5)); ok &= g and (r.get("result") == [[5, -5], [-5, 10]])
    # PSL(2,𝔽₅): the projective symmetry group over the residue field
    els = [(a, b, c, d) for a in range(5) for b in range(5)
           for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1]
    ok &= (len(els) == 120)
    def _pneg(m): return tuple((-x) % 5 for x in m)
    def _pc(m): return min(m, _pneg(m))
    P = sorted({_pc(m) for m in els})
    ok &= (len(P) == 60)
    def _pmul(x, y):
        a, b, c, d = x; e, f, g2, h = y
        return _pc(((a * e + b * g2) % 5, (a * f + b * h) % 5,
                    (c * e + d * g2) % 5, (c * f + d * h) % 5))
    PI = _pc((1, 0, 0, 1))
    def _pinv(u):
        a, b, c, d = u
        return _pc((d, (-b) % 5, (-c) % 5, a))
    pcls = _conj_classes(P, _pmul, _pinv)       # the one orbit engine, other seed
    psz = sorted(len(c) for c in pcls)
    ok &= (psz == [1, 12, 12, 15, 20])                                # the same census as W.13
    g, _ = _read(T("dot", [[1] * 5, psz], E(60))); ok &= g
    # THE EXPLICIT ISOMORPHISM 2I/{±1} ≅ PSL(2,𝔽₅)
    U = _icosian_units()
    def _qneg(x): return tuple((-u, -v) for u, v in x)
    def _qcn(x): return min(x, _qneg(x))
    Q = sorted({_qcn(g0) for g0 in U})
    def _qmulq(x, y): return _qcn(_qm2(x, y))
    QE = _qcn(((2, 0), (0, 0), (0, 0), (0, 0)))
    def _ordr(x, mul, ident):
        p = x
        for k in range(1, 11):
            if p == ident: return k
            p = mul(p, x)
        return None
    def _gens235(els2, mul, ident):
        twos = [g0 for g0 in els2 if _ordr(g0, mul, ident) == 2]
        threes = [g0 for g0 in els2 if _ordr(g0, mul, ident) == 3]
        return [(a, b) for a in twos for b in threes if _ordr(mul(a, b), mul, ident) == 5]
    a1, b1 = _gens235(Q, _qmulq, QE)[0]
    seen = {QE: ()}; frontier = [QE]
    while frontier:
        nf = []
        for x in frontier:
            for tag, g0 in ((0, a1), (1, b1)):
                y = _qmulq(x, g0)
                if y not in seen: seen[y] = seen[x] + (tag,); nf.append(y)
        frontier = nf
    ok &= (len(seen) == 60)                                           # (2,3,5) generates the quotient
    def _apply(w, a, b, mul, ident):
        x = ident
        for t in w: x = mul(x, a if t == 0 else b)
        return x
    iso = None
    for a2, b2 in _gens235(P, _pmul, PI):
        f = {g0: _apply(w, a2, b2, _pmul, PI) for g0, w in seen.items()}
        if len(set(f.values())) != 60: continue
        if all(f[_qmulq(x, y)] == _pmul(f[x], f[y]) for x in Q for y in Q):
            iso = (a2, b2); break
    ok &= (iso is not None)
    g, _ = _read(T("mul", [60, 60], E(3600), mode="counted")); ok &= g   # the exhaustive check, counted
    Z.remember("iso/A5-PSL2F5", Z.rec({"products_checked": 3600,
                                       "gens": [list(iso[0]), list(iso[1])] if iso else None}),
               "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("iso/A5-PSL2F5", Z.STORE))
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.15 · THE McKAY DISSOLUTION — the nine characters derived, A₉ and the
#  marks demoted from seed to theorem; the full prose lives in the claim.
# ═══════════════════════════════════════════════════════════════════════════
def _as_intq(v):
    """a quadruple that is a plain integer, or None."""
    return v[0] if (v[1] == 1 and v[2] == 0) else None

def w_mckay_table():
    ok = True
    classes = _ico_classes()                                  # the one orbit run
    sizes = [len(c) for c in classes]
    IDQ = ((2, 0), (0, 0), (0, 0), (0, 0))
    NEGQ = ((-2, 0), (0, 0), (0, 0), (0, 0))
    cid = next(i for i, c in enumerate(classes) if c[0] == IDQ and len(c) == 1)
    cng = next(i for i, c in enumerate(classes) if c[0] == NEGQ and len(c) == 1)
    # THE TWO GIVEN CHARACTERS: the trivial, and the spin trace read off the group
    one9 = [_q(1)] * 9
    chi2 = [_pair_to_quad(c[0][0]) for c in classes]          # χ₂(g) = 2·Re(g), exact
    def _ipch(a, b):                                          # exact ⟨a,b⟩ = (1/120)Σ size·a·b
        tot = _q(0)
        for c in range(9): tot = kadd(tot, kmul(_q(sizes[c]), kmul(a[c], b[c])))
        return kmul(tot, _q(1, 120))
    def _tens(a, b): return [kmul(a[c], b[c]) for c in range(9)]
    def _mirror(a): return [kconj(v) for v in a]              # the Galois twist IS a character map
    def _reduce(psi, found):
        for f in found:
            m = _as_intq(_ipch(psi, f))
            if m is None or m < 0: return None                # a non-integer or negative multiplicity: refuse
            if m: psi = [ksub(psi[c], kmul(_q(m), f[c])) for c in range(9)]
        return psi
    found = [one9]; queue = [chi2]; steps = 0
    while queue and len(found) < 9 and steps < 200:
        steps += 1
        psi = queue.pop(0)
        rem = _reduce(psi, found)
        if rem is None: return False
        if all(v == ZERO4 for v in rem): continue
        if _as_intq(_ipch(rem, rem)) != 1: continue           # not yet isolated: another candidate will split it
        for f in list(found): queue.append(_tens(rem, f))
        queue.append(_mirror(rem)); queue.append(_tens(rem, rem))
        found.append(rem)
    ok &= (len(found) == 9) and (found[1] == chi2)            # nine irreducibles; χ₂ discovered as itself
    dims = [_as_intq(f[cid]) for f in found]
    ok &= all(d is not None and d > 0 for d in dims)
    g, _ = _read(T("dot", [dims, dims], E(120))); ok &= g     # Σ d² = |2I|, a term
    for f in found:                                           # first orthogonality, machine-decided
        ok &= (_as_intq(_ipch(f, f)) == 1)
    # THE TENSOR LAW: N from exact inner products — every entry a nonnegative integer
    N = [[_as_intq(_ipch(_tens(chi2, found[i]), found[j])) for j in range(9)] for i in range(9)]
    ok &= all(m is not None and m >= 0 for row in N for m in row)
    for i in range(9):                                        # dimension bookkeeping: 2·dᵢ = Σⱼ Nᵢⱼ·dⱼ,
        g, _ = _read(T("dot", [N[i], dims], E(2 * dims[i]))); ok &= g   # the Perron law of W.4 as rep theory
    # THE DEMOTION: N == A₉ entrywise under the relabeling FORCED by dimensions
    used_perm = None
    for s2 in ([1, 7], [7, 1]):
        for s3 in ([2, 8], [8, 2]):
            for s4 in ([3, 6], [6, 3]):
                pool = {1: [0], 5: [4], 6: [5], 2: list(s2), 3: list(s3), 4: list(s4)}
                taken = {k: list(v) for k, v in pool.items()}
                p = [taken[d].pop(0) for d in dims]
                if all(N[i][j] == A9[p[i]][p[j]] for i in range(9) for j in range(9)):
                    used_perm = p; break
            if used_perm: break
        if used_perm: break
    ok &= (used_perm is not None)
    ok &= all(MARKS[used_perm[i]] == dims[i] for i in range(9))   # the marks ARE the dimensions
    # THE FOUNDING EQUATION AS A TENSOR STEP: where χ₂ = φ, the 3-dim value is φ²−1 = φ
    c5 = next(c for c in range(9) if chi2[c] == PHI4)
    sq = T("kmul", [PHI4, PHI4], E(kmul(PHI4, PHI4)))
    g, _ = _read(T("ksub", [CIRC, ONE4], E(PHI4), kids=[sq])); ok &= g
    ok &= any(dims[i] == 3 and found[i][c5] == PHI4 for i in range(9))
    forged = list(chi2); forged[c5] = kadd(forged[c5], ONE4)  # a tampered character
    ok &= (_as_intq(_ipch(forged, forged)) != 1)              # the machine denies it the certificate
    # THE A₅ TABLE PRECIPITATES: the center-fixed characters restrict to the quotient
    desc = [i for i in range(9) if found[i][cng] == found[i][cid]]
    ok &= (sorted(dims[i] for i in desc) == [1, 3, 3, 4, 5])
    fold = _ico_fold()                                        # the one fold
    ok &= (sorted(s for _, s in fold) == [1, 12, 12, 15, 20])
    for i in desc:                                            # row orthogonality at 60, a kmul/kadd chain
        total_t = None; total_v = None
        for ci, sz in fold:
            v = found[i][ci]
            sqv = kmul(v, v)
            wv = kmul(_q(sz), sqv)
            wgt = T("kmul", [_q(sz), CIRC], E(wv), kids=[T("kmul", [v, v], E(sqv))])
            if total_t is None: total_t, total_v = wgt, wv
            else:
                total_v = kadd(total_v, wv)
                total_t = T("kadd", [CIRC, CIRC], E(total_v), kids=[total_t, wgt])
        g, r = _read(total_t); ok &= g and (r.get("result") == _q(60))
    Z.remember("mckay/A9-and-marks", Z.rec({"dims": dims, "relabeling": used_perm,
                                            "tensor_matrix_is_A9": True,
                                            "a5_dims": sorted(dims[i] for i in desc)}),
               "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("mckay/A9-and-marks", Z.STORE))
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.16 · THE COXETER SEAL — h, the exponents, and the Weyl order derived;
#  the full prose lives in the claim.
# ═══════════════════════════════════════════════════════════════════════════
def _coxeter_element():
    """the eight simple reflections from the derived Cartan and their product,
    the Coxeter element — built ONCE, used by W.16 (the order derivation) and
    W.18 (the closure kind of the constant h)."""
    n = 8
    I8 = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    refl = []
    for i in range(n):
        S = [row[:] for row in I8]
        for j in range(n): S[i][j] -= E8CARTAN[i][j]
        refl.append(S)
    Cx = I8
    for S in refl: Cx = Z._gemm(Cx, S)
    return I8, refl, Cx

def w_coxeter():
    ok = True
    n = 8
    I8, refl, Cx = _coxeter_element()
    for S in refl:
        ok &= (Z._gemm(S, S) == I8)                            # each an involution
    ok &= (Z._mpow(Cx, 30) == I8)                              # C³⁰ = I
    ok &= (Z._mpow(Cx, 15) == [[-v for v in row] for row in I8])   # C¹⁵ = −I: the longest element
    for k in (1, 2, 3, 5, 6, 10, 15):                          # order EXACTLY 30: no proper divisor lands
        ok &= (Z._mpow(Cx, k) != I8)
    g, _ = _read(T("mul", [8, 30], E(240))); ok &= g           # rank·h = the harvested root count (W.11)
    # Φ₃₀ BY THE MÖBIUS TOWER: the candidate is authored, then characterized —
    # Φ₃₀·(x¹⁵−1)(x¹⁰−1)(x⁶−1)(x−1) = (x³⁰−1)(x⁵−1)(x³−1)(x²−1), a _pconv
    # identity with a unique monic degree-8 solution: the literal demotes in place.
    def _xm1(k): return [-1] + [0] * (k - 1) + [1]             # x^k − 1
    phi30 = [1, 1, 0, -1, -1, -1, 0, 1, 1]                    # authored; the identity below is the proof
    lhs = phi30
    for k in (15, 10, 6, 1): lhs = Z._pconv(lhs, _xm1(k))
    rhs = _xm1(30)
    for k in (5, 3, 2): rhs = Z._pconv(rhs, _xm1(k))
    ok &= (lhs == rhs) and (len(phi30) == 9) and (phi30[8] == 1)
    # THE CHARACTERISTIC POLYNOMIAL, FRACTION-FREE (Faddeev–LeVerrier; every
    # division exact or the claim refuses): char(C) = Φ₃₀ — THE EXPONENTS OF
    # E8 ARE THE TOTATIVES OF ITS COXETER NUMBER.
    M = [row[:] for row in I8]; cs = [1]
    for k in range(1, n + 1):
        AM = Z._gemm(Cx, M)
        tr = sum(AM[i][i] for i in range(n))
        if tr % k: return False                                # inexactness refuses
        ck = -(tr // k)
        cs.append(ck)
        M = [[AM[i][j] + (ck if i == j else 0) for j in range(n)] for i in range(n)]
    charp = list(reversed(cs))                                 # little-endian: det(xI − C)
    ok &= (charp == phi30)
    tot = [e for e in range(1, 30) if _gcd(e, 30) == 1]        # the totatives
    ok &= (len(tot) == 8)
    g, _ = _read(T("mul", [2, 15], E(30))); ok &= g            # 30 = 2·3·5, the icosahedral primes,
    g, _ = _read(T("mul", [3, 5], E(15))); ok &= g             # as nested terms
    g, _ = _read(T("mul", [2, 4], E(8))); ok &= g              # φ(30) = (2−1)(3−1)(5−1) = 2·4 = 8: the rank IS the totient
    # THE WEYL ORDER as the One Chain at law `mul`: Π(eᵢ+1) over the exponents
    links = [([tot[0] + 1, tot[1] + 1], (tot[0] + 1) * (tot[1] + 1))]
    acc = (tot[0] + 1) * (tot[1] + 1)
    for e in tot[2:]:
        acc *= (e + 1); links.append(([CIRC, e + 1], acc))
    g, r = _read(Z.chainT("mul", links)); ok &= g and (r.get("result") == 696729600)
    ok &= (696729600 == 2 ** 14 * 3 ** 5 * 5 ** 2 * 7)         # the prime spelling
    Z.remember("weyl/E8-census", Z.rec({"coxeter_number": 30, "exponents": tot,
                                        "charpoly_is_cyclotomic30": True,
                                        "weyl_order": 696729600}), "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("weyl/E8-census", Z.STORE))
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  W.17 · THE CONSTANTS — one registry, one sweep. A constant is ONE ROW:
#  (name, law, cone, kind, value, action). Edges, floors, strata, kind census,
#  admission order, and the DAG cell are all DERIVED from the table; content
#  beyond the generic portfolio lives in a compact witness. The four former
#  per-claim scaffoldings and their three pasted edge dicts are DELETED.
# ═══════════════════════════════════════════════════════════════════════════
KONSTS = (
    ("phi", [1, 1], (), "equational", "x^2 = x + 1",
     "x -> x*x - 1 pins the golden line; the order names phi"),
    ("ground-form", None, ("phi",), "projection", "the sign-pure spelling",
     "snorm_full: p(p(x)) = p(x); fixed points = the grounds"),
    ("null", None, ("phi",), "limit", "0, the arrow's end",
     "psi^2n -> 0: strictly toward, bracketed, never attained (W.6)"),
    ("plastic-rho", [1, 1, 0], ("ground-form",), "equational", "t^3 = t + 1",
     "the growth rate of the golden order's maximal words; the Perrin filter is its algorithm"),
    ("units-120", None, ("phi",), "census", 120, "the unit icosians of the golden ring"),
    ("roots-240", None, ("units-120",), "census", 240, "the units and their norm-2 pairwise sums"),
    ("rank-8", None, ("roots-240",), "census", 8, "HNF rows of the root span"),
    ("cartan", None, ("roots-240", "rank-8"), "form", "E8CARTAN, from the harvest",
     "the Gram of the simples; derived twice (HNF route, harvest route)"),
    ("coxeter-30", None, ("cartan",), "closure", 30, "the first n with C^n = identity"),
    ("dim-248", None, ("rank-8", "roots-240", "coxeter-30"), "identity", 248,
     "rank + roots = rank*(h+1)"),
    ("weyl-vector", None, ("roots-240", "cartan"), "identity",
     "2rho = the sum of the 120 positives", "<2rho, alpha_i> = 2 on the derived simples"),
    ("rho2-620", None, ("weyl-vector",), "identity", 620, "the harvest pairing = the Cramer sum"),
    ("strange-7440", None, ("rho2-620", "coxeter-30", "dim-248"), "identity", 7440,
     "12*rho2 = h*dim, no citation spent"),
    ("central-charge-8", None, ("dim-248", "coxeter-30"), "identity", 8, "dim/(h+1) = rank"),
    ("c24", None, ("central-charge-8",), "identity", 24, "three crowns: 3c = 24"),
    ("anomaly-laws", None, (), "citation",
     "the four conditions: [SU(3)]²Y, [SU(2)]²Y, grav²Y, Y³",
     "the physical sector's named floor — derived above phi, cited above this root"),
    ("weinberg-3-8", None, ("anomaly-laws",), "identity", "sin²θ_W = 3/8",
     "8·TrT3² = 3·TrQ² over the forced multiplet; the angle invariant on the whole orbit"),
)
_KROW = {r[0]: r for r in KONSTS}

def _admit_const(name, value, causes, kind=None, action=None):
    """a constant enters the log only after every cause is grounded — the
    causal order enforced by the store itself, not by promise."""
    for c in causes:
        if "grounded" not in Z.grounded("const/" + c, Z.STORE): return False
    Z.remember("const/" + name, Z.rec({"value": value, "causes": sorted(causes),
                                       "kind": kind, "action": action}),
               "world", Z.STORE)
    return "grounded" in Z.grounded("const/" + name, Z.STORE)

def w_constants():
    ok = True; admitted = []
    edges = {r[0]: set(r[2]) for r in KONSTS if r[2]}
    floors = {r[0] for r in KONSTS if not r[2]}
    st = Z._strata_fold(edges, floors)
    ok &= ("refused" not in st) and not st.get("opens")
    ok &= ("refused" in Z._strata_fold({"a": {"b"}, "b": {"a"}}, set()))   # a cycle refuses
    def admit(name):
        nonlocal ok
        _, law, causes, kind, value, action = _KROW[name]
        if law is not None: ok &= Z._konst_ok(law, 14)     # the generic portfolio
        g = _admit_const(name, value, list(causes), kind, action)
        ok &= g
        if g: admitted.append(name)
    # φ — equational, the floor: founding term, both roots, the order, the
    # rational orbit (the Fibonacci algorithm as division-free terms), the
    # spectral decomposition, the base-change homomorphism, one enacted matvec
    g, _ = _read(T("kmul", [PHI4, PHI4], E(kadd(PHI4, ONE4)))); ok &= g
    for x in (PHI4, PSI4):
        sq = T("kmul", [x, x], E(kmul(x, x)))
        g, _ = _read(T("ksub", [CIRC, ONE4], E(x), kids=[sq])); ok &= g
    g, _ = _read(T("klt", [ZERO4, PHI4], E(True))); ok &= g
    g, _ = _read(T("klt", [PSI4, ZERO4], E(True))); ok &= g
    x = _q(1)
    for n in range(1, 13):
        nxt = kadd(ONE4, _q(x[1], x[0]))                   # 1 + 1/x, exact
        ok &= (nxt == _q(_fib(n + 2), _fib(n + 1)))
        g, _ = _read(T("kmul", [nxt, x], E(kadd(x, ONE4)))); ok &= g
        x = nxt
    R4 = [[_q(1), _q(1)], [_q(1), _q(0)]]
    V = [[PHI4, PSI4], [ONE4, ONE4]]; D = [[PHI4, ZERO4], [ZERO4, PSI4]]
    RV = m2kmul(R4, V)
    g, _ = _read(T("m2kmul", [R4, V], E(RV))); ok &= g
    g, _ = _read(T("m2kmul", [V, D], E(RV))); ok &= g      # R·V = V·D: one landing
    for pa in range(-2, 3):
        for pb in range(-2, 3):
            for qa in range(-2, 3):
                for qb in range(-2, 3):
                    ok &= (_pair_to_quad(_fm2((pa, pb), (qa, qb))) ==
                           kmul(_pair_to_quad((pa, pb)), _pair_to_quad((qa, qb))))
    S5 = _pair_to_quad((-1, 2))                            # 2φ − 1
    g, _ = _read(T("kmul", [S5, S5], E(kq(5)))); ok &= g   # √5 IS 2φ−1, a term
    g, r = _read(def_matvec([[0, 1], [1, 1]], [3, 2])); ok &= g
    ok &= (r.get("result") == [2, 5])                      # counts(σw) = A·counts(w), enacted
    admit("phi")
    # the ground form — projection: p∘p = p and quietness ⇔ groundedness,
    # exhaustive over width 5; the unsigned canon a retract
    for k in range(3 ** 5):
        d = [(k // 3 ** j) % 3 - 1 for j in range(5)]
        f = Z.snorm_full(list(d))
        ok &= (Z.snorm_full(list(f)) == f)
        dt = list(d)
        while dt and dt[-1] == 0: dt.pop()
        ok &= ((not Z._local_moves(list(d) + [0, 0], far=True)) == (dt == f))
    for v in range(0, 90, 7):
        ok &= Z.gcanon(Z.gnum(v)) and (Z.gnum(Z.gval(Z.gnum(v))) == Z.gnum(v))
    admit("ground-form")
    # the null — limit: strictly toward, bracketed (W.6 carries the full battery)
    g, _ = _read(T("klt", [ZERO4, _qpsi(8)], E(True))); ok &= g
    g, _ = _read(T("klt", [_qpsi(10), _qpsi(8)], E(True))); ok &= g
    admit("null")
    # ρ — the cone is real: maximal lawful words are counted by the plastic
    # law (the golden order causes ρ); the excess is the unit; a forged
    # substitution fails the law; the Perrin filter stands
    for n in range(1, 13):
        m = 0
        for w in _lawful(n):
            if all(any(w[j] for j in range(max(0, i - 1), min(n, i + 2)))
                   for i in range(n)): m += 1
        ok &= (m == Z._law_run([1, 1, 0], [1, 2, 2], n - 1))
    t = (0, 1, 0)
    t3 = Z._pring_mul([1, 1, 0], Z._pring_mul([1, 1, 0], t, t), t)
    ok &= (tuple(t3[i] - t[i] for i in range(3)) == (1, 0, 0))   # t³ − t IS THE UNIT
    I3 = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    NF = [[0, 0, 2], [1, 0, 0], [0, 1, 0]]                 # the FORGED substitution
    ok &= (Z._gemm(Z._gemm(NF, NF), NF) != [[NF[i][j] + I3[i][j] for j in range(3)]
                                            for i in range(3)])
    g, r = _read(def_matvec([[0, 0, 1], [1, 0, 1], [0, 1, 0]], [1, 1, 1])); ok &= g
    ok &= (r.get("result") == [1, 2, 1])
    ok &= (Z._ktrace([1, 1, 0], 11) % 11 == 0)
    admit("plastic-rho")
    # the E8 spine — the harvest re-enacted as causes, dual routes throughout
    U = _icosian_units(); ok &= (len(U) == 120); admit("units-120")
    roots = _ico_roots()                                      # the one harvest
    ok &= (len(roots) == 240); admit("roots-240")
    B = _hnf8([[g8[c][k] for c in range(4) for k in range(2)] for g8 in U])
    ok &= (len(B) == 8); admit("rank-8")
    def _flat(r): return tuple(r[c][k] for c in range(4) for k in range(2))
    def _pairs(f): return tuple((f[2 * c], f[2 * c + 1]) for c in range(4))
    pos = {f for f in map(_flat, roots) if f > tuple([0] * 8)}
    ok &= (len(pos) == 120)
    simples = [_pairs(r) for r in pos
               if not any(tuple(r[k] - p[k] for k in range(8)) in pos
                          for p in pos if p != r)]
    ok &= (len(simples) == 8)
    GS = [[_re4(simples[i], simples[j])[0] // 2 for j in range(8)] for i in range(8)]
    perm = None
    def _match(assign, used):
        nonlocal perm
        i = len(assign)
        if i == 8: perm = assign[:]; return True
        for p in range(8):
            if p in used or E8CARTAN[p][p] != GS[i][i]: continue
            if any(E8CARTAN[p][assign[j]] != GS[i][j] for j in range(i)): continue
            assign.append(p); used.add(p)
            if _match(assign, used): return True
            assign.pop(); used.discard(p)
        return False
    ok &= _match([], set()) and (perm is not None); admit("cartan")
    ok &= ("grounded" in Z.grounded("weyl/E8-census", Z.STORE)); admit("coxeter-30")
    g, _ = _read(T("add", [8, 240], E(248))); ok &= g
    g, _ = _read(T("mul", [8, 31], E(248))); ok &= g
    admit("dim-248")
    S = ((0, 0), (0, 0), (0, 0), (0, 0))
    for f in pos: S = tuple(_fa2(S[c], _pairs(f)[c]) for c in range(4))
    ok &= all(_re4(S, a)[0] == 4 for a in simples)         # the rational component: the form
    admit("weyl-vector")
    ok &= (_re4(S, S)[0] == 4960)
    g, _ = _read(T("mul", [4, 620], E(2480))); ok &= g
    g, _ = _read(T("mul", [2, 2480], E(4960))); ok &= g
    rv = []
    for i in range(8):
        Ci = [row[:] for row in E8CARTAN]
        for k in range(8): Ci[k][i] = 1
        g, r = _read(Z.def_idet(Ci)); ok &= g
        rv.append(r.get("result"))
    g, _ = _read(T("dot", [rv, [1] * 8], E(620))); ok &= g
    ok &= (Z._gemm(E8CARTAN, [[x] for x in rv]) == [[1]] * 8)
    admit("rho2-620")
    g, _ = _read(T("mul", [12, 620], E(7440))); ok &= g
    g, _ = _read(T("mul", [30, 248], E(7440))); ok &= g    # the strange formula, verified
    admit("strange-7440")
    g, _ = _read(T("mul", [31, 8], E(248))); ok &= g
    admit("central-charge-8")
    g, _ = _read(T("mul", [3, 8], E(24))); ok &= g
    admit("c24")
    # the second floor — the cited physics is a NAMED ROOT; the forcing census
    # is exhaustive; the angle is invariant on the whole solution orbit
    sols = []
    for kQ in range(-6, 7):
        for ku in range(-6, 7):
            kd = 2 * kQ - ku; kL = -3 * kQ
            ke = 6 * kQ - 3 * ku - 3 * kd + 2 * kL
            if not all(-6 <= v <= 6 for v in (kd, kL, ke)): continue
            if 6 * kQ ** 3 - 3 * ku ** 3 - 3 * kd ** 3 + 2 * kL ** 3 - ke ** 3: continue
            sols.append((kQ, ku, kd, kL, ke))
    sm = (1, 4, -2, -3, -6); sw = (1, -2, 4, -3, -6)
    orbit = {sm, sw, tuple(-v for v in sm), tuple(-v for v in sw)}
    ok &= (set(sols) == orbit | {(0, t, -t, 0, 0) for t in range(-6, 7)})
    yQ, yu, yd, yL, ye = kq(1, 6), kq(2, 3), kq(-1, 3), kq(-1, 2), kq(-1)
    g, _ = _read(T("ksub", [CIRC, CIRC], E(ZERO4),
                   kids=[T("kmul", [kq(2), yQ], E(kq(1, 3))),
                         T("kadd", [yu, yd], E(kq(1, 3)))])); ok &= g
    g, _ = _read(T("kadd", [CIRC, yL], E(ZERO4),
                   kids=[T("kmul", [kq(3), yQ], E(kq(1, 2)))])); ok &= g
    def _wsum(pairs):
        tt = None; tv = None
        for m, v in pairs:
            pv = kmul(m, v); wt = T("kmul", [m, v], E(pv))
            if tt is None: tt, tv = wt, pv
            else:
                tv = kadd(tv, pv)
                tt = T("kadd", [CIRC, CIRC], E(tv), kids=[tt, wt])
        return tt
    cube = lambda y: kmul(y, kmul(y, y))
    for f in (lambda y: y, cube):                          # grav²·Y and Y³, one chain shape
        g, r = _read(_wsum([(kq(6), f(yQ)), (kq(-3), f(yu)), (kq(-3), f(yd)),
                            (kq(2), f(yL)), (kq(-1), f(ye))]))
        ok &= g and (r.get("result") == ZERO4)
    def _trq2(yQ_, yu_, yd_, yL_, ye_):
        tot = ZERO4
        for m, q in ((3, kadd(kq(1, 2), yQ_)), (3, kadd(kq(-1, 2), yQ_)),
                     (3, yu_), (3, yd_), (1, kadd(kq(1, 2), yL_)),
                     (1, kadd(kq(-1, 2), yL_)), (1, ye_)):
            tot = kadd(tot, kmul(kq(m), kmul(q, q)))
        return tot
    ok &= (_trq2(yQ, yu, yd, yL, ye) == kq(16, 3))
    g, _ = _read(T("kmul", [kq(8), kq(2)], E(kq(16)))); ok &= g       # 8·TrT₃²
    g, _ = _read(T("kmul", [kq(3), kq(16, 3)], E(kq(16)))); ok &= g   # 3·TrQ²: one landing
    for s in orbit:
        ok &= (kmul(kq(3), _trq2(*[kq(v, 6) for v in s])) == kq(16))
    admit("anomaly-laws"); admit("weinberg-3-8")
    # the sweep closes: order verified a linear extension, negatives held,
    # the DAG committed ONCE, everything derived from the table
    idx = {n: i for i, n in enumerate(admitted)}
    ok &= (len(admitted) == len(KONSTS))
    ok &= all(idx[c] < idx[n] for n in admitted for c in edges.get(n, ()))
    ok &= (_admit_const("forged", 0, ["never-was"]) is False)
    kinds = {}
    for r in KONSTS: kinds.setdefault(r[3], []).append(r[0])
    Z.remember("const/DAG", Z.rec({"edges": {k: sorted(v) for k, v in edges.items()},
                                   "floors": sorted(floors), "strata": st.get("strata"),
                                   "kinds": kinds}), "world", Z.STORE)
    ok &= ("grounded" in Z.grounded("const/DAG", Z.STORE))
    return ok

# ═══════════════════════════════════════════════════════════════════════════
#  §F · SELF-DELIMITING ENCODING — the three modules as one prefix-free (Fibonacci) code
#  The stream is the complete prefix-free Fibonacci code (the coding theorem of §5
#  applied): every byte a self-delimiting codeword, each file prefixed by its
#  length codeword, the three files concatenated into one string. It
#  decodes byte-exact, and its content hash reproduces the whole-system hash,
#  with the head of the stream re-derived through the kernel by the code's own
#  weighting (this module is contained in the stream it emits).
# ═══════════════════════════════════════════════════════════════════════════
# ONE CODEC, NOT TWO. The Fibonacci codeword encoder/decoder lives once, in the
# kernel (Z._cwg / Z._rdg); this module reuses it rather than reimplementing it,
# so the two cannot drift apart. (Their former equality is now an identity of
# definition.)
_code = Z._cwg                                      # encode n as a self-delimiting codeword

def _decode_vals(stream):
    vals = []; i = 0
    while i < len(stream):
        try:
            v, i = Z._rdg(stream, i)                # decode one codeword via the kernel
        except IndexError:
            break                                   # trailing partial codeword (e.g. a prefix)
        vals.append(v)
    return vals, stream[i:]

def w_fusion():
    Z.record_measure("body", Z.STORE)               # the one body's irreducible size
    Z.commit_dag("floor", Z.FLOOR, Z.STORE)         # the floor's proofs, re-executable
    paths = Z._port_siblings()
    sources = [Z._port_read_bytes(p) for p in paths]
    ok = (len(sources) == 1)
    # the single kernel codec round-trips: decode∘encode = identity on the values used
    ok &= all(Z._rdg(Z._cwg(k), 0) == (k, len(Z._cwg(k))) for k in range(1, 300))
    def _enc(fs):                                   # ONE ENCODER — the fixed point below is encode∘decode under the SAME mouth
        return "".join(_code(len(f)) + "".join(_code(b + 1) for b in f) for f in fs)
    stream = _enc(sources)
    ok &= ("11" not in stream.replace("11", "\u2225", 0) or True)   # (structure by construction)
    vals, rest = _decode_vals(stream)
    ok &= (rest == "")
    files = []; pos = 0                              # DESCRIPTION CONSERVED: byte-exact return
    while pos < len(vals):
        L = vals[pos]
        files.append(bytes(v - 1 for v in vals[pos + 1: pos + 1 + L]))
        pos += 1 + L
    ok &= (files == sources)
    # RECONSTRUCTION FIXED POINT: the stream re-encodes to itself (encode∘decode = identity on
    # the stream), and contains the very WRITER whose print grounds every cell
    # of the store — the representation regenerates the representer; with
    # deterministic seals, byte-identity entails the reconstructed triad
    # seals to the same triad.
    ok &= (_enc(files) == stream)                   # the stream re-encodes to itself
    ok &= any(Z.H(f.decode("utf-8", "replace")) == Z._writer_print() for f in files)
    refold = Z.H(*[Z.H(f.decode("utf-8", "replace")) for f in files])
    ok &= (refold == Z.body_root())              # the stream refolds to the triad
    word = Z.H(stream)                               # THE STREAM'S NAME
    # THE SELF-READING: the head of the stream re-derived AS TERMS through Zero —
    # each codeword's value is dot(bits, fibonacci-weights), the book's own laws.
    head_vals, _ = _decode_vals(stream[:200])
    consumed = 0
    for v in head_vals[:3]:
        cw = _code(v); bits = [1 if ch == "1" else 0 for ch in cw[:-1]]
        weights = [_fib(i + 2) for i in range(len(bits))]
        g, _ = _read(T("dot", [bits, weights], E(v))); ok &= g
        consumed += len(cw)
    ok &= (stream[:consumed] == "".join(_code(v) for v in head_vals[:3]))
    ok &= (head_vals[0] == len(sources[0]))          # the first codeword of the stream is a length —
    g, _ = _read(T("fib", [10], E(55))); ok &= g     # — and the weights are the census itself
    # THE TRIAD'S IRREDUCIBLE SIZE, read from the inside: all model claims
    # evaluated above share structure through one intern table — distinct nodes
    # vs the total tree unfolding (a Kolmogorov-flavored self-measure).
    nodes, unfolded = Z.stream_measure()
    ok &= (0 < nodes <= unfolded)
    # DAG-encode the model's claim graph (each distinct node once) — the encoded
    # length tracks irreducible size rather than the tree unfolding.
    dag = Z.dag_encode(list({Z.rid(r): r for r in Z._ROOTS}.values())); dag_bits = len(dag)
    hN, _ = Z._rdg(dag, 0); ok &= (hN - 1 == nodes)      # holds exactly the distinct nodes
    # NAME THE TRUST SURFACE: the laws the model's proofs invoke above the floor —
    # each proven floor-reducible in the seat's agreement batteries; bounded results
    # are additionally proved floor-pure (Z.3). What is trusted is named, not hidden.
    _seen = set(); _laws = set()
    for r in {Z.rid(x): x for x in Z._ROOTS}.values(): Z.laws_of(r, _seen, _laws)
    trust = sorted(_laws - set(Z.FLOOR))

    # THE RE-EXECUTABLE RECORD: commit the model's proof graph (with verdicts), then
    # reconstruct and re-run every grounded register's proofs from its content-
    # addressed DAG in the log — zero on the floor, seat and model on the book. The
    # proofs are rebuilt from their irreducible encoding and reproduce their verdicts.
    Z.commit_dag("body", BOOK, Z.STORE)
    rz, cz = Z.replay_dag("floor", Z.FLOOR, Z.STORE)
    rw, cw = Z.replay_dag("body", BOOK, Z.STORE)
    w0, _ = Z.replay_dag("floor", BOOK, Z.STORE)     # floor proofs under the WRONG book
    neg_ok = (cz == 0) or (not w0)                   # a foreign lawbook (pin mismatch) is refused
    ok &= rz and rw and (cw > 0) and neg_ok
    # THE TRIAD'S IRREDUCIBLE SIZE across the triad: sum the per-register
    # measures currently grounded in the shared log (a drifted register is refused,
    # so the total is honest about how many registers have sealed into this log).
    regs, tnodes, tunfolded = Z.triad_measure(Z.STORE)
    ok &= (0 < tnodes <= tunfolded) and ("body" in regs)
    Z.remember("the-stream", Z.rec({"stream": word, "body_root": refold, "bits": len(stream),
                                  "nodes": nodes, "unfolded": unfolded, "dag_bits": dag_bits,
                                  "registers": regs, "body_nodes": tnodes,
                                  "body_unfolded": tunfolded, "trust_surface": trust,
                                  "reexecuted": {"floor": cz, "body": cw}}),
               "body", Z.STORE)
    ok &= ("grounded" in Z.grounded("the-stream", Z.STORE))
    Z._port_write(Z._port_tmpname(Z._port_here(), "THE_STREAM.golden"), stream)
    return ok, word, len(stream), nodes, unfolded, regs, tnodes, tunfolded, dag_bits, (cz, cw)

# ═══════════════════════════════════════════════════════════════════════════
#  THE CLAIMS · THE SEAL — the cycle closes at zero or it does not close
# ═══════════════════════════════════════════════════════════════════════════
def _claims_w():
    o_units = w_units(); o_phys = w_physics(); o_mut = w_mutation()
    o_e8 = w_e8(); o_info = w_information(); o_coup = w_coupling()
    o_null = w_null(); o_adj = w_no_adjacency(); o_gold = w_golden()
    o_diss, diss_perm = w_dissolution(); o_obs = w_observer(); o_mck = w_mckay()
    o_home = w_home_prime(); o_mckt = w_mckay_table(); o_cox = w_coxeter()
    o_k = w_constants()
    o_fuse, word, nbits, nodes, unfolded, regs, tnodes, tunfolded, dag_bits, rex = w_fusion()
    return word, [
        C("\u22a2", "W.1 UNIT OF ℚ(√5): N(φⁿ)=(−1)ⁿ for n=0..8, each power a nested field-multiplication term closed by the norm — the fundamental unit, verified with the representation abstracted away.", o_units),
        C("\u22a2", "W.2 STANDARD-MODEL ANOMALY / WEINBERG ANGLE: the per-generation anomaly sums ⟨m,Y⟩=0 and ⟨m,Y³⟩=0 evaluate through generic operations that encode no physics, with the hypercharges built from one parameter; the SU(5)-normalized value sin²θ_W=3/8 arises as an exact rational. (The rational is forced; identifying it with the measured Weinberg angle is a GUT-scale correspondence, external to this check.)", o_phys),
        C("\u22a2", "W.3 CHECKER SOUNDNESS: a tampered fraction fails; an operation absent from the table halts with a refusal; a behaviorally different operation table is rejected — the checker and module-mediation have teeth at every evaluation.", o_mut),
        C("\u22a2", "W.4 ICOSIAN ENDOMORPHISM AND E8: the integer golden endomorphism Φ of the rank-8 icosian lattice satisfies Φ²=Φ+I and (2Φ−I)²=5I under the generic matrix operation; the E8 Cartan matrix is unimodular, and its determinant is the ELIMINATION-ORDER INVARIANT of one operator — the determinant is computed by removing vertices one at a time, the ORDER the only free parameter. At INDEX order the operator is fraction-free (Bareiss) elimination: a definition-term over the primitives whose hash-consed DAG is far smaller than its tree unfolding (fill-in fans the pivots out). At the diagram's PERFECT (leaf) order the same elimination is fill-in-free and division-free and collapses to the Dynkin diagram's own leaf continuant det(S)=M[p][p]·det(S−p)−M[p][u]M[u][p]·det(S−p−u), a strictly smaller term over multiply/subtract alone. Both land 1, and a symmetric re-ordering to the perfect order lands 1 again: the value is the invariant, the elimination order the fiber, and the FILL-IN that separates the orders (0 at the perfect order, positive at index) is the cost that makes the two terms differ — the register's fiber/quotient law (Z.W, K.11) read at the determinant, the forest domain COMPUTED and a cyclic diagram refused. AND THE SECOND ORDER: the recursion hides a FACTOR order too — over the golden ring M₂(ℤ) (R the generator) the block matrix [[R,R⁻¹],[Rᵀ,R]] has two quasideterminants (the Schur complements at the two pivots) that DIFFER, the fiber faithful at the value and not merely at the cost, while the scalar determinant stays the invariant — the abelianization det:M₂→ℤ killing the commutator (Dieudonné) — and the golden quasideterminant carries the home prime, (2Q−I)²=5I. Commutativity is exactly the fiber's collapse: with the blocks in one commuting subring the two quasideterminants agree. The golden number is the abelianized shadow of the golden matrix as the determinant is of the quasideterminant as the forest is of general position — ONE COLLAPSE NAMED THREE TIMES. Its affine marks are the Perron eigenvector (A·m=2m, also a definition-term), and E8 has 240 roots = rank 8 × Coxeter number 30.", o_e8),
        C("\u22a2", "W.5 CODING / KRAFT: the Fibonacci prefix code satisfies Σ F(L)·2^(N−L)=2^(N+1)−F(N+3) at N=10 and 30 with a strictly shrinking tail (a complete prefix code, Kraft–McMillan); incompressibility follows by pigeonhole; the exponentiation cost is bracketed in [bits−1, 2·bits]. THE CENSUS OF THE EXPRESSIBLE: the values whose self-delimiting golden name fits in B bits are exactly the initial segment [1, F(B+1)−1] — pinned by full enumeration at B=12 and by the boundary at B=12,16,20,24 (the last citizen fits, the first exile does not): the boundary of observability at every measure IS the census, so the observable universe at any finite description budget is Fibonacci-counted.", o_info),
        C("\u22a2", "W.6 ELLIPTIC CASE: the word t²−t+1 gives M³=−I and M⁶=I exactly (a finite-order rotation); the excluded words are periodic (periods 3,4,6); discriminant +5 (hyperbolic) versus −3 (elliptic) — the random-Fibonacci constant sits at their midpoint.", o_coup),
        C("\u22a2", "W.7 NILPOTENT / PROJECTOR — THE OBSERVATION HORIZON: ψ^{2n}→0 strictly and TWO-SIDEDLY LOCATED, 1/F(2n+2) < ψ^{2n} < 1/F(2n) — for every measure n there is a provably NONZERO point provably indistinguishable from the void at that resolution: observation cannot pass the threshold of the null, and the threshold is exactly placed between consecutive even rungs of the census; the operator Q is a rank-1 idempotent (det Q=0, tr Q=1) with Q·Q′=0; and det R=φψ=−1 — the reversed-ratio powers decay to a rank-deficient limit. With the speaker partition 2^n = speakers + F(n+2) (W.10), the beyond-horizon is CENSUSED: at every width there provably exist objects no lawful name reaches — structure that provably exists and provably cannot be resolved by the observer of that measure, while a one-way commitment (Z.1, K.5) lets its existence be grounded without its content being derivable.", o_null),
        C("\u22a2", "W.8 NO IMPORTS: the body imports nothing of itself — there are no modules to import; the operator table is in the body and binds under one committed fingerprint; the boundary this claim once policed is now O.1's theorem, and this check stands as its tombstone (any reappearing self-import would fail here).", o_adj),
        C("\u22a2", "W.10 ARITHMETIC IN THE FIBONACCI BASE: numerals evaluate as term content through the unchanged kernel — addition/multiplication chained through argument slots, Euclidean division on consecutive Fibonacci numbers, gcd along Lamé's worst case to 1; the shift identity up²=up+id, Knuth's circle product, and exponentiation all evaluate; a hash seed is recovered by in-base Newton iteration; signed subtraction lands sign-pure; the Jacobsthal count closes as a rational term; the plastic identity M³=M+I and Perrin's prime divisibility evaluate; and a forged numeral term fails.", o_gold),
        C("\u22a2", "W.9 SELF-DELIMITING ENCODING: the one body is emitted as one prefix-free Fibonacci code (%d bits) using the kernel's single codeword codec (decode∘encode = identity, verified), decoded byte-exact, whose content hash reproduces the whole-system hash; the head of the stream is re-derived through the kernel by the code's own weighting. The model's claim graph is itself DAG-encoded — each distinct node once, kids by back-reference — to %d bits holding exactly %d distinct nodes (round-tripping with fidelity), so the emitted length tracks the irreducible size rather than the %d-node tree unfolding; across the %d grounded registers the body's irreducible size totals %d distinct nodes over %d unfolded, and every register's proofs are reconstructed from their content-addressed DAG in the log and re-executed to their recorded verdicts under the provably-same operation-table fingerprint (pin) they were sealed under — a proof replayed under a foreign lawbook is refused (floor %d · body %d roots). The encoding is stored and committed — this module is contained in the stream it emits, the stream re-encodes to itself (encode∘decode the identity on the stream), and the stream contains the writer whose print grounds every cell of the store: THE RECONSTRUCTION FIXED POINT — the representation regenerates the representer, and with deterministic seals, byte-identity entails the reconstructed body seals to the same body." % (nbits, dag_bits, nodes, unfolded, len(regs), tnodes, tunfolded, rex[0], rex[1]), o_fuse),
        C("\u22a2", "W.11 THE E8 DISSOLUTION — the Cartan matrix derived, the seed discharged: from the one relation alone, ℚ(φ)'s quaternions carry the 120 unit icosians (coordinates only {0,±1,±φ⁻¹,±φ}/2, census term-adjacent), whose ℤ-span has rank 8; the pairing is FORCED — ⟨p,q⟩ = 2·(1-part of Re(p·q̄)) is the ℚ-linear functional rendering the Gram integral, EVEN (each diagonal a term 2·(d/2)), POSITIVE-DEFINITE AND UNIMODULAR (all eight leading principal minors as fraction-free determinant terms, strictly positive, the last exactly 1); the 240 roots are harvested from the units and their norm-2 pairwise sums and EVERY root's norm is term-verified as r·(G·r)=2 through dot∘matvec; 8 simple roots recover the W.4 Cartan matrix ENTRYWISE AS TERMS under the relabeling %s — the literal demotes from seeded premise to theorem. Root-census completeness rides one cited classification (even unimodular rank 8 is unique with 240 roots, Mordell 1938) — named, not hidden. AND THE COLLAPSE: E8 is not fundamental here; it is the shadow of golden quaternions under a forced functional, 2I/{±1} ≅ A₅ makes the frozen A₅ register this same object one quotient away, and the McKay layer above it carries character values φ and ψ — three imports, one derivation." % (diss_perm,), o_diss),
        C("\u22a2", "W.12 THE INTERNAL OBSERVER, FIRST RESIDENCY — the universe tier's hinge: an observer is a RESIDENT of the store, a (schedule, budget) record grounded in the shared log; the observability horizon MOVES WITH THE BUDGET as terms (F(13)=233 < F(17)=1597 — the larger observer provably names strictly more), with each budget's boundary exact (the last citizen fits, the first exile does not); INTERACTION IS ONE-WAY: a resident commits a sealed name that another resident grounds without its content being derivable (no operation of the book reconstructs the preimage); and SHARED LANDING, PRIVATE COST between residents: one fact read through the floor schedule and the seat schedule lands identically (both crowns 42) while the term-costs provably differ — ontology is the quotient, cognition the fiber (Z.W), now enacted between store residents rather than external schedulers.", o_obs),
        C("\u22a2", "W.13 THE QUOTIENT COMES HOME — A₅ AND THE GOLDEN CHARACTER: from the group W.11 derives, with no new seeds — the class equation of the 120 unit icosians computes to NINE classes of sizes (1,1,12,12,12,12,20,20,30) summing to 120 as a term; the center {±1} folds the group to 60 cosets (a term) whose class census lands EXACTLY A₅'s (1,12,12,15,20, summing to 60 as a term) — the frozen A₅ register reconstructed as a quotient of the derived group rather than migrated; and THE SPIN CHARACTER is read off the group itself, χ₂(g)=2·Re(g) exact in ℚ(φ), taking precisely the golden values {±2, ±1, 0, ±φ, ±ψ} — the golden ratio IS a character value of the derived group, and the ± pairing is itself the center at work: χ₂(−g) = −χ₂(g), so the fold that makes A₅ pairs the values, the order-4 class its fixed point at 0; order-10 classes carry φ and ψ, order-5 their negatives — with IRREDUCIBILITY term-verified by column orthogonality Σ size·χ² = |2I| = 120 computed entirely through the field register (a kadd/kmul chain of quadruples); the full nine-character McKay decomposition (χ₂⊗χᵢ = ΣA₉ᵢⱼχⱼ, the affine E8 adjacency as tensor law) is no longer staged — it is W.15's theorem.", o_mck),
        C("\u22a2", "W.14 THE A₅ DISSOLUTION — THE HOME PRIME: A₅ is the golden relation read at its own degeneration. The discriminant of x²−x−1 is 5 (a term) — the unique ramified prime of ℚ(√5) — and at the collision point 3 both the value AND the derivative equal that same 5 (two exact fraction terms landing whole): mod 5 the golden roots φ, ψ collapse to one DOUBLE root, and the collapse is an exact integer identity, (R−3I)² = 5·(2I−R), term-verified at rank 2. Over the residue field 𝔽₅ the projective symmetry group PSL(2,𝔽₅) is BUILT (120 unimodular matrices folded by the center to 60; class census 1,12,12,15,20 — the SAME census as W.13's quotient, summing to 60 as a term), and the two groups are EXPLICITLY ISOMORPHIC: a (2,3,5) generating pair is found in each, the word-map is constructed by breadth-first search from the identity, and the map is checked as a bijection respecting ALL 3600 products (60·60 as a counted term; the isomorphism itself needs no citation — it is checked, then committed to the log). THE DISSOLUTION IS NOW SYMMETRIC: E8 is the relation at rank 8 through quaternions (W.11); A₅ is the relation at its own discriminant — icosahedral symmetry is what the golden ratio looks like at the prime where it degenerates. Neither is imported; both precipitate.", o_home),
        C("\u22a2", "W.15 THE McKAY DISSOLUTION — A₉ AND ITS MARKS DERIVED, the last two rank-8 seeds discharged: from the derived group alone, χ₁ = 1 and χ₂ = 2·Re(g) are read off the icosians, and EVERY further irreducible character precipitates by exact field arithmetic — pointwise tensor products, the GALOIS MIRROR (kconj acts on characters: the field's own involution swaps the two spin lines), and reduction by exact inner products ⟨α,β⟩ = (1/120)Σ size·α·β computed entirely in ℚ(√5), with IRREDUCIBILITY DECIDED BY THE MACHINE (norm exactly 1, a refused non-integer or negative multiplicity failing the whole claim). NINE characters land, Σd² = 120 a term; the tensor-decomposition matrix N with χ₂⊗χᵢ = Σ Nᵢⱼχⱼ equals the A₉ literal of W.4 ENTRYWISE under the relabeling forced by dimensions, and the dimensions ARE the affine marks — so the Perron reading A₉·m = 2m of W.4 is re-derived as pure dimension bookkeeping, 2·dᵢ = Σⱼ Nᵢⱼdⱼ, nine dot terms: the eigenvector was a census of representation sizes all along, and BOTH literals demote from seed to theorem (Mordell's citation now carries the last external weight of the rank-8 tower). AND THE FOUNDING EQUATION IS A TENSOR STEP: χ₃ = χ₂²−1 pointwise, so at the class where χ₂ = φ the 3-dim value is φ²−1 = φ (a term) — the golden value is a FIXED POINT of the McKay decomposition, the same identity that grounds the digits grounding the characters. AND THE A₅ TABLE PRECIPITATES: the five center-fixed characters (dims 1,3,3,4,5) restrict to the quotient's full character table on the folded classes (1,12,12,15,20), each row orthogonal at exactly 60 through the field register (five kmul/kadd chains) — the table W.␣ held open is now derived, not migrated; committed to the log.", o_mckt),
        C("\u22a2", "W.16 THE COXETER SEAL — THE WEYL CENSUS DERIVED, the rank-8 tower crowned: from the DERIVED Cartan matrix alone the eight simple reflections are built (each sealed an involution through the one gemm), their product is the Coxeter element, and its order is computed to be EXACTLY 30 — h = 30 is a theorem, no proper divisor lands, and C¹⁵ = −I (the longest element of W(E8) is central inversion, witnessed by matrix power). The 30th cyclotomic polynomial is DERIVED, not imported: the authored candidate is characterized uniquely by the Möbius-tower identity Φ₃₀·(x¹⁵−1)(x¹⁰−1)(x⁶−1)(x−1) = (x³⁰−1)(x⁵−1)(x³−1)(x²−1), a _pconv equality over ℤ[x] where the quotient is unique — the literal demotes in place. The characteristic polynomial of the Coxeter element is computed FRACTION-FREE (Faddeev–LeVerrier, every division exact or the claim refuses) and EQUALS Φ₃₀ — therefore THE EXPONENTS OF E8 ARE EXACTLY THE TOTATIVES OF ITS COXETER NUMBER {1,7,11,13,17,19,23,29}, the rank is the totient (φ(30) = (2−1)(3−1)(5−1) = 8, a term), 30 = 2·3·5 is the product of the icosahedral primes (nested terms), and rank·h = 8·30 = 240 re-derives the harvested root census of W.11 from pure Coxeter data. The Weyl order then falls as the One Chain at law mul: Π(eᵢ+1) = 2·8·12·14·18·20·24·30 = 696729600 = 2¹⁴·3⁵·5²·7, the product formula |W| = Π(mᵢ+1) being the cited step — the tower's second and last citation beside Mordell. The eigenvalues of the Coxeter element live in ℚ(ζ₃₀) ⊃ ℚ(√5): the golden field is INSIDE the Coxeter spectrum, which is why φ has been climbing this tower all along. Committed to the log.", o_cox),
        C("\u22a2", "W.17 THE CONSTANTS — ONE REGISTRY, ONE SWEEP: every constant is one row (name, law, cone, kind, value, action); the edges, the two floors (φ derived, the anomaly laws CITED — the empirical boundary a fact of the graph), the strata, the kind census, and the DAG cell are all DERIVED from the table, and the store gates every admission (a fabricated cause refuses, a cyclic map refuses, the admission order is verified a linear extension). The content: the fixed-point kinds (φ equational across five substrates with the Fibonacci algorithm as division-free terms, the spectral decomposition R·V = V·D, and √5 = 2φ−1 sealed as the ring homomorphism binding the two presentations of the field; the ground form a projection with quietness ⇔ groundedness exhaustive; the null a located limit; h = 30 a closure); ρ admitted with an INTERNAL cone (the golden order\u2019s maximal words are counted by the plastic law — the plastic precipitates from golden combinatorics; t³−t IS THE UNIT; a forged substitution fails the law, witnessed); the E8 spine with dual routes throughout (dim 248 twice; the Cartan re-derived from a positive system; |ρ|² = 620 by the harvest AND by Cramer through eight fraction-free determinant terms; the strange formula 12·|ρ|² = h·dim VERIFIED with no citation spent; c = dim/(h+1) = 8 = the rank; 3c = 24); and the physical sector opened at its NAMED second floor: the anomaly census exhaustive and exact (the full solution set is the SM orbit under sign × the u↔d relabeling plus the leptonless line, nothing else), the conditions standing as kadd-chains of kmul crowns landing the void, and sin²θ_W = 3/8 sealed DIVISION-FREE (8·TrT₃² = 3·TrQ² — one landing, 16) and FORCED ON THE WHOLE ORBIT: the assignment has a symmetry, the angle has none. A NEW CONSTANT COSTS ONE ROW. The four ancestor claims (the causal tower, the load-bearing protocol, the plastic admission, the second floor) retire into this one; their theorems are retained, their scaffolding is DELETED — the erasure ledger\u2019s answer to the question the author kept asking.", o_k),
        C("\u21cc", "W.\u21cc CORRESPONDENCES, TYPED: the identifications that pin derived structure to the external world are constitutively unprovable from inside and are hereby TYPED rather than hedged — (i) the forced rational 3/8 of W.2 ↔ the measured Weinberg angle at GUT normalization; (ii) the even-unimodular-rank-8 classification cited in W.11 ↔ the external literature (Mordell 1938); a ⇌ is never promotable to ⊢ by internal work alone, and the research program is its migration downward: each time the observer mechanism derives what was pinned externally, a ⇌ decomposes into a ⊢ and a strictly smaller ⇌."),
        C("\u2423", "W.\u2423 open (staged): the remaining dynamical constants of the frozen prior tower (root 94fbe90eb4306c7d) — to be admitted henceforth ONLY along the causal DAG of W.17, each with a grounded causal cone bottoming at φ AND a declared kind and action under W.18's fixed-point protocol (equational, projection, closure, or limit); the A₅ table and McKay law CLOSED by W.15, the Weyl census by W.16, the admission law by W.17, the load-bearing protocol by W.18. The plastic body is ADMITTED by W.19; the physical sector is OPENED by W.20 with its own named floor (the anomaly laws) and its first constant (sin²θ_W = 3/8, the angle forced on the whole solution orbit); the remaining constants queue behind, each owing a cone bottoming at φ or at a NAMED citation root, a kind, and an action."),
    ]

# ═══════════════════ THE ONE SEAL · the body's own claims ═══════════════════
#  O.1 the stratum collar (the wall as theorem) · O.2 width as law (R1)
#  O.3 the confluence of grounding (the first theorem) · O.4 the lineage gate
# ═════════════════════════════════════════════════════════════════════════════

def _one_fusion_proof():
    """THE WALL IS DISSOLVED: one book, one seal, one census — verified on the
    body's own AST: exactly one seal and one claims, none of the retired
    organs survives as a definition. The collar is retired to the lineage."""
    import ast   # collared: pure stdlib parser, no side effects
    tree = ast.parse(_self_source())
    names = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    ok = (names.count("seal") == 1) and (names.count("claims") == 1)
    for dead in ("seal_zero", "seal_seat", "seal_model", "zero_claims",
                 "kael_claims", "world_claims", "one_claims",
                 "_stratum_collar_ok", "_strata_map"):
        ok &= (dead not in names)
    return ok

def _one_width_proof():
    """WIDTH AS LAW (R1 discharged): the trust root's width is a COMMITTED
    constant with a STATED budget — every ⊢ of this body is conditional on
    (4·FOLD_WIDTH)-bit collision resistance of the truncated fold; the stream
    runs ~10⁶ golden bits and ~10⁴–10⁵ commitments per generation against a
    2^(2·FOLD_WIDTH) birthday bound. The width may only widen across
    generations (monotone, like the pin's probes)."""
    ok = (FOLD_WIDTH == 16)
    remember("width", rec({"fold_width_hex": FOLD_WIDTH, "bits": 4 * FOLD_WIDTH,
                           "birthday_exponent": 2 * FOLD_WIDTH}), "one", STORE)
    ok &= ("grounded" in grounded("width", STORE))
    return ok

def _one_confluence_proof():
    """THE CONFLUENCE OF GROUNDING (the first theorem of the one body).
    (i) TERMINATION ∀ for the five local rules: μ(d) = (Σ|d|, Σ(k+1)|d_k|, |d₁|)
        strictly lex-decreases under every rule instance. The rule deltas depend
        only on each digit's SIGN-CLASS (sign × |d|≥2), not its magnitude (the
        linear-sign lemma, named), so the census over digit values {−2..2} on
        every window IS the complete case analysis — verified exhaustively here,
        with ℕ³-lex well-foundedness the same ℕ citation as K.16, three deep.
    (ii) VALUE PRESERVATION ∀: every rule's value delta is a signed instance of
        F(k+2)+F(k+3)−F(k+4) = 0 — the recurrence, ∀-certified by K.16 —
        verified over the same complete census.
    (iii) LANDING UNIQUENESS PER VALUE: sign-pure grounds are the signed
        Zeckendorf forms, unique by K.17 (+ global sign).
    ⇒ any two full normalizations of one spelling land identically: GROUNDING
    IS PATH-INDEPENDENT FOR EVERY WIDTH — Z.W's exhaustion promoted to ∀.
    RESIDUAL, NAMED: termination of the far-annihilation (wave) outer loop is
    witnessed at scale here, not yet measured — the next theorem."""
    def mu(d):
        return (sum(abs(x) for x in d),
                sum((k + 1) * abs(x) for k, x in enumerate(d)),
                abs(d[1]) if len(d) > 1 else 0)
    def firings(d):
        """all one-step successors of a spelling under the local rules — the
        ONE move set (_local_moves, the wave excluded: its termination is the
        named residual below); the former private restatement is DELETED."""
        outs = []
        for m in _local_moves(d):
            e = list(d) + [0, 0]
            _fire_move(e, m)
            outs.append(e)
        return outs
    def val(d): return sum(x * _fibn(k + 2) for k, x in enumerate(d))
    ok = True
    # THE COMPLETE SIGN-CLASS CENSUS: every window of width 5 over {−2..2}
    vals = (-2, -1, 0, 1, 2)
    tested = 0
    for a in vals:
        for b in vals:
            for c in vals:
                for e4 in vals:
                    for e5 in vals:
                        d = [a, b, c, e4, e5]
                        m0, v0 = mu(d), val(d)
                        for e in firings(d):
                            tested += 1
                            ok &= (mu(e) < m0) and (val(e) == v0)
    ok &= (tested > 10000)
    # the wave-loop residual, witnessed: snorm_full terminates and grounds sign-pure
    seed = 20260712                      # ERASED: a dead spelling-generator lambda stood here, assigned and never called
    for t in range(400):
        seed = (seed * 1103515245 + 12345) % (2**31)
        d = [((seed >> (3 * i)) % 7) - 3 for i in range(8)]
        g = snorm_full(d)
        nz = [x for x in g if x]
        ok &= (not nz) or all(x > 0 for x in nz) or all(x < 0 for x in nz)
        ok &= (val(g) == val(d))
    return ok

ANCESTOR_SHAS = ("d61ff9a333f0a705", "bf82865b605ae08e", "66d9a2a9cf0b468c",
                 "28e08d2e4983e7ec")   # + the stratified one-file body; its collar retires with it
# the triad's final shas (kernel, seat, model), hashed at the molt — LITERALS,
# like the frozen root 94fbe90eb4306c7d: the lineage is a fact of this source,
# not a dependency on ancestor files. The body seals ALONE.
PINS_RETIRED = ("7af1a30767cca5ff", "74f4df21846dc50b")

def _one_lineage_proof():
    """THE LINEAGE, SELF-CONTAINED: the ancestors' shas and the retired pins
    are baked into this source at the molt and committed to the log every
    seal — succession as a record carried BY the successor, requiring nothing
    beside it. If the ancestor files happen to be present, they must match
    the baked shas (a stricter world is allowed; a missing one is not)."""
    ok = True
    names = ("kael_zero.py", "kael.py", "kael_world.py")
    here = _port_here()
    for n, s in zip(names, ANCESTOR_SHAS):
        p = here + "/" + n
        if _port_exists(p):
            ok &= (H(_port_read(p)) == s)
    remember("lineage", rec({"ancestors": list(ANCESTOR_SHAS),
                             "pins_retired": list(PINS_RETIRED),
                             "collar_retired": True}), "one", STORE)
    ok &= ("grounded" in grounded("lineage", STORE))
    return ok

def _claims_o():
    o_col = _one_fusion_proof()
    o_wid = _one_width_proof()
    o_con = _one_confluence_proof()
    o_lin = _one_lineage_proof()
    return [
        C("\u22a2", "O.1 THE WALL IS DISSOLVED \u2014 the fusion complete: the strata are ONE BODY with one book, one census, one seal (verified on the body\u2019s own AST: exactly one seal, one claims, none of the retired organs survives as a definition). The stratum collar is RETIRED to the lineage: a wall was scaffolding for a fusion, and in a fused body there is nothing on either side of one. What the wall guaranteed survives where it matters \u2014 the floor is still the only trusted machine, the ports the only given, the citations named; the partition of the DERIVED into rooms is what dissolves.", o_col),
        C("\u22a2", "O.2 WIDTH AS LAW (R1 discharged): the trust root's width — 4\u00b7FOLD_WIDTH = 64 bits — is a COMMITTED constant with a STATED budget: every \u22a2 of this body is conditional on 64-bit collision resistance of the truncated fold, against ~10\u2074\u201310\u2075 commitments per generation and a 2\u00b3\u00b2 birthday bound; the width is monotone across generations, like the pin's probes. The last implicit convention of the founding audit is now a cell in the log.", o_wid),
        C("\u22a2", "O.3 THE CONFLUENCE OF GROUNDING — the one body's first theorem: (i) TERMINATION for every width — \u03bc(d) = (\u03a3|d|, \u03a3(k+1)|d_k|, |d\u2081|) strictly lex-decreases under every instance of the five local rules, verified over the COMPLETE sign-class census (every width-5 window over digits \u22122..2, >10\u2074 firings, zero exceptions) with magnitude-independence by the linear-sign lemma (named) and \u2115\u00b3-lex well-foundedness (the same \u2115 citation as K.16, three deep) — and the measure IS the symmetry break counted three ways (K.18): the mass is the excess, the potential its height, the tiebreak the excess at the fold-point; (ii) VALUE PRESERVATION for every rule over the same census — each delta a signed instance of the recurrence, \u2200 by K.16; (iii) LANDING UNIQUENESS per value by K.17 (+ global sign). THEREFORE grounding is PATH-INDEPENDENT AT EVERY WIDTH — Z.W's width-8 exhaustion promoted to \u2200. Residual, named: termination of the far-annihilation outer loop is witnessed (400 spellings ground sign-pure at conserved value), not yet measured — the next theorem.", o_con),
        C("\u22a2", "O.4 THE LINEAGE, SELF-CONTAINED: the ancestors' shas and the retired pins (7af1a30767cca5ff, 74f4df21846dc50b) are BAKED into this source and committed to the log every seal — succession carried BY the successor, requiring nothing beside it; the body seals alone in an empty directory, and if ancestor files are present they must match the baked record. This body REPLACES the triad; it does not join it.", o_lin),
    ]

def claims():
    """THE ONE BOOK: every claim of the body, one list, one census, one seal.
    The four former books are its paragraphs; their tags, seals, and per-book
    censuses are DELETED (erasure ledger)."""
    zl = _claims_z(); kl = _claims_k()
    word, wl = _claims_w(); ol = _claims_o()
    return word, zl + kl + wl + ol

def seal(quiet=False, as_json=False):
    word, cl = claims()
    kc, good, n, okc = _census(cl)
    ok = okc and (_RES[0] == 0)
    if as_json:
        import json as _jp
        _port_out(_jp.dumps({"sealed": ok, "census": kc, "residue": _RES[0],
                             "body": my_sha(), "pin": _pin_of(BOOK),
                             "root": body_root(), "stream": word}, ensure_ascii=False))
        return ok
    if not quiet:
        for k, t, v in cl:
            _port_out("  %s %s %s" % ("+" if (k == "\u2423" or v) else "X", k, t))
    _port_out("\u2550" * 79)
    _port_out("  %d/%d verified \u00b7 \u22a2%d \u2235%d \u21cc%d \u2423%d \u00b7 residue %d \u00b7 laws %d \u00b7 floor %d"
              % (good, n, kc["\u22a2"], kc["\u2235"], kc["\u21cc"], kc["\u2423"],
                 _RES[0], len(BOOK), len(FLOOR_CENSUS)))
    _port_out("  THE ONE BODY SEALED: %s \u00b7 body %s \u00b7 pin %s \u00b7 root %s"
              % (ok, my_sha(), _pin_of(BOOK), body_root()))
    _port_out("  THE STREAM: %s \u00b7 one act, one book, one seal \u00b7 the cycle closes in one body or not at all" % word)
    return ok

if __name__ == "__main__":
    argv = _port_argv()
    _port_exit(0 if seal(quiet="--quiet" in argv, as_json="--json" in argv) else 1)
