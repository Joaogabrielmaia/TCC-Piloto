def generate_integers(a, b):
    low, high = sorted((a, b))
    return [digit for digit in (0, 2, 4, 6, 8) if low <= digit <= high]
