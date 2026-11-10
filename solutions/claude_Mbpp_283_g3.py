def validate(n):
    s = str(abs(int(n)))
    for d in set(s):
        if s.count(d) > int(d):
            return False
    return True
