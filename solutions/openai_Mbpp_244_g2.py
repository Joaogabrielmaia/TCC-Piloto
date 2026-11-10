def next_Perfect_Square(number):
    from math import floor, isqrt

    if number < 0:
        return 0
    return (isqrt(floor(number)) + 1) ** 2
