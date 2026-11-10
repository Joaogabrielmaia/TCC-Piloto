def perfect_squares(a, b):
    from math import isqrt

    if a > b or b < 0:
        return []

    start = isqrt(max(a, 0))
    if start * start < a:
        start += 1

    return [n * n for n in range(start, isqrt(b) + 1)]
