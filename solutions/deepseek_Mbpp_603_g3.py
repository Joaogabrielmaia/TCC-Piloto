def get_ludic(n):
    if n < 1:
        return []
    ludics = [1]
    candidates = list(range(2, n + 1))
    while candidates:
        p = candidates[0]
        ludics.append(p)
        del candidates[::p]
    return ludics
