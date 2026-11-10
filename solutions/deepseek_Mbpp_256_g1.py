import math

def count_Primes_nums(n):
    if n <= 2:
        return 0
    if n == int(n):
        limit = int(n) - 1
    else:
        limit = int(n)
    if limit < 2:
        return 0

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            start = i * i
            sieve[start:limit + 1:i] = [False] * (((limit - start) // i) + 1)

    return sum(sieve)
