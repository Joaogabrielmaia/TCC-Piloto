def count_up_to(n):
    if n <= 2:
        return []
    primes = []
    for x in range(2, n):
        is_prime = True
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes
