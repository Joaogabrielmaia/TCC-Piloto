import math

def perfect_squares(a, b):
    if a > b:
        a, b = b, a
    a = max(a, 0)
    if b < 0 or a > b:
        return []
    low = math.isqrt(a)
    if low * low < a:
        low += 1
    high = math.isqrt(b)
    return [i * i for i in range(low, high + 1)]
