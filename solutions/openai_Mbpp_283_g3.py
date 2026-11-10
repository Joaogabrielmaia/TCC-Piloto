def validate(n):
    counts = [0] * 10
    for char in str(abs(n)):
        digit = int(char)
        counts[digit] += 1
        if counts[digit] > digit:
            return False
    return True
