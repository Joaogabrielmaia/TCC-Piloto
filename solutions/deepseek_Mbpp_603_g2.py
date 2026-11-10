def get_ludic(n):
    if n <= 0:
        return []
    ludic = [1]
    candidates = list(range(2, n + 1))
    while candidates:
        num = candidates.pop(0)
        ludic.append(num)
        del candidates[num - 1::num]
    return ludic
