def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    """
    count = 0
    for num in arr:
        if num >= 0:
            total = sum(int(d) for d in str(num))
        else:
            digits = str(num)[1:]
            total = -int(digits[0]) + sum(int(d) for d in digits[1:])
        if total > 0:
            count += 1
    return count
