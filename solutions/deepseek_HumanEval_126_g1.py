from collections import Counter

def is_sorted(lst):
    if any(lst[i] > lst[i + 1] for i in range(len(lst) - 1)):
        return False
    return all(count <= 2 for count in Counter(lst).values())
