def next_Perfect_Square(n):
    import math

    if n < 0:
        return 0
    return (math.isqrt(n) + 1) ** 2
