def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        s = str(num)
        valid = True
        for ch in s:
            digit = int(ch)
            if digit == 0 or num % digit != 0:
                valid = False
                break
        if valid:
            result.append(num)
    return result
