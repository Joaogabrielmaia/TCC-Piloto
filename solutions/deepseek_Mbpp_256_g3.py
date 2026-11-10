def count_Primes_nums(n):
    if n < 2:
        return 0

    if n == int(n):
        limit = int(n) - 1
    else:
        limit = int(n)

    if limit < 2:
        return 0

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return sum(is_prime)
