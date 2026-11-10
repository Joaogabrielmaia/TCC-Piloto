import math

def next_Perfect_Square(n):
    if n < 0:
        return 0
    root = math.isqrt(int(n))
    return (root + 1) ** 2
