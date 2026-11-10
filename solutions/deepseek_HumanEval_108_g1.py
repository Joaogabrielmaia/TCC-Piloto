def count_nums(arr):
    count = 0
    for num in arr:
        if num > 0:
            if sum(int(d) for d in str(num)) > 0:
                count += 1
        elif num < 0:
            digits = str(num)[1:]
            signed_sum = -int(digits[0]) + sum(int(d) for d in digits[1:])
            if signed_sum > 0:
                count += 1
    return count
