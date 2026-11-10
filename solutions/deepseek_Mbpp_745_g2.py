def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum + 1):
        valid = True
        for digit_char in str(num):
            if not digit_char.isdigit():
                continue
            digit = int(digit_char)
            if digit == 0 or num % digit != 0:
                valid = False
                break
        if valid:
            result.append(num)
    return result
