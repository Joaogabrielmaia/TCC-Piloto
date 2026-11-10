import math

def perfect_squares(a, b):
    lo, hi = min(a, b), max(a, b)
    if hi < 0:
        return []
    lo = max(lo, 0)
    start = math.isqrt(lo)
    if start * start < lo:
        start += 1
    end = math.isqrt(hi)
    return [i * i for i in range(start, end + 1)]
