import math

def count_Primes_nums(n):
    if n <= 2:
        return 0

    if isinstance(n, float) and n != int(n):
        upper = int(n)
    else:
        upper = int(n) - 1

    if upper < 2:
        return 0

    is_prime = [True] * (upper + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, math.isqrt(upper) + 1):
        if is_prime[i]:
            for j in range(i * i, upper + 1, i):
                is_prime[j] = False

    return sum(is_prime)
