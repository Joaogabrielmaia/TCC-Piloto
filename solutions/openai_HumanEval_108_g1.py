def count_nums(arr):
    count = 0
    for number in arr:
        digits = [int(digit) for digit in str(abs(number))]
        digit_sum = sum(digits)
        if number < 0:
            digit_sum -= 2 * digits[0]
        if digit_sum > 0:
            count += 1
    return count
