def validate(n):
    n = abs(n)
    if n == 0:
        return False

    counts = [0] * 10
    while n:
        n, digit = divmod(n, 10)
        counts[digit] += 1
        if counts[digit] > digit:
            return False

    return True
