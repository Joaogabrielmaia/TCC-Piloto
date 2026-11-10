def is_majority(arr, n, x):
    from bisect import bisect_left, bisect_right

    first = bisect_left(arr, x, 0, n)
    last = bisect_right(arr, x, first, n)
    return last - first > n // 2
