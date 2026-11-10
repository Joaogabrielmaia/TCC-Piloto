import math

def perfect_squares(a, b):
    low = min(a, b)
    high = max(a, b)
    if high < 0:
        return []
    low = max(low, 0)
    start = math.isqrt(low)
    if start * start < low:
        start += 1
    end = math.isqrt(high)
    return [i * i for i in range(start, end + 1)]
