import math

def perfect_squares(a, b):
    lo, hi = (a, b) if a <= b else (b, a)
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
