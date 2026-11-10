def count_up_to(n):
    if n <= 2:
        return []
    primes = []
    for x in range(2, n):
        if all(x % d != 0 for d in range(2, int(x**0.5) + 1)):
            primes.append(x)
    return primes
