def generate_integers(a, b):
    lower, upper = sorted((a, b))
    even_digits = [0, 2, 4, 6, 8]
    return [d for d in even_digits if lower <= d <= upper]
