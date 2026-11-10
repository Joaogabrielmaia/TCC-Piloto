from collections import Counter

def validate(n):
    s = str(abs(n))
    counts = Counter(s)
    return all(count <= int(digit) for digit, count in counts.items())
