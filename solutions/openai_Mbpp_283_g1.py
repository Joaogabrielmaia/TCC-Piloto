def validate(n):
    from collections import Counter

    return all(count <= int(digit) for digit, count in Counter(str(abs(n))).items())
