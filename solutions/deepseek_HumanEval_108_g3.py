def count_nums(arr):
    count = 0
    for num in arr:
        s = str(num)
        if s[0] == '-':
            digit_sum = sum(int(d) for d in s[1:]) - 2 * int(s[1])
        else:
            digit_sum = sum(int(d) for d in s)
        if digit_sum > 0:
            count += 1
    return count
