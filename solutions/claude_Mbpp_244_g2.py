import math

def next_Perfect_Square(N):
    if N < 0:
        return 0
    n = int(math.floor(N)) if not isinstance(N, int) else N
    r = math.isqrt(n) + 1
    return r * r
