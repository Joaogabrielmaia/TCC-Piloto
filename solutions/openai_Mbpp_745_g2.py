def divisible_by_digits(startnum, endnum):
    return [
        number
        for number in range(max(1, startnum), endnum + 1)
        if all(digit != "0" and number % int(digit) == 0 for digit in str(number))
    ]
