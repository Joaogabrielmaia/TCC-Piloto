def validate(n):
    s = str(abs(n))
    for digit in set(s):
        if s.count(digit) > int(digit):
            return False
    return True
