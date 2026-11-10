def divisible_by_digits(startnum, endnum):
    return [
        number
        for number in range(startnum, endnum + 1)
        if all(
            digit != "0" and number % int(digit) == 0
            for digit in str(abs(number))
        )
    ]
