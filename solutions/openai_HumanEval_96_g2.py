def count_up_to(n):
    if n <= 2:
        return []

    from math import isqrt

    sieve = bytearray(b"\x01") * n
    sieve[0:2] = b"\x00\x00"

    for p in range(2, isqrt(n - 1) + 1):
        if sieve[p]:
            start = p * p
            sieve[start:n:p] = b"\x00" * ((n - 1 - start) // p + 1)

    return [i for i in range(2, n) if sieve[i]]
