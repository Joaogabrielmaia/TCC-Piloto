def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        if num <= 0:
            continue
        digits = str(num)
        if '0' in digits:
            continue
        if all(num % int(d) == 0 for d in digits):
            result.append(num)
    return result
