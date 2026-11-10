from bisect import bisect_left, bisect_right

def is_majority(arr, n, x):
    left = bisect_left(arr, x, 0, n)
    right = bisect_right(arr, x, 0, n)
    return (right - left) > n / 2
