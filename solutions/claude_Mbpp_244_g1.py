import math

def next_Perfect_Square(N):
    if N < 0:
        return 0
    n = math.floor(N)
    r = math.isqrt(int(n)) + 1
    return r * r
