def count_Primes_nums(n):
    import math

    if n <= 2:
        return 0

    limit = math.ceil(n)
    sieve = bytearray(b"\x01") * limit
    sieve[0:2] = b"\x00\x00"

    for prime in range(2, math.isqrt(limit - 1) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start:limit:prime] = b"\x00" * (
                (limit - 1 - start) // prime + 1
            )

    return sum(sieve)
