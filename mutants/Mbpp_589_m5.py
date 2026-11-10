import math

def perfect_squares(a, b):
    if a > b:
        a, b = (b, a)
    if b < 0:
        return []
    if a <= 0:
        a = 0
    return list(filter(lambda x: math.sqrt(x).is_integer(), range(a, b + 1)))