import math

def perfect_squares(a, b):
    lo, hi = min(a, b), max(a, b)
    result = []
    if hi < 0:
        return result
    start = 0 if lo <= 0 else math.isqrt(int(math.ceil(lo)) - 1) + 1
    i = start
    while i * i <= hi:
        if i * i >= lo:
            result.append(i * i)
        i += 1
    return result
