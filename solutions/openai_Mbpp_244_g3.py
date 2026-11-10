def next_Perfect_Square(number):
    from math import isqrt

    if number < 0:
        return 0
    return (isqrt(number) + 1) ** 2
