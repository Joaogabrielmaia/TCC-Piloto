import math

def perfect_squares(a, b):
    if b < 0:
        return []
    low = max(a, 0)
    start = math.isqrt(low)
    if start * start < low:
        start += 1
    end = math.isqrt(b)
    return [i * i for i in range(start, end + 1)]
