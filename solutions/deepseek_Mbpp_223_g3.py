def is_majority(arr, n, element):
    from bisect import bisect_left, bisect_right

    left = bisect_left(arr, element)
    right = bisect_right(arr, element)

    return (right - left) > n // 2
