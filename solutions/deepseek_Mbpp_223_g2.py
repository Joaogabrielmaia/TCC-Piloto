from bisect import bisect_left, bisect_right

def is_majority(arr, n, element):
    if n == 0:
        return False
    left = bisect_left(arr, element)
    right = bisect_right(arr, element)
    return (right - left) > n // 2
