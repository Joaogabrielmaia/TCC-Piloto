def divisible_by_digits(startnum, endnum):
    result = []
    for n in range(startnum, endnum + 1):
        digits = str(abs(n))
        ok = True
        for ch in digits:
            d = int(ch)
            if d == 0 or n % d != 0:
                ok = False
                break
        if ok:
            result.append(n)
    return result
