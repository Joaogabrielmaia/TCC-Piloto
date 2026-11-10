def count_nums(arr):
    def digit_sum(n):
        neg = n < 0
        digits = [int(d) for d in str(abs(n))]
        if neg:
            digits[0] = -digits[0]
        return sum(digits)
    return sum(1 for x in arr if digit_sum(x) > 0)
