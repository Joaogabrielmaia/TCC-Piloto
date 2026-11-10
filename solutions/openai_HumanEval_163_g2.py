def generate_integers(a, b):
    lower, upper = sorted((a, b))
    return [digit for digit in (0, 2, 4, 6, 8) if lower <= digit <= upper]
