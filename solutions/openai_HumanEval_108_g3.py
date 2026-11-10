def count_nums(arr):
    count = 0
    for num in arr:
        remaining = abs(num)
        digit_sum = 0
        while remaining >= 10:
            remaining, digit = divmod(remaining, 10)
            digit_sum += digit
        digit_sum += -remaining if num < 0 else remaining
        if digit_sum > 0:
            count += 1
    return count
