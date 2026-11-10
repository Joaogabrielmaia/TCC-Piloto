def sum_digits(n):
    total = 0
    n = int(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total
