def get_ludic(n):
    if n <= 0:
        return []
    ludic = [1]
    arr = list(range(2, n + 1))
    while arr:
        first = arr[0]
        ludic.append(first)
        del arr[::first]
    return ludic
