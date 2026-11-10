def count_nums(arr):
    count = 0
    for number in arr:
        if number > 0:
            count += 1
        elif number < 0:
            remaining = -number
            digit_sum = 0
            while remaining >= 10:
                remaining, digit = divmod(remaining, 10)
                digit_sum += digit
            if digit_sum - remaining > 0:
                count += 1
    return count
