def validate(n):
    s = str(abs(n))
    return all(s.count(digit) <= int(digit) for digit in set(s))
