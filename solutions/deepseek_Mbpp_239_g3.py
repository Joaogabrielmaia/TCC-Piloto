from fractions import Fraction
from math import comb


def _build_sum_power(max_deg):
    """Return S_p(q) = sum_{u=0}^{q} u^p for p = 0..max_deg."""
    sum_power = [[Fraction(1), Fraction(1)]]  # S_0(q) = q + 1

    for p in range(1, max_deg + 1):
        n = p + 2
        poly = [Fraction(0)] * n

        # (q + 1)^(p + 1)
        for j in range(p + 2):
            poly[j] = Fraction(comb(p + 1, j), 1)

        # subtract lower-degree sums using the telescoping identity
        for j in range(p):
            factor = Fraction(comb(p + 1, j), 1)
            lower = sum_power[j]
            for deg, coeff in enumerate(lower):
                poly[deg] -= factor * coeff

        for j in range(n):
            poly[j] /= (p + 1)

        sum_power.append(poly)

    return sum_power


def _substitute_and_sum(poly, h, sum_power):
    """
    Given P(x), return sum_{u=0}^{q} P(2u + h)
    as a polynomial in q.
    """
    d = len(poly) - 1
    expanded = [Fraction(0)] * (d + 1)

    for j, c in enumerate(poly):
        if c == 0:
            continue
        for t in range(j + 1):
            coeff = Fraction(comb(j, t) * (2 ** t) * (h ** (j - t)), 1)
            expanded[t] += c * coeff

    result = [Fraction(0)] * (d + 2)
    for t, coeff in enumerate(expanded):
        if coeff == 0:
            continue
        sp = sum_power[t]
        for deg, val in enumerate(sp):
            result[deg] += coeff * val

    return result


def get_total_number_of_sequences(m, n):
    K = n - 1

    # If even the smallest possible last term 2^K exceeds m, no sequence exists.
    if K >= m.bit_length():
        return 0

    M = m - (1 << K)
    Q = M >> K
    R = M & ((1 << K) - 1)

    sum_power = _build_sum_power(K)

    # P_0(q) = C_0(q) = q + 1
    P = [Fraction(1), Fraction(1)]

    for i in range(1, K + 1):
        h = (R >> (i - 1)) & 1
        P = _substitute_and_sum(P, h, sum_power)

    # Evaluate P(Q) by Horner's method.
    ans = Fraction(0)
    for coeff in reversed(P):
        ans = ans * Q + coeff

    return int(ans)
