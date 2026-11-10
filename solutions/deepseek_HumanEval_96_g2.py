from math import isqrt

def count_up_to(n):
    """Return a list of prime numbers less than n."""
    def is_prime(num):
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
        for i in range(3, isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

    return [i for i in range(2, n) if is_prime(i)]
