def perfect_squares(a, b):
    from math import isqrt

    if a > b or b < 0:
        return []

    lower = max(0, a)
    first = isqrt(lower)
    if first * first < lower:
        first += 1

    return [n * n for n in range(first, isqrt(b) + 1)]
