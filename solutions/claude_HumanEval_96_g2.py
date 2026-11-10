def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    if n is None or n < 3:
        return []
    sieve = bytearray([1]) * n
    sieve[0] = 0
    sieve[1] = 0
    i = 2
    while i * i < n:
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(range(i * i, n, i)))
        i += 1
    return [k for k in range(2, n) if sieve[k]]
