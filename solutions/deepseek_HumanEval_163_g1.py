def generate_integers(a, b):
    lo, hi = sorted((a, b))
    return [d for d in (0, 2, 4, 6, 8) if lo <= d <= hi]
