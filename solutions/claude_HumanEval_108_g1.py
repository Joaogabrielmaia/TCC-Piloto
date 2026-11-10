def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -n, -1
        d = [int(c) for c in str(n)]
        d[0] = d[0] * neg
        return sum(d)
    return len([x for x in arr if digits_sum(x) > 0])
