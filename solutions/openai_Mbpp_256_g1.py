def count_Primes_nums(n):
    from math import isqrt

    if n <= 2:
        return 0

    sieve = bytearray(b"\x01") * n
    sieve[0:2] = b"\x00\x00"

    for prime in range(2, isqrt(n - 1) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:n:prime] = b"\x00" * ((n - 1 - start) // prime + 1)

    return sum(sieve)
