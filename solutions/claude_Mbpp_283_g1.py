def validate(n):
    s = str(abs(int(n)))
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch, c in counts.items():
        if c > int(ch):
            return False
    return True
