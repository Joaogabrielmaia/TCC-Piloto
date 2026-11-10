def is_majority(arr, n, element):
    from bisect import bisect_left, bisect_right

    if n <= 0:
        return False

    first = bisect_left(arr, element, 0, n)
    last = bisect_right(arr, element, first, n)
    return last - first > n // 2
